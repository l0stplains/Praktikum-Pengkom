# Not final version, still waiting for review and adding some description later

uang = int(input("Masukkan uang yang dibawa Tuan Leo: "))
N = int(input("Masukkan jumlah stasiun: "))

harga = [0 for i in range(N)]
maks = 0
index = 0

for i in range(N):
  harga[i] = int(input(f"Masukkan harga stasiun ke-{i+1}: "))

for i in range(N):
  total = 0
  j = 0
  while total + harga[(i+j) % N] <= uang and j < N:
    total += harga[(i + j) % N]
    j += 1
  if j > maks:
    maks = j
    index = i

if maks > 0:
  print(f"Tuan Leo dapat mengunjungi {maks} stasiun dimulai dari stasiun ke-{index + 1}")
else:
  print("Tuan Leo kekurangan uang.")

  

