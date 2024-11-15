nama_siswa = input("Masukkan nama siswa          = ")
nilai      = float(input("Masukkan nilai siswa (0-100) = "))

if nilai < 0 or nilai > 100:
    print("Nilai harus berada dalam rentang 0 hingga 100.")
else:
    if nilai >= 90:
        grade = 'A'
    elif nilai >= 80:
        grade = 'B'
    elif nilai >= 70:
        grade = 'C'
    elif nilai >= 60:
        grade = 'D'
    else:
        grade = 'E'

print(f"Nama Siswa = {nama_siswa}")
print(f"Nilai      = {nilai}")
print(f"Grade      = {grade}")