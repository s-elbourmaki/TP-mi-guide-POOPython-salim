"""
Nom: Salim EL BOURMAKI
LST: IDAI 25-26
Module: Python
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

# PART 1 : CLASSE DE BASE

class Boisson(ABC):
    """
    Classe abstraite representant une boisson generique.
    Toute boisson doit pouvoir retourner son prix et sa description.
    """
    @abstractmethod
    def cout(self):
        """Retourne le prix de la boisson"""
        pass

    @abstractmethod
    def description(self):
        """Retourne la description de la boisson"""
        pass

# PART 2 : BOISSONS CONCRETES

class Cafe(Boisson):
    """Represente un cafe simple"""

    def cout(self):
        return 2.0

    def description(self):
        return "Cafe simple"


class The(Boisson):
    """Represente un the"""

    def cout(self):
        return 1.5

    def description(self):
        return "The"

# PART 3 : DECORATEURS (INGREDIENTS) 

class DecorateurBoisson(Boisson):
    """
    Classe decorateur de base.
    Cette classe recoit une boisson existante et pourra modifier son comportement.
    """

    def __init__(self, boisson):
        self._boisson = boisson


class Lait(DecorateurBoisson):
    """Ajoute du lait a une boisson"""

    def cout(self):
        return self._boisson.cout() + 0.5

    def description(self):
        return self._boisson.description() + ", Lait"


class Sucre(DecorateurBoisson):
    """Ajoute du sucre a une boisson"""

    def cout(self):
        return self._boisson.cout() + 0.2

    def description(self):
        return self._boisson.description() + ", Sucre"


class Caramel(DecorateurBoisson):
    """Ajoute du caramel a une boisson"""

    def cout(self):
        return self._boisson.cout() + 0.7

    def description(self):
        return self._boisson.description() + ", Caramel"

# PART 4 : COMBINAISON DE BOISSONS

class BoissonCombinee(Boisson):
    """
    Represente la combinaison de deux boissons.
    Utilisee lorsqu'on fait boisson1 + boisson2
    """

    def __init__(self, boisson1, boisson2):
        self._boisson1 = boisson1
        self._boisson2 = boisson2

    def cout(self):
        return self._boisson1.cout() + self._boisson2.cout()

    def description(self):
        return f"{self._boisson1.description()} + {self._boisson2.description()}"


# Ajout de la methode __add__ aux classes existantes
def ajouter_combinaison(cls):
    """Decorateur pour ajouter la methode __add__ a une classe"""
    def __add__(self, other):
        if not isinstance(other, Boisson):
            return NotImplemented
        return BoissonCombinee(self, other)
    
    cls.__add__ = __add__
    return cls

# Application du decorateur aux classes de boissons
Cafe = ajouter_combinaison(Cafe)
The = ajouter_combinaison(The)
DecorateurBoisson = ajouter_combinaison(DecorateurBoisson)
BoissonCombinee = ajouter_combinaison(BoissonCombinee)

# PARTIE 5 : REPRESENTATION CLIENT

@dataclass
class Client:
    """
    Represente un client du cafe.
    Utilise @dataclass pour generer automatiquement __init__, __repr__, __eq__
    """
    nom: str
    numero: int
    points_fidelite: int

# PARTIE 6 : AFFICHAGE SIMPLE D'UNE BOISSON

def afficher_boisson(boisson):
    """Affiche les informations d'une boisson de maniere formatee"""
    print(f"Commande : {boisson.description()}")
    print(f"Prix : {boisson.cout()} euros")

# PARTIE 7 : GESTION DES COMMANDES

class Commande:
    """
    Represente une commande passee par un client.
    Contient :
        - un client
        - une liste de boissons
        - methodes pour gerer la commande
    """

    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        """Ajoute une boisson a la commande"""
        self.boissons.append(boisson)

    def prix_total(self):
        """Calcule le prix total de la commande"""
        return sum(boisson.cout() for boisson in self.boissons)

    def afficher(self):
        """Affiche les informations de la commande"""
        print("=" * 60)
        print("COMMANDE")
        print("=" * 60)
        print(f"Client : {self.client.nom} (N {self.client.numero})")
        print(f"Points de fidelite : {self.client.points_fidelite}")
        print("-" * 60)
        
        if not self.boissons:
            print("Aucune boisson dans la commande")
        else:
            print("Boissons :\n")
            for i, boisson in enumerate(self.boissons, 1):
                print(f"   {i}. {boisson.description()}")
                print(f"      Prix : {boisson.cout():.2f} euros")
                print()
        
        print("-" * 60)
        print(f"PRIX TOTAL : {self.prix_total():.2f} euros")
        print("=" * 60)

