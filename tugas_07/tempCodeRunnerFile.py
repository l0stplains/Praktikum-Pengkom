N = int(input("Masukkan ukuran array T: "))


T = [0 for i in range(N)]

for i in range(N):
  T[i] = int(input())

X = int(input("Masukkan elemen yang ingin dicari: "))

i = N - 1
found = False

while(n >= 0 and found = False):
  if T[i] == X:
    found = True
  else:
    i -= 1

print(f"Elemen yang dicari ditemukan di index {i}")