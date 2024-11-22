#Untuk Menghitung Waktu Habisnya Langganan
from datetime import datetime, timedelta

#Mempercantik Isi Pada Judul Film
from prettytable import PrettyTable

#Mewarnai Tulisan Yang Ada Di Output
from colorama import init, Fore
init()

#Menjaga Privasi Pada Input Sandi
import pwinput

# Daftar Film
Judul_Film = [
    {"No" : 1, "Film": "Despicable Me", "Genre": "Komedi", "Batasan Usia": "SU"},
    {"No" : 2,"Film": "Inside Out", "Genre": "Komedi", "Batasan Usia": "SU"},
    {"No" : 3,"Film": "Home Alone", "Genre": "Komedi", "Batasan Usia": "SU"},
    {"No" : 4,"Film": "Cek Toko Sebelah", "Genre": "Komedi", "Batasan Usia": "13+"},
    {"No" : 5,"Film": "Agak Laen", "Genre": "Komedi", "Batasan Usia": "13+"},
    {"No" : 6,"Film": "Avenger", "Genre": "Aksi", "Batasan Usia": "13+"},
    {"No" : 7,"Film": "Kingsman", "Genre": "Aksi", "Batasan Usia": "17+"},
    {"No" : 8,"Film": "Extraction", "Genre": "Aksi", "Batasan Usia": "17+"},
    {"No" : 9,"Film": "The Conjuring", "Genre": "Horor", "Batasan Usia": "17+"},
    {"No" : 10,"Film": "Annabelle", "Genre": "Horor", "Batasan Usia": "17+"},
    {"No" : 11,"Film": "Pengabdi Setan", "Genre": "Horor", "Batasan Usia": "17+"},
    {"No" : 12,"Film": "Dilan 1990", "Genre": "Romantis", "Batasan Usia": "13+"},
    {"No" : 13,"Film": "Mariposa", "Genre": "Romantis", "Batasan Usia": "13+"}
]

Judul_film_premium = [
    {"No" : 1,"Film": "Despicable Me", "Genre": "Komedi", "Batasan Usia": "SU"},
    {"No" : 2,"Film": "Inside Out", "Genre": "Komedi", "Batasan Usia": "SU"},
    {"No" : 3,"Film": "Home Alone", "Genre": "Komedi", "Batasan Usia": "SU"},
    {"No" : 4,"Film": "Cek Toko Sebelah", "Genre": "Komedi", "Batasan Usia": "13+"},
    {"No" : 5,"Film": "Agak Laen", "Genre": "Komedi", "Batasan Usia": "13+"},
    {"No" : 6,"Film": "How to Make Millions Before Grandma Dies", "Genre": "Komedi", "Batasan Usia": "13+"},
    {"No" : 7,"Film": "Avenger", "Genre": "Aksi", "Batasan Usia": "13+"},
    {"No" : 8,"Film": "Kingsman", "Genre": "Aksi", "Batasan Usia": "17+"},
    {"No" : 9,"Film": "Extraction", "Genre": "Aksi", "Batasan Usia": "17+"},
    {"No" : 10,"Film": "Dune", "Genre": "Romantis", "Batasan Usia": "17+"},
    {"No" : 11,"Film": "Hitman", "Genre": "Aksi", "Batasan Usia": "17+"},
    {"No" : 12,"Film": "The Conjuring", "Genre": "Horor", "Batasan Usia": "17+"},
    {"No" : 13,"Film": "Annabelle", "Genre": "Horor", "Batasan Usia": "17+"},
    {"No" : 14,"Film": "Pengabdi Setan", "Genre": "Horor", "Batasan Usia": "17+"},
    {"No" : 15,"Film": "Perempuan Tanah Jahanam", "Genre": "Horor", "Batasan Usia": "17+"},
    {"No" : 16,"Film": "Titanic", "Genre": "Romantis", "Batasan Usia": "17+"},
    {"No" : 17,"Film": "Dilan 1990", "Genre": "Romantis", "Batasan Usia": "13+"},
    {"No" : 18,"Film": "Mariposa", "Genre": "Romantis", "Batasan Usia": "13+"},
    {"No" : 19,"Film": "La la land", "Genre": "Romantis", "Batasan Usia": "17+"},
    {"No" : 20,"Film": "Tenggelamnya Kapal Van Der Wijck", "Genre": "Romantis", "Batasan Usia": "17+"}
]

