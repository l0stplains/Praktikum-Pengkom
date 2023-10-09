# Not final version, still waiting for review and adding some description later

N = int(input("Masukkan nilai N: "))
M = int(input("Masukkan nilai M: "))

arr = [i for i in range(1, N+1)]

for i in range(M):
  x = int(input(f"Masukkan data ke-{i+1}: "))
  arr[x-1] = 0

print("Nomor perwakilan yang tidak datang: ", end="")

for i in range(N):
  if arr[i] != 0:
    print(arr[i], end=" ")


