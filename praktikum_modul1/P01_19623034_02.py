# Problem 2 P01_19623034_02.py
# Nama: Refki Alfarizi
# Tanggal: 21 September 2023
# Deskripsi singkat: Program menentukan apakah suatu angka 4 digit merupakan angka spesial

# KAMUS
# angka : int
# d1 : int
# d2 : int
# d3 : int
# d4 : int

# ALGORITMA

angka = int(input("Masukkan Angka: "))

d1 = angka % 10 // 1
d2 = angka % 100 // 10
d3 = angka % 1000 // 100
d4 = angka % 10000 // 1000

if d2 + d3 != 0:
  if (d1 * d4) % (d2 + d3) == 0:
    print(f"Angka {angka} adalah angka spesial.")
  else: # (d1 * d4) % (d2 + d3) != 0
    print(f"Angka {angka} bukan angka spesial.")
else: # d2 + d3 == 0
  print(f"Angka {angka} bukan angka spesial.")