# Latihan-3 T07_19623034_03.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program mencari nilai terkecil dari array T

# KAMUS
# t : int
# T : array [t] of int
# mini : int
# i : int

# t = 10
# T = [5, 7, 3, 2, 7, 12, 46, 4, 10, 9]

# ALGORITMA

t = int(input("Masukkan nilai T (ukuran array): "))

T = [0 for i in range(t)]

T[0] = int(input(f"Masukkan elemen ke-1: "))

mini = T[0]

for i in range(1, t):
  T[i] = int(input(f"Masukkan elemen ke-{i+1}: "))
  if T[i] < mini:
    mini = T[i]
  
print(f"Nilai terkecil = {mini}")

# Nilai terkecil = 2
