import math


print("==================================")
print("\tPROGRAM LINGKARAN")
print("==================================")

r = float(input('''
masukan jari jari lingkaran = '''))

luas = math.pi * r * r
keliling = 2 * math.pi * r

print(("Luasnya adalah     = "), luas)
print(("kelilingnya adalah = "), keliling)