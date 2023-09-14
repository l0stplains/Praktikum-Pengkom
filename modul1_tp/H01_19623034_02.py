# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 14 September 2023
# Deskripsi: Program akan menentukan apakah garis yang melalui kedua titik dari input
# adalah garis horizontal, vertikal, atau garis bergradien tertentu.

# KAMUS
# x1: integer
# y1: integer
# x2: integer
# y2: integer
# gradien: float

# ALGORITMA

# Input
x1 = int(input("Masukkan x1: "))
y1 = int(input("Masukkan y1: "))
x2 = int(input("Masukkan x2: "))
y2 = int(input("Masukkan y2: "))

# Proses
if x2 - x1 != 0:
  gradien = (y2 - y1) / (x2 - x1)

  if gradien == 0:
    print("Garis tersebut merupakan garis horizontal.")
  else: # gradien != 0
    print(f"Garis tersebut memiliki gradien {gradien}.")

else: # x2 == x1
  print("Garis teresbut merupakan garis vertikal.")