# Fungsi Menampilkan Semua Film Non Premium
def lihat_menu_film_Non_premium():
    print("=== Lihat Menu Film ===")
    table = PrettyTable(["No", "film", "Genre", "Batasan Usia"])
    for info in Judul_Film:
        table.add_row([info["No"], info["Film"], info["Genre"], info["Batasan Usia"], ])
    print(table)

# Fungsi Menampilkan Semua Film Premium
def lihat_menu_film_premium():
    print("=== Lihat Menu Film Premium ===")
    table = PrettyTable(["No", "film", "Genre", "Batasan Usia"])
    for info in Judul_film_premium:
        table.add_row([info["No"], info["Film"], info["Genre"], info["Batasan Usia"], ])
    print(table)

#-----------------------------------------------------------------------------------------------------------------------------------------
# Akun Khusus Admin
akun_admin = "admin"
password_admin = "admin123"

#Melihat Pengguna Aplikasi
def tampilkan_daftar_pengguna():
    print("=== Daftar Pengguna ===")
    
    print("Pengguna Non-Premium:")
    for username in akun_non_premium:
        print(f"- {username}")
    
    print("Pengguna Premium:")
    for username, details in akun_premium_details.items():
        if details["berakhir"] >= datetime.now():
            print(f"- {username} (Berakhir: {details['berakhir'].strftime('%d-%m-%Y')})")
    
    print("Pengguna Trial:")
    if akun_trial["aktif"]:
        print(f"- {akun_non_premium} (Berakhir: {akun_trial['berakhir'].strftime('%d-%m-%Y')})")


# Fungsi Menambah Film Baru
def kelola_daftar_film():
    while True:
        # Tampilkan daftar film biasa
        print("=== Daftar Film Biasa ===")
        for film in Judul_Film:
            print(f"No: {film['No']}, Film: {film['Film']}, Genre: {film['Genre']}, Batasan Usia: {film['Batasan Usia']}")

        # Tampilkan daftar film premium
        print("=== Daftar Film Premium ===")
        for film in Judul_film_premium:
            print(f"No: {film['No']}, Film: {film['Film']}, Genre: {film['Genre']}, Batasan Usia: {film['Batasan Usia']}")

        print("=== Pilih Film Yang Ingin Di Tambah ===")
        print("1. Tambah film ke daftar biasa")
        print("2. Tambah film ke daftar premium")
        print("3. Tambah film ke kedua daftar")
        print("4. Keluar")
        print("_"* 40)

        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ").strip()
        if pilihan not in ["1", "2", "3", "4"]:
            print("Pilihan tidak valid! Masukkan angka 1, 2, 3, atau 4.")
            continue
        elif pilihan == "4":
            print("Keluar dari pengelolaan daftar film.")
            break

        # Masukkan data film baru
        print("\n=== Tambah Film Baru ===")
        while True:
            nama_film = input("Masukkan nama film: ").strip()
            if not nama_film:
                print("Nama film tidak boleh kosong. Silakan coba lagi.")
            elif (pilihan in ["1", "3"] and any(film["Film"].strip().lower() == nama_film.lower() for film in Judul_Film)) or \
                 (pilihan in ["2", "3"] and any(film["Film"].strip().lower() == nama_film.lower() for film in Judul_film_premium)):
                print(f"Nama film '{nama_film}' sudah ada dalam daftar. Silakan masukkan nama film lain.")
            else:
                break

        while True:
            genre_film = input("Masukkan genre film: ").strip()
            if genre_film:
                break
            print("Genre film tidak boleh kosong. Silakan coba lagi.")

        valid_usia = ["SU", "13+", "17+"]
        while True:
            batasan_usia = input("Masukkan batasan usia film (SU, 13+, 17+): ").strip()
            if batasan_usia in valid_usia:
                break
            print("Batasan usia tidak valid. Pilih salah satu: SU, 13+, atau 17+.")

        # Tambah ke daftar berdasarkan pilihan
        if pilihan in ["1", "3"]:
            no_biasa = len(Judul_Film) + 1
            film_baru_biasa = {
                "No": no_biasa,
                "Film": nama_film,
                "Genre": genre_film,
                "Batasan Usia": batasan_usia
            }
            Judul_Film.append(film_baru_biasa)
            print(f"Film '{nama_film}' berhasil ditambahkan ke daftar biasa dengan No: {no_biasa}.")

        if pilihan in ["2", "3"]:
            no_premium = len(Judul_film_premium) + 1
            film_baru_premium = {
                "No": no_premium,
                "Film": nama_film,
                "Genre": genre_film,
                "Batasan Usia": batasan_usia
            }
            Judul_film_premium.append(film_baru_premium)
            print(f"Film '{nama_film}' berhasil ditambahkan ke daftar premium dengan No: {no_premium}.")






