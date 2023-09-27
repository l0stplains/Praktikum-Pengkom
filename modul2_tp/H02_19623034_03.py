# Problem 3 H02_19623034_03.py
# Nama: Refki Alfarizi
# NIM: 19623034
# # Deskripsi: Program mencari apakah Tuan Kil dan Tuan Leo dapat mencapai bilangan N dengan 
# cara mengkalikan bilangan A dan bilangan B secara bergantian. Baik Tuan Kil
# maupun Tuan Leo dapat mulai terlebih dahulu, namun urutan harus selalu bergantian.

# KAMUS

# ALGORITMA

A = int(input("Masukkan bilangan A: "))
B = int(input("Masukkan bilangan B: "))
N = int(input("Masukkan bilangan N: "))

a = 0
b = 0
n = N

while n != 1:
  if n % A == 0 and A != 1:
    n //= A
    a += 1
  else: # n % k != 0 or k == 1
    n = 1

n = N
while n != 1:
  if n % B == 0 and B != 1:
    n //= B
    b += 1
  else: # n % k != 0 or k == 1
    n = 1

if -1 <= a-b <= 1 and A**a * B**b == N:
  print(f"Bilangan {N} dapat dicapai.")
else: #-1 > a-b or a-b > 1 or A**a * B**b != N
  print(f"Bilangan {N} tidak dapat dicapai.")
