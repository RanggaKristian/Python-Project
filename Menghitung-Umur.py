import datetime

# --- FUNGSI PROGRAM ---
def hitung_umur(tahun_lahir):
    # Process
    tahun_sekarang = datetime.datetime.now().year
    umur = tahun_sekarang - tahun_lahir
    # Output
    print(f"[OUTPUT] Tahun Lahir: {tahun_lahir} | Umur Anda: {umur} tahun")
    return umur

# --- INPUT PENGGUNA ---
print("=== E. PROGRAM MENGHITUNG UMUR ===")
thn = int(input("[INPUT] Masukkan tahun lahir Anda: "))
hitung_umur(thn)

# --- TESTING (MINIMAL 3 DATA UJI) ---
print("\n--- TESTING DATA UJI ---")
data_uji = [1998, 2005, 2012]
for i, val in enumerate(data_uji, 1):
    print(f"Data Uji {i} (Input Tahun: {val}):")
    hitung_umur(val)