# Konversi Suhu 02_KonversiSuhu_tugas5.py
# Nama: Refki Alfarizi
# NIM: 19623034
# Deskripsi: Program menerima input suhu dalam satuan kelvin, celcus, reamur, atau fahrenheit
# kemudian suhu tersebut dikonversikan ke kelvin, celcius, reamur, atau fahrenheit sesuai dengan pilihan.

# KAMUS
# opsi: string
# opsi_konv: string
# satuan: int
# konv: int
# suhu: float
# hasil: float
# satuan_hasil: string

# ALGORITMA

opsi = """
KONVERSI SUHU
1. Kelvin
2. Celcius
3. Reamur
4. Fahrenheit
Pilih satuan suhu yang akan dikonversi (masukkan angkanya saja): """

opsi_konv = """
1. Kelvin
2. Celcius
3. Reamur
4. Fahrenheit
Pilih satuan suhu hasil konversi (masukkan angkanya saja): """

satuan = int(input(opsi))
konv = int(input(opsi_konv))

if satuan == 1:
  suhu = float(input("Masukkan suhu dalam Kelvin: "))
  hasil = 0.
  satuan_hasil = ""
  if konv == 1:
    hasil = suhu
    satuan_hasil = "K"
  elif konv == 2:
    hasil = suhu - 273
    satuan_hasil = "°C"
  elif konv == 3:
    hasil = 4/5 * (suhu - 273)
    satuan_hasil = "°R"
  elif konv == 4:
    hasil = 9/5 * (suhu - 273) + 32
    satuan_hasil = "°F"
  else:
    satuan_hasil = "\nMohon masukkan pilihan satuan sesuai opsi yang diberikan"
  
  print(f"Hasil konversi dari {suhu:.2f} K adalah {hasil:.2f} {satuan_hasil}")
  
elif satuan == 2:
  suhu = float(input("Masukkan suhu dalam derajat Celcius: "))
  hasil = 0.
  satuan_hasil = ""
  if konv == 1:
    hasil = suhu + 273
    satuan_hasil = "K"
  elif konv == 2:
    hasil = suhu
    satuan_hasil = "°C"
  elif konv == 3:
    hasil = 4/5 * suhu
    satuan_hasil = "°R"
  elif konv == 4:
    hasil = 9/5 * suhu + 32
    satuan_hasil = "°F"
  else:
    satuan_hasil = "\nMohon masukkan pilihan satuan sesuai opsi yang diberikan"
  
  print(f"Hasil konversi dari {suhu:.2f} °C adalah {hasil:.2f} {satuan_hasil}")
elif satuan == 3:
  suhu = float(input("Masukkan suhu dalam derajat Reamur: "))
  hasil = 0.
  satuan_hasil = ""
  if konv == 1:
    hasil = 5/4 * suhu + 273
    satuan_hasil = "K"
  elif konv == 2:
    hasil = 5/4 * suhu
    satuan_hasil = "°C"
  elif konv == 3:
    hasil = suhu
    satuan_hasil = "°R"
  elif konv == 4:
    hasil = 9/4 * suhu + 32
    satuan_hasil = "°F"
  else:
    satuan_hasil = "\nMohon masukkan pilihan satuan sesuai opsi yang diberikan"
  
  print(f"Hasil konversi dari {suhu:.2f} °R adalah {hasil:.2f} {satuan_hasil}")

elif satuan == 4:
  suhu = float(input("Masukkan suhu dalam derajat Fahrenheit: "))
  hasil = 0.
  satuan_hasil = ""
  if konv == 1:
    hasil = 5/9 * (suhu - 32) + 273
    satuan_hasil = "K"
  elif konv == 2:
    hasil = 5/9 * (suhu - 32)
    satuan_hasil = "°C"
  elif konv == 3:
    hasil = 4/9 * (suhu - 32)
    satuan_hasil = "°R"
  elif konv == 4:
    hasil = suhu
    satuan_hasil = "°F"
  else:
    satuan_hasil = "\nMohon masukkan pilihan satuan sesuai opsi yang diberikan"
  
  print(f"Hasil konversi dari {suhu:.2f} °F adalah {hasil:.2f} {satuan_hasil}")
else:
  print("Mohon masukkan pilihan sesuai opsi yang diberikan")