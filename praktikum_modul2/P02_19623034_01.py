# Problem 1 P02_19623034_01.py
# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 5 Oktober 2023
# Deskripsi: Program menentukan berapa banyak kegiatan yang bisa dilaksanakan dalam 1 hari 
# dan banyak kegiatan setiap gedung.

# KAMUS
# N : int
# A : int
# B : int
# i : int
# p : int

# ALGORITMA

N = int(input("Masukkan nilai N: "))

A = 0
B = 0

# Inisiasi jumlah kegiatan
i = 0

# Selama B tidak penuh
while B < 3:
  i += 1
  p = int(input(f"Masukkan peserta kegiatan ke-{i}: "))
  # Jika jumlah peserta muat di gedung A dan gedung A masih kosong
  if p < N and A < 5:
    A += 1
  else: # Masukkan ke gedung B
    B += 1
  

print(f"Terdapat {A} kegiatan di gedung A dan {B} kegiatan di gedung B.")


