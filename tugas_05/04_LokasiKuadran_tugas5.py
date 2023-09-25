# Lokasi Kuadran 04_LokasiKuadran_tugas5.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program menerima sebuah titik lokasi, kemudian mengidentifikasi lokasi titik tersebut.

# KAMUS
# x: float
# y: float

# ALGORITMA

x = float(input("Masukkan lokasi absis (sumbu x) titik: "))
y = float(input("Masukkan lokasi ordinat (sumbu y) titik: "))

if x == 0 and y == 0:
  print("Titik berada pada titik origin")
elif x == 0:
  if y > 0:
    print("Titik berada pada sumbu y positif")
  else: # y < 0
    print("Titik berada pada sumbu y negatif")
elif y == 0:
  if x > 0:
    print("Titik berada pada sumbu x positif")
  else: # x < 0
    print("Titik berada pada sumbu x negatif")
elif x > 0 and y > 0:
  print("Titik berada pada kuadran I")
elif x < 0 and y > 0:
  print("Titik berada pada kuadran II")
elif x < 0 and y < 0:
  print("Titik berada pada kuadran III")
else: # x > 0 and y < 0
  print("Titik berada pada kuadran IV")