# TYPES DE COMMANDES (POLYMORPHISME)

class CommandeSurPlace(Commande):
    """
    Commande consommee sur place.
    Affichage personnalise avec indication "Sur place".
    """

    def afficher(self):
        """Affichage specifique pour commande sur place"""
        print("=" * 60)
        print("COMMANDE - SUR PLACE")
        print("=" * 60)
        print(f"Client : {self.client.nom} (N {self.client.numero})")
        print(f"Points de fidelite : {self.client.points_fidelite}")
        print("-" * 60)
        
        if not self.boissons:
            print("Aucune boisson dans la commande")
        else:
            print("Boissons :\n")
            for i, boisson in enumerate(self.boissons, 1):
                print(f"   {i}. {boisson.description()}")
                print(f"      Prix : {boisson.cout():.2f} euros")
                print()
        
        print("-" * 60)
        print(f"Type : Sur place")
        print(f"PRIX TOTAL : {self.prix_total():.2f} euros")
        print("=" * 60)


class CommandeEmporter(Commande):
    """
    Commande a emporter.
    Affichage personnalise avec indication "A emporter".
    Peut inclure des frais d'emballage.
    """

    FRAIS_EMBALLAGE = 0.50

    def prix_total(self):
        """Prix total avec frais d'emballage"""
        return super().prix_total() + self.FRAIS_EMBALLAGE

    def afficher(self):
        """Affichage specifique pour commande a emporter"""
        print("=" * 60)
        print("COMMANDE - A EMPORTER")
        print("=" * 60)
        print(f"Client : {self.client.nom} (N {self.client.numero})")
        print(f"Points de fidelite : {self.client.points_fidelite}")
        print("-" * 60)
        
        if not self.boissons:
            print("Aucune boisson dans la commande")
        else:
            print("Boissons :\n")
            for i, boisson in enumerate(self.boissons, 1):
                print(f"   {i}. {boisson.description()}")
                print(f"      Prix : {boisson.cout():.2f} euros")
                print()
        
        prix_boissons = sum(b.cout() for b in self.boissons)
        
        print("-" * 60)
        print(f"Type : A emporter")
        print(f"Sous-total boissons : {prix_boissons:.2f} euros")
        print(f"Frais d'emballage : {self.FRAIS_EMBALLAGE:.2f} euros")
        print(f"PRIX TOTAL : {self.prix_total():.2f} euros")
        print("=" * 60)

# SYSTEME DE FIDELITE

class Fidelite:
    """
    Systeme de fidelite du cafe.
    Permet d'ajouter des points en fonction du montant depense.
    Regle : 1 euro depense = 1 point de fidelite
    """

    POINTS_PAR_EURO = 1

    def calculer_points(self, montant):
        """Calcule les points gagnes pour un montant donne"""
        return int(montant * self.POINTS_PAR_EURO)

    def ajouter_points(self, client, montant):
        """Ajoute des points de fidelite au client"""
        points_gagnes = self.calculer_points(montant)
        client.points_fidelite += points_gagnes
        return points_gagnes

# HERITAGE MULTIPLE : COMMANDE FIDELE

