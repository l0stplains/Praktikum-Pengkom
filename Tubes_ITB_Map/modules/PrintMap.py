def printPixel(color):
  print(f"{color}{'█'}\033[0m", end="")

def printMap(mapArray):
  """
  Program akan menampilkan peta ke user dengan mengubah data pada data array map menjadi peta yang mudah dimengerti oleh pengguna.
  """
  black = '\033[30m'
  red = '\033[31m'
  green = '\033[32m'
  orange = '\033[38;2;205;112;0m'
  blue = '\033[34m'
  purple = '\033[35m'
  cyan = '\033[36m'
  lightgrey = '\033[37m'
  darkgrey = '\033[90m'
  lightred = '\033[91m'
  lightgreen = '\033[92m'
  yellow = '\033[93m'
  lightblue = '\033[94m'
  pink = '\033[95m'
  lightcyan = '\033[96m'
  chocolate = '\033[38;2;123;63;0m'

  for i in range(len(mapArray)):
    for j in range(len(mapArray[0])):
      x = mapArray[i][j]
      if x == 'J' or x == 'j':
        printPixel(darkgrey)
      elif x == 'H':
        printPixel(green)
      elif x[0] == "X":
        printPixel(darkgrey)
      elif x[0] == 'Z':
        printPixel(blue)
      elif x in ['G2', 'G1', 'LR', 'KIA', 'GF', 'JB', 'IP', 'L3', 'WTP']:
        printPixel(lightgrey)
      elif x in ['AD', 'VA', 'VB', 'VC', 'R', 'GSG', 'TB1','TB2','TB3', 'TB4', 'TB5']:
        printPixel(chocolate)
      elif x in ["L", "LB", 'AMP']:
        printPixel(lightgreen)
      elif x in ['A']:
        printPixel(lightblue)
      else:
        printPixel(orange)
    print("")