# Menghitung Hari 03_MenghitungHari_tugas5.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program menghitung jumlah hari dalam rentang tanggal pada tahung yang sama.

# KAMUS
# opsi_bulan: string
# tahun: int
# bulan1: int
# tanggal1: int
# bulan2: int
# tanggal2: int
# jan, feb, mar, apr, mei, jun, jul, agu, sep, okt, nov, des: int
# rentang_hari: int

# ALGORITMA

opsi_bulan = """
1. Januari
2. Februari
3. Maret
4. April
5. Mei
6. Juni
7. Juli
8. Agustus
9. September
10. Oktober
11. November
12. Desember
Pilih bulan pada tahun tersebut (masukkan angka): """

tahun = int(input("Masukkan tahun: "))

print("\nTanggal Pertama")
bulan1 = int(input(opsi_bulan))
tanggal1 = int(input("Masukkan tanggal pada bulan tersebut: "))

print("\nTanggal Kedua")
bulan2 = int(input(opsi_bulan))
tanggal2 = int(input("Masukkan tanggal pada bulan tersebut: "))

# Definisikan jumlah hari dari awal tahun sampai sebelum bulan tertentu
jan = 0
feb = jan + 31

# Cek apakah tahun merupakan tahun kabisat
if tahun % 4 == 0:
  mar = feb + 29
else: # tahun % 4 != 0
  mar = feb + 28

apr = mar + 31
mei = apr + 30
jun = mei + 31
jul = jun + 30
agu = jul + 31
sep = agu + 31
okt = sep + 30
nov = okt + 31
des = nov + 30

# Tambah jumlah hari sebelum bulan dengan hari dari tanggal pada bulan tersebut
if bulan1 == 1 and 0 < tanggal1 <= feb-jan:
  tanggal1 += jan
elif bulan1 == 2 and 0 < tanggal1 <= mar-feb:
  tanggal1 += feb
elif bulan1 == 3 and 0 < tanggal1 <= apr-mar:
  tanggal1 += mar
elif bulan1 == 4 and 0 < tanggal1 <= mei-apr:
  tanggal1 += apr
elif bulan1 == 5 and 0 < tanggal1 <= jun-mei:
  tanggal1 += mei
elif bulan1 == 6 and 0 < tanggal1 <= jul-jun:
  tanggal1 += jun
elif bulan1 == 7 and 0 < tanggal1 <= agu-jul:
  tanggal1 += jul
elif bulan1 == 8 and 0 < tanggal1 <= sep-agu:
  tanggal1 += agu
elif bulan1 == 9 and 0 < tanggal1 <= okt-sep:
  tanggal1 += sep
elif bulan1 == 10 and 0 < tanggal1 <= nov-okt:
  tanggal1 += okt
elif bulan1 == 11 and 0 < tanggal1 <= des-nov:
  tanggal1 += nov
elif bulan1 == 12 and 0 < tanggal1 <= 31:
  tanggal1 += des
else:
  tanggal1 = 0
  print("Tanggal pertama yang dimasukkan tidak terdapat dalam kalender")

if bulan2 == 1 and 0 < tanggal2 <= feb-jan:
  tanggal2 += jan
elif bulan2 == 2 and 0 < tanggal2 <= mar-feb:
  tanggal2 += feb
elif bulan2 == 3 and 0 < tanggal2 <= apr-mar:
  tanggal2 += mar
elif bulan2 == 4 and 0 < tanggal2 <= mei-apr:
  tanggal2 += apr
elif bulan2 == 5 and 0 < tanggal2 <= jun-mei:
  tanggal2 += mei
elif bulan2 == 6 and 0 < tanggal2 <= jul-jun:
  tanggal2 += jun
elif bulan2 == 7 and 0 < tanggal2 <= agu-jul:
  tanggal2 += jul
elif bulan2 == 8 and 0 < tanggal2 <= sep-agu:
  tanggal2 += agu
elif bulan2 == 9 and 0 < tanggal2 <= okt-sep:
  tanggal2 += sep
elif bulan2 == 10 and 0 < tanggal2 <= nov-okt:
  tanggal2 += nov
elif bulan2 == 11 and 0 < tanggal2 <= des-nov:
  tanggal2 += feb
elif bulan2 == 12 and 0 < tanggal2 <= 31:
  tanggal2 += des
else:
  tanggal2 = 0
  print("Tanggal kedua yang dimasukkan tidak terdapat dalam kalender")

if tanggal1 > tanggal2:
  rentang_hari = tanggal1 - tanggal2
else: # tanggal1 <= tanggal2
  rentang_hari = tanggal2 - tanggal1

print(f"Jumlah hari dari rentang tanggal pertama dan kedua adalah {rentang_hari} hari")
