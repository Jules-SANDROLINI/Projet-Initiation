def division (a,b) :
       try:
         print(a/b)
         return(a/b)
       except ZeroDivisionError :
         print("Erreur! La division par 0 n'est pas possible")
c=float(input())
d=float(input())
division(c,d)

"""
idem : ajouter des print pour informer l'utilisateur qu'il doit saisir les valeurs à diviser. 
"""