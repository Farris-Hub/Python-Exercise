nilai_rata_rata = float(input("Masukkan nilai rata-rata Anda: "))
penghasilan_orangtua = float(input("Masukkan penghasilan orang tua per bulan (dalam juta): "))
prestasi_ekstrakurikuler = input("Apakah Anda memiliki prestasi ekstrakurikuler? (ya/tidak): ").lower()

if nilai_rata_rata >= 90 and penghasilan_orangtua <= 5 and prestasi_ekstrakurikuler == "ya":
    print("Selamat! Anda mendapatkan Beasiswa Unggulan.")
elif nilai_rata_rata >= 85 and penghasilan_orangtua <= 8:
    print("Selamat! Anda mendapatkan Beasiswa Prestasi.")
elif nilai_rata_rata >= 80 and penghasilan_orangtua <= 10:
    print("Selamat! Anda mendapatkan Beasiswa Bantuan Pendidikan.")
else:
    print("Maaf, Anda belum memenuhi syarat untuk mendapatkan beasiswa.")
