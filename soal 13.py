x = int(input("Masukkan nilai x = "))
y = int(input("Masukkan nilai y = "))
z = int(input("Masukkan nilai z = "))

if x >= y and x >= z:
    terbesar = x
elif y >= x and y >= z:
    terbesar = y
else:
    terbesar = z
    
if x <= y and x <= z:
    terkecil = x
elif y <= x and y <= z:
    terkecil = y
else:
    terkecil = z
    
print("Nilai terbesar adalah = ",terbesar)
print("Nilai terkecil adalah = ",terkecil)

