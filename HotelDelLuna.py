# sys adalah modul untuk mengakses konfigurasi untuk berinteraksi dengan sistem operasi
import sys as program # Memamnggil sys sebagai program
# Membuat Program Pemesanan Tiket Kamar Hotel, Hotel Del Luna
def garis1(): # Membuat Fungsi garis agar mudah untuk di panggil
    print("-----------------------------------------------------------")

def main(): # Membuat fungsi main, agar tidak mengulang lagi
    # Ini adalah judul
    print("===========================================================")
    print("                    - HOTEL DEL LUNA -")
    print("                      Selamat Datang")
    print("===========================================================\n")
    
    # Keterangan
    print("Keterangan")
    print("1. Penthouse Room: Harga Rp. 650.000/malam")
    print("2. Kamar Deluxe  : Harga Rp. 500.000/malam")
    print("3. Kamar Superior: Harga Rp. 430.000/malam")
    print("4. Kamar Standard: Harga Rp. 280.000/malam")

    garis1() # Fungsi dipanggil, untuk menampilkan garis

    # Pilihan
    print("Silahkan Pilih Kamar Pesanan Anda")
    tipe_kmr = input("Masukkan Tipe Kamar (1/2/3/4): ")
    inap = int(input("Berapa Lama Menginap: "))