# Fungsi Update Film
def update_film():
    print("=== Update Data Film ===")

    while True:
        if not Judul_Film and not Judul_film_premium:
            print("Tidak ada data film untuk diupdate!")
            return

        # Tampilkan opsi daftar
        print("\nPilih daftar untuk diupdate:")
        print("1. Update daftar biasa")
        print("2. Update daftar premium")
        print("3. Kembali ke menu admin")
        print("_"* 40)
        pilihan_daftar = input("Masukkan pilihan (1/2/3): ").strip()
        if not pilihan_daftar or pilihan_daftar not in ["1", "2", "3"]:
            print("Pilihan tidak valid! Masukkan angka 1, 2, atau 3.")
            continue

        if pilihan_daftar == "3":
            print("Kembali ke menu admin.")
            return

        # Pilih daftar sesuai opsi
        if pilihan_daftar == "1":
            daftar = Judul_Film
            daftar_nama = "biasa"
        elif pilihan_daftar == "2":
            daftar = Judul_film_premium
            daftar_nama = "premium"

        if not daftar:
            print(f"Daftar film {daftar_nama} kosong! Tidak ada yang bisa diupdate.")
            continue

        # Tampilkan daftar film yang dipilih
        print(f"\n=== Daftar Film {daftar_nama.capitalize()} ===")
        for i, film in enumerate(daftar):
            print(f"{i + 1}. {film['Film']} - Genre: {film['Genre']}, Batas Usia: {film['Batasan Usia']}")

        # Pilih film untuk diupdate
        while True:
            try:
                nomor = input("Masukkan nomor film yang ingin diubah: ").strip()
                if not nomor:
                    print("Input tidak boleh kosong! Silakan coba lagi.")
                    continue
                nomor = int(nomor) - 1
                if nomor < 0 or nomor >= len(daftar):
                    print("Nomor film tidak valid! Silakan coba lagi.")
                    continue
                break
            except ValueError:
                print("Input harus berupa angka! Silakan coba lagi.")

        film_dipilih = daftar[nomor]
        print(f"Film yang dipilih: {film_dipilih['Film']}")

        # Konfirmasi perubahan
        while True:
            yakin = input("Apakah Anda yakin ingin mengubah data film ini? (iya/tidak): ").strip().lower()
            if not yakin:
                print("Input tidak boleh kosong! Silakan coba lagi.")
            elif yakin not in ['iya', 'tidak']:
                print("Pilihan tidak valid! Harus 'iya' atau 'tidak'.")
            else:
                break

        if yakin != 'iya':
            print("Perubahan dibatalkan.")
            continue

        # Tampilkan opsi perubahan
        print("=== Pilihan Perubahan ===")
        print("1. Ubah Nama Film")
        print("2. Ubah Genre")
        print("3. Ubah Batas Usia")
        print("4. Ubah Semua")

        while True:
            try:
                pilihan = input("Masukkan pilihan: ").strip()
                if not pilihan:
                    print("Pilihan tidak boleh kosong! Silakan coba lagi.")
                    continue
                pilihan = int(pilihan)
                if pilihan not in [1, 2, 3, 4]:
                    print("Pilihan tidak valid! Silakan coba lagi.")
                    continue
                break
            except ValueError:
                print("Input harus berupa angka! Silakan coba lagi.")

        # Perubahan sesuai pilihan
        if pilihan == 1 or pilihan == 4:
            while True:
                nama_film_baru = input("Masukkan nama film baru: ").strip()
                if not nama_film_baru:
                    print("Nama film tidak boleh kosong! Silakan coba lagi.")
                elif nama_film_baru == film_dipilih['Film']:
                    print("Nama film baru tidak boleh sama dengan nama sebelumnya! Silakan coba lagi.")
                else:
                    film_dipilih['Film'] = nama_film_baru
                    break

        if pilihan == 2 or pilihan == 4:
            while True:
                genre_baru = input("Masukkan genre baru: ").strip()
                if not genre_baru:
                    print("Genre tidak boleh kosong! Silakan coba lagi.")
                elif genre_baru == film_dipilih['Genre']:
                    print("Genre baru tidak boleh sama dengan genre sebelumnya! Silakan coba lagi.")
                else:
                    film_dipilih['Genre'] = genre_baru
                    break

        if pilihan == 3 or pilihan == 4:
            valid_usia = ["SU", "13+", "17+"]
            while True:
                batas_usia = input("Masukkan batas usia baru (SU, 13+, 17+): ").strip()
                if not batas_usia:
                    print("Batas usia tidak boleh kosong! Silakan coba lagi.")
                elif batas_usia not in valid_usia:
                    print("Batas usia tidak valid! Pilih salah satu dari SU, 13+, atau 17+.")
                elif batas_usia == film_dipilih['Batasan Usia']:
                    print("Batas usia baru tidak boleh sama dengan batas usia sebelumnya! Silakan coba lagi.")
                else:
                    film_dipilih['Batasan Usia'] = batas_usia
                    break

        print("Data film berhasil diperbarui!")
        print(f"Film setelah diupdate: {film_dipilih['Film']} - Genre: {film_dipilih['Genre']}, Batas Usia: {film_dipilih['Batasan Usia']}")

        # Tanya pengguna apakah ingin mengupdate film lain
        while True:
            lanjut = input("Ingin kembali ke menu admin? (iya/tidak): ").strip().lower()
            if not lanjut:
                print("Input tidak boleh kosong! Silakan coba lagi.")
            elif lanjut == 'iya':
                print("Kembali ke menu admin.")
                return
            elif lanjut == 'tidak':
                print("Kembali ke tampilan update.")
                break
            else:
                print("Pilihan tidak valid! Harus 'iya' atau 'tidak'.")


        

