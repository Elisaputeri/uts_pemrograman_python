# Tarif Dasar (menggunakan dict untuk lookup cepat) [cite: 429]
TARIF_DASAR_KOTA = {
    "jakarta": 10000,
    "bandung": 8000,
    "surabaya": 12000
}

def hitung_ongkir(berat_kg, kota, asuransi=False): # Default Parameter 
    """
    (2) Docstring: Menghitung biaya ongkir berdasarkan berat, kota, dan opsi asuransi. [cite: 364-370]
    """ 
    
    # Ambil tarif kota, pakai .get() biar aman kalau kotanya gak ada
    tarif_kota = TARIF_DASAR_KOTA.get(kota.lower(), 0)
    
    if tarif_kota == 0:
        return f"Waduh, kota '{kota}' belum ada tarifnya."
    
    # (1) Rumus perhitungan
    biaya_berat = 2000 * berat_kg
    
    # Tambah 3000 jika asuransi=True, kalau tidak ya 0 (pakai ternary if) [cite: 918]
    biaya_asuransi = 3000 if asuransi else 0 
    
    total_ongkir = tarif_kota + biaya_berat + biaya_asuransi
    
    return total_ongkir

# (3) Dua Contoh Pemanggilan:

# Contoh 1: Ongkir Normal (asuransi pakai default False)
ongkir_c1 = hitung_ongkir(3.0, "bandung") # Positional Parameter 
print(f"Ongkir Bandung (3 kg, tanpa asuransi): Rp{ongkir_c1:,.0f}")

# Contoh 2: Ongkir dengan Asuransi (pakai keyword parameter biar jelas) 
ongkir_c2 = hitung_ongkir(berat_kg=1.5, kota="Surabaya", asuransi=True)
print(f"Ongkir Surabaya (1.5 kg, ADA asuransi): Rp{ongkir_c2:,.0f}")