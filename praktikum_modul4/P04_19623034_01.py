# NIM/Nama : 19623034/Refki Alfarizi
# Tanggal : 2 November 2023
# Deskripsi : Program menghitung nilai tugas praktikunm

# KAMUS
# cek_valid : function
# hitung : function
# a, b, c : float
# n1, n2, n3 : float

# ALGORITMA

def cek_valid(a, b, c):
  # FUNGSI

  # KAMUS
  # a , b , c : float

  return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1 and a + b + c == 1

def hitung(a, b, c, n1, n2, n3):
  # PROSEDUR

  # KAMUS
  # a, b, c : float
  # n1, n2, n3 : float
  # nilai : float
  
  if cek_valid(a, b, c):
    nilai = a*n1 + b*n2 + c*n3
    print("Nilai tugas praktikum adalah ", nilai)
  else:
    print("bobot tidak valid")

# PROGRAM UTAMA
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
n1 = float(input("Masukkan nilai soal 1: "))
n2 = float(input("Masukkan nilai soal 2: "))
n3 = float(input("Masukkan nilai soal 3: "))

hitung(a, b, c, n1, n2, n3)