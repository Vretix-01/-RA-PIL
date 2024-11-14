n = int(input("Koliko brojeva želite unijeti za provjeru parnosti"))

parni_brojevi = 0
neparni_brojevi = 0 

for i in range(n):
    broj = int(input(f"Unesite broj {f+1}"))

    if broj % 2 == 0:
        print(f"Broj {broj} je paran.")
        parni_brojevi += 1
    else:
        print(f"Broj {broj} neparan")
        neparni_brojevi += 1



print("Ukupno parnih brojeva: " ,parni_brojevi)
print("Ukupno nepranih brojva: ",neparni_brojevi)