# Menghapus Film
def Menghapus_Film():
    print("=== Hapus Film ===")
    
    if not Judul_Film and not Judul_film_premium:
        print("Tidak ada film dalam daftar biasa maupun premium.")
        return

    # Pilih daftar yang akan dihapus
    print("\nPilih daftar film:")
    print("1. Daftar biasa")
    print("2. Daftar premium")
    print("3. Kembali ke menu")

    while True:
        pilihan_daftar = input("Masukkan pilihan (1/2/3): ").strip()
        if not pilihan_daftar:
            print("Input tidak boleh kosong. Silakan coba lagi.")
        elif pilihan_daftar not in ["1", "2", "3"]:
            print("Pilihan tidak valid. Masukkan angka 1, 2, atau 3.")
        else:
            break

    if pilihan_daftar == "3":
        print("Kembali ke menu.")
        return

    # Tentukan daftar yang dipilih
    if pilihan_daftar == "1":
        daftar = Judul_Film
        daftar_nama = "biasa"
    elif pilihan_daftar == "2":
        daftar = Judul_film_premium
        daftar_nama = "premium"

    if not daftar:
        print(f"Daftar film {daftar_nama} kosong! Tidak ada yang bisa dihapus.")
        return

    # Tampilkan daftar film yang dipilih
    print(f"=== Daftar Film {daftar_nama.capitalize()} ===")
    for i, film in enumerate(daftar):
        print(f"{i + 1}. {film['Film']} - Genre: {film['Genre']}, Batas Usia: {film['Batasan Usia']}")

    # Pilih film yang akan dihapus
    while True:
        try:
            pilihan = input(f"Pilih nomor film yang ingin dihapus (1 - {len(daftar)}): ").strip()
            if not pilihan:
                print("Input tidak boleh kosong. Silakan coba lagi.")
                continue
            pilihan = int(pilihan)
            if 1 <= pilihan <= len(daftar):
                break
            else:
                print(f"Nomor tidak valid. Pilih angka antara 1 dan {len(daftar)}.")
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

    # Film yang dipilih
    film_terpilih = daftar[pilihan - 1]
    print(f"\nAnda memilih: {film_terpilih['Film']} - Genre: {film_terpilih['Genre']}, Batas Usia: {film_terpilih['Batasan Usia']}")

    # Konfirmasi penghapusan
    while True:
        print("pakah Anda ingin menghapus film ini?")
        print("1. Hapus film ini.")
        print("2. Pilih ulang.")
        print("3. Batal.")
        konfirmasi = input("Pilih (1/2/3): ").strip()

        if konfirmasi == "1":
            daftar.pop(pilihan - 1)
            print(f"Film '{film_terpilih['Film']}' berhasil dihapus.")
            
            # Opsi setelah penghapusan
            while True:
                print("\nApakah Anda ingin menghapus film lain?")
                print("1. Ya, hapus film lain.")
                print("2. Tidak, kembali ke menu.")
                opsi_lanjut = input("Pilih (1/2): ").strip()

                if opsi_lanjut == "1":
                    Menghapus_Film()  # Panggil ulang fungsi untuk menghapus film lain
                    break
                elif opsi_lanjut == "2":
                    print("Kembali ke menu.")
                    return  # Kembali ke menu sebelumnya
                else:
                    print("Input tidak valid. Silakan pilih 1 atau 2.")
            break  # Keluar dari loop konfirmasi penghapusan
        elif konfirmasi == "2":
            print("Mengedit pilihan...")
            return Menghapus_Film()  # Panggil ulang fungsi untuk memilih ulang
        elif konfirmasi == "3":
            print("Penghapusan dibatalkan.")
            return  # Kembali ke menu sebelumnya
        else:
            print("Input tidak valid. Silakan pilih opsi yang tersedia.")


