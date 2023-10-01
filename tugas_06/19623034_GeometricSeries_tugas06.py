# Geometric Series 19623034_GeometricSeries_tugas06.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program menghitung suatu deret geometri dan apabila konvergen
# dapat ditentukan nilai error-nya (nilai G konvergen ke - G)

# KAMUS
# a : float
# r : float
# n : int
# G : float
# E : float
# i : int
# isConvergence : bool

# ALGORITMA
print("Program menghitung suatu deret geometri dan apabila konvergen dapat dicari nilai error (nilai G konvergen ke - G)")
print("G = a + ar + ar^2 + ar^3 + ... + ar^n\n")
a = float(input("Masukkan nilai a: "))
r = float(input("Masukkan nilai r: "))
n = int(input("Masukkan nilai n: "))

# Hitung nilai G (deret geometri)
G = 0.
for i in range(0, n+1):
  G += a  * (r ** i)

# Tentukan apakah G konvergen atau tidak
if 0 <= r < 1:
  isConvergence = True

  # Hitung error
  E = a/(1-r) - G
else: # r >= 1
  isConvergence = False

print(f"Nilai G adalah: {G}")
if isConvergence:
  print(f"Nilai E (error) adalah: {E}")
else: # isConvergence == False
  print("Geometric series/deret geometri tersebut tidak konvergen")




