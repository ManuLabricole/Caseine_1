# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

# 1) Ecrire une fonction tarif_carte qui prend en argument une chaîne de caractère correspondant au nom de la carte ("Jeune" ou "Senior")
# et qui renvoie le prix de la carte. Si un autre nom que "Jeune" ou "Senior" est utilisé, la fonction affichera "Carte inconnue" 
# et ne renverra rien (ou renverra None, ce qui revient au même).

# 2) Ecrire une fonction plein_tarif qui prend en argument deux chaînes de caractères correspondant respectivement à la ville de 
# départ de la ville d'arrivée et qui renvoie le prix d'un billet plein tarif sur ce trajet-là. Si le trajet demandé n'est aucun 
# des 6 trajets existants dans cet exercice, la fonction affichera "Trajet inconnu" et renverra None (ou rien).

# 3) Ecrire une fonction tarif_billet qui prend en argument la ville de départ, la ville d'arrivée 
# et 3 arguments optionnels : un booléen modifiable indiquant si le billet est modifiable (True par défaut), 
# un argument carte correspondant au nom de l'éventuelle carte de réduction (None par défaut; pourra valoir "Jeune" ou "Senior" 
# dans les appels), et enfin un argument periode  (None par défaut; pourra valoir "bleue" ou "blanche" dans les appels), et qui 
# renvoie le tarif du billet. Si le trajet ou la carte demandé(e) est inconnu(e), un message d'erreur s'affichera et la fonction 
# renverra None.

def tarif_carte(carte:str) -> float:
    if carte == "Jeune":
        return float(50)
    elif carte == "Senior":
        return float(60)
    else:
        print("Carte inconnue")
        return None
    pass

def reduc_carte(carte:str, periode:str) -> float:
    
    if carte == "Jeune":
        if periode == "bleue":
            return float(0.5)
        elif periode == "blanche":
            return float(0.3)
        
    elif carte == "Senior":
        if periode == "bleue":
            return float(0.5)
        elif periode == "blanche":
            return float(0.25)
    else:
        print("Carte inconnue")
        return None

        
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Votre programme principal ne sera pas évalué.
    # Utilisez-le pour tester votre programme en faisant
    # les appels de votre choix.
    # Respectez bien ce niveau d'identation.
    print("Debut du prog. principal")
