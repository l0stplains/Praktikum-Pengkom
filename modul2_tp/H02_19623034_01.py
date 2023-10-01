# Problem 1 H02_19623034_01.py
# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 28 September 2023
# Deskripsi: Program menentukan apakah bilangan N merupakan perpangkatan bilangan k atau bukan.

# KAMUS
# N : int
# k : int
# n : int
# isFactor : bool

# ALGORITMA

# Dari asprak diberitahu batasannya adalah 1 <= N,k
N = int(input("Masukkan bilangan N: "))
k = int(input("Masukkan nilai k: "))

# Copy nilai variabel N ke variabel lain
n = N
isFactor = True

# Jika n == 1 dan k lebih dari nol, maka n selalu bisa didapatkan dari k pangkat 0
if n == 1 and k > 0:
  isFactor = True

# Program akan terus berjalan hingga n tidak dapat dibagi dengan k atau n = 1
while n != 1 and isFactor:
  if n % k == 0 and k != 1:
    n //= k
  else: # n % k != 0 or k == 1
    isFactor = False

if isFactor:
  print(f"{N} merupakan perpangkatan {k}.")
else: # isFactor == False
  print(f"{N} bukan merupakan perpangkatan {k}.")