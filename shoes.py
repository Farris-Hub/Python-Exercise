ukuran = int(input("masukan ukuran sepatu (30-45) = "))

if ukuran > 40 and ukuran <= 45:
    print("Ukurannya besar")
elif ukuran > 35 and ukuran <=40:
    print("Ukurannya sedang")
elif ukuran >= 30 and ukuran <=35:
    print("Ukurannya kecil")
else:
    print("Ukuran tidak valid")

