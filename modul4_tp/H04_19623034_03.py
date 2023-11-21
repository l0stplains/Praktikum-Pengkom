# NIM/Nama : 19623034/Refki Alfarizi
# Tanggal : 23 Oktober 2023
# Deskripsi : Program menentukan banyaknya kapal musuh.

# KAMUS
# N, M : int
# mtx : array of character
# i, j : int
# total : int

# ALGORITMA

N = int(input("Masukkan N: "))
M = int(input("Masukkan M: "))

mtx = ["" for i in range(N)]

print("Masukkan peta: ")
for i in range(N):
  mtx[i] = input()

total = 0

# awal dari sebuah kapal (dari ujung kiri atas) bisa ditentukan dengan memeriksa apakah di kiri dan di atas pesawat tersebut kosong atau tidak
for i in range(N):
  for j in range(M):
    if mtx[i][j] == '1':
      if i == 0 and j == 0:
        total += 1
      elif i == 0:
        if mtx[i][j-1] == '0':
          total += 1
      elif j == 0:
        if mtx[i-1][j] == '0':
          total += 1
      elif mtx[i-1][j] == '0' and mtx[i][j-1] == '0':
          total += 1

if total:
  print(f"Terdapat {total} kapal musuh pada peta")
else:
  print("Tidak terdapat kapal musuh pada peta")


