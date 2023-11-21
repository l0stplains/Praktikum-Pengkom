def bisaDilewati(mat, dikunjungi, x, y, min_dist, dist):
  return (dist <= min_dist and x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and (mat[x][y] == 'J' or mat[x][y][0] == 'X') and (not dikunjungi[x][y]))


def findShortestPath(mat, dikunjungi, i, j, x, y, min_dist, dist, min_path, path):
  """
  Fungsi berikut merupakan implementasi dari algroitma menemukan jalan (path finding) Depth First Search (DFS)
  dengan menggunakan metode rekursi dengan optimisasi heuristik.
  """
  if (i == x and j == y):
    if min_dist < dist:
      return (min_dist, min_path)
    return (dist, path)

  # set (i, j) cell as dikunjungi
  dikunjungi[i][j] = True

  # Percabangan kasus di bawah ini merupakan bentuk dari optimisasi heuristik.
  # jika destinasi ada di bawah posisi sekarang, maka prioritaskan gerak ke bawah
  if (i <= x):
     # pindah ke bawah
    if (bisaDilewati(mat, dikunjungi, i + 1, j, min_dist, dist + 1)):
      min_dist, min_path = findShortestPath(mat, dikunjungi, i + 1, j, x, y, min_dist, dist + 1, min_path, path + [(i+1,j)])
    # jika destinasi ada di kanan posisi sekarang, maka prioritaskan gerak ke kanan
    if (j <= y):
      # pindah ke kanan
      if (bisaDilewati(mat, dikunjungi, i, j + 1, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i, j + 1, x, y, min_dist, dist + 1, min_path,  path + [(i,j+1)])
      # pindah ke atas
      if (bisaDilewati(mat, dikunjungi, i - 1, j, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i - 1, j, x, y, min_dist, dist + 1, min_path,  path + [(i-1,j)])
      # pindah ke kiri
      if (bisaDilewati(mat, dikunjungi, i, j - 1, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i, j - 1, x, y, min_dist, dist + 1, min_path,  path + [(i,j-1)])
    else:
      # pindah ke kiri
      if (bisaDilewati(mat, dikunjungi, i, j - 1, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i, j - 1, x, y, min_dist, dist + 1, min_path,  path + [(i,j-1)])
      # pindah ke atas
      if (bisaDilewati(mat, dikunjungi, i - 1, j, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i - 1, j, x, y, min_dist, dist + 1, min_path,  path + [(i-1,j)])
      # pindah ke kanan
      if (bisaDilewati(mat, dikunjungi, i, j + 1, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i, j + 1, x, y, min_dist, dist + 1, min_path,  path + [(i,j+1)])
  else:
    # pindah ke atas
    if (bisaDilewati(mat, dikunjungi, i - 1, j, min_dist, dist + 1)):
      min_dist, min_path = findShortestPath(mat, dikunjungi, i - 1, j, x, y, min_dist, dist + 1, min_path,  path + [(i-1,j)])
    if (j <= y):
      # pindah ke kanan
      if (bisaDilewati(mat, dikunjungi, i, j + 1, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i, j + 1, x, y, min_dist, dist + 1, min_path,  path + [(i,j+1)])
      # pindah ke bawah
      if (bisaDilewati(mat, dikunjungi, i + 1, j, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i + 1, j, x, y, min_dist, dist + 1, min_path, path + [(i+1,j)])
      # pindah ke kiri
      if (bisaDilewati(mat, dikunjungi, i, j - 1, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i, j - 1, x, y, min_dist, dist + 1, min_path,  path + [(i,j-1)])
    else:
      # pindah ke kiri
      if (bisaDilewati(mat, dikunjungi, i, j - 1, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i, j - 1, x, y, min_dist, dist + 1, min_path,  path + [(i,j-1)])
      # pindah ke bawah
      if (bisaDilewati(mat, dikunjungi, i + 1, j, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i + 1, j, x, y, min_dist, dist + 1, min_path, path + [(i+1,j)])
      # pindah ke kanan
      if (bisaDilewati(mat, dikunjungi, i, j + 1, min_dist, dist + 1)):
        min_dist, min_path = findShortestPath(mat, dikunjungi, i, j + 1, x, y, min_dist, dist + 1, min_path,  path + [(i,j+1)])

  # backtracking: hapus (i, j) dari matriks dikunjungi 
  dikunjungi[i][j] = False
  return (min_dist, min_path)
 

def findShortestPathLength(mat, src, dest):
  """
  Fungsi berikut merupakan fungsi yang melakukan pre-proccessing sebelum mencari rute terpendek
  Fungsi ini lalu akan memanggil fungsi findShortestPath lalu mengembalikan hasil dari fungsi tersebut.
  """
  if ((mat[src[0]][src[1]][0] not in ['J','X']) or (mat[dest[0]][dest[1]][0] not in ['J', 'X'])):
    return (-1, [])

  row = len(mat)
  col = len(mat[0])

  if src[0] < dest[0]:
    temp = src
    src = dest
    dest = temp

  dikunjungi = [[None for _ in range(col)] for i in range(row)]

  dist = float("inf")
  path = [src]
  dist, path = findShortestPath(mat, dikunjungi, src[0],
                          src[1], dest[0], dest[1], dist, 0, path, path)

  if (dist != float("inf")):
    return (dist, path)
  return (-1, path)
