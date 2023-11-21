from modules.ITBMap import getOptimizedMatrix
from modules.PrintMap import printMap
from modules.FindShortestPath import findShortestPathLength
import os


def daftar_gedung(list_lokasi):
  """
  Fungsi menampilkan list lokasi yang bisa dikunjungi
  """
  for i, lokasi in enumerate(list_lokasi, start=1):
    if i % 6 == 1: # maksimal menampilkan 6 lokasi dalam 1 baris
        print()
    
    print("{:<4s}{:<15s}".format(f"{i}. ", lokasi), end='')

def clear():
   print()
   os.system("cls||clear")

list_lokasi = [
    "GKU 1", "GKU 2", "GKU 3", "Gerbang Utama", "Gedung E", "Gedung C",
    "Mushola FSRD", "Toilet FSRD", "Danau", "Gedung D", "KOICA", "Rektorat",
    "Labtek IA&IB", "Gedung A", "Gedung SBM", "Lap. Basket", "GSG", "GOR Futsal",
    "Asrama TBI", "Asrama TBII", "Asrama TBIII", "Asrama TBIV", "Asrama TBV", "Lapangan",
    "Labtek IIA", "Labtek IIB", "Screenhouse", "WTP", "Gedung Baca", "Studio Kriya",
    "Labtek IC", "Asrama Dosen", "IPST", "Labtek VA", "Labtek VB", "Labtek VC",
    "Al-Jabbar", "Kehutanan", "Amphiteater"
  ]
list_pintu = ["X-G1", "X-G2", "X-GK3", "X-GU", "X-GE", "X-GC", "X-MU", "X-TO", "X-D", "X-GD", "X-KIA", "X-R", "X-L3", "X-GA", "X-SBM", "X-LB", "X-GSG", "X-GF", "X-TB1",
              "X-TB2", "X-TB3", "X-TB4", "X-TB5", "X-L", "X-2A", "X-2B", "X-SH", "X-WTP", "X-GB", "X-ST", "X-LR", "X-AD", "X-IP", "X-VA", "X-VB", "X-VC", "X-JB", "X-KH", "X-AMP"]
koor_pintu = {'X-GF': (21, 55), 'X-L': (29, 32), 'X-TB1': (33, 49), 'X-GSG': (33, 63), 'X-TB2': (36, 45), 'X-TB3': (39, 40), 'X-WTP': (41, 7), 'X-TB4': (41, 35), 'X-SH': (43, 29), 'X-AMP': (45, 54), 'X-LB': (48, 65), 'X-2A': (49, 31), 'X-2B': (53, 33), 'X-SBM': (58, 41), 'X-GA': (59, 44), 'X-GK3': (59, 73), 'X-KIA': (61, 69), 'X-TB5': (62, 15), 'X-ST': (64, 40), 'X-GB': (64, 42), 'X-GC': (65, 49), 'X-MU': (66, 41), 'X-TO': (66, 43), 'X-GD': (70, 47), 'X-R': (70, 74), 'X-GE': (72, 42), 'X-LR': (78, 17), 'X-L3': (79, 26), 'X-G1': (84, 54), 'X-G2': (97, 31), 'X-IP': (105, 62), 'X-VA': (134, 67), 'X-KH': (136, 69), 'X-AD': (138, 47), 'X-VB': (139, 66), 'X-VC': (143, 67), 'X-D': (158, 9), 'X-JB': (159, 70), 'X-GU': (170, 1)}

clear()
print(
'''
           _   _           __      __  _____    _____               _____   _____ 
          | \ | |     /\   \ \    / / |_   _|  / ____|     /\      / ____| |_   _|
          |  \| |    /  \   \ \  / /    | |   | |  __     /  \    | (___     | |  
          | . ` |   / /\ \   \ \/ /     | |   | | |_ |   / /\ \    \___ \    | |  
          | |\  |  / ____ \   \  /     _| |_  | |__| |  / ____ \   ____) |  _| |_ 
          |_| \_| /_/    \_\   \/     |_____|  \_____| /_/    \_\ |_____/  |_____|
                                 _____   _______   ____  
                                |_   _| |__   __| |  _ \ 
                                  | |      | |    | |_) |
                                  | |      | |    |  _ < 
                                 _| |_     | |    | |_) |
                                |_____|    |_|    |____/ 
       _            _______   _____   _   _              _   _    _____    ____    _____  
      | |     /\   |__   __| |_   _| | \ | |     /\     | \ | |  / ____|  / __ \  |  __ \ 
      | |    /  \     | |      | |   |  \| |    /  \    |  \| | | |  __  | |  | | | |__) |
  _   | |   / /\ \    | |      | |   | . ` |   / /\ \   | . ` | | | |_ | | |  | | |  _  / 
 | |__| |  / ____ \   | |     _| |_  | |\  |  / ____ \  | |\  | | |__| | | |__| | | | \ \ 
  \____/  /_/    \_\  |_|    |_____| |_| \_| /_/    \_\ |_| \_|  \_____|  \____/  |_|  \_\               
 

'''
)
loop1 = True
pertamaKali = True
while loop1 == True:
  selectionOne = "1"
  mapArr = getOptimizedMatrix()
  while selectionOne not in ["2", "3"]:
    if pertamaKali == True:
      print("Silakan input angka '1' atau '2'")
      print("1. Tampilkan peta ITB Jatinangor.")
      print("2. Program navigasi ITB Jatinangor")
      selectionOne = input("Input : ")
      print("----------------------------------------------------------------")
      if selectionOne == "2":
          pertamaKali = False
    else:
      print("Apakah ingin navigasi lagi?")
      print("1. Tampilkan peta ITB Jatinangor.")
      print("2. Ya")
      print("3. Tidak (tutup program)")
      selectionOne = input("Input : ")
      print("----------------------------------------------------------------")
    if selectionOne == "1":
      clear()
      # Tampilkan peta
      printMap(mapArr)
      # Untuk spasi di terminal (looks less crowded!)
      print("----------------------------------------------------------------")
    if selectionOne == "3":
      mapArr = getOptimizedMatrix()
      loop1 = False
      clear()
      print("Terima kasih telah menggunakan program kami!")

  # run program navigasi
  if loop1 == True:
    clear()
    daftar_gedung(list_lokasi)
    mapArr = getOptimizedMatrix()
    print("")
    print("Gunakan tabel index nomor di atas untuk input tempat asal dan tujuan Anda di bawah.")
    print("Contoh : Jika ingin memilih 'Danau' inputlah '9'")
    print("")
    index_awal = int(input("Masukkan nomor tempat asal Anda: ")) - 1
    index_akhir = int(input("Masukkan nomor tempat tujuan Anda: ")) - 1
    print("\nMencari rute tercepat...")
    asal = koor_pintu[list_pintu[index_awal]]
    tujuan = koor_pintu[list_pintu[index_akhir]]

    dist, path = findShortestPathLength(mapArr, asal, tujuan)

    clear()
    
    for i in path:
      mapArr[i[0]][i[1]] = 'Z'
    printMap(mapArr)

    if (dist != -1):
        print(f"Jarak dari {list_lokasi[index_awal]} ke {list_lokasi[index_akhir]} sekitar {dist*5.143:.2f} m")
        print(f"Dengan sekitar {dist*5.143/1000 * 11.33:.0f} menit berjalan kaki")

    else:
        print("Rute terpendek tidak ditemukan")

    print("----------------------------------------------------------------")
