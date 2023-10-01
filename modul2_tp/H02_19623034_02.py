# Problem 2 H02_19623034_02.py
# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 28 September 2023
# Deskripsi: Program membuat segitiga istimewa kembar tercermin sehingga membentuk
# sebuah segitiga sama kaki yang tersusun vertikal dengan tinggi H. Segitiga istimewa adalah 
# segitiga yang dibentuk dengan mengisi baris segitiga dengan angka berurutan,
# dimulai dengan angka 1 di sudut kiri atas

# KAMUS
# H : int
# n : int
# set_awal : int
# set_akhir : int
# i : int
# j : int

# ALGORITMA

H = int(input("Masukkan nilai H: "))

n = 0

# Menentukan lebar segitiga menaik hingga ketinggian berapa, jika H ganjil maka ketinggiannya ditambah 1
set_awal = H // 2 + H % 2

# Menentukan lebar segitiga menurun hingga ketinggian berapa
set_akhir = H // 2

# Mengiterasi ketinggian awal menaik hingga pertengahan segitiga
for i in range(1, set_awal + 1):
  # Print element tiap barisnya
  for j in range(i):
    # Increment element yang akan di-print tiap iterasi 
    n += 1
    print(n, end=" ")
  print("")

# Mengiterasi ketinggian awal menurun hingga akhir
for i in range(set_akhir, 0, -1):
  for j in range(i):
    n += 1
    print(n, end=" ")
  print("")
