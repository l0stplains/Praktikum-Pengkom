# NIM/Nama : 19623034/Refki Alfarizi
# Tanggal : 19 Oktober 2023
# Deskripsi : Program memberitahu berapa banyak uang (minimum) yang harus dikeluarkan duntuk makan di
# restoran jika akan makan selama 3 jam tanpa henti.

# KAMUS
# N : int
# arr : array of int
# i : int
# harga_min : int
# harga_temp: int

# ALGORITMA

# N > 3
N = int(input("Masukkan nilai N: "))

arr = [0 for i in range(N)]

for i in range(N):
  arr[i] = int(input(f"Masukkan harga jam ke-{i + 1}: "))
  
# Inisiasi harga minimal dengan jumlah harga 3 jam pertama
harga_min = arr[0] + arr[1] + arr[2]
for i in range(1, N-2):
  harga_temp = arr[i] + arr[i+1] + arr[i+2]
  if harga_temp < harga_min:
    harga_min = harga_temp

print(f"Total harga yang harus dibayar adalah {harga_min}.")