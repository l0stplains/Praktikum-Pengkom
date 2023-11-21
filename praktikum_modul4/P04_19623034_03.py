# NIM/Nama : 19623034/Refki Alfarizi
# Tanggal : 2 November 2023
# Deskripsi : Program mengidentifikasi apakah pion Raja aman dari serangan pion Kuda 

# KAMUS
# gerak_kuda : function
# M : int
# mtx : array of array of char
# index_raja : array of int
# raja_meninggal : boolean
# serangan_mungkin : array of array of int

# ALGORITMA

def gerak_kuda(i, j):
  # FUNGSI

  # KAMUS
  # i, j : int
  # list_gerak : array of array of int

  # Inisiasi array untuk menyimpan semua (8) kemungkinan dari pergerakan pion Kuda
  list_gerak = [[-1, -1] for i in range(8)]

  list_gerak[0] = [i-2, j+1] # gerak 2atas 1kanan
  list_gerak[1] = [i-2, j-1] # gerak 2atas 1kiri
  list_gerak[2] = [i+2, j+1] # gerak 2bawah 1kanan
  list_gerak[3] = [i+2, j-1] # gerak 2bawah 1kiri

  list_gerak[4] = [i+1, j-2] # gerak 2kanan 1bawah
  list_gerak[5] = [i-1, j-2] # gerak 2kanan 1atas
  list_gerak[6] = [i+1, j+2] # gerak 2kiri 1bawah
  list_gerak[7] = [i-1, j+2] # gerak 2kiri 1atas

  return list_gerak

# PROGRAM UTAMA
M = int(input("Masukkan nilai m: "))

mtx = [['' for i in range(M)] for i in range(M)]

index_raja = [-1, -1]
for i in range(M):
  for j in range(M):
    mtx[i][j] = input(f"Masukkan elemen matriks ke-{i+1} {j+1}: ")
    if mtx[i][j] == 'R':
      index_raja = [i, j]

raja_meninggal = False

print("Hasil papan catur")
for i in range(M):
  for j in range(M):
    print(mtx[i][j], end=" ")
    if mtx[i][j] == 'K':
      serangan_mungkin = gerak_kuda(i, j)
      for k in range(8):
        if serangan_mungkin[k] == index_raja: # cek apakah ada serangan yang menuju raja
          raja_meninggal = True
  print()

if raja_meninggal:
  print("Raja tidak aman dari serangan kuda.")
else:
  print("Raja aman dari serangan kuda.")