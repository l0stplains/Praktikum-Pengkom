# Latihan-4 T07_19623034_04.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program mencari indeks terakhir di mana X ditemukan di T

# KAMUS
# N : int
# T : array [N] of int
# i : int
# X : int
# found : bool

# N = 10
# T = [5, 6, 3, 4, 7, 1, 4, 9, 10, 1]
# X = 4

# ALGORITMA

N = int(input("Masukkan ukuran array T: "))


T = [0 for i in range(N)]

for i in range(N):
  T[i] = int(input(f"Masukkan elemen array ke-{i+1}: "))

X = int(input("Masukkan elemen yang ingin dicari: "))

i = N - 1
found = False

while(i >= 0 and found == False):
  if T[i] == X:
    found = True
  else:
    i -= 1

print(f"Elemen yang dicari ditemukan di index {i}")

# Elemen yang dicari ditemukan di index 6