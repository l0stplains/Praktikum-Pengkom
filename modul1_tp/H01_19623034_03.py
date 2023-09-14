# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 14 September 2023
# Deskripsi: Program menentukan pembagian kelas dan harga tiket pesawat berdasarkan kursi yang dipilih

# KAMUS
# kelas: string
# harga: integer
# nomor: integer
# posisi: string

# ALGORITMA

# Input
nomor = int(input("Tentukan Nomor Kursi: "))
posisi = input("Tentukan Posisi Kursi: ")

# Proses
kelas = ""
harga = 0

if (nomor > 0 and nomor <= 20) or (nomor > 50 and nomor <= 60):
  kelas = "Hot Seat"

  if posisi == "A" or posisi == "F":
    harga = 1600 * 1000
  elif posisi == "B" or posisi == "E":
    harga = 1550 * 1000
  elif posisi == "C" or posisi == "D":
    harga = 1500 * 1000

elif (nomor > 20 and nomor <= 50) or (nomor > 60 and nomor <= 100):
  kelas = "Regular"

  if posisi == "A" or posisi == "F":
    harga = 1000 * 1000
  elif posisi == "B" or posisi == "E":
    harga = 950 * 1000
  elif posisi == "C" or posisi == "D":
    harga = 900 * 1000

print(f"Tuan Kil memilih kursi {kelas} dengan harga {harga}.")