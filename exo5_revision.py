nb = int(input("Entrez un nombre  : "))
while nb < 1:
    nb = int(input("Saisie invalide, entrer un nombre positif"))

print(f"Les nombres pairs avec pas de 2 à partir de 2 a {nb} sont : ")
for i in range(2, nb + 1, 2):
    print(i, end="  ")