print("===================")
print("     lingkaran")
print("===================")

import math

r = int(input("masukan jari-jari lingkaran = "))

keliling = math.pi * 2 * r
luas = math.pi * r * r

print("keliling = ",round(keliling,2))
print("luas     = ",round(luas,2))