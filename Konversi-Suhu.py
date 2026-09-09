# --- FUNGSI PROGRAM ---
def konversi_suhu(celsius):
    # Process
    fahrenheit = (celsius * 9/5) + 32
    # Output
    print(f"[OUTPUT] Hasil: {celsius}°C = {fahrenheit:.2f}°F")
    return fahrenheit

# --- INPUT PENGGUNA ---
print("=== A. PROGRAM KONVERSI CELSIUS KE FAHRENHEIT ===")
suhu_celsius = float(input("[INPUT] Masukkan suhu dalam Celsius: "))
konversi_suhu(suhu_celsius)

# --- TESTING (MINIMAL 3 DATA UJI) ---
print("\n--- TESTING DATA UJI ---")
data_uji = [0, 37.5, 100]
for i, val in enumerate(data_uji, 1):
    print(f"Data Uji {i} (Input: {val}°C):")
    konversi_suhu(val)