import csv # Modul untuk bekerja dengan file CSV (Comma Separated Values).
import json   # Modul untuk bekerja dengan format data JSON.
import logging  # Modul untuk mencatat aktivitas dan kesalahan 
from pathlib import Path  # Modul Pathlib untuk mengelola jalur file secara aman (lintas OS).

# Setup logging sederhana (INFO saat mulai, ERROR saat gagal)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Tentukan Path file
FOLDER_DATA = Path("data") # Objek Path untuk folder 'data'
PATH_CSV = FOLDER_DATA / "presensi.csv" # Menggabungkan path CSV secara aman
PATH_JSON = FOLDER_DATA / "ringkasan.json"  # Menggabungkan path JSON

def rekap_presensi():
    """Melakukan proses lengkap penulisan CSV, pembacaan, perhitungan, dan penyimpanan ke JSON."""
    
    # 1) Membuat folder data (jika sudah ada, lanjut)
    try:
        FOLDER_DATA.mkdir(exist_ok=True)
        logging.info(f"Folder '{FOLDER_DATA}' dipastikan ada.")
    except Exception as e:
        logging.error(f"Gagal membuat/memverifikasi folder: {e}")
        return # Hentikan proses jika gagal di awal
        
    # Data yang akan ditulis
    data_presensi = [
        {"nim": "A01", "nama": "Budi", "hadir_uts": "1"},
        {"nim": "A02", "nama": "Ani", "hadir_uts": "0"},
        {"nim": "A03", "nama": "Cica", "hadir_uts": "1"},
        {"nim": "A04", "nama": "Doni", "hadir_uts": "1"}
    ]
    
    # 2) Menulis CSV data/presensi.csv 
    logging.info("Mencoba menulis data ke CSV...")
    try:
        with PATH_CSV.open("w", encoding="utf-8", newline="") as f: # Selalu gunakan newline="" 
            fieldnames = ["nim", "nama", "hadir_uts"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_presensi)
        print(f"✅ Data presensi berhasil ditulis ke {PATH_CSV}")
    except Exception as e:
        logging.error(f"❌ GAGAL MENULIS CSV: {e}")
        return

    # 3) Membaca kembali CSV, hitung, lalu simpan ke JSON 
    logging.info("Mencoba membaca CSV dan menghitung rekap...")
    
    try:
        total_siswa = 0
        total_hadir = 0
        
        with PATH_CSV.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_siswa += 1
                # Menggunakan int() untuk konversi dan penjumlahan
                total_hadir += int(row["hadir_uts"])
        
        # Perhitungan Persentase (Lindungi dari ZeroDivisionError) salah satu jenis runtime error (exception) di Python yang terjadi ketika program mencoba melakukan operasi pembagian (/) atau modulus (%) dengan angka nol
        try:
            persentase = (total_hadir / total_siswa) * 100
        except ZeroDivisionError:
            persentase = 0

        # Siapkan struktur data untuk JSON
        ringkasan = {
            "total_siswa": total_siswa,
            "total_hadir": total_hadir,
            "total_tidak_hadir": total_siswa - total_hadir,
            "persentase_hadir": f"{persentase:.2f}%"
        }
        
        # Simpan ke JSON dengan format rapi (indent=2) [cite: 824, 848]
        PATH_JSON.write_text(
            json.dumps(ringkasan, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        
        print(f"✅ Ringkasan berhasil disimpan ke {PATH_JSON}")
        print(json.dumps(ringkasan, indent=2))
        
    except Exception as e:
        # 4) Lindungi dengan try/except dan 5) Logging ERROR
        logging.error(f"❌ GAGAL MEMPROSES CSV ATAU MENULIS JSON: {e}")
        print("Operasi gagal. Cek log untuk detail error.")
        return
        
    logging.info("Operasi rekap presensi selesai dan sukses.") # 5) Logging sukses

if __name__ == "__main__":
    rekap_presensi() # Panggil fungsi utama