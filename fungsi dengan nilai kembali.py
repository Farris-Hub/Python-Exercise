nilai_rata_rata = float(input("Masukkan nilai rata-rata Anda: "))
penghasilan_orangtua = float(input("Masukkan penghasilan orang tua per bulan (dalam juta): "))
prestasi_ekstrakurikuler = input("Apakah Anda memiliki prestasi ekstrakurikuler? (ya/tidak): ").lower()

if nilai_rata_rata >= 90 and penghasilan_orangtua <= 5 and prestasi_ekstrakurikuler == "ya":
    hasil = "Selamat! Anda mendapatkan Beasiswa Unggulan."
elif nilai_rata_rata >= 85 and penghasilan_orangtua <= 8:
    hasil = "Selamat! Anda mendapatkan Beasiswa Prestasi."
elif nilai_rata_rata >= 80 and penghasilan_orangtua <= 10:
    hasil = "Selamat! Anda mendapatkan Beasiswa Bantuan Pendidikan."
else:
    hasil = "Maaf, Anda belum memenuhi syarat untuk mendapatkan beasiswa."

print(hasil)
