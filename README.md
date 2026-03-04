
# 📘 Analisis Modul OOP Python

## Analisis 1

Jika nilai hero1.hp diubah menjadi 500, maka HP milik objek hero1 akan berubah dari HP awal menjadi 500. Saat print(hero1.hp) dijalankan, program akan menampilkan angka 500.
<img width="1027" height="472" alt="Screenshot 2026-03-04 101320" src="https://github.com/user-attachments/assets/dc8f7c44-27fb-41c7-ba2f-23e9a02184d9" />

Hal ini terjadi karena atribut hp bersifat publik sehingga dapat diubah langsung dari luar class tanpa pembatasan atau validasi.

## Analisis 2

Parameter lawan pada method serang() menerima sebuah objek, bukan hanya string nama, karena objek memiliki atribut dan method yang bisa digunakan.

Jika hanya mengirimkan string seperti "Zilong", maka kita tidak bisa mengakses atau mengurangi HP miliknya. Dengan mengirim objek secara langsung, method serang() bisa memanggil lawan.diserang(self.attack_power) sehingga terjadi interaksi antar objek.
<img width="1029" height="588" alt="Screenshot 2026-03-04 101346" src="https://github.com/user-attachments/assets/d8b119ab-2ecc-4dca-8a18-3379bf9ff463" />

Ini menunjukkan konsep OOP bahwa objek dapat saling berinteraksi.

## Analisis 3

Jika baris super().__init__(name, hp, attack_power) dihapus pada class Mage, maka akan muncul error:

AttributeError: 'Mage' object has no attribute 'name'

Hal ini terjadi karena constructor milik parent class (Hero) tidak dijalankan, sehingga atribut name, hp, dan attack_power tidak pernah dibuat.
<img width="1015" height="859" alt="Screenshot 2026-03-04 101429" src="https://github.com/user-attachments/assets/eb4d6d0a-3c9c-412d-b48c-715f7f1386c7" />

Fungsi super() berperan untuk memanggil constructor class induk agar atribut dan method dari parent dapat diwariskan dengan benar ke class anak.

## Analisis 4
Bagian 1

Jika mencoba mengakses:

print(hero1._Hero__hp)

Nilai HP tetap dapat muncul. Hal ini terjadi karena Python menggunakan sistem Name Mangling, yaitu mengubah __hp menjadi _Hero__hp.

Walaupun bisa diakses, cara ini tidak disarankan karena melanggar prinsip Encapsulation dan standar pemrograman yang baik.

Bagian 2

Jika logika validasi pada method set_hp() dihapus dan hanya berisi:

self.__hp = nilai_baru

Kemudian dijalankan hero1.set_hp(-100), maka HP akan menjadi -100.
<img width="1033" height="650" alt="Screenshot 2026-03-04 101439" src="https://github.com/user-attachments/assets/fae7eba1-22c9-4339-8c16-25c6c48748d2" />

Hal ini membuktikan bahwa method setter sangat penting untuk menjaga integritas data agar tidak negatif atau dimanipulasi.

## Analisis 5

Jika method serang() dihapus dari class Hero yang mewarisi GameUnit, maka akan muncul error:

TypeError: Can't instantiate abstract class Hero with abstract method serang

Error tersebut berarti class Hero belum memenuhi kontrak dari abstract class GameUnit. Semua method abstrak wajib diimplementasikan.

Jika mencoba membuat objek dari GameUnit secara langsung:

unit = GameUnit()
<img width="1039" height="853" alt="Screenshot 2026-03-04 101506" src="https://github.com/user-attachments/assets/752caf31-02bc-4a26-b207-6cd55ea63a90" />

akan muncul error karena abstract class tidak boleh diinstansiasi. Abstract class hanya berfungsi sebagai blueprint atau kerangka dasar.

## Analisis 6

Jika menambahkan class baru seperti Healer tanpa mengubah looping:

for pahlawan in pasukan:
    pahlawan.serang()

Program tetap berjalan dengan lancar selama method serang() ada di class tersebut.

Hal ini menunjukkan keuntungan Polymorphism, yaitu sistem tetap berjalan tanpa perlu mengubah kode lama ketika menambahkan fitur baru.

Namun, jika nama method pada salah satu class diubah (misalnya serang() menjadi tembak_panah()), maka akan muncul error karena looping memanggil method serang() yang sudah tidak ada.
<img width="1026" height="859" alt="Screenshot 2026-03-04 101518" src="https://github.com/user-attachments/assets/7076f620-feb6-46f1-901b-5ef208868144" />

Dalam Polymorphism, nama method harus konsisten agar dapat dipanggil secara umum.
