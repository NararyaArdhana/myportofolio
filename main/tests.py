from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Education


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
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Freelance")
        self.assertContains(response, "Ongoing")
        self.assertContains(
            response,
            f'href="{reverse("main:show_main")}"'
        )

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(
            response,
            "Belum ada pengalaman yang ditambahkan."
        )

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()

        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "completed")
        self.assertNotContains(response, "Ongoing")

class EducationTest(TestCase):
        def setUp(self):
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

            self.assertRedirects(response, reverse("main:show_education"))

            self.education.refresh_from_db()

            self.assertEqual(self.education.institution, "Universitas Indonesia")
            self.assertEqual(self.education.degree, "Computer Science")
            self.assertEqual(self.education.start_year, 2025)
            self.assertIsNone(self.education.end_year)