# Problem 1 H02_19623034_01.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program menentukan apakah bilangan N merupakan perpangkatan bilangan k atau bukan.

# KAMUS

# ALGORITMA

N = int(input("Masukkan bilangan N: "))
k = int(input("Masukkan nilai k: "))

# Copy nilai variabel N ke variabel lain
n = N
isFactor = True

if n == 1 and k > 1:
  isFactor = False

while n != 1 and isFactor:
  if n % k == 0 and k != 1:
    n //= k
  else: # n % k != 0 or k == 1
    isFactor = False

if isFactor:
  print(f"{N} merupakan perpangkatan {k}.")
else: # isFactor == False
  print(f"{N} bukan merupakan perpangkatan {k}.")