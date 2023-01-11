n=int(input("entrez un nombre entre 1 et 7 :"))


while n<1 or n>7 :

   n=int(input(" erreur , veuillez entrer un nombre entre 1 et 7 :"))



if n==1 :

  jour="lundi"

elif n==2 :

  jour="mardi"

elif n==3 :

  jour="mercredi"

elif n==4 :

  jour="jeudi"

elif n==5 :

  jour="vendredi"

elif n==6 :

  jour="samedi"

else :

  jour="dimanche"



print("cela correspond au jour de la semaine : "+jour)