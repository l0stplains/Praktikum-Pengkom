# NIM/ Nama: 19623034/Refki Alfarizi
# Tanggal: 23 Oktober 2023
# Deskripsi: Program menentukan banyaknya bakteri setelah ditinggal selama beberapa detik

# KAMUS
# reproduksi : function
# N, K : int
# total : int

# ALGORITMA

def reproduksi(awal, detik):
  # KAMUS
  # awal : int
  # detik : int
  
  return   (2**(detik+1) - 1)  * awal 

N = int(input("Masukkan N: "))
K = int(input("Masukkan K: "))

total = reproduksi(N, K)

print(f"Terdapat {total} Bakteri Pengkombacter.")