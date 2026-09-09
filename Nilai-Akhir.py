# --- FUNGSI PROGRAM ---
def hitung_nilai_akhir(tugas, uts, uas):
    # Process (Bobot: Tugas 20%, UTS 30%, UAS 50%)
    nilai = (tugas * 0.20) + (uts * 0.30) + (uas * 0.50)
    status = "LULUS" if nilai >= 60 else "TIDAK LULUS"
    # Output
    print(f"[OUTPUT] Nilai Akhir: {nilai:.1f} | Status KELULUSAN: {status}")
    return nilai

# --- INPUT PENGGUNA ---
print("=== D. PROGRAM HITUNG NILAI AKHIR ===")
n_tugas = float(input("[INPUT] Masukkan nilai Tugas (0-100): "))
n_uts = float(input("[INPUT] Masukkan nilai UTS (0-100): "))
n_uas = float(input("[INPUT] Masukkan nilai UAS (0-100): "))
hitung_nilai_akhir(n_tugas, n_uts, n_uas)

# --- TESTING (MINIMAL 3 DATA UJI) ---
print("\n--- TESTING DATA UJI ---")
data_uji = [
    (80, 75, 85),   # Kasus Lulus
    (50, 40, 50),   # Kasus Tidak Lulus
    (90, 95, 100)   # Kasus Nilai Tinggi
]
for i, (t, u, ua) in enumerate(data_uji, 1):
    print(f"Data Uji {i} (Tugas: {t}, UTS: {u}, UAS: {ua}):")
    hitung_nilai_akhir(t, u, ua)