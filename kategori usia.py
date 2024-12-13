usia = int(input("Masukkan usia Anda: "))

if usia < 0:
    hasil = "Usia tidak valid."
elif 0 <= usia <= 12:
    hasil = "Anda berada dalam kategori Anak-anak."
elif 13 <= usia <= 17:
    hasil = "Anda berada dalam kategori Remaja."
elif 18 <= usia <= 64:
    hasil = "Anda berada dalam kategori Dewasa."
else:
    hasil = "Anda berada dalam kategori Lansia."

print(hasil)
