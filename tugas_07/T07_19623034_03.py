# Not final version, still waiting for review and adding some description later

t = int(input("Masukkan nilai T (ukuran array): "))

T = [0 for i in range(t)]

T[0] = int(input(f"Masukkan elemen ke-1: "))

mini = T[0]

for i in range(1, t):
  T[i] = int(input(f"Masukkan elemen ke-{i+1}: "))
  if T[i] < mini:
    mini = T[i]
  
print(f"Nilai terkecil = {mini}")

