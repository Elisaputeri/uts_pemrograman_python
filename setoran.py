try:
    # 1) Meminta tiga angka satu per satu
    setoran1 = int(input("Masukkan setoran minggu 1: "))
    setoran2 = int(input("Masukkan setoran minggu 2: "))
    setoran3 = int(input("Masukkan setoran minggu 3: "))

except ValueError:
    print("Input tidak valid. Masukkan hanya angka bulat.")
else:
    # 4) Cek input tidak valid (<= 0)
    if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
        print("Input tidak valid. Setoran harus lebih dari 0.") # Tampilkan pesan jika <= 0
    else:
        # 2) Menjumlahkan semuanya
        total_setoran = setoran1 + setoran2 + setoran3
        print(f"Total setoran: Rp {total_setoran:,.0f}")
        
        # 3) Menampilkan kategori menggunakan struktur if/elif/else [cite: 554]
        if total_setoran >= 600000:
            print("Kategori setoran: tinggi")
        elif total_setoran >= 300000: # Antara 300000 sampai <600000
            print("Kategori setoran: sedang")
        else: # Kurang dari 300000
            print("Kategori setoran: rendah")