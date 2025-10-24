# Data jadwal menggunakan List of Dictionaries
JADWAL_SEMESTER = [
    {"hari": "Senin", "matkul": "Pemrograman Python", "jam": "08:00"},
    {"hari": "Selasa", "matkul": "Struktur Data", "jam": "10:00"},
    {"hari": "Senin", "matkul": "Jaringan Komputer", "jam": "13:00"},
    {"hari": "Rabu", "matkul": "Basis Data", "jam": "15:00"},
]

def jadwal_hari(hari):
    """Mencari dan menampilkan jadwal untuk hari tertentu."""
    
    jadwal_ditemukan = []
    
    # Melakukan iterasi pada list of dictionaries [cite: 947-950]
    for mata_kuliah in JADWAL_SEMESTER:
        # Pengecekan kondisi [cite: 909]
        if mata_kuliah["hari"].lower() == hari.lower():
            jadwal_ditemukan.append(mata_kuliah)
    
    if jadwal_ditemukan:
        print(f"\nJadwal untuk hari {hari.title()}:")
        # Iterasi hasil [cite: 947-950]
        for item in jadwal_ditemukan:
            print(f"- {item['matkul']} pada jam {item['jam']}")
    else:
        print(f"\nTidak ada jadwal untuk hari {hari.title()}.")

# Contoh Pemanggilan
jadwal_hari("senin")
jadwal_hari("kamis")

# Penjelasan:
#Penjelasan: Pencarian jadwal ini harus mengecek satu per satu isi list (looping `for`),
# membandingkan nilai kunci **"hari"** pada setiap kamus dalam list dengan input `hari`, 
# hingga semua isi list selesai diperiksa.