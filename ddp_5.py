pilih = int(input("""selamat datang diaplikasi menghitung
1. untuk menghitung luas persegi 
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga 
                  
masukan pilahan anda: """))

match pilih:
    case 1 : 
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukan sisi persegi: "))
        luaspsg = sisi*sisi
        print("luas persegi yang sisinya ",sisi,"adalah", luaspsg)
    case 2 :
        print("kamu memilih 2 untuk menghitung lingkaran")
        jari2 = int(input("masukan jari-jari: "))
        luaslkr = 3.14 * jari2 * jari2 
        print("luas lingkaran yang jari-jarinya ", jari2, "adalah", luaslkr )
    case 3 : 
        print("kamu memilih 3 untuk menghitung segitiga ")
        alas = int(input("masukan alas segitiga "))
        tinggi = int(input("masukan tinggi segitiga: "))
        luassegitiga = 0.5 * alas * tinggi
        print("luas segitiga dengan alas ",alas, "dan tinggi",tinggi, "adalah", luassegitiga )
    case _:
        print("anda salah pilih")

print('==============================')

#list utama kendaraan 
kendaraan = ["nama kendaraan", "jenis kendaraan", "cc kendaraan", "warna kendaraan", "roda kendaraan"]

#mencetak isi dari list kendaraan
print(kendaraan)

#menambahkan value atau nilai 3 di ujung list (pakai spend())

#proses append 1 (harga kendaraan)
kendaraan.append("25.000.000")

#proses append 2 (tipe kendaraan)
kendaraan.append("matic")

#cetak nilai kendaraan setelah perubahan 
print(kendaraan)

#sisipkan nilai untuk tipe kendaraan 
kendaraan.insert(2, "honda")

#cetak hasil list akhirnya
print(kendaraan)





