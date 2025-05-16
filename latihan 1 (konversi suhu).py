#Laihan konversi satuan temperatur

#Program konversi celcius ke satuan Lain 

print("\nPROGRAM KONVERSI TEMPERATUR DALAM CELCIUS\n")

celcius = float(input("Masukan suhu dalam celcius :"))
print("suhu adalah : ", celcius, "celcius")

#Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah :", reamur, "reamur")


#Fahrenheit
fahrenheit = (9/5) * celcius + 32 
print("suhu dalam fahrenheit adalah :", fahrenheit, "fahrenheit")

#Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah :",  kelvin, "kelvin")

#Program konversi reamur ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR DALAM REAMUR\n")

reamur = float(input("Masukan suhu dalam reamur :"))
print("suhu adalah : ", reamur, "reamur")

#celcius
celcius = (5/4) * reamur
print("suhu dalam celcius adalah :", celcius, "celcius")

#fahrenheit
fahrenheit = (9/4) * reamur + 32  
print("suhu dalam fahrenheit adalah :", fahrenheit, "fahrenheit")

#kelvin
kelvin = (5/4) * reamur + 273
print("suhu dalam kelvin adalah :", kelvin, "kelvin") 

#Program konversi fahrenheit ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR DALAM FAHRENHEIT\n")

fahrenheit = float(input("Masukan suhu dalam fahrenheit :"))
print("suhu adalah : ", fahrenheit, "fahrenheit")

#Celcius
celcius = (5/9) * (fahrenheit - 32)
print("suhu dalam celcius adalah :", celcius, "celcius")

#reamur
reamur = (4/9) * (fahrenheit - 32)
print("suhu dalam reamur adalah :", reamur, "reamur")

#kelvin
celcius = (5/9) * (fahrenheit - 32)
kelvin = (celcius + 273)
print("suhu dalam kelvin adalah :", kelvin, "kelvin")

#Program konversi kelvin ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATUR DALAM KELVIN\n")

kelvin = float(input("Masukan suhu dalam kelvin :"))
print("suhu adalah : ", kelvin, "kelvin")

#Celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah :", celcius, "celcius")

#reamur
reamur = (4/5) * (kelvin - 273)
print("suhu dalam reamur adalah :", reamur, "reamur")

#fahrenheit
celcius = kelvin - 273
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit :", fahrenheit, "fahrenheit")