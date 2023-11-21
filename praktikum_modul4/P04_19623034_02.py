# NIM/Nama : 19623034/Refki Alfarizi
# Tanggal : 2 November 2023
# Deskripsi : Program mengubah sebuah matriks yang berukuran mxn menjadi matriks baru
# dengan jumlah elemen-elemen yang berada di sekitarnya secara vertikal dan horizontal.

# KAMUS
# M, N : int
# mtx : array of array of int
# new_mtx : array of array of int

# ALGORITMA

M = int(input("Masukkan nilai m: "))
N = int(input("Masukkan nilai n: "))

mtx = [[0 for i in range(N)] for i in range(M)]

for i in range(M):
  for j in range(N):
    mtx[i][j] = int(input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))

new_mtx = [[0 for i in range(N)] for i in range(M)]

for i in range(M):
  for j in range(N):
    if i > 0:
      new_mtx[i][j] += mtx[i-1][j]
    if i < M-1:
      new_mtx[i][j] += mtx[i+1][j]
    if j > 0:
      new_mtx[i][j] += mtx[i][j-1]
    if j < M-1:
      new_mtx[i][j] += mtx[i][j+1]

print("Matriks baru: ")
for i in range(M):
  for j in range(N):
    print(new_mtx[i][j], end=" ")
  print()  