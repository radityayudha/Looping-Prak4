print("Program untuk menentukan bilangan ganjil")
bilangan_awal = int(input("Masukkan bilangan awal: "))
bilangan_akhir = int(input("Masukkan bilangan akhir: "))

i = bilangan_awal
while i <= bilangan_akhir:
    if i % 2 != 0:  
        print(i)
    i+=1