#------------------------------------------------------------------------------------------------------------------------------------------------

#Fungsi User
akun_non_premium = {}
akun_premium = {}
akun_trial = {"aktif": False, "berakhir": None}
akun_premium_details = {}

# Daftar User
def daftar_akun():
    global akun_non_premium  
    print("=== Daftar Akun Baru ===")
    
    while True:
        # Input username
        username = input("Masukkan username (hanya huruf, tidak boleh kosong): ").strip()

        # Validasi username
        if not username:
            print("Username tidak boleh kosong!")
        elif not username.isalpha():
            print("Username hanya boleh terdiri dari huruf!")
        elif username in akun_non_premium:
            print("Username sudah terdaftar, silakan gunakan nama lain!")
        else:
            break

    while True:
        # Input password
        password = input("Masukkan password (harus lebih dari 3 karakter, tidak boleh kosong): ").strip()

        # Validasi password
        if not password:
            print("Password tidak boleh kosong!")
        elif len(password) <= 3:
            print("Password harus lebih dari 3 karakter!")
        else:
            break

    while True:
        # Konfirmasi data
        print("=== Konfirmasi Akun ===")
        print(f"Username: {username}")
        print(f"Password: {password}")
        konfirmasi = input("Apakah data ini sudah benar? (ya/tidak): ").strip().lower()

        if konfirmasi == "ya":
            # Simpan akun ke database
            akun_non_premium[username] = password
            print("Akun berhasil didaftarkan! Anda sekarang dapat login.")
            break
        elif konfirmasi == "tidak":
            print("Pilih opsi:")
            print("1. Edit Username")
            print("2. Edit Password")
            print("3. Kembali ke awal pendaftaran")
            print("_" * 40)
            opsi = input("Masukkan pilihan (1/2/3): ").strip()

            if opsi == "1":
                # Edit username
                while True:
                    new_username = input("Masukkan username baru (hanya huruf, tidak boleh kosong): ").strip()

                    # Validasi username
                    if not new_username:
                        print("Username tidak boleh kosong!")
                    elif not new_username.isalpha():
                        print("Username hanya boleh terdiri dari huruf!")
                    elif new_username in akun_non_premium:
                        print("Username sudah terdaftar, silakan gunakan nama lain!")
                    else:
                        username = new_username  # Update username
                        print("\nUsername berhasil diperbarui!")
                        break
            elif opsi == "2":
                # Edit password
                while True:
                    new_password = input("Masukkan password baru (harus lebih dari 3 karakter): ").strip()

                    # Validasi password
                    if not new_password:
                        print("Password tidak boleh kosong!")
                    elif len(new_password) <= 3:
                        print("Password harus lebih dari 3 karakter!")
                    else:
                        password = new_password  # Update password
                        print("\nPassword berhasil diperbarui!")
                        break
            elif opsi == "3":
                print("\nKembali ke awal pendaftaran.")
                return  # Kembali ke awal fungsi daftar_akun
            else:
                print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")
        else:
            print("Input tidak valid! Silakan pilih 'ya' atau 'tidak'.")

