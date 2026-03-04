from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0 
        self.__harga_dasar = harga_dasar  
        
    def get_stok(self):
        return self.__stok
    def get_harga_dasar(self):
        return self.__harga_dasar
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor
    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")

    def hitung_harga_total(self, jumlah):
        harga = self.get_harga_dasar()
        pajak = 0.10 * harga
        subtotal = (harga + pajak) * jumlah

        print(f"   Harga Dasar: Rp {harga:,}".replace(",", ".") +
              f" | Pajak(10%): Rp {int(pajak):,}".replace(",", "."))
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}".replace(",", "."))

        return subtotal


class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")

    def hitung_harga_total(self, jumlah):
        harga = self.get_harga_dasar()
        pajak = 0.05 * harga
        subtotal = (harga + pajak) * jumlah

        print(f"   Harga Dasar: Rp {harga:,}".replace(",", ".") +
              f" | Pajak(5%): Rp {int(pajak):,}".replace(",", "."))
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}".replace(",", "."))

        return subtotal

def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0

    for i, (barang, jumlah) in enumerate(daftar_barang, start=1):
        print(f"{i}. ", end="")
        barang.tampilkan_detail()
        total += barang.hitung_harga_total(jumlah)
        print()

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}".replace(",", "."))
    print("----------------------------------------")


print("--- SETUP DATA ---")

laptop1 = Laptop("ROG Zephyrus", 20000000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15000000, "12MP")

laptop1.tambah_stok(10)
hp1.tambah_stok(-5)  
hp1.tambah_stok(20)

keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

# 4. Proses transaksi
proses_transaksi(keranjang)