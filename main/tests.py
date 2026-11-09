from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education
from django.contrib.auth.models import User,Group

from rest_framework.test import APIClient
from rest_framework import status



class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Portfolio Website Project",
            description="Designed and developed a personal portfolio website using HTML, CSS, Django, and database integration.",
            category="freelance",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(
            response,
            f'href="{reverse("main:show_experience")}"'
        )

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/a-page-that-does-not-exist/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Portfolio Website Project")
        self.assertEqual(self.experience.category, "freelance")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(
            reverse("main:show_experience")
        )

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            "experience.html"
        )

        self.assertContains(
            response,
            "Experience"
        )

        self.assertContains(
            response,
            "experience-grid"
        )

        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(
            response,
            "No experience has been added yet"
        )

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "completed")
        response = self.client.get(
            reverse("main:get_experience_json")
        )

        self.assertEqual(response.status_code, 200)

        data = response.json()

        experience_data = next(
            item
            for item in data
            if item["title"] == self.experience.title
        )

        self.assertIsNotNone(
            experience_data["ended_at"]
        )

    def test_experience_json(self):
        response = self.client.get(
            reverse("main:get_experience_json")
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Type"],
            "application/json",
        )

        data = response.json()

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertTrue(
            any(
                item["title"] == self.experience.title
                for item in data
            )
        )

class EducationTest(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="admin",
            password="admin12345",
        )

        self.education = Education.objects.create(
            institution="Universitas Indonesia",
            degree="Bachelor of Computer Science",
            start_year=2025,
        )

    def test_education_model(self):
        self.assertEqual(str(self.education), "Universitas Indonesia")
        self.assertEqual(
            self.education.degree,
            "Bachelor of Computer Science"
        )
        self.assertEqual(self.education.start_year, 2025)
        self.assertIsNone(self.education.end_year)

    def test_education_page(self):
        response = self.client.get(
            reverse("main:show_education")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, "Universitas Indonesia")
        self.assertContains(response, "Bachelor of Computer Science")
        self.assertContains(response, "Present")

    def test_empty_education_page(self):
        Education.objects.all().delete()

        response = self.client.get(
            reverse("main:show_education")
        )

        self.assertContains(
            response,
            "No education history available."
        )

    def test_update_education(self):
        self.client.force_login(self.superuser)

        response = self.client.post(
            reverse(
                "main:update_education",
                args=[self.education.id],
            ),
            {
                "institution": "Universitas Indonesia",
                "degree": "Computer Science",
                "start_year": 2025,
                "end_year": "",
            },
        )

        self.assertRedirects(
            response,
            reverse("main:show_education")
        )

        self.education.refresh_from_db()

        self.assertEqual(
            self.education.institution,
            "Universitas Indonesia"
        )
        self.assertEqual(
            self.education.degree,
            "Computer Science"
        )
        self.assertEqual(
            self.education.start_year,
            2025
        )
        self.assertIsNone(
            self.education.end_year
        )


class ExperienceAPITest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Test Experience",
            description="Testing Django REST Framework",
            category="freelance",
        )

        self.editor_group = Group.objects.get_or_create(
            name="Editor"
        )[0]

        self.visitor = APIClient()

        self.user = User.objects.create_user(
            username="regular_user",
            password="testpassword123",
        )

        self.editor = User.objects.create_user(
            username="editor_user",
            password="testpassword123",
        )
        self.editor.groups.add(self.editor_group)

        self.owner = User.objects.create_superuser(
            username="owner",
            email="owner@example.com",
            password="testpassword123",
        )

    def test_visitor_can_get_experiences(self):
        response = self.visitor.get("/api/v1/experiences/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_visitor_cannot_create_experience(self):
        response = self.visitor.post(
            "/api/v1/experiences/",
            {
                "title": "New Experience",
                "description": "Test",
                "category": "freelance",
            },
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_user_can_star_experience(self):
        self.visitor.force_authenticate(user=self.user)

        response = self.visitor.post(
            f"/api/v1/experiences/{self.experience.id}/star/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            self.experience.starred_by.filter(pk=self.user.pk).exists()
        )

    def test_editor_can_update_experience(self):
        self.visitor.force_authenticate(user=self.editor)

        response = self.visitor.patch(
            f"/api/v1/experiences/{self.experience.id}/",
            {"title": "Updated by Editor"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Updated by Editor")

    def test_editor_cannot_create_experience(self):
        self.visitor.force_authenticate(user=self.editor)

        response = self.visitor.post(
            "/api/v1/experiences/",
            {
                "title": "New Experience",
                "description": "Test",
                "category": "freelance",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_editor_cannot_delete_experience(self):
        self.visitor.force_authenticate(user=self.editor)

        response = self.visitor.delete(
            f"/api/v1/experiences/{self.experience.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_owner_can_create_experience(self):
        self.visitor.force_authenticate(user=self.owner)

        response = self.visitor.post(
            "/api/v1/experiences/",
            {
                "title": "Owner Experience",
                "description": "Created by owner",
                "category": "freelance",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_owner_can_delete_experience(self):
        self.visitor.force_authenticate(user=self.owner)

        response = self.visitor.delete(
            f"/api/v1/experiences/{self.experience.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )
