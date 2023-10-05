# Problem 3 P02_19623034_03.py
# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 5 Oktober 2023
# Deskripsi: Program membuat piramida bilangan dengan beberapa ketentuan khusus.

# KAMUS
# p : int
# s : int
# n : int
# lebar_X : int
# i, j : int


# ALGORITMA

# Kata kaka pengawasnya inputnya udh kurang dari 75
p = int(input("Masukkan panjang piramida: "))

# Jika panjang genap maka akan menjadi bilangan ganjil terdekat dibawahnya
p -= (1-p%2)

s = int(input("Masukkan selisih: "))

# inisiasi bilangan pertama
n = 1
for i in range(1, (p + 1)//2 + 1):
  lebar_X = (p - (i * 2 - 1))//2
  for j in range(lebar_X):
    print("X", end="")
  for j in range(p - 2*lebar_X):
    print(n, end="")
  for j in range(lebar_X):
    print("X", end="")
  print()
  # n hanya dalam rentang 0 - 9
  n = (n + s) % 10