# Login User
def login():
    global akun_non_premium
    print("\n=== Login ===")
    attempts = 0

    while attempts < 3:
        username = input("Masukkan username: ").strip()
        password = pwinput.pwinput("Masukkan password: ").strip()

        # Validasi input kosong
        if not username or not password:
            print("Username dan password tidak boleh kosong!")
            continue

        # Cek apakah username terdaftar
        if username not in akun_non_premium:
            print("Username belum terdaftar. Silakan daftar terlebih dahulu.")
            print("1. Daftar sekarang")
            print("2. Keluar")
            opsi = input("Masukkan pilihan Anda (1/2): ").strip()

            if opsi == "1":
                daftar_akun()
                return  # Kembali ke menu login setelah daftar
            elif opsi == "2":
                print("Terima kasih! Anda keluar dari sistem login.")
                return
            else:
                print("Pilihan tidak valid! Kembali ke login.")
                continue

        # Cek password
        if akun_non_premium[username] == password:
            print(f"\nSelamat datang, {username}! Login berhasil.")
            return  # Masuk ke menu setelah login
        else:
            print("Password salah. Silakan coba lagi.")
            attempts += 1

    print("\nAnda telah gagal login sebanyak 3 kali. Kembali ke menu utama.")


def mengelola_akun():
    print("=== Pengelolaan Akun ===")
    print("1. Aktivasi Akun Trial (Gratis selama 7 hari)")
    print("2. Pembelian Akun Premium")
    
    try:
        pilihan = int(input("\nPilih opsi (1/2): ").strip())
        
        if pilihan == 1:
            # Aktivasi akun trial
            global akun_trial
            print("\n=== Aktivasi Akun Trial ===")
            aktivasi = input("Apakah Anda ingin mengaktifkan akun trial? [ya/tidak]: ").lower().strip()
            
            if aktivasi == "ya":
                if akun_trial["aktif"]:
                    print("Akun trial Anda sudah aktif! Masa trial berakhir pada:", akun_trial["berakhir"].strftime('%d-%m-%Y'))
                else:
                    masa_trial = datetime.now() + timedelta(days=7)
                    akun_trial["aktif"] = True
                    akun_trial["berakhir"] = masa_trial
                    print(f"\nSelamat! Akun trial Anda telah aktif selama 7 hari. Masa trial berakhir pada: {masa_trial.strftime('%d-%m-%Y')}")
            elif aktivasi == "tidak":
                print("Akun trial tidak diaktifkan.")
            else:
                print("Input salah! Silahkan coba lagi.")
        
        elif pilihan == 2:
            # Pembelian akun premium
            global akun_premium, akun_premium_details
            print("\n=== Pembelian Akun Premium ===")
            print("Silahkan pilih paket yang ingin Anda beli:")
            print("1. Paket A berlangsung selama 1 bulan dengan biaya langganan Rp 270.000")
            print("2. Paket B berlangsung selama 6 bulan dengan biaya langganan Rp 630.000")
            
            try:
                pilihan_paket = int(input("\nPilih paket berlangganan (1/2): ").strip())
                
                if pilihan_paket not in [1, 2]:
                    print("Pilihan tidak valid! Silahkan coba kembali.")
                else:
                    konfirmasi_paket = input("Apakah Anda ingin melanjutkan pembelian? (ya/tidak): ").strip().lower()
                    if konfirmasi_paket == "ya":
                        username_premium = input("Masukkan username premium baru: ").strip()
                        password_premium = input("Masukkan password premium (tidak boleh sama dengan password akun biasa): ").strip()
                        
                        # Validasi password premium
                        while password_premium in akun_non_premium.values():
                            print("Password tidak boleh sama dengan password akun biasa. Silakan pilih password lain.")
                            password_premium = input("Masukkan password premium (tidak boleh sama dengan password akun biasa): ").strip()
                        
                        akun_premium[username_premium] = password_premium
                        
                        # Tentukan masa berlaku langganan premium
                        if pilihan_paket == 1:
                            masa_langganan = datetime.now() + timedelta(days=30)  # 1 bulan
                        elif pilihan_paket == 2:
                            masa_langganan = datetime.now() + timedelta(days=180)  # 6 bulan
                        
                        akun_premium_details[username_premium] = {"berakhir": masa_langganan}
                        print(f"Terima kasih telah berlangganan akun premium! Masa aktif akun premium Anda hingga: {masa_langganan.strftime('%d-%m-%Y')}")
                    elif konfirmasi_paket == "tidak":
                        print("Pembelian dibatalkan.")
                    else:
                        print("Input tidak valid! Silahkan pilih 'ya' atau 'tidak'.")
            except ValueError:
                print("Input tidak valid! Silahkan masukkan angka.")
        
        else:
            print("Pilihan tidak valid! Silahkan coba kembali.")
    
    except ValueError:
        print("Input tidak valid! Silahkan masukkan angka.")


