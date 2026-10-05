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

### Tugas 3
1.ModelForm digunakan karena dapat membuat form berdasarkan model Django secara otomatis, sehingga proses pembuatan dan pengelolaan form menjadi lebih sederhana serta mengurangi penulisan kode yang berulang. Field pada form juga dapat langsung disesuaikan dengan field yang terdapat pada model.{% csrf_token %} digunakan untuk memberikan perlindungan terhadap serangan Cross-Site Request Forgery (CSRF). Token ini memastikan bahwa request POST berasal dari form yang valid pada aplikasi dan bukan dari request berbahaya yang dibuat oleh pihak lain.

2.JSON lebih populer karena memiliki struktur yang sederhana dan lebih ringkas sehingga lebih mudah dibaca oleh manusia maupun diproses oleh program. JSON juga menggunakan struktur data yang mirip dengan object dan array pada banyak bahasa pemrograman, sehingga mudah digunakan dalam komunikasi antara frontend dan backend.Selain itu, JSON umumnya memiliki ukuran data yang lebih kecil dibandingkan XML untuk informasi yang sama, sehingga cocok digunakan dalam pertukaran data melalui API.

3.Alurnya dimulai ketika client mengirim request ke endpoint JSON. View kemudian mengambil data dari database menggunakan Django ORM. Data tersebut selanjutnya diproses menggunakan serializers.serialize() untuk mengubah object atau QuerySet Django menjadi format JSON.JSON tersebut kemudian dikembalikan melalui HttpResponse dengan content_type="application/json". Serialisasi diperlukan karena object Django dan QuerySet tidak dapat langsung dikirim sebagai JSON. Data perlu diubah terlebih dahulu menjadi format yang dapat ditransmisikan dan dipahami oleh client.Pada implementasi ini, data JSON juga dapat dilakukan deserialization, yaitu mengubah kembali data JSON menjadi object Django sebelum ditampilkan pada halaman portfolio.

### AI DISCLOSURE
Dalam pengerjaan Tugas 3 saya menggunakan ChatGPT untuk membantu memahami dan debugging web.

Bagian yang dibantu oleh AI:
1.Membantu merancang implementasi fitur Create, Update, dan Delete pada data Education dan Experience.
2.Membantu implementasi JSON data delivery, filtering, serialization, dan deserialization.
3.Membantu melakukan debugging berdasarkan error yang muncul saat menjalankan aplikasi.
4.Membantu memberikan saran untuk memperbaiki tampilan UI, seperti styling tombol Add, Update, Delete, dan search bar.

Strategi prompting yang digunakan:
Saya memberikan konteks berupa struktur project, potongan kode, screenshot error, serta hasil pengujian kepada ChatGPT.Saya kemudian meminta bantuan secara bertahap untuk menemukan penyebab masalah dan menentukan perubahan kode yang diperlukan.

### TUGAS 4
### AI DISCLOSURE
Dalam pengerjaan Tugas 4 saya menggunakan ChatGPT untuk membantu memahami, mengimplementasikan, dan melakukan debugging fitur authentication, authorization, dan star pada web.

Bagian yang dibantu oleh AI:
Membantu memahami dan mengimplementasikan fitur login, register, dan logout menggunakan Django Authentication.
Membantu mengimplementasikan role dan authorization, termasuk membedakan hak akses antara visitor, user biasa, Editor, dan Superuser.
Membantu mengimplementasikan fitur Star/Unstar pada data Experience menggunakan ManyToManyField, termasuk menghitung jumlah Star dan menampilkan status Star pengguna.
Membantu melakukan debugging berdasarkan error yang muncul saat menjalankan aplikasi, termasuk pengecekan template, URL, view, model, dan CSS.
Membantu memberikan saran untuk memperbaiki UI, seperti posisi tombol Star, tombol Add/Update/Delete, tampilan Login/Register, serta posisi Last Login pada footer.

Strategi prompting yang digunakan:
Saya memberikan konteks berupa struktur project, potongan kode, screenshot tampilan atau error, serta hasil pengujian kepada ChatGPT. Saya kemudian meminta bantuan secara bertahap untuk memahami penyebab masalah, menentukan perubahan kode yang diperlukan, dan melakukan pengujian kembali setelah perubahan dilakukan.

### TUGAS 5
1. Debouncing adalah teknik untuk menunda eksekusi suatu fungsi sampai pengguna berhenti melakukan input selama waktu tertentu. Pada fitur search menggunakan AJAX, debouncing penting agar request ke server tidak dikirim pada setiap karakter yang diketik pengguna. Dengan menggunakan debounce, request hanya dikirim setelah pengguna berhenti mengetik selama beberapa waktu. Hal ini dapat mengurangi jumlah request ke server dan membuat proses pencarian menjadi lebih efisien.

2.await digunakan untuk menunggu hasil dari operasi asynchronous sebelum melanjutkan ke baris kode berikutnya. Pada penggunaan fetch(), await membuat program menunggu sampai request selesai dan mendapatkan response dari server sebelum response tersebut diproses.Jika tidak menggunakan await, hasil dari fetch() masih berupa Promise sehingga kode dapat melanjutkan eksekusi sebelum response dari server tersedia. Hal ini dapat menyebabkan data belum tersedia ketika program mencoba mengakses atau memproses response tersebut.

3.XSS (Cross-Site Scripting) adalah serangan yang memanfaatkan input berbahaya berupa script atau HTML yang kemudian ditampilkan dan dijalankan pada browser pengguna. Data yang ditampilkan melalui JavaScript dan AJAX perlu diperhatikan karena data dari server dapat dimasukkan secara langsung ke dalam HTML menggunakan JavaScript.

#### AI DISCLOSURE

Dalam pengerjaan Tugas 5 saya menggunakan ChatGPT untuk membantu memahami, mengimplementasikan, dan melakukan debugging fitur AJAX, search, modal, toast, serta keamanan XSS.

Bagian yang dibantu oleh AI:
1. Membantu memahami dan mengimplementasikan pengambilan data Experience menggunakan AJAX dan endpoint JSON.
2. Membantu memahami dan menerapkan perlindungan terhadap XSS pada data yang ditampilkan melalui JavaScript.
3. Membantu melakukan debugging berdasarkan error yang muncul saat menjalankan aplikasi.
4. Membantu melakukan pengecekan dan perbaikan konsistensi tampilan form serta struktur template.

Strategi prompting yang digunakan:
Saya memberikan konteks berupa struktur project, potongan kode, screenshot tampilan atau error, serta hasil pengujian kepada ChatGPT. Saya kemudian meminta bantuan secara bertahap untuk memahami penyebab masalah, menentukan perubahan kode yang diperlukan, dan melakukan pengujian kembali setelah perubahan dilakukan.

#### Project Setup

Untuk menjalankan project secara lokal:

1. Clone repository dan masuk ke folder project.
2. Buat dan aktifkan virtual environment.
3. Install dependency yang diperlukan.
4. Jalankan migration database 
5. Jalankan development server menggunakan:

```bash
py manage.py runserver

buka website melalui
http://127.0.0.1:8000/



