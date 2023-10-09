# Not final version, still waiting for review and adding some description later

S = [0 for i in range(30)]

for i in range(30):
  S[i] = int(input(f"Masukkan suhu Kota Bandung {i+1} September 2018: "))

terendah = S[0]
jumlah = 0
found = -1
lebih30 = 0

for i in range(30):
  jumlah += S[i]
  if S[i] < terendah:
    terendah = S[i]
  if S[i] < 15 and found == -1:
    found = i
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
  print(f"Suhu kota bandung di bawah 15 derajat Celcius pada tanggal {i+1} Sept 2018")
else:
  print("Suhu tidak pernah di bawah 15 derajat Celcius")  