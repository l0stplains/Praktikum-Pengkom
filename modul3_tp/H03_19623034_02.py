# Not final version, still waiting for review and adding some description later

S = int(input("Masukkan banyak data: "))
N = int(input("Masukkan nilai N: "))

arr = [0 for i in range(S)]

for i in range(S):
  arr[i] = int(input(f"Masukkan data ke-{i+1}: "))

for i in range(S):
  for j in range(S-i-1):
    if arr[j] < arr[j+1]:
      temp = arr[j+1]
      arr[j+1] = arr[j]
      arr[j] = temp
          

print(arr)

print(f"Nilai terbesar ke-{N} adalah: {arr[N-1]}")
  
