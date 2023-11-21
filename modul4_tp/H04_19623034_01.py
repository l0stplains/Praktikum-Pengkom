# NIM/ Nama: 19623034/Refki Alfarizi
# Tanggal: 23 Oktober 2023
# Deskripsi: Program menentukan jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil.

# KAMUS
# m, n : int
# mtx : array of array of int
# i, j : int
# jumlah_maks : int
# nilai : int

# ALGORITMA

m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

# inisiasi matriks
mtx = [[0 for i in range(n)] for i in range(m)]

for i in range(m):
  for j in range(n):
    mtx[i][j] = int(input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))

jumlah_maks = -1
for i in range(m-1):
  for j in range(n-1):
    nilai = mtx[i][j] + mtx[i+1][j] + mtx[i][j+1] + mtx[i+1][j+1]
    if (mtx[i][j] % 2 or mtx[i+1][j] % 2 or mtx[i][j+1] % 2 or mtx[i+1][j+1] % 2) and jumlah_maks < nilai:
      jumlah_maks = nilai

if jumlah_maks != -1:
  print(f"Jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjill adalah {jumlah_maks}")
else:
  print("Tidak ada submatriks 2x2 yang memenuhi syarat")