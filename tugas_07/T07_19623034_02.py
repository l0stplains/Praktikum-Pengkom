# Not final version, still waiting for review and adding some description later

N = ['' for i in range(50)]

lulus = 0
tidaklulus = 0

for i in range(50):
  N[i] = input(f"Nilai ke-{i+1}: ")
  if  N[i] == 'D' or N[i] == 'E':
    tidaklulus += 1
  else:
    lulus += 1

print(f"{lulus} mahasiswa lulus")
print(f"{tidaklulus} mahasiswa tidak lulus")