def Cek_Status_dan_Lihat_Film_Akun():
    global akun_premium, akun_trial, akun_premium_details
    # Input username untuk cek status
    username = input("Masukkan username Anda: ").strip()

    # Memeriksa apakah username ada di akun_non_premium atau akun_premium_details
    if username in akun_non_premium or username in akun_premium_details:
        now = datetime.now()

        # Cek akun premium
        if username in akun_premium_details:
            if now <= akun_premium_details[username]["berakhir"]:
                print(f"Akun Premium Anda aktif! Anda dapat mengakses film premium hingga {akun_premium_details[username]['berakhir'].strftime('%d-%m-%Y')}")
                lihat_menu_film_premium()
            else:
                print("Masa langganan akun premium Anda telah berakhir. Silakan lakukan pembaruan langganan.")
        
        # Cek akun trial
        elif username not in akun_premium_details and akun_trial["aktif"] and now <= akun_trial["berakhir"]:
            print(f"\nAkun trial Anda aktif. Anda dapat mengakses film premium hingga {akun_trial['berakhir'].strftime('%d-%m-%Y')}")
            lihat_menu_film_premium()
        
        # Masa trial habis
        elif username not in akun_premium_details and akun_trial["aktif"] and now > akun_trial["berakhir"]:
            akun_trial["aktif"] = False
            akun_trial["berakhir"] = None
            print("Masa trial Anda telah berakhir. Silakan upgrade ke akun premium.")
        
        # Akun biasa (Non Premium)
        elif username not in akun_premium_details and not akun_trial["aktif"]:
            print("Akun Anda bukan Premium dan tidak memiliki trial aktif.")
        
        # Setelah pengecekan selesai, menanyakan opsi jika ingin lanjut mencari atau keluar
        opsi = input("\nApakah Anda ingin melanjutkan mencari akun lain? (ya/tidak): ").strip().lower()
        if opsi == "ya":
            Cek_Status_dan_Lihat_Film_Akun()  # Memanggil lagi untuk mencari akun lain
        else:
            print("Kembali ke tampilan awal.")
            # Panggil tampilan menu awal (misalnya fungsi menu utama)


    else:
        print(f"Username '{username}' tidak ditemukan.")
        opsi = input("Apakah Anda ingin mencari username lain? (ya/tidak): ").strip().lower()
        if opsi == "ya":
            Cek_Status_dan_Lihat_Film_Akun()  # Memanggil lagi untuk mencari akun lain
        else:
            print("Kembali ke tampilan awal.")


 


