import math

print("="*20)
print("   rumus kerucut")
print("="*20)

r = int(input("masukan jari-jari = "))
s = float(input("masukan sisi kerucut = "))
t = float(input("masukan tinggi kerucut = "))

ls = math.pi * r * s
lp = (math.pi * r * s) + (math.pi * r ** 2)
v = 1/3 * math.pi * r ** 2 * t

print(f"luas selimut = {ls} ")
print(f"luas permukaan = {lp}")
print("Volume \t= ",round(v,2))