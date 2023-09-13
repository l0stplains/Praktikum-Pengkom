# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 14 September 2023
# Deskripsi: Program menerima input berupa dua buah titik pada bidang kartesius.
# Program akan menentukan apakah garis yang melalui kedua titik tersebut
# adalah garis horizontal, vertikal, atau garis bergradien tertentu.

# KAMUS
# x1: Absis dari titik pertama (int)
# y1: Ordinat dari titik pertama (int)
# x2: Absis dari titik pertama (int)
# y2: Ordinat dari titik kedua (int)
# gradien: Kemiringan garis (float)

# ALGORITMA

# Input
x1 = int(input("Masukkan x1: "))
y1 = int(input("Masukkan y1: "))
x2 = int(input("Masukkan x2: "))
y2 = int(input("Masukkan y2: "))

# Proses
# Tentukan apakah gradien garis terdefinisi (Jika tidak maka garis vertikal)
if x2 - x1 != 0:
  gradien = (y2 - y1) / (x2 - x1)

  # Tentukan apakah garis merupakan garis horizontal
  if gradien == 0:
    print("Garis tersebut merupakan garis horizontal.")
  else:
    print(f"Garis tersebut memiliki gradien {gradien}.")

else:
  print("Garis teresbut merupakan garis vertikal.")