try :
    choix=int(input("Hello, to perform a calculation you can type: 1 for addition, 2 for soustraction, 3 for multiplication, 4 for division"))
    if choix==3 :
        open("multiplication.py") 
    elif choix==4 :
        open("division.py")
    elif choix==2 :
        open("soustraction.py")
    elif choix==1 :
        open("addition.py")
    elif choix!=1 and choix!=2 and choix!=3 and choix!=4 :
        print("please, enter correct number : 1 , 2 , 3 or 4")
except ValueError :
    print("please, enter correct number : 1 , 2 , 3 or 4")
    

"""
L'idée est bonne, mais ouvrir un fichier Python avec 'open' ne l'exécute pas.
Voici un exemple pour vous aider à comprendre comment vous pourriez structurer votre code différemment :
try:
    choix = int(input("Hello, to perform a calculation you can type: 1 for addition, 2 for soustraction, 3 for multiplication, 4 for division"))
    if choix == 1:
        # Exemple : appel une fonction pour l'addition
        print("Vous avez choisi l'addition.") # Permet à l'utilisateur de comfirmé son choix
    elif choix == 2:
        # Exemple : appel une fonction pour la soustraction
        print("Vous avez choisi la soustraction.") # Permet à l'utilisateur de comfirmé son choix
   [...]


"""

 
 
