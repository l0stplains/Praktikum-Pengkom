# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 14 September 2023
# Deskripsi: Program akan menentukan apakah pemilik nilai (Pada kasus ini bernama Tuan Kil) lulus atau tidak lulus.

# KAMUS
# n1: integer
# n2: integer
# n3: integer
# n4: integer
# rata_rata: float

# ALGORITMA

# Input
n1 = int(input("Masukkan nilai ujian 1: "))
n2 = int(input("Masukkan nilai ujian 2: "))
n3 = int(input("Masukkan nilai ujian 3: "))
n4 = int(input("Masukkan nilai ujian 4: "))

# Proses
rata_rata = (n1+n2+n3+n4) / 4

if n1 >= 50 and n2 >= 50 and n3 >= 50 and n4 >= 50 and rata_rata >= 70:
    print("Tuan Kil lulus kelas Tuan Leo.")
else: # Ada nilai kurang dari 50 atau rata-rata nilai kurang dari 70
    print("Tuan Kil tidak lulus kelas Tuan Leo.")
