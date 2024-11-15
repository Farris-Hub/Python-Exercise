harga_barang = float(input("Masukkan total harga barang = "))

diskon = 0
if harga_barang >= 100000:
    diskon = harga_barang * 0.05
    
total_bayar = harga_barang - diskon

print("Diskon yang didapat            = Rp",diskon)
print("Total harga yang harus dibayar = Rp",total_bayar)