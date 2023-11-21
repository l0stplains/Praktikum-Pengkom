# Latihan-1 T07_19623034_01.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program mengalikan semua elemen array T berukuran 20 dengan bilangan X dari input user

# KAMUS
# T : array [20] of integer
# i : int
# X : int

# T = [4, 1, 3, 4, 5, 6, 8, 9, 12, 30, -1, 0, 4, -1, 3, 10, 14, 6, 7, 0]
# X = 3

# ALGORITMA

T = [0 for i in range(20)]

for i in range(20):
  T[i] = int(input(f"Masukkan elemen ke-{i+1}: "))

X = int(input("Masukkan nilai X: "))

for i in range(20):
  T[i] *= X

print(T)

# T = [12, 3, 9, 12, 15, 18, 24, 27, 36, 90, -3, 0, 12, -3, 9, 30, 42, 18, 21, 0]