# Problem 2 P02_19623034_02.py
# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 5 Oktober 2023
# Deskripsi: Program membuat sebuah barisan bilangan yang dimulai dari angka 1 dan memiliki sifat unik. 

# KAMUS
# n : int
# k : int
# naik : bool
# x, y : int
# i : int

# ALGORITMA

n = 1
k = 1
naik = True

x = int(input("Masukkan x: "))
y = int(input("Masukkan y: "))

# JIka |y| = 1 maka program akan menurun di kelipatan kedua 
if (y == 1 or y == -1) and k == 1:
    k+=1
    
for i in range(x):
  print(n, end=" ")

  # Jika naik dan bertemu dengan kelipatan angka y berikutnya
  if y != 0 and naik and n % (y*k) == 0:
    naik = False
    k += 1
    n -= 1
  elif naik == False:
    
    if n == 1:
      # barisan menaik lagi
      n += 1
      naik = True
    else: # n != 1 (program terus turun sampai bertemu n = 1)
      n -= 1
  else: # naik == True and n%(y*k) != 0
    n += 1
  
