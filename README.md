Nama    :Muhammad Nararya Ardhana
NPM     :2506657094
Kelas   :PBP F

### Tugas 1
1.Dalam merancang struktur HTML pada website portfolio, saya menggunakan elemen semantik seperti `<header>`, `<main>`, `<section>`, dan `<footer>`. Penggunaan elemen tersebut membantu saya membagi halaman menjadi beberapa bagian yang lebih terstruktur dan mudah dipahami. Selain itu, struktur semantik juga membuat kode lebih rapi dan memudahkan saya ketika ingin mengembangkan website di tahap berikutnya.

2.Tantangan yang saya temukan ketika membuat CSS responsive adalah menyesuaikan tata letak agar tetap terlihat rapi pada ukuran layar yang berbeda. Pada tampilan desktop, beberapa elemen dapat ditampilkan dalam dua kolom menggunakan CSS Grid, sedangkan pada perangkat mobile saya perlu mengubahnya menjadi satu kolom. Saya mengatasinya dengan menggunakan media query sehingga ukuran dan tata letak elemen dapat menyesuaikan dengan lebar layar.

3. Karena website yang dibuat saat ini masih berupa static web, informasi yang ditampilkan masih ditulis secara langsung di dalam HTML dan belum dapat dikelola secara dinamis. Batasan ini membuat perubahan informasi seperti riwayat pendidikan atau data portfolio harus dilakukan dengan mengubah kode secara manual. Pada iterasi berikutnya, saya ingin menambahkan fungsionalitas dinamis seperti penyimpanan data portfolio menggunakan database dan membuat halaman yang dapat menampilkan data tersebut secara otomatis.

## AI Disclosure

Dalam pengerjaan tugas ini, saya menggunakan ChatGPT untuk membantu memahami struktur Django, HTML5, CSS, dan responsive design serta membantu memberikan contoh struktur kode dan memberikan saran dalam memperbaiki beberapa bagian kode.

Implementasi akhir tetap saya lakukan dan sesuaikan sendiri, termasuk memasukkan data pribadi, riwayat pendidikan, mengatur struktur halaman, serta melakukan pengecekan dan perbaikan kode agar dapat dijalankan dengan baik.

### Tugas 2
1.Ketika pengguna membuka halaman portofolio baru, browser mengirimkan request ke   Django. Request tersebut pertama kali diproses oleh urls.py pada project yang mengarahkan request ke urls.py pada aplikasi main. Selanjutnya,urls.py aplikasi menentukan view yang sesuai, misalnya show_education.View kemudian mengambil data Education dari model Education menggunakan Django ORM. Data tersebut dimasukkan ke dalam context dan dikirimkan ke template education.html. Template menggunakan data dari context untuk menampilkan informasi Education secara dinamis. Setelah template dirender oleh Django, hasil HTML dikirim kembali ke browser dan ditampilkan kepada pengguna.

2.Data sebaiknya disimpan pada model karena data menjadi terpisah dari tampilan atau template. Dengan begitu, perubahan data seperti menambahkan, mengubah, atau menghapus riwayat Education tidak mengharuskan kita mengubah kode HTML secara langsung.Hal ini membuat aplikasi lebih mudah dipelihara dan dikembangkan. Template hanya bertugas menampilkan data, sedangkan model bertugas menyimpan dan mengelola struktur data. Selain itu, data yang disimpan dalam model dapat digunakan kembali pada beberapa halaman tanpa harus menulis ulang data tersebut di setiap template. 

3.makemigrations digunakan untuk membuat file migration berdasarkan perubahan pada model Django. File migration tersebut berisi instruksi mengenai perubahan struktur database yang perlu dilakukan.Sedangkan migrate digunakan untuk menerapkan migration tersebut ke database sehingga struktur database benar-benar diperbarui.
Contohnya:ketika menambahkan model Education dengan field institution, degree, start_year, dan end_year, kita menjalankan:

