ulang = 0
while ulang < 3:
    print("Masukkan Username Anda: ")
    nama = input()
    print("Masukkan Password Anda: ")
    password = int(input())
    if nama == "rizky" and password == 113:
        print("Login Telah Berhasil!! Apakah Anda Ingin Melanjutkan? (lanjut/berhenti)")
        proses = input()
        if proses == "berhenti":
            print("Proses Selesai")
        else:
            print("Proses Lanjut")
        print("Tesla = 1, Toyota = 2, Hyundai = 3")
        print("Masukkan Nomor Mobil Anda: ")
        nomobil = int(input())
        print("Masukkan Harga Mobil: ")
        harga = int(input())
        if nomobil == 1:
            diskon = harga * 0.17
            total = harga - diskon
            print("Total Mobil Tesla Seharga: ")
            print(total)
            break
        else:
            if nomobil == 2:
                diskon = harga * 0.21
                total = harga - diskon
                print("Total Mobil Toyota Seharga: ")
                print(total)
                break
            else:
                if nomobil == 3:
                    diskon = harga * 0.23
                    total = harga - diskon
                    print("Total Mobil Hyundai Seharga: ")
                    print(total)
                    break
                else:
                    print("Mobil Yang Anda Cari Tidak Ada!")
                    break
    else:
        print("Apa Anda Ingin Mencoba Lagi: (lanjut/berhenti)")
        proses = input()
        if proses == "berhenti":
            print("Proses Selesai")
        else:
            ulang = ulang + 1
            print("Percobaan Yang Sudah Di Coba: ")
            print(ulang)
            