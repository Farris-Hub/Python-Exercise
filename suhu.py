suhu = float(input("Masukkan suhu dalam Celcius: "))
if suhu < 0:
    print("Suhu sangat dingin (bawah nol).")
elif 0 <= suhu <= 20:
    print("Suhu dingin.")
elif 21 <= suhu <= 30:
    print("Suhu sedang.")
else:
    print("Suhu panas.")
