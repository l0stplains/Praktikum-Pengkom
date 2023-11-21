# Problem 1 H03_19623034_01.py
# NIM/Nama: 19623034/Refki Alfarizi
# Tanggal: 10 Oktober 2023
# Deskripsi: Program menentukan nomor-nomor perwakilan yang tidak mendatangi acara

# KAMUS
# N : int
# M : int
# arr : array [1...N] of int
# i : int
# x : int


# ALGORITMA

N = int(input("Masukkan nilai N: "))
M = int(input("Masukkan nilai M: "))

# Inisiasi array dengan nomor 1 - N
arr = [i for i in range(1, N+1)]

# Jika hadir, tandai dengan cara mengubah nilai pada array yang sesuai dengan nomor perwakilannya menjadi nol
for i in range(M):
  x = int(input(f"Masukkan data ke-{i+1}: "))
  arr[x-1] = 0

print("Nomor perwakilan yang tidak datang: ", end="")

# Jika tidak ditandai maka tidak datang
for i in range(N):
  if arr[i] != 0:
    print(arr[i], end=" ")


