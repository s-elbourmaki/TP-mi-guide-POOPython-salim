from part1 import Boisson
from part2 import Cafe, The
from part3 import DecorateurBoisson, Lait, Sucre
from part5 import Client

# 1. AJOUT D'UN NOUVEL INGREDIENT : CARAMEL

class Caramel(DecorateurBoisson):
    """Ajoute du caramel à une boisson"""

    def cout(self):
        return self._boisson.cout() + 0.7

    def description(self):
        return self._boisson.description() + ", Caramel"

# 2. IMPLÉMENTATION DE LA COMBINAISON AVEC +

class BoissonCombinee(Boisson):
    """
    Représente la combinaison de deux boissons.
    Utilisée lorsqu'on fait boisson1 + boisson2
    """

    def __init__(self, boisson1, boisson2):
        self._boisson1 = boisson1
        self._boisson2 = boisson2

    def cout(self):
        return self._boisson1.cout() + self._boisson2.cout()

    def description(self):
        return f"{self._boisson1.description()} + {self._boisson2.description()}"

    def __add__(self, other):
        """Permet de continuer à combiner"""
        if not isinstance(other, Boisson):
            return NotImplemented
        return BoissonCombinee(self, other)

# Ajout de la méthode __add__ aux classes existantes
def ajouter_combinaison(cls):
    """Décorateur pour ajouter la méthode __add__ à une classe"""
    def __add__(self, other):
        if not isinstance(other, Boisson):
            return NotImplemented
        return BoissonCombinee(self, other)
    
    cls.__add__ = __add__
    return cls

# Application du décorateur aux classes existantes
Cafe = ajouter_combinaison(Cafe)
The = ajouter_combinaison(The)
DecorateurBoisson = ajouter_combinaison(DecorateurBoisson)

# 3. CLASSE COMMANDE POUR AFFICHAGE COMPLET

class Commande:
    """
    Représente une commande passée par un client.
    Permet d'afficher proprement les informations.
    """

    def __init__(self, client=None):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        """Ajoute une boisson à la commande"""
        self.boissons.append(boisson)

    def prix_total(self):
        """Calcule le prix total de la commande"""
        return sum(boisson.cout() for boisson in self.boissons)

    def afficher_commande(self):
        """Affiche une commande complète de manière formatée"""
        print("=" * 60)
        print(" COMMANDE")
        print("=" * 60)
        
        if self.client:
            print(f" Client : {self.client.nom} (N° {self.client.numero})")
            print(f" Points de fidélité : {self.client.points_fidelite}")
            print("-" * 60)
        
        if not self.boissons:
            print(" Aucune boisson dans la commande")
        else:
            print(" Boissons commandées :\n")
            for i, boisson in enumerate(self.boissons, 1):
                print(f"   {i}. {boisson.description()}")
                print(f"       {boisson.cout():.2f}€")
                print()
        
        print("-" * 60)
        print(f" PRIX TOTAL : {self.prix_total():.2f}€")
        print("=" * 60)

# 4. AFFICHAGE SIMPLE D'UNE BOISSON (méthode demandée)

def afficher_boisson(boisson):
    """Affiche les informations d'une boisson de manière formatée"""
    print(f"Commande : {boisson.description()}")
    print(f"Prix : {boisson.cout()}€")


if __name__ == "__main__":
    
    print("\n" + "" * 30)
    print("TEST 1 : AJOUT DE CARAMEL")
    print("" * 30 + "\n")
    
    cafe_caramel = Caramel(Cafe())
    afficher_boisson(cafe_caramel)
    
    # Combinaison multiple d'ingrédients
    print("\n")
    cafe_complet = Caramel(Sucre(Lait(Cafe())))
    afficher_boisson(cafe_complet)
  
    print("\n\n" + "" * 30)
    print("TEST 2 : COMBINAISON DE BOISSONS")
    print("" * 30 + "\n")
    
    cafe = Cafe()
    the = The()
    
    # Combinaison simple
    menu = cafe + the
    afficher_boisson(menu)
    
    # Combinaison avec décorateurs
    print("\n")
    cafe_lait = Lait(Cafe())
    the_sucre = Sucre(The())
    menu_complet = cafe_lait + the_sucre
    afficher_boisson(menu_complet)
    
    print("\n\n" + "" * 30)
    print("TEST 3 : AFFICHAGE DE COMMANDE")
    print("" * 30 + "\n")
    
    # Création d'un client
    client1 = Client("Salim", 1001, 50)
    
    # Création d'une commande
    commande = Commande(client1)
    
    # Ajout de boissons variées
    commande.ajouter_boisson(Sucre(Lait(Cafe())))
    commande.ajouter_boisson(The())
    commande.ajouter_boisson(Caramel(Cafe()))
    
    # Affichage de la commande complète
    commande.afficher_commande()

    print("\n\n" + "" * 30)
    print("TEST 4 : AFFICHAGE ATTENDU DE L'ÉNONCÉ")
    print("" * 30 + "\n")
    
    boisson_enonce = Sucre(Lait(Cafe()))
    afficher_boisson(boisson_enonce)
    
    print("\n\n" + "" * 30)
    print("TEST 5 : EXEMPLE COMPLET")
    print("" * 30 + "\n")
    
    client2 = Client("EL BOURMAKI", 1002, 120)
    commande2 = Commande(client2)
    
    # Boissons individuelles avec ingrédients
    boisson1 = Caramel(Lait(Cafe()))
    boisson2 = Sucre(The())
    
    # Combinaison de deux boissons
    boisson3 = Cafe() + The()
    
    commande2.ajouter_boisson(boisson1)
    commande2.ajouter_boisson(boisson2)
    commande2.ajouter_boisson(boisson3)
    
    commande2.afficher_commande()