# Problem 1
# Program akan menentukan apakah pemilik nilai tersebut (Pada kasus ini bernama Tuan Kil) lulus atau tidak lulus.
# Program menerima input berupa nilai ujian.
# Tuan Kil dikatakan lulus apabila tidak ada nilai yang kurang dari 50 dan rata-rata nilai minimal 70.

# Kamus
# n1: Nilai ujian 1 (int)
# n2: Nilai ujian 2 (int)
# n3: Nilai ujian 3 (int)
# n4: Nilai ujian 4 (int)
# rata_rata: Rata-rata nilai ujian (float)

n1 = int(input("Masukkan nilai ujian 1: "))
n2 = int(input("Masukkan nilai ujian 2: "))
n3 = int(input("Masukkan nilai ujian 3: "))
n4 = int(input("Masukkan nilai ujian 4: "))

rata_rata = (n1+n2+n3+n4) / 4

if n1 >= 50 and n2 >= 50 and n3 >= 50 and n4 >= 50 and rata_rata >= 70:
    print("Tuan Kil lulus kelas Tuan Leo.")
else:
    print("Tuan Kil tidak lulus kelas Tuan Leo.")
