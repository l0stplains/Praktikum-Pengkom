# Latihan-5 T07_19623034_05.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program menjumlahkan dua vektor

# KAMUS
# W, U, V : array [5] of int
# i : int

# U = [1, 2, 3, 4, 5]
# V = [5, 4, 3, 2, 1]

# ALGORITMA

W = [0 for i in range(5)]
U = [0 for i in range(5)]
V = [0 for i in range(5)]

for i in range(5):
  U[i] = int(input(f"Masukkan elemen ke-{i+1} dari U: "))

for i in range(5):
  V[i] = int(input(f"Masukkan elemen ke-{i+1} dari V: "))

for i in range(5):
  W[i] = U[i] + V[i]

print(W)

# [6, 6, 6, 6, 6]