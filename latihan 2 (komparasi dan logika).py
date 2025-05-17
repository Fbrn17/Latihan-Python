# latihan logika dan komparasi

# membuat gabungan area rentang dari angka
#soal satu (gabungan (OR))
# ----0+++5---8+++11---
print("========Angka lebih dari 0 dan  kurang dari 5=======")
inputUser = (float(input("Masukan angka yang bernilai besar dari 0 dan kurang dari 5")))

#memeriksa lebih dari 0 
isLebihDari = inputUser > 0
print("Lebih dari 0 =", isLebihDari)

#memeriksa kurang dari 5 
isKurangDari = inputUser < 5 
print("kurang dari 5 =", isKurangDari)

isCorrect1 = isKurangDari and isLebihDari
print("Angka yang anda masukan bernilai =", isCorrect1)

print(50* '=')
print("========Angka lebih dari 8 dan  kurang dari 11=======")
inputUser = (float(input("Masukan angka yang bernilai besar dari 8 dan kurang dari 11")))

#memeriksa lebih dari 8
isLebihDari = inputUser > 8
print("Lebih dari 8 =", isLebihDari)

#memeriksa kurang dari 11 
isKurangDari = inputUser < 11 
print("kurang dari 11 =", isKurangDari)

isCorrect2 = isKurangDari and isLebihDari
print("Angka yang anda masukan bernilai =", isCorrect2)

#gabungan kasus 1 
print('==========Gabungan kasus 1==========')
isGabungan = isCorrect1 or isCorrect2
print("Gabungan kasus satu bernilai =", isGabungan)

print(50* '=')
#soal 2 (irisan(AND))
#+++0---5+++8---11+++

print("========Angka kurang dari 0 atau lebih dari 5=======")
inputUser = (float(input("Masukan angka yang bernilai kurang dari 0 atau besar dari 5")))

#memeriksa kecil dari 0 
isKurangDari = inputUser < 0
print("kurang dari 0 =", isKurangDari)

#memeriksa besar dari 5 
isLebihDari = inputUser > 5 
print("lebih dari 5 =", isLebihDari)

isCorrect1 = isKurangDari or isLebihDari
print("Angka yang anda masukan bernilai =", isCorrect1)

print(50* '=')
print("========Angka kurang dari 8 atau lebih dari 11=======")
inputUser = (float(input("Masukan angka yang bernilai kurang dari 8 atau lebih dari 11")))

#memeriksa kurang dari 8
iskurangDari = inputUser < 8
print("kurang dari 8 =", isKurangDari)

#memeriksa lebih dari 11 
isLebihDari = inputUser > 11 
print("lebih dari 11 =", isLebihDari)

isCorrect2 = isKurangDari or isLebihDari
print("Angka yang anda masukan bernilai =", isCorrect2)

#gabungan kasus 2 
print('==========Gabungan kasus 2==========')
isGabungan = isCorrect1 and isCorrect2
print("Gabungan kasus dua bernilai =", isGabungan)

