# Skala Gempa Bumi 01_SkalaGempaBumi_tugas5.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi Program menerima bilangan ritcher dari sebuah gempa bumi 
# dan mengeluarkan output kondisi yang bersesuaian dengan gempa bumi tersebut

# KAMUS
# sr: float
# kondisi: string

# ALGORITMA

sr = float(input("Masukkan Skala Ritcher dari gempa bumi: "))

kondisi = ""
if sr < 0:
  kondisi = "Tidak terdefinisi"
elif sr < 2.0:
  kondisi = "Micro"
elif sr < 3.9:
  kondisi = "Minor"
elif sr < 4.9:
  kondisi = "Light"
elif sr < 5.9:
  kondisi = "Moderate"
elif sr < 6.9:
  kondisi = "Strong"
elif sr <= 7.9:
  kondisi = "Major"
else: # sr > 7.9
  kondisi = "Great"
print(f"Gempa bumi tersebut berkondisi {kondisi}")