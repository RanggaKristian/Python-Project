# --- FUNGSI PROGRAM ---
def hitung_luas_lingkaran(r):
    # Process
    phi = 3.14159
    luas = phi * (r ** 2)
    # Output
    print(f"[OUTPUT] Luas lingkaran dengan jari-jari {r} cm = {luas:.2f} cm²")
    return luas

# --- INPUT PENGGUNA ---
print("=== B. PROGRAM HITUNG LUAS LINGKARAN ===")
jari_jari = float(input("[INPUT] Masukkan jari-jari lingkaran (cm): "))
hitung_luas_lingkaran(jari_jari)

# --- TESTING (MINIMAL 3 DATA UJI) ---
print("\n--- TESTING DATA UJI ---")
data_uji = [7, 10, 14.5]
for i, val in enumerate(data_uji, 1):
    print(f"Data Uji {i} (Input r = {val}):")
    hitung_luas_lingkaran(val)