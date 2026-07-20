# PROJECT PERTAMA
Gudang = {}
print("╔" + "═"*36 + "╗")
print("║     Pencatatan Gudang Digital      ║")
print("╠" + "═"*36 + "╣")
print("║ 1. Penginputan Nama Barang         ║")
print("║ 2. Penambahan Stok Barang          ║")
print("║ 3. Menampilkan isi Rak             ║")
print("║ 4. Pencarian Barang                ║")
print("║ 5. Pemberhentian Mesin             ║")
print("╚" + "═"*36 + "╝")

while True :
    # inputan pertama
    user = int(input("Masukkan Angka 1/2/3/4/5 : "))
    if user not in range (1,6) :
        print("Eror!!!! Masukkan Angka Sesuai Kriteria")
        continue
    else :
        print(f"Anda Memilih Menu : {user}")

    # Nambah Barang
    if user == 1 :
        print("\n" + "─" * 36)
        print("     Pendaftaran Barang Baru     ")
        print("─" * 36)

        while True :
            barang = input("Masukkan Nama Barang : ").strip().title()
            next_rak = len(Gudang) + 1
            Gudang[f"Rak {next_rak}"] = [barang]
            pass

            Qna = input("Apakah Anda ingin menambah Barang Lagi, pilih (Y/N) : ").strip().upper()
            if Qna == "Y" :
                print()
            else :
                print("\n" + "─" * 35)
                print(" ✓ Barang Berhasil Ditambahkan!!!\n")
                break 

    # Menambah Barang 2
    elif user == 2 :
        print("\n" + "─" * 36)
        print("     Penambahan Stok Barang      ")
        print("─" * 36)

        while True :
            try :
                stok = int(input(f"Total Loker {len(Gudang)}\nMasukkan Loker Tujuan : "))
                if stok not in range (1, len(Gudang) + 1) :
                    print("Eror!!!! Masukkan Angka Sesuai Jumlah Loker\n")
                    continue
            except ValueError :
                print("Eror!!!! Masukkan Angka \n")
                continue

            stok_1 = input("Masukkkan Barang Tambahan : ").strip().title()
            Gudang[f"Rak {stok}"].append(stok_1)
            pass
        
            Qna = input("\nApakah Anda ingin menambah Barang Lagi? (Y/N) : ").strip().upper()
            if Qna == "Y" :
                print("Masukkan Barang\n")
            else :
                print("\n" + "─" * 31)
                print(f" ✓ Rak {stok} Behasil Diupdate!!!\n")
                break
            
    # Menampilkan Barang 
    elif user == 3 :
        print("\n" + "─" * 18)
        print("     Isi Rak     ")
        print("─" * 18)

        for rak, barang in Gudang.items() :
            print(f"Inventaris yang Tersedia {rak} = {barang}")

        print("\n" + "─" * 24)
        print("     Status Gudang     ")
        print("─" * 24)
        print(f"Jumlah Rak sebanyak {len(Gudang)}")
        print(f"Jumlah Inventaris sebanyak {sum(len(isi_rak) for isi_rak in Gudang.values())}\n")

    # Mencari Barang
    elif user == 4 :
        print("\n" + "─" * 27)
        print("     Pencarian Barang     ")
        print("─" * 27)

        while True :
            buka_loker = input("Masukkan Nama Barang yang Ingin Dicari : ").strip().title()
            ditemukan = False
            for rak, barang in Gudang.items() :
                if buka_loker in barang :
                    print(f"barang {buka_loker} Ditemukan, berada di {rak} !!!\n")
                    ditemukan = True

            if not ditemukan :
                print(f"Maaf !!! Barang {buka_loker} Tidak Terdaftar Di Pencatatan!!!\n")

            ulang = input("Apakah Anda Ingin Mencari Barang Lagi, pilih? (Y/N) :  ").strip().upper()
            if ulang == "Y" :
                print("Baik, Masukkan Barang yang Ingin Anda Cari!!! \n")
            else :
                print("\n" + "─" * 33)
                print(f" ✓ Pencarian Barang Selesai!!!\n")
                break
                
    else :
        print("\nSistem Dimatikan...... \nTerima Kasih")
        break