angka = int(input("Masukkan sebuah angka: "))
kelipatan = int(input("Masukkan angka kelipatan yang ingin dicek: "))

if angka % kelipatan == 0:
    hasil = "{} adalah kelipatan dari {}.".format(angka, kelipatan)
else:
    hasil = "{} bukan kelipatan dari {}.".format(angka, kelipatan)

print(hasil)
