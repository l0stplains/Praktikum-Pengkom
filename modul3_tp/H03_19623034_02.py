# Problem 2 H03_19623034_02.py
# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 10 Oktober 2023
# Deskripsi: Program menentukan nilai terbesar ke-N dari kumpulan nilai

# KAMUS
# S : int
# N : int
# arr : array [S] of int
# i, j : int
# temp : int

# ALGORITMA

S = int(input("Masukkan banyak data: "))
N = int(input("Masukkan nilai N: "))

arr = [0 for i in range(S)]

for i in range(S):
  arr[i] = int(input(f"Masukkan data ke-{i+1}: "))

# Urutkan semua elemen di list dari yang terbesar ke yang terkecil
for i in range(S):
  for j in range(S-i-1):
    if arr[j] < arr[j+1]:
      temp = arr[j+1]
      arr[j+1] = arr[j]
      arr[j] = temp

print(f"Nilai terbesar ke-{N} adalah {arr[N-1]}")

