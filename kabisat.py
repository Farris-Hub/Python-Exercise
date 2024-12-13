tahun = int(input("Masukkan tahun: "))

if tahun % 4 == 0 and tahun % 100 != 0:
    hasil = "Tahun {} adalah tahun kabisat.".format(tahun)
elif tahun % 400 == 0:
    hasil = "Tahun {} adalah tahun kabisat.".format(tahun)
else:
    hasil = "Tahun {} bukan tahun kabisat.".format(tahun)

print(hasil)
