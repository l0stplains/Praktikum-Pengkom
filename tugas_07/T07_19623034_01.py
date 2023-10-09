# Not final version, still waiting for review and adding some description later

T = [0 for i in range(20)]

for i in range(20):
  T[i] = int(input())

X = int(input("Masukkan nilai X: "))

for i in range(20):
  T[i] *= X

print(T)
