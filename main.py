POUCE = 2.54
CM = 0.394

def afficher_menu():
    print("Conversion d'unités")
    print("Choix 1 : Conversion pouces en cm")
    print("Choix 2 : Conversion cm en pouces")
    print("Choix 0 : Quitter le programme de conversion")
    print()

def convertir_pouces_en_cm():
    while True:
        pouces = input("Veuillez saisir le nombre à convertir : ")
        try:
            pouces_float = float(pouces)
            calcul = pouces_float * POUCE
            print(f"Le résultat de la conversion est {calcul}cm.")
            print()
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        # Demander à l'utilisateur s'il veut reconvertir ou retourner au menu
        choix_sous_menu = input("Voulez-vous convertir à nouveau? (1: Oui, 2: Retour au menu principal) : ")
        if choix_sous_menu == "2":
            break
        elif choix_sous_menu != "1":
            print("Choix non valide, retour au menu principal.")
            break

def convertir_cm_en_pouces():
    while True:
        cm = input("Veuillez saisir le nombre à convertir : ")
        try:
            cm_float = float(cm)
            calcul = cm_float * CM
            print(f"Le résultat de la conversion est {calcul} pouces.")
            print()
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        # Demander à l'utilisateur s'il veut reconvertir ou retourner au menu
        choix_sous_menu = input("Voulez-vous convertir à nouveau? (1 : Oui, 2 : Retour au menu principal) : ")
        if choix_sous_menu == "2":
            break
        elif choix_sous_menu != "1":
            print("Choix non valide, retour au menu principal.")
            break

# Fonction principale
def conversion():
    while True:
        # Menu du programme
        afficher_menu()
        choix = input("Quel est votre choix ? ")
        try:
            choix_int = int(choix)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        # Conversion pouces vers cm
        if choix_int == 1:
            convertir_pouces_en_cm()

        # Conversion cm en pouces
        elif choix_int == 2:
            convertir_cm_en_pouces()

        # Quitter le programme
        elif choix_int == 0:
            print("Fermeture du programme.")
            break
        else:
            print("Choix non valide. Veuillez essayer à nouveau.")
            print()

conversion()