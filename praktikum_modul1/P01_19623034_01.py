# Problem 1 P01_19623034_01.py
# Nama: Refki Alfarizi
# Tanggal: 21 September 2023
# Deskripsi singkat: Program membandingkan total nilai uang Peng dan uang Kom

# KAMUS
# nPeng : int
# nKom : int
# konvPeng : int
# konvKom : int

# ALGORITMA

nPeng = int(input("Banyak uang Peng yang ditawarkan: "))
nKom = int(input("Banyak uang Kom yang ditawarkan: "))
konvPeng = int(input("Konversi mata uang Peng ke rupiah: "))
konvKom = int(input("Konversi mata uang Kom ke rupiah: "))

if (nPeng * konvPeng) > (nKom * konvKom):
  print("Adik Tuan Kil memilih uang Peng.")
elif (nPeng * konvPeng) < (nKom * konvKom):
  print("Adik Tuan Kil memilih uang Kom.")
else: # (nPeng * konvPeng) == (nKom * konvKom)
  print("Uang Peng dan Kom sama besar.") 