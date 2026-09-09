# --- FUNGSI PROGRAM ---
def hitung_total_belanja(harga_satuan, jumlah):
    # Process
    subtotal = harga_satuan * jumlah
    diskon = subtotal * 0.10 if subtotal > 100000 else 0  # Diskon 10% jika belanja > 100rb
    total = subtotal - diskon
    # Output
    print(f"[OUTPUT] Subtotal: Rp{subtotal:,.0f} | Diskon: Rp{diskon:,.0f} | Total Bayar: Rp{total:,.0f}")
    return total

# --- INPUT PENGGUNA ---
print("=== C. PROGRAM HITUNG TOTAL BELANJA ===")
harga = float(input("[INPUT] Masukkan harga barang (Rp): "))
qty = int(input("[INPUT] Masukkan jumlah barang: "))
hitung_total_belanja(harga, qty)

# --- TESTING (MINIMAL 3 DATA UJI) ---
print("\n--- TESTING DATA UJI ---")
data_uji = [
    (15000, 3),   # Belanja <= 100rb (tanpa diskon)
    (50000, 3),   # Belanja > 100rb (dapat diskon)
    (120000, 1)   # Belanja > 100rb (dapat diskon)
]
for i, (h, q) in enumerate(data_uji, 1):
    print(f"Data Uji {i} (Harga: Rp{h}, Qty: {q}):")
    hitung_total_belanja(h, q)