nb = int(input("Entrez un nombre  : "))
while nb <1:
    nb = int(input("Saisie invalide, entrer un nombre positif"))
print(f"Les nombres naturels de 1 a {nb}")
for i in range(1,nb+1):
    print(i,end="  ")