# Template Proyek Django PBP
# Kak untuk jawaban tugas 2 dibawah soalnya saya gatau ini dihapus atau tidak
# Untuk jawaban tugas 3 dibawah jawaban tugas 2

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Pendahuluan

Repositori ini merupakan sebuah template yang dirancang untuk membantu mahasiswa yang sedang mengambil mata kuliah Pemrograman Berbasis Platform (CSGE602022) mengetahui struktur sebuah proyek aplikasi Django serta file dan konfigurasi yang penting dalam berjalannya aplikasi. Kamu dapat dengan bebas menyalin isi dari repositori ini atau memanfaatkan repositori ini sebagai pembelajaran sekaligus awalan dalam membuat sebuah proyek Django.

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.

Link App : https://tugas-2-pbp-muhammadalifismady.herokuapp.com/katalog/

Jawaban pertanyaan

1.Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
![1_5tlbCdsQHDW38Yn1eP97Kg](https://user-images.githubusercontent.com/112617789/190299779-c0f4a0de-e572-4adf-a8b6-804ae4a0031d.jpeg)
(Sumber foto : https://medium.com/@ahmadzuliamrullah/belajar-django-framework-81385df4565)
Berdasarkan ilustrasi dari arsitektur tersebut, terlihat bahwa yang pertama kali dilakukan adalah request dari user ke django yang nantinya akan pertama melalui urls yang selanjutnya diteruskan ke views. Setelah masuk kedalam views, developer akan menganggap request ini untuk segera diproses. Pemrosesan request akan masuk ke data base lalu dikembalikan menuju models. Hasil dari data pada models ini akan dikembalikan lagi kedalam views, lalu data yang didapatkan akan dipetakan dalam bentuk html yang selanjutnya akan dapat dikembalikan lagi ke user.



2.Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual enviroment adalah tools untuk kita membuat enviroment python  virtual yang terisolasi, yang artinya tertutup dan tidak bisa diakses dari luar. Program Python yang berjalan didalam virtual enviroment memiliiki modul tersendiri dan program ini tidak bisa diakses dari luar. Virtual Enviroment merupakan dedicated enviroment untuk projek django yang kita buat. Menggunakan Virtual Enviroment bukan merupakan hal yang wajib tetapi dengan melakukan ini berarti kita telah melakukan best practice dan memudahkan kita untuk mendeploy projek yang kita buat.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Pertama, fungsi yang dibuat adalah show_katalog dimana fungsi ini akan mereturn data list item yang diambil dari models dan direturn dalam bentuk html dengan nama file katalog. Membuat routing pada urls dengan import fungsi show_katalog dari views. Kemudian menambahkan data item dengan iterasi pada file katalog.html . Setelah tes dengan localhost, melakukan deployment ke heroku dengan membuat file txt yang berisi API dari akun heroku dan nama aplikasi yang telah dibuat. Setelah itu melakukan git add, commit, dan push, lalu mengecek pada actions di github untuk lihat apakah deployment berhasil atau tidak.

Tugas 3
Link App : https://tugas-2-pbp-muhammadalifismady.herokuapp.com/mywatchlist/
1. Perbedaan antara html, xml, dan json. Html dan Xml merupakan bahasa yang menggunakan teks penandaan. Html diugnakan untuk menyusun hal atau teks pada halaman web agar dapat ditampilkan dengan benar. XML umumnya digunakan untuk menyusun data atau pesan. JSON digunakan untuk merepresentasikan data sebagai pasangan nilai kunci, yang dapat dengan mudah dikonversi ke dan dari objek JavaScript

2. Kita perlu melakukan data delivery karena hal ini menguntukan saat kita ingin implementasi sautu platform. Dalam penggunaan platform akan banyak terjadi pertukaran data antara client dan server. Untuk melakukan update, create, delete, pertukaran ini akan mudah untuk dikomunikasikan dengan data delivery. Untuk melakukan data delivery bisa menggunakan html, xml, atau json

3. Pertama, saya startapp bernama mywatchlist pada terminal directory rep saya. Kemudian menambahkan path mywatchlist pada urls pada project_django. Kemudian menambahkan model untuk watchlist pada file models.py. Kemudian saya membuat file json yang berisi 10 data untuk objek mywatchlist dan menaruh models itu pada folder bernama fixtures. Kemudian saya implementasikan fitur untuk menyajikan data. Untuk html, saya membuat file html pada templates dengan menggunakan fungsi yang saya gunakan pada tugas 2. Kemudian saya membuat fungsi pada views yang akan mengambil data. Untuk json dan xml saya membuat fungsi pada views yang akan di import ke file urls yang nantinya agar bisa di routing pada local host. Saya juga tidak lupa untuk make migrations migrate dan loaddata untuk file json agar data dapat masuk ke database. Untuk deployment, saya menambahkan fungsi migrations migrate dan loaddata untuk fil ejson mywatchlist agar dapat masuk ke heroku. Setelah itu saya melakukan git add git commit dan git push agra deployment dapat dilakukan. 

Screenshot Postman
1. HTML![messageImage_1663763379995](https://user-images.githubusercontent.com/112617789/191504463-0191d243-627e-4178-ba91-6dc4e60f006d.jpg)

2. XML![messageImage_1663763394871](https://user-images.githubusercontent.com/112617789/191504495-08dbc87e-6c27-4a77-a0ca-d1c83f860e54.jpg)

3. JSON![messageImage_1663763514932](https://user-images.githubusercontent.com/112617789/191504530-0b58042e-9690-458d-874e-75ab061c7a60.jpg)

Jawaban Tugas 4
Link App : https://tugas-2-pbp-muhammadalifismady.herokuapp.com/todolist/
Dummy Acc:
1. user : DummyAcc1 ; pass: passakun1
2. user : DummyAcc2 ; pass: passakun2

1. Kegunaan dari {% csrf_token %} adalah untuk mencegah penyerangan CRSF dengan membuat orang yang ingin menyerang membuat sebuah HTTP request yang valid. CRSF token sendiri adalah token yang unik, rahasia, dan tidak bisa diperkirakan yang di buat oleh server dan di transmit ke client. Saat request dibuat, server akan cek semua hal termasuk token, apakah token tersebut valid atau invalid. Dengan CRSFH, user yang tidak terverivikasi tidak akan bisa menggunakan data-data yang terdapat pada server yang dimiliki oleh orang lain.

2. Kita dapat membuat form secara manual tanpa harus menggunakan generator dengan menggunakan <form>. Contoh kode form :
<form action="" method="get" class="form-example">
  <div class="form-example">
    <label for="name">Enter your name: </label>
    <input type="text" name="name" id="name" required>
  </div>
  <div class="form-example">
    <label for="email">Enter your email: </label>
    <input type="email" name="email" id="email" required>
  </div>
  <div class="form-example">
    <input type="submit" value="Subscribe!">
  </div>
</form>

3. Proses alur data :
Setelah user meminta, akan diminta request ke localhost/path pada browser, server akan menerima HTTP request pada localhost/path tersebut kemudian melihat fungsi pada views.py yang sesuai dengan permintaan. Fungsi itu kemudian akan menghasilkan halaman form HTML yang akan ditampilkan oleh user. Setelah diisi dan disubmit, browser akan menghasilkan HTTP request ke url yang dituju sesuai HTML form. Hal selanjutnya bergantung kepada kode dimana kalau kode itu diminta menampilkan HTML(pada views.py) maka browser akan menampilkan HTML kepada user

4. Pertama membuat app baru yang bernama todolist menggunakan startapp. Menambahkan path todolist pada urls.py agar dapat diakses. Membuat class ToDoList pada models.py dan melakukan migrate agar fungsi masuk kedalam base. Membuat fungsi untuk register,login,dan logout pada views.py, kemudian menambahkan urls, lalu membuat html untuk register dan login. Membuat HTML utama todolist, yang akan berisi username, task yang ada, lalu tombol create baru dan logout. Routing dibuat pada urls.py. Deployment dilakukan dengan git add. git commit, git push. 