# ----------------------------------------------------------------------------------------------------------------------------------------------------------



# Program Utama
while True:
    print(Fore.BLUE + "=" * 50)
    print(Fore.RED + "--- Selamat Datang Di Aplikasi APDFLIX ---")
    print(Fore.WHITE + "Silakan pilih role kamu!!!")
    print("1. Admin")
    print("2. User ")
    print("3. Keluar")
    print(Fore.BLUE + "=" * 50)
    opsi = input(Fore.WHITE + "Pilih opsi: ").strip()

    if opsi == "1":
        akun_siadmin = input("Masukkan Username: ").strip()
        password_siadmin = pwinput.pwinput("Masukkan Password: ").strip()
        if akun_siadmin == akun_admin and password_siadmin == password_admin:
            while True:
                print("_" * 30)
                print("Selamat Datang Di Tampilan Admin")
                print("Silahkan Pilih Opsi Yang Ada Inginkan!")
                print("1. Melihat Pengguna APDFLIX")
                print("2. Melihat Semua Judul Film")
                print("3. Tambah Film Baru")
                print("4. Update Film")
                print("5. Hapus Film")
                print("6. Keluar")
                print("_" * 30)
                pilihan_admin = input("Silahkan Pilih Opsi Yang Sudah Tersedia: ").strip()
                if pilihan_admin == "1":
                    tampilkan_daftar_pengguna()
                elif pilihan_admin == "2":
                    lihat_menu_film_Non_premium()
                    print("-"* 50)
                    lihat_menu_film_premium()
                elif pilihan_admin == "3":
                    kelola_daftar_film()
                elif pilihan_admin == "4":
                    update_film()
                elif pilihan_admin == "5":
                    Menghapus_Film()
                elif pilihan_admin == "6":
                    print("Keluar dari Tampilan Admin.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
        else:
            print("Username atau password salah.") 
            
    elif opsi == "2":
        while True:
            print("-----Selamat Datang Di APDFLIX-----")
            print("_"* 30)
            print("1. Daftar Akun")
            print("2. Login")
            print("3.Keluar")
            print("_"* 50)
            pilihan_user = input("Silahkan Pilih Opsi Tersebut: ").strip()

            if pilihan_user == "1":
                daftar_akun()
            elif pilihan_user == "2":
                login()
                while True:
                    print("_"* 40)
                    print(Fore.RED + "Halo Selamat Datang Di APDFLIX")
                    print(Fore.WHITE + "1.Lihat Menu Film")
                    print("2. Upgrade ke premium ")
                    print("3. Cek Status Dan Lihat Judul Premium")
                    print("4. Keluar")
                    print("_"* 40)
                    pilihan_login = input("Silahkan Pilih Opsi: ").strip()

                    if pilihan_login == "1":
                        lihat_menu_film_Non_premium()
                    elif pilihan_login == "2":
                        mengelola_akun()
                    elif pilihan_login =="3":
                        Cek_Status_dan_Lihat_Film_Akun()
                    elif pilihan_login == "4":
                        print("Keluar ")
                        break
            elif pilihan_user =="3":
                break
            else:
                print("Pilihan tidak valid Silakan pilih Opsi Yang Di Sediakan")

    elif opsi == "3":
        print("Terima kasih telah menggunakan Aplikasi APDFLIX")
        break  # Keluar dari loop jika opsi 3 dipilih
    else:
        print("Pilihan tidak valid Silakan pilih Opsi Yang Di Sediakan")