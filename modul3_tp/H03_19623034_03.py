# Problem 3 H03_19623034_03.py
# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 10 Oktober 2023
# Deskripsi: Program menentukan stasius tempat memulai perjalanan dan banyaknya stasiun yang dapat dikunjungi.

# KAMUS
# uang : int
# N : int
# harga : array [N] of int
# maks, index : int
# i : int
# total : int
# j : int

# ALGORITMA
uang = int(input("Masukkan uang yang dibawa Tuan Leo: "))
N = int(input("Masukkan jumlah stasiun: "))

harga = [0 for i in range(N)]
maks = 0 # variabel untuk menyimpan banyak maks stasiun yang dikunjngi jika dimulai dari stasiun tertentu 
index = 0 # variabel untuk menyimpan posisi stasiun tersebut

for i in range(N):
  harga[i] = int(input(f"Masukkan harga stasiun ke-{i+1}: "))

for i in range(N):
  total = 0
  j = 0

  # Selama masih ada uang untuk ke stasiun berikutnya dan selama semua stasiun masih belum dikunjungi maka stasiun selanjutnya dapat dikunjungi
  while total + harga[(i+j) % N] <= uang and j < N:
    total += harga[(i + j) % N]
    j += 1
  if j > maks:
    maks = j
    index = i

if maks > 0:
  print(f"Tuan Leo dapat mengunjungi {maks} stasiun dimulai dari stasiun ke-{index + 1}")
else:
  print("Tuan Leo kekurangan uang.")

  

