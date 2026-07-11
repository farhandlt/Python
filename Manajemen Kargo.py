print("\t  Selamat Datang di \n--- Sistem Manajemen Kargo Gudang ---")
print("─" * 38, "\n")
gudang_barang = {'General':[], 'Special':[]}

while True :
    admin = input("Masukkan Username : ").title()
    if admin == "" :
        print("Masukkan Username")
        continue
    else : 
        break
while True :
    pw_teks = input("Masukkan Kata Sandi : ")
    if pw_teks == "" : 
        print("Masukkan Kata Sandi Admin")
        continue
    try :
        pw = int(pw_teks)
        print("\n✔ Berhasil Masuk ke Sistem")
        break
    except :   
        print("Kata Sandi Salah, Masukkan Kata Sandi Kembali")
        continue
    
def menu(login_berhasil) :
    print("\n╔" + "═"*36 + "╗")
    print("║            Fitur Sistem            ║")
    print("╠" + "═"*36 + "╣")
    print("║ 1. Penginputan Barang Kargo        ║")
    print("║ 2. Pencetakan Laporan Inventaris   ║")
    print("║ 3. Pengiriman Kargo                ║")
    print("║ 4. Penutupan Sistem                ║")
    print("╚" + "═"*36 + "╝")

menu("berhasil\n")

print("\n🔴 Peringatan kategori Kargo")
def karakteristik():
    print("╔" + "═"*43 + "╗")
    print("║        General       ║       Special      ║")
    print("╠" + "═"*43 + "╣")
    print("║ • Tidak Mudah Busuk  ║ • Makhluk Hidup    ║")
    print("║ • Tidak Mudah Rusak  ║ • Mudah Rusak      ║")
    print("║ • Tidak Berbahya     ║ • Barang Berharga  ║")
    print("╚" + "═"*43 + "╝")

karakteristik()
while True :
    try:
        nomor = int(input("Masukkan Nomor Tujuan : "))
        print(f"Anda Memilih Menu {nomor}")
        if nomor not in range (1, 5) :
            print("Masukkan Nomor Tujuan Sesuai yang Ada di sistem ")
    except ValueError:
        print("Invalid!!! Masukkan Angka")
        continue
#Penginputan Barang Kargo
    if nomor == 1 :
        print("\n  penginputan Barang")
        print("─" * 22)
        while True :
            kargo = input("\nMasukkan Kategori Kargo (General/Special) : ").strip().title()
            if kargo not in ["General","Special"]:
                print("Masukkan Kategori Kargo General/Special")
                continue
            barang = input("Masukkan Barang Kargo Baru : ").strip().title()
            if kargo == "General" :
                gudang_barang ["General"].append(barang) 
            else :
                gudang_barang ["Special"].append(barang)
            Qna = input("Apakah Anda Ingin Menginput Lagi (Y/N): ").strip().title()
            if Qna == "Y" :
                continue
            else :
                print("\n" + "─" * 29)
                print("  Barang Berhasil Tersimpan  ")
                print("─" * 29, "\n")
                break
#Laporan Inventaris
    if nomor == 2 :
        print("\n   Inventaris")
        print("─" * 16)
        index = 0
        for kategori, barang in gudang_barang.items() :
            index +=1
            print(f"Kategori Kargo {index} = {kategori}", end=" ║ ")
            print(f"Barang Kargo = {", ".join(barang)}")
        print("\n" + "─" * 18)
        print("  Status Gudang  ")
        print("─" * 18)
        for kargo, i in gudang_barang.items():
            if kargo == "General" :
                print(f"Jumlah Barang Kategori General {len(i)}")
            else :
                print(f"Jumlah Barang Kategori Special {len(i)}")
        print(f"Jumlah Barang Keseluruhan {sum(len(i) for i in gudang_barang.values())}\n")
    
#Pengiriman Kargo 
    barang = []
    if nomor == 3 :
        print("\n  Pengirimaan Barang")
        print("─" * 22)
        while True :
            barang_kargo = input("Masukkan Nama Barang yang Ingin dikirim : ").strip().title()
            ditemukan = False
            for kirim_kargo, kirim_barang in gudang_barang.items():
                if barang_kargo in kirim_barang :
                    print(f"Barang {barang_kargo} ditemukan, Berada dalam jenis kargo {kirim_kargo} ")
                    barang.append(barang_kargo)
                    ditemukan = True
            if not ditemukan :
                print(f"Barang tidak ditemukan\n")

            Qna1 = input("Apakah Anda Ingin Menacari Barang Lagi (Y/N)?: ").strip().title()
            print()
            if Qna1 == "Y" :
                continue
            else :
                general = [] 
                special = []
                print("\nRincian Barang yang Ingin Dikrimkan :")
                for kirim_kargo1, kirim_barang1 in gudang_barang.items():
                    for barang1 in barang :
                        if barang1 in kirim_barang1 :
                            if kirim_kargo1 == "General" :
                                general.append(barang1)
                            else :
                                special.append(barang1)

                print("Kategori      : General")
                print(f"Nama Barang   : {", ".join(general)} \n")
                print("Kategori      : Special")
                print(f"Nama Barang   : {", ".join(special)}")

                print("\n" + "─" * 29)
                print("  Status Pengiriman Barang  ")
                print("─" * 29)
                print(f"Total Pengiriman Barang Kategori General : {len(general)}")
                print(f"Total Pengiriman Barang Kategori Special : {len(special)}\n")
                break

#Keluar dari Sistem
    if nomor == 4 :
        print("\nTerima Kasih, Sistem ditutup")
        print("Pengiriman Barang Akan dilakukan Sesuai dengan jadwal yang ditentukan")
        break