# Nama Pembeli
Nama = input("Masukkan Nama Pembeli: ")

# Nama Mobil Yang Ingin Dibeli
jenis_mobil = input("Masukkan Nama Jenis Mobil: ")

# Harga Setiap Mobil
harga_mobil = int(input("Masukkan Harga Mobil: "))

# Ketika Bu Navira Membeli Mobil
if jenis_mobil == "tesla":
    diskon_tesla = harga_mobil*17/100
    harga_tesla = int(harga_mobil - diskon_tesla)
    print(f"{Nama} Ingin Membeli Mobil {jenis_mobil} maka mendapatkan diskon 17%")
    print(f"Jadi ketika {Nama} Membeli Mobil {jenis_mobil} Seharga {harga_tesla}")
elif jenis_mobil == "toyota":
    diskon_toyota = harga_mobil*21/100
    harga_toyota = int(harga_mobil - diskon_toyota)
    print(f"{Nama} Ingin Membeli Mobil {jenis_mobil} maka mendapatkan diskon 21%")
    print(f"Jadi ketika {Nama} Membeli Mobil {jenis_mobil} Seharga {harga_toyota}")
elif jenis_mobil == "hyundai":
    diskon_hyundai = harga_mobil*23/100
    harga_hyundai = int(harga_mobil - diskon_hyundai)
    print(f"{Nama} Ingin Membeli Mobil {jenis_mobil} Maka Mendapatkan Diskon 23%")
    print(f"Jadi ketika {Nama} Membeli Mobil {jenis_mobil} Seharga {harga_hyundai}")
else:
    print("Tidak Ada Mobil Yang ingin dibeli")