class CommandeFidele(Commande, Fidelite):
    """
    Commande qui utilise le systeme de fidelite.
    Herite de :
        - Commande : pour les fonctionnalites de commande
        - Fidelite : pour le systeme de points
    """

    def __init__(self, client):
        Commande.__init__(self, client)
        self._validee = False
        self._points_gagnes = 0

    def valider(self):
        """Valide la commande et ajoute les points de fidelite"""
        if self._validee:
            print("Cette commande a deja ete validee !")
            return
        
        montant = self.prix_total()
        self._points_gagnes = self.ajouter_points(self.client, montant)
        self._validee = True
        
        print(f"Commande validee !")
        print(f"Points gagnes : {self._points_gagnes}")
        print(f"Total points : {self.client.points_fidelite}")

    def afficher(self):
        """Affichage avec informations de fidelite"""
        print("=" * 60)
        print("COMMANDE FIDELITE")
        print("=" * 60)
        print(f"Client : {self.client.nom} (N {self.client.numero})")
        print(f"Points de fidelite : {self.client.points_fidelite}")
        print("-" * 60)
        
        if not self.boissons:
            print("Aucune boisson dans la commande")
        else:
            print("Boissons :\n")
            for i, boisson in enumerate(self.boissons, 1):
                print(f"   {i}. {boisson.description()}")
                print(f"      Prix : {boisson.cout():.2f} euros")
                print()
        
        print("-" * 60)
        print(f"PRIX TOTAL : {self.prix_total():.2f} euros")
        
        if self._validee:
            print(f"Commande validee")
            print(f"Points gagnes : {self._points_gagnes}")
        else:
            points_potentiels = self.calculer_points(self.prix_total())
            print(f"Commande en attente de validation")
            print(f"Points a gagner : {points_potentiels}")
        
        print("=" * 60)

# VARIANTES AVEC FIDELITE ET TYPE

class CommandeSurPlaceFidele(CommandeSurPlace, Fidelite):
    """Commande sur place avec systeme de fidelite"""

    def __init__(self, client):
        CommandeSurPlace.__init__(self, client)
        self._validee = False
        self._points_gagnes = 0

    def valider(self):
        """Valide la commande et ajoute les points"""
        if self._validee:
            print("Cette commande a deja ete validee !")
            return
        
        montant = self.prix_total()
        self._points_gagnes = self.ajouter_points(self.client, montant)
        self._validee = True
        
        print(f"Commande sur place validee !")
        print(f"Points gagnes : {self._points_gagnes}")

    def afficher(self):
        """Affichage sur place avec fidelite"""
        print("=" * 60)
        print("COMMANDE - SUR PLACE - FIDELITE")
        print("=" * 60)
        print(f"Client : {self.client.nom} (N {self.client.numero})")
        print(f"Points de fidelite : {self.client.points_fidelite}")
        print("-" * 60)
        
        if self.boissons:
            print("Boissons :\n")
            for i, boisson in enumerate(self.boissons, 1):
                print(f"   {i}. {boisson.description()}")
                print(f"      Prix : {boisson.cout():.2f} euros")
                print()
        
        print("-" * 60)
        print(f"Type : Sur place")
        print(f"PRIX TOTAL : {self.prix_total():.2f} euros")
        
        if self._validee:
            print(f"Validee | +{self._points_gagnes} points")
        
        print("=" * 60)


class CommandeEmporterFidele(CommandeEmporter, Fidelite):
    """Commande a emporter avec systeme de fidelite"""

    def __init__(self, client):
        CommandeEmporter.__init__(self, client)
        self._validee = False
        self._points_gagnes = 0

    def valider(self):
        """Valide la commande et ajoute les points"""
        if self._validee:
            print("Cette commande a deja ete validee !")
            return
        
        montant = self.prix_total()
        self._points_gagnes = self.ajouter_points(self.client, montant)
        self._validee = True
        
        print(f"Commande a emporter validee !")
        print(f"Points gagnes : {self._points_gagnes}")

    def afficher(self):
        """Affichage a emporter avec fidelite"""
        print("=" * 60)
        print("COMMANDE - A EMPORTER - FIDELITE")
        print("=" * 60)
        print(f"Client : {self.client.nom} (N {self.client.numero})")
        print(f"Points de fidelite : {self.client.points_fidelite}")
        print("-" * 60)
        
        if self.boissons:
            print("Boissons :\n")
            for i, boisson in enumerate(self.boissons, 1):
                print(f"   {i}. {boisson.description()}")
                print(f"      Prix : {boisson.cout():.2f} euros")
                print()
        
        prix_boissons = sum(b.cout() for b in self.boissons)
        
        print("-" * 60)
        print(f"Type : A emporter")
        print(f"Sous-total boissons : {prix_boissons:.2f} euros")
        print(f"Frais d'emballage : {self.FRAIS_EMBALLAGE:.2f} euros")
        print(f"PRIX TOTAL : {self.prix_total():.2f} euros")
        
        if self._validee:
            print(f"Validee | +{self._points_gagnes} points")
        
        print("=" * 60)

# PARTIE 8 : TESTS ET DEMONSTRATIONS

def separateur(titre):
    """Affiche un separateur visuel avec un titre"""
    print("\n" + "=" * 60)
    print(titre)
    print("=" * 60 + "\n")

def test_partie1():
    """Test de la classe abstraite"""
    separateur("TEST PARTIE 1 : CLASSE ABSTRAITE")
    
    try:
        boisson = Boisson()
    except TypeError as e:
        print(f"Erreur attendue : Impossible d'instancier Boisson directement")
        print(f"Raison : {e}")
        print("La classe abstraite fonctionne correctement !")

def test_partie2():
    """Test des boissons concretes"""
    separateur("TEST PARTIE 2 : BOISSONS CONCRETES")
    
    cafe = Cafe()
    the = The()
    
    print(f"Cafe : {cafe.description()}")
    print(f"Prix : {cafe.cout()} euros\n")
    
    print(f"The : {the.description()}")
    print(f"Prix : {the.cout()} euros")

def test_partie3():
    """Test des decorateurs (ingredients)"""
    separateur("TEST PARTIE 3 : DECORATEURS (INGREDIENTS)")
    
    # Cafe simple
    boisson = Cafe()
    print(f"1. {boisson.description()}")
    print(f"   Prix : {boisson.cout()} euros\n")
    
    # Cafe avec lait
    boisson = Lait(boisson)
    print(f"2. {boisson.description()}")
    print(f"   Prix : {boisson.cout()} euros\n")
    
    # Cafe avec lait et sucre
    boisson = Sucre(boisson)
    print(f"3. {boisson.description()}")
    print(f"   Prix : {boisson.cout()} euros\n")
    
    # Cafe complet avec caramel
    boisson = Caramel(boisson)
    print(f"4. {boisson.description()}")
    print(f"   Prix : {boisson.cout()} euros")

def test_partie4():
    """Test de la combinaison de boissons"""
    separateur("TEST PARTIE 4 : COMBINAISON DE BOISSONS")
    
    cafe = Cafe()
    the = The()
    
    # Combinaison simple
    menu1 = cafe + the
    print(f"Menu 1 : {menu1.description()}")
    print(f"Prix : {menu1.cout()} euros\n")
    
    # Combinaison avec decorateurs
    cafe_lait = Lait(Cafe())
    the_sucre = Sucre(The())
    menu2 = cafe_lait + the_sucre
    print(f"Menu 2 : {menu2.description()}")
    print(f"Prix : {menu2.cout()} euros")

def test_partie5():
    """Test de la classe Client"""
    separateur("TEST PARTIE 5 : CLASSE CLIENT")
    
    client1 = Client("Alice Dubois", 1001, 50)
    client2 = Client("Bob Martin", 1002, 120)
    
    print(f"Client 1 : {client1}")
    print(f"Client 2 : {client2}\n")
    
    # Modification des points
    print(f"Points de {client1.nom} avant : {client1.points_fidelite}")
    client1.points_fidelite += 10
    print(f"Points de {client1.nom} apres : {client1.points_fidelite}")

def test_partie6():
    """Test de l'affichage demande dans l'enonce"""
    separateur("TEST PARTIE 6 : AFFICHAGE ATTENDU")
    
    boisson = Sucre(Lait(Cafe()))
    afficher_boisson(boisson)

def test_partie7_commandes():
    """Test du systeme de commandes"""
    separateur("TEST PARTIE 7 : SYSTEME DE COMMANDES")
    
    # Commande de base
    print("1. COMMANDE DE BASE\n")
    client1 = Client("Mohamed", 1003, 30)
    commande1 = Commande(client1)
    commande1.ajouter_boisson(Cafe())
    commande1.ajouter_boisson(Lait(The()))
    commande1.afficher()
    
    print("\n")
    
    # Commande sur place
    print("2. COMMANDE SUR PLACE\n")
    client2 = Client("Silya", 1004, 50)
    commande2 = CommandeSurPlace(client2)
    commande2.ajouter_boisson(Sucre(Lait(Cafe())))
    commande2.ajouter_boisson(Caramel(Cafe()))
    commande2.afficher()
    
    print("\n")
    
    # Commande a emporter
    print("3. COMMANDE A EMPORTER\n")
    client3 = Client("Ahmed", 1005, 100)
    commande3 = CommandeEmporter(client3)
    commande3.ajouter_boisson(The())
    commande3.ajouter_boisson(Sucre(The()))
    commande3.afficher()

def test_partie7_fidelite():
    """Test du systeme de fidelite"""
    separateur("TEST PARTIE 7 : SYSTEME DE FIDELITE")
    
    client = Client("Frank Dupont", 1006, 25)
    
    print(f"Client : {client.nom}")
    print(f"Points initiaux : {client.points_fidelite}\n")
    
    # Creation d'une commande fidele
    commande = CommandeFidele(client)
    commande.ajouter_boisson(Caramel(Lait(Cafe())))
    commande.ajouter_boisson(Sucre(The()))
    commande.ajouter_boisson(Cafe())
    
    # Affichage avant validation
    commande.afficher()
    
    print("\n")
    
    # Validation
    commande.valider()
    
    print(f"\nPoints finaux : {client.points_fidelite}")

def test_polymorphisme():
    """Test du polymorphisme avec differentes commandes"""
    separateur("TEST BONUS : POLYMORPHISME")
    
    client1 = Client("Grace Martin", 1007, 10)
    client2 = Client("Hugo Lefebvre", 1008, 5)
    client3 = Client("Isabelle Roux", 1009, 80)
    
    # Creation de commandes de types differents
    commandes = [
        CommandeSurPlace(client1),
        CommandeEmporter(client2),
        CommandeFidele(client3)
    ]
    
    # Ajout d'une boisson a chaque commande
    for commande in commandes:
        commande.ajouter_boisson(Lait(Cafe()))
    
    # Affichage polymorphique
    print("Affichage de toutes les commandes :\n")
    for i, commande in enumerate(commandes, 1):
        print(f"COMMANDE {i} :\n")
        commande.afficher()
        print("\n")

def exemple_complet():
    """Exemple complet d'utilisation du systeme"""
    separateur("EXEMPLE COMPLET : SCENARIO REEL")
    
    print("Bienvenue au Cafe Python !\n")
    
    # Creation d'un nouveau client
    client = Client("Salim", 2001, 0)
    print(f"Nouveau client : {client.nom}")
    print(f"Points de fidelite : {client.points_fidelite}\n")
    
    # Le client passe une commande
    print("Le client passe une commande...\n")
    
    commande = CommandeFidele(client)
    
    # Ajout de plusieurs boissons variees
    commande.ajouter_boisson(Caramel(Sucre(Lait(Cafe()))))  # Cafe gourmand
    commande.ajouter_boisson(Sucre(The()))                   # The sucre
    commande.ajouter_boisson(Cafe())                         # Cafe simple
    
    # Affichage de la commande
    commande.afficher()
    
    print("\n")
    
    # Validation et attribution des points
    print("Validation de la commande...\n")
    commande.valider()
    
    print(f"\n{client.nom} a maintenant {client.points_fidelite} points de fidelite !")
    print("Merci pour votre visite !")

def test_mro():
    """Test du Method Resolution Order"""
    separateur("TEST MRO (METHOD RESOLUTION ORDER)")
    
    print("Hierarchie des classes :\n")
    print(f"CommandeFidele MRO :")
    print(f"  {[c.__name__ for c in CommandeFidele.__mro__]}\n")
    
    print(f"CommandeSurPlaceFidele MRO :")
    print(f"  {[c.__name__ for c in CommandeSurPlaceFidele.__mro__]}\n")
    
    print(f"CommandeEmporterFidele MRO :")
    print(f"  {[c.__name__ for c in CommandeEmporterFidele.__mro__]}")

def menu_tests():
    """Menu principal des tests"""
    print("\n")
    print("=" * 60)
    print("         SYSTEME DE GESTION DE CAFE")
    print("           Tests complets du TP")
    print("=" * 60)
    
    # Execution de tous les tests
    test_partie1()
    test_partie2()
    test_partie3()
    test_partie4()
    test_partie5()
    test_partie6()
    test_partie7_commandes()
    test_partie7_fidelite()
    test_polymorphisme()
    exemple_complet()
    test_mro()
    

if __name__ == "__main__":
    menu_tests()