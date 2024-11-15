import math


print("================================")
print("\tPROGRAM tabung")
print("================================")

r = float(input("masukan jari-jari tabung = "))
t = float(input("masukan tinggi tabung    = "))

volume = 2 * math.pi * r * t
luas_permukaan = math.pi * r* r + 2 * math.pi * r * t

print("volumenya adalah         = ", volume)
print("luas permukaannya adalah = ", luas_permukaan)