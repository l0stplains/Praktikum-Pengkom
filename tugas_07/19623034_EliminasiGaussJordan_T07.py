# Eliminasi Gauss Jordan 19623034_EliminasiGaussJordan_T07.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program mencari inverse matrix 3x3 menggunakan Eliminasi Gauss-Jordan

# KAMUS
# A : array [3] of array [6] of float
# i, j, k: int
# rasio : float
# bagi : float

# A = [[3, 4, 5], [1, 3, 7], [2, 4, 7]]

# ALGORITMA

# in range(2*3) karena ada tambahan augmented matrix
A = [[0. for i in range(2*3)] for i in range(3)]

for i in range(3):
  for j in range(3):
    A[i][j] = float(input(f"Masukkan elemen pada baris ke-{i+1} kolom ke-{j+1}: "))

# Menambah augmented matrix
for i in range(3):        
  for j in range(3):
    if i == j:
      A[i][j+3] = 1

# Eliminasi Gauss-Jordan
for i in range(3):
  for j in range(3):
    if i != j:
      rasio = A[j][i]/A[i][i]

      for k in range(2*3):
        A[j][k] = A[j][k] - rasio * A[i][k]

for i in range(3):
    bagi = A[i][i]
    for j in range(2*3):
        A[i][j] = A[i][j]/bagi

# Cetak inverse A
print("Inverse dari matriks tersebut adalah: ")
for i in range(3):
  for j in range(3, 2*3):
    print(A[i][j], end=" ")
  print()

# Inverse dari matriks tersebut adalah:
# 7/3	8/3	-13/3
# -7/3 11/3	16/3
# 2/3	4/3	-5/3
