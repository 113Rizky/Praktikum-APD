akuns = {}
daftar_serial = {"Spongebob SquarePants": 7, "Money Heist": 5, "Squid Game": 24}

while True:
    print("--- Selamat Datang Di Aplikasi APDFLIX ---")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("_____________________")
    opsi = input("Pilih opsi: ")

    if opsi == "1":
        print("Halo Pengguna Akun Baru Silahkan isi data tersebut ^^")
        username = input("Masukkan Username Anda: ")
        if username in akuns:
            print("Username Sudah Terpakai, Silahkan Coba Lagi.")
        else:
            password = input("Password: ")
            role = input("Role (admin/pengguna): ")
            akuns[username] = {"password": password, "role": role}
            print(f"Akun berhasil terdaftar dengan username: {username}")

    elif opsi == "2":
        print("Silakan login!")
        username = input("Username: ")
        password = input("Password: ")

        if username in akuns and akuns[username]["password"] == password:
            print(f"Selamat datang {username}! Anda login sebagai {akuns[username]['role']}.")

            if akuns[username]["role"] == 'admin':
                while True:
                    print("--- Menu Admin ---")
                    print("1. Tambah serial baru")
                    print("2. Lihat daftar serial")
                    print("3. Update jumlah episode")
                    print("4. Hapus serial")
                    print("5. Logout")
                    print("_____________________")
                    admin_opsi = input("Pilih opsi: ")

                    if admin_opsi == "1":
                        judul = input("Judul serial baru: ")
                        jumlah_episode = input("Jumlah episode: ")
                        if jumlah_episode.isdigit():
                            daftar_serial[judul] = int(jumlah_episode)
                            print(f"Serial '{judul}' berhasil ditambahkan.")
                        else:
                            print("Input tidak valid. Jumlah episode harus berupa angka.")

                    elif admin_opsi == "2":
                        if not daftar_serial:
                            print("Tidak ada serial dalam daftar.")
                        else:
                            print("Daftar Serial:")
                            for judul, jumlah in daftar_serial.items():
                                print(f"Judul: {judul}, Jumlah Episode: {jumlah}")

                    elif admin_opsi == "3":
                        if not daftar_serial:
                            print("Tidak ada serial yang bisa diupdate.")
                        else:
                            judul = input("Masukkan judul serial yang ingin diupdate: ")
                            if judul in daftar_serial:
                                tambahan_episode = input("Jumlah episode yang ingin ditambahkan: ")
                                if tambahan_episode.isdigit():
                                    daftar_serial[judul] += int(tambahan_episode)
                                    print(f"Jumlah episode untuk serial '{judul}' berhasil diupdate.")
                                else:
                                    print("Input tidak valid. Jumlah episode harus berupa angka.")
                            else:
                                print("Serial tidak ditemukan.")

                    elif admin_opsi == "4":
                        if not daftar_serial:
                            print("Tidak ada serial yang bisa dihapus.")
                        else:
                            judul = input("Masukkan judul serial yang ingin dihapus: ")
                            if judul in daftar_serial:
                                del daftar_serial[judul]
                                print(f"Serial '{judul}' berhasil dihapus.")
                            else:
                                print("Serial tidak ditemukan.")

                    elif admin_opsi == "5":
                        print("Anda telah logout.")
                        break
                    else:
                        print("Input tidak valid. Silakan pilih 1-5.")

            else:  # Pengguna biasa
                while True:
                    print("--- Menu Pengguna ---")
                    print("1. Lihat daftar serial")
                    print("2. Logout")
                    print("_____________________")
                    pengguna_opsi = input("Pilih opsi: ")

                    if pengguna_opsi == "1":
                        if not daftar_serial:
                            print("Tidak ada serial dalam daftar.")
                        else:
                            print("Daftar Serial:")
                            for judul, jumlah in daftar_serial.items():
                                print(f"Judul: {judul}, Jumlah Episode: {jumlah}")
                    elif pengguna_opsi == "2":
                        print("Anda telah logout.")
                        break
                    else:
                        print("Input tidak valid. Silakan pilih 1-2.")
        else:
            print("Username atau password salah. Silakan coba lagi.")

    elif opsi == "3":
        print("Apakah Anda yakin ingin keluar dari aplikasi?")
        print("1. Ya")
        print("2. Tidak")
        print("_____________________")
        konfirmasi = input("Pilih opsi: ")

        if konfirmasi == "1":
            print("Terima kasih sudah menggunakan aplikasi.")
            break
        elif konfirmasi == "2":
            print("Anda tetap berada dalam aplikasi.")
        else:
            print("Input tidak valid. Silakan pilih 1 atau 2.")                                                           
            