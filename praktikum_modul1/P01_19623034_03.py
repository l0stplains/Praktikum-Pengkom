# Problem 3 P01_19623034_03.py
# Nama: Refki Alfarizi
# Tanggal: 21 September 2023
# Deskripsi singkat: Program menentukan banyaknya baju yang dapat dibuat

# KAMUS
# kain : float
# pita : float
# ks : float
# ps : float
# km : float
# pm : float
# kl : float
# pl : float
# s : int
# m : int
# l : int
# maksKain : int
# maksPita : int

# ALGORITMA

kain = float(input("Jumlah Kain : "))
pita = float(input("Jumlah Pita : "))

ks = 1.2
ps = 0.8
km = 1.5
pm = 1.0
kl = 2.0
pl = 1.3

s = 0
m = 0
l = 0

if kain > (ks + km + kl) and pita > (ps + pm + pl):
  kain -= (ks + km + kl)
  pita -= (ps + pm + pl)
  s += 1
  m += 1
  l += 1

  if kain > kl and pita > pl:
    maksKain = int(kain // kl)
    maksPita = int(pita // pl)

    # Tentukan pembatas baju yang bisa dibuat (min{banyak baju dari sisa kain, banyak baju dari sisa pita})
    if maksKain < maksPita:
      l += maksKain

      kain -= maksKain * kl
      pita -= maksKain * pl
    else:
      l += maksPita

      kain -= maksPita * kl
      pita -= maksPita * pl

  if kain > km and pita > pm:
    maksKain = int(kain // km)
    maksPita = int(pita // pm)
    if maksKain < maksPita:
      m += maksKain

      kain -= maksKain * km
      pita -= maksKain * pm
    else:
      m += maksPita

      kain -= maksPita * km
      pita -= maksPita * pm

  if kain > ks and pita > ps:
    maksKain = int(kain // ks)
    maksPita = int(pita // ps)
    if maksKain < maksPita:
      s += maksKain

      kain -= maksKain * ks
      pita -= maksKain * ps
    else:
      s += maksPita

      kain -= maksPita * ks
      pita -= maksPita * ps

  print(f"Nona Deb dapat membuat {s} ukuran S, {m} ukuran M, {l} ukuran L.")
else:
  print("Bahan tidak cukup untuk membuat baju")
