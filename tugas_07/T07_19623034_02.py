# Latihan-2 T07_19623034_02.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program menentukan berapa banyak mahasiswa yang lulus dan tidak lulus

# KAMUS
# N : array [50] of char
# lulus : int
# tidaklulus : int
# i : int

# N = ['D', 'B', 'B', 'A', 'C', 'B', 'B', 'B', 'D', 'C', 'D', 'D', 'B', 'C', 'B', 'B', 'A', 'B', 'D', 'D', 'C', 'B', 'B', 'D', 'A', 'D', 'B', 'C', 'A', 'A', 'C', 'B', 'B', 'D', 'A', 'C', 'D', 'D', 'A', 'D', 'C', 'B', 'B', 'B', 'C', 'B', 'D', 'D', 'A', 'B']

# ALGORITMA

N = ['' for i in range(50)]

lulus = 0
tidaklulus = 0

for i in range(50):
  N[i] = input(f"Nilai ke-{i+1}: ")
  if  N[i] == 'D' or N[i] == 'E':
    tidaklulus += 1
  else:
    lulus += 1

print(f"{lulus} mahasiswa lulus")
print(f"{tidaklulus} mahasiswa tidak lulus")

# 36 mahasiswa lulus
# 14 mahasiswa tidak lulus