print("="*32)
print("\tselinder tabung")
print("="*32)

t = int(input("masukan nilai tinggi tabung    = "))
r = int(input("masukan nilai jari-jari tabung = "))

pi = 3.14

selimut = 2 * pi * r * t
luas_permukaan = selimut + ( 2 * pi * r ** 2 )
luas = pi * t * 2 * t

print(f"selimut               = {selimut}")
print(f"luas permukaan        = {luas_permukaan}")
print(f"luas alas dan tinggi  = {luas}")
