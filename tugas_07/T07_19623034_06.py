# Latihan-6 T07_19623034_06.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program mencatat data suhu kota Bandung di bulan Sept. 2018
# dan menuliskan data rata-rata, suhu terendah, tanggal dimana suhu >= 30 derajat, dan tanggal pertamakali suhu di bawah 15 derajat celcius.

# KAMUS
# S : array [30] of int
# terendah : int
# jumlah : int
# found : int
# lebih30 : int

# S = [14, 40, 32, 36, 24, 13, 39, 35, 17, 18, 13, 13, 37, 24, 13, 39, 34, 12, 16, 32, 14, 19, 24, 34, 13, 20, 30, 13, 29, 36]

# ALGORITMA

S = [0 for i in range(30)]

for i in range(30):
  S[i] = int(input(f"Masukkan suhu Kota Bandung {i+1} September 2018: "))

terendah = S[0]
jumlah = 0
found = -1
lebih30 = 0

for i in range(30):
  jumlah += S[i]

  # Mencari suhu terendah
  if S[i] < terendah:
    terendah = S[i]
  # Mencari tanggal pertama suhu < 15
  if S[i] < 15 and found == -1:
    found = i
  # Menentukan banyak tanggak dimana suhu >= 30
  if S[i] >= 30:
    lebih30 += 1

print(f"Rata-rata suhu di kota bandung di bulan Sept. 2018 adalah {jumlah/30} °C")
print(f"Suhu terendah di bulan Sept. 2018 adalah {terendah} °C")


if lebih30 != 0:
  print(f"Suhu harian kota Bandung >= 30 °C pada tanggal berikut: ")
  for i in range(30):
    if S[i] >= 30:
      print(i+1, end=" ")
  print()
else:
  print("Suhu tidak pernah lebih dari samadengan 30 derajat Celcius")

if found != -1:
  print(f"Suhu kota bandung di bawah 15 derajat Celcius pada tanggal {found+1} Sept 2018")
else:
  print("Suhu tidak pernah di bawah 15 derajat Celcius")  

# Rata-rata suhu di kota bandung di bulan Sept. 2018 adalah 24.433333333333334 °C
# Suhu terendah di bulan Sept. 2018 adalah 12 °C
# Suhu harian kota Bandung >= 30 °C pada tanggal berikut:
# 2 3 4 7 8 13 16 17 20 24 27 30
# Suhu kota bandung di bawah 15 derajat Celcius pada tanggal 1 Sept 2018