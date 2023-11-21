# NIM/Nama : 19623034/Refki Alfarizi
# Tanggal : 19 Oktober 2023
# Deskripsi : Program menentukan apakah tulisan Komi sudah benar atau belum.

# KAMUS
# nA : int
# A : string
# nT : int 
# T : SyntaxWarning
# S : array of character
# currIndex : int
# currLen : int
# i : int
# isSame : bool
# panjang_tulis_seharusnya : int

# ALGORITMA

nA = int(input("Masukkan panjang kata asli: "))
A = input("Masukkan kata asli: ")

# kata aspraknya anggap nT tidak akan lebih dari seharusnya
nT = int(input("Masukkan panjang kata yang ditulis: "))
T = input("Masukkan kata yang ditulis: ")

S = ['' for i in range(nT)]

currIndex = 0
currLen = 1
for i in range(nT):
  S[i] = A[currIndex]
  currIndex = (currIndex + 1) % nA # jaga jaga kalo ternyata nT lebih dari seharusnya
  if currIndex == currLen:
    currIndex = 0
    currLen += 1

# Cek jika kata yang ditulis sudah sesuai
isSame = True
for i in range(nT):
  if S[i] != T[i]:
    isSame = False

panjang_tulis_seharusnya = (nA*(1+nA)/2) # jaga jaga kalo panjang tulis ga sesuai seharusnya
if isSame and panjang_tulis_seharusnya == nT:
  print("Tulisan Komi sudah benar.")
else:
  print("Tulisan Komi masih salah.")