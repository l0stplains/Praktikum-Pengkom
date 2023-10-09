# Not final version, still waiting for review and adding some description later

W = [0 for i in range(5)]
U = [0 for i in range(5)]
V = [0 for i in range(5)]

for i in range(5):
  U[i] = int(input(f"Masukkan elemen ke-{i} dari U: "))

for i in range(5):
  V[i] = int(input(f"Masukkan elemen ke-{i} dari V: "))

for i in range(5):
  W[i] = U[i] + V[i]

print(W)