print("="*25)
print("     prisma segitiga")
print("="*25)

a = int(input("masukan nilai alas      = "))
s1 = int(input("masukan sisi 1          = "))
s2 = int(input("masukan sisi 2          = "))
s3 = int(input("masukan sisi 3          = "))
t1 = int(input("masukan tinggi segitiga = "))
t2 = int(input("masukan tinggi prisma   = "))

ls = (s1 + s2 + s3) * t2
lp = (s1 + s2 + s3) * t2 + (a * t1)
l2 = 0.50 * a * t1 * t2 

print(f"nilai ls = {ls}")
print(f"nilai lp = {lp}")
print(f"nilai l  = {l2}")







