# Problem 2 H02_19623034_02.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program membuat segitiga istimewa kembar tercermin sehingga membentuk
# sebuah segitiga sama kaki yang tersusun vertikal dengan tinggi H. Segitiga istimewa adalah 
# segitiga yang dibentuk dengan mengisi baris segitiga dengan angka berurutan,
# dimulai dengan angka 1 di sudut kiri atas

# KAMUS

# ALGORITMA

H = int(input("Masukkan nilai H: "))

n = 0
set_awal = H // 2 + H % 2
set_akhir = H // 2

for i in range(set_awal):
  for j in range(i + 1):
    n += 1
    print(n, end=" ")
  print("")

for i in range(set_akhir, 0, -1):
  for j in range(i):
    n += 1
    print(n, end=" ")
  print("")