# Proses
    if tipe_kmr == "1":     # Percabangan Bersarang
        tipe = "Penthouse"
        # Program Diskon
        if inap >= 3:
            diskon = 0.1 # diskon 10 persen, atau 0.1
            dsk = ("10%") # ini untuk pernyataan diskon di struk
            hrg = int((inap * 650000) * diskon) # harga awal untuk menghitung besar uang diskon
            total = int((inap * 650000) - hrg) # menghitung total (harga awal dikurang diskon)
        else:
            dsk = ("-") # ini untuk pernyataan diskon di struk
            total = int(inap * 650000) # tidak ada diskon, dan langsung menampilkan harga awal
        garis1()
        print("Pesanan kamar bertipe", tipe, "dengan harga Rp.",total)
        lanjut = input("Lanjutkan pesanan? (Y/N): ")
        print("")
        if lanjut == "Y" or lanjut == "y":
            garis1()
            # Proses Output
            print("                     STRUK PEMBAYARAN")
            garis1()
            nama = input("Masukkan Nama Pemesan    : ")
            print("Deskripsi                : Pesanan Kamar Hotel Tipe",tipe)
            print("Diskon                   :",dsk)
            print("Tagihan                  :",total)
            bayar = int(input("Masukkan Uang Pembayaran : "))
            if bayar > total:
                kembali = bayar - total
                print("Kembali                  :",kembali)
                garis1()
                print("Pemesanan kamar bertipe", tipe, "sukses!")
            elif bayar == total:
                kembali = ("-")
                print("Kembali                  :",kembali)
                garis1()
                print("Pemesanan kamar bertipe", tipe, "sukses!")
            else:
                garis1()
                print("Terjadi Kesalahan!")
                print("Pemesanan kamar bertipe", tipe, "gagal!")
        elif lanjut == "N" or lanjut == "n":
            print("Anda membatalkan pesanan")
        else:
            print("Keyword Error!")
    elif tipe_kmr == "2":
        tipe = "Deluxe"
        # Program Diskon
        if inap >= 3:
            diskon = 0.1 # diskon 10 persen, atau 0.1
            dsk = ("10%") # ini untuk pernyataan diskon di struk
            hrg = int((inap * 500000) * diskon) # harga awal untuk menghitung besar uang diskon
            total = int((inap * 500000) - hrg) # menghitung total (harga awal dikurang diskon)
        else:
            dsk = ("-") # ini untuk pernyataan diskon di struk
            total = int(inap * 500000) # tidak ada diskon, dan langsung menampilkan harga awal
        garis1()
        print("Pesanan kamar bertipe", tipe, "dengan harga Rp.",total)
        lanjut = input("Lanjutkan pesanan? (Y/N): ")
        print("")
        if lanjut == "Y" or lanjut == "y":
            garis1()
            # Proses Output
            print("                     STRUK PEMBAYARAN")
            garis1()
            nama = input("Masukkan Nama Pemesan    : ")
            print("Deskripsi                : Pesanan Kamar Hotel Tipe",tipe)
            print("Diskon                   :",dsk)
            print("Tagihan                  :",total)
            bayar = int(input("Masukkan Uang Pembayaran : "))
            if bayar > total:
                kembali = bayar - total
                print("Kembali                  :",kembali)
                garis1()
                print("Pemesanan kamar bertipe", tipe, "sukses!")
            elif bayar == total:
                kembali = ("-")
                print("Kembali                  :",kembali)
                garis1()
                print("Pemesanan kamar bertipe", tipe, "sukses!")
            else:
                garis1()
                print("Terjadi Kesalahan!")
                print("Pemesanan kamar bertipe", tipe, "gagal!")
        elif lanjut == "N" or lanjut == "n":
            print("Anda membatalkan pesanan")
        else:
            print("Keyword Error!")
    elif tipe_kmr == "3":
        tipe = "Superior"
        # Program Diskon
        if inap >= 3:
            diskon = 0.1 # diskon 10 persen, atau 0.1
            dsk = ("10%") # ini untuk pernyataan diskon di struk
            hrg = int((inap * 430000) * diskon) # harga awal untuk menghitung besar uang diskon
            total = int((inap * 430000) - hrg) # menghitung total (harga awal dikurang diskon)
        else:
            dsk = ("-") # ini untuk pernyataan diskon di struk
            total = int(inap * 430000) # tidak ada diskon, dan langsung menampilkan harga awal
        garis1()
        print("Pesanan kamar bertipe", tipe, "dengan harga Rp.",total)
        lanjut = input("Lanjutkan pesanan? (Y/N): ")
        print("")
        if lanjut == "Y" or lanjut == "y":
            garis1()
            # Proses Output
            print("                     STRUK PEMBAYARAN")
            garis1()
            nama = input("Masukkan Nama Pemesan    : ")
            print("Deskripsi                : Pesanan Kamar Hotel Tipe",tipe)
            print("Diskon                   :",dsk)
            print("Tagihan                  :",total)
            bayar = int(input("Masukkan Uang Pembayaran : "))
            if bayar > total:
                kembali = bayar - total
                print("Kembali                  :",kembali)
                garis1()
                print("Pemesanan kamar bertipe", tipe, "sukses!")
            elif bayar == total:
                kembali = ("-")
                print("Kembali                  :",kembali)
                garis1()
                print("Pemesanan kamar bertipe", tipe, "sukses!")
            else:
                garis1()
                print("Terjadi Kesalahan!")
                print("Pemesanan kamar bertipe", tipe, "gagal!")
        elif lanjut == "N" or lanjut == "n":
            print("Anda membatalkan pesanan")
        else:
            print("Keyword Error!")
    elif tipe_kmr == "4":
        tipe = "Standard"
        # Program Diskon
        if inap >= 3:
            diskon = 0.1 # diskon 10 persen, atau 0.1
            dsk = ("10%") # ini untuk pernyataan diskon di struk
            hrg = int((inap * 280000) * diskon) # harga awal untuk menghitung besar uang diskon
            total = int((inap * 280000) - hrg) # menghitung total (harga awal dikurang diskon)
        else:
            dsk = ("-") # ini untuk pernyataan diskon di struk
            total = int(inap * 280000) # tidak ada diskon, dan langsung menampilkan harga awal
        garis1()
        print("Pesanan kamar bertipe", tipe, "dengan harga Rp.",total)
        lanjut = input("Lanjutkan pesanan? (Y/N): ")
        print("")
        if lanjut == "Y" or lanjut == "y":
            garis1()
            # Proses Output
            print("                     STRUK PEMBAYARAN")
            garis1()
            nama = input("Masukkan Nama Pemesan    : ")
            print("Deskripsi                : Pesanan Kamar Hotel Tipe",tipe)
            print("Diskon                   :",dsk)
            print("Tagihan                  :",total)
            bayar = int(input("Masukkan Uang Pembayaran : "))
            if bayar > total:
                kembali = bayar - total
                print("Kembali                  :",kembali)
                garis1()
                print("Pemesanan kamar bertipe", tipe, "sukses!")
            elif bayar == total:
                kembali = ("-")
                print("Kembali                  :",kembali)
                garis1()
                print("Pemesanan kamar bertipe", tipe, "sukses!")
            else:
                garis1()
                print("Terjadi Kesalahan!")
                print("Pemesanan kamar bertipe", tipe, "gagal!")
        elif lanjut == "N" or lanjut == "n":
            print("Anda membatalkan pesanan")
        else:
            print("Keyword Error!")
    else:
        print("Ada Kesalahan!")
# Akhir dari percabangan bersarang

# While Loop dengan metode 'While True'
while True: # Perulangan dengan memanfaatkan 'import sys'
    main() # memanggil fungsi main
    ulang = input("\nIngin pesan kamar lagi?(Y/N): ")
    if ulang == 'Y' or ulang == 'y':
        print("\n")
        continue # Untuk eksekusi lanjutan program
    elif ulang == 'N' or ulang == 'n':
        # 'program' sebagai sys
        program.exit() # Program akan keluar atau selesai
    else: # Pernyataan jika tidak memilih Y ataupun N
        print("Ada Kesalahan!") # Menampilkan sebuah alert
        # 'program' sebagai sys
        program.exit() # Setelahnya akan dikeluarkan