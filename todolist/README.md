Pertanyaan
1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
2. Jelaskan tag HTML5 yang kamu ketahui.
3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Terdapat 3 cara untuk menambahkan style CS ke website, yaitu internal dengan menambahkan CSS ke dalam bagian head pada dokumen html, atau menghubungkan external yang mengandung semua rule css, atau yang terakhir menggunakan inline CSS. Internal CSS diletakan pada bagian head pada halaman. Style ini akan didownload setiap kali halaman dipanggil, ini akan meningkatkan kecepatan akses. Kelebihan internal adalah tidak perlu mengupload beberapa file karena html dan css bisa digunakan di file yang sama. Kekurangan nya adalah perubahan hanya terjadi pada 1 halaman sehingga tidak efisien. External CSS merupakan cara paling nyaman karena kita tinggal menaruh file eksternal pada halaman. Kelebihannya ukuran file html jadi kecil dan struktur lebih rapih, kemudian kecepatan loadingnya lebih cepat, tetatpi halaman tidak tampil secara sempurna sebelum file css eksternal tersebut selesai dipanggil. Inline CSS biasanya digunakan untuk tag html tertentu. Ini kurang direkomendasi karena harus memberikan style masing-masing. Inclne berguna jika ingin lihat perubahan langsung, sehingga enak untuk memperbaiki suatu hal, kekurangannya adalah harus diimplementasi satu-satu

2. <a> menunjukan sebuah hyper link
<b> text dalam bold style
<base> base url untuk url pada dokumen
<body> body dari sebuah dokumen
<br> break lin
<button> membuat tombol
<div> ini untuk spesifikasi sebuah section pada dokumen

3. selector adalah pattern yang diugnakan untuk memilih elemen yang ingin kita style. beberapa contoh adalah:
.class, dimana ini memilih semua elemen dengan class
elemen, memilih semua <p> elemen

4. Menambahkan setting bootstrap pada basehtml kemudian menggunakan kustomisasi template dari bootstrap. Kebanyakan menggunakan template dari web getbootstrap.com dimana langsung diimplementasi pada file-file html yang ingin diubah. Hal seperti cards digunakan forloop untuk tiap-tiap task yang telah dibuat agar dapat menampilkan card yang berisi task dibuat