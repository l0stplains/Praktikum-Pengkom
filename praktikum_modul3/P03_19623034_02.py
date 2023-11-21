# NIM/Nama : 19623034/Refki Alfarizi
# Tanggal : 19 Oktober 2023
# Deskripsi : Program menentukan jumlah potongan list yang jika seluruh elemen
# penyusun potongannya dijumlahkan akan menghasilkan bilangan prima.

# KAMUS
# prime_subarray : int
# N : int
# arr : array of int
# i : int
# currSum : int
# j : int
# isPrime : bool
# d : int

# ALGORITMA

# inisiasi banyak potongan array yang jumlah elemennya prima
prime_subarray = 0

N = int(input("Masukkan nilai N: "))
              
arr = [0 for i in range(N)]

for i in range(N):
  arr[i] = int(input(f"Masukkan bilangan ke {i+1}: "))

for i in range(N):
  # inisiasi jumlah dari elemen-elemen potongan array
  currSum = 0 
  for j in range(i, N):
    currSum += arr[j]

    isPrime = True
    # Cek apakah curSum prima
    for d in range(2, int(currSum ** 0.5) + 1):
      if currSum % d == 0:
        isPrime = False
    
    if isPrime and currSum != 1:
      prime_subarray += 1

if prime_subarray != 0:
  print(f"Terdapat {prime_subarray} potongan list yang jumlahnya prima.")
else:
  print("Tidak ada potongan list yang jumlahnya prima.")