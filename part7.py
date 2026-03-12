"""
PARTIE 7 - Gestion des commandes (héritage multiple et polymorphisme)
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from part1 import Boisson
from part2 import Cafe, The
from part3 import DecorateurBoisson, Lait, Sucre
from part5 import Client

class Caramel(DecorateurBoisson):
    """Ajoute du caramel a une boisson"""

    def cout(self):
        return self._boisson.cout() + 0.7

    def description(self):
        return self._boisson.description() + ", Caramel"

# 1. CLASSE COMMANDE DE BASE

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

# 2. TYPES DE COMMANDES (POLYMORPHISME)

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

    FRAIS_EMBALLAGE = 0.50  # Frais supplementaires pour emporter

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
        
        # Prix des boissons seulement
        prix_boissons = sum(b.cout() for b in self.boissons)
        
        print("-" * 60)
        print(f"Type : A emporter")
        print(f"Sous-total boissons : {prix_boissons:.2f} euros")
        print(f"Frais d'emballage : {self.FRAIS_EMBALLAGE:.2f} euros")
        print(f"PRIX TOTAL : {self.prix_total():.2f} euros")
        print("=" * 60)

# 3. SYSTEME DE FIDELITE

class Fidelite:
    """
    Systeme de fidelite du cafe.
    Permet d'ajouter des points en fonction du montant depense.
    Regle : 1 euro depense = 1 point de fidelite
    """

    POINTS_PAR_EURO = 1  # Points gagnes par euro depense

    def calculer_points(self, montant):
        """Calcule les points gagnes pour un montant donne"""
        return int(montant * self.POINTS_PAR_EURO)

    def ajouter_points(self, client, montant):
        """Ajoute des points de fidelite au client"""
        points_gagnes = self.calculer_points(montant)
        client.points_fidelite += points_gagnes
        return points_gagnes

# 4. HERITAGE MULTIPLE : COMMANDE FIDELE

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
        
        # Calcul et ajout des points
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
        
        # Affichage des points a gagner ou gagnes
        if self._validee:
            print(f"Commande validee")
            print(f"Points gagnes : {self._points_gagnes}")
        else:
            points_potentiels = self.calculer_points(self.prix_total())
            print(f"Commande en attente de validation")
            print(f"Points a gagner : {points_potentiels}")
        
        print("=" * 60)

# 5. VARIANTES AVEC FIDELITE ET TYPE (Bonus)

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

# 6. TESTS COMPLETS DU SYSTEME

if __name__ == "__main__":
    
    # Test 1 : Commande de base
    print("\n" + "=" * 60)
    print("TEST 1 : COMMANDE DE BASE")
    print("=" * 60 + "\n")
    
    client1 = Client("Alice Dubois", 1001, 50)
    
    commande1 = Commande(client1)
    commande1.ajouter_boisson(Cafe())
    commande1.ajouter_boisson(Lait(Cafe()))
    commande1.ajouter_boisson(The())
    
    commande1.afficher()
    
    # Test 2 : Commande sur place
    print("\n\n" + "=" * 60)
    print("TEST 2 : COMMANDE SUR PLACE")
    print("=" * 60 + "\n")
    
    client2 = Client("Bob Martin", 1002, 30)
    
    commande2 = CommandeSurPlace(client2)
    commande2.ajouter_boisson(Sucre(Lait(Cafe())))
    commande2.ajouter_boisson(Caramel(Cafe()))
    
    commande2.afficher()
    
    # Test 3 : Commande a emporter
    print("\n\n" + "=" * 60)
    print("TEST 3 : COMMANDE A EMPORTER")
    print("=" * 60 + "\n")
    
    client3 = Client("Claire Petit", 1003, 100)
    
    commande3 = CommandeEmporter(client3)
    commande3.ajouter_boisson(The())
    commande3.ajouter_boisson(Sucre(The()))
    
    commande3.afficher()
    
    # Test 4 : Systeme de fidelite seul
    print("\n\n" + "=" * 60)
    print("TEST 4 : SYSTEME DE FIDELITE")
    print("=" * 60 + "\n")
    
    fidelite = Fidelite()
    
    print(f"Points pour 5 euros : {fidelite.calculer_points(5)}")
    print(f"Points pour 10.50 euros : {fidelite.calculer_points(10.50)}")
    
    client_test = Client("Test", 9999, 0)
    print(f"\n{client_test.nom} - Points avant : {client_test.points_fidelite}")
    
    points_ajoutes = fidelite.ajouter_points(client_test, 15)
    print(f"Points ajoutes : {points_ajoutes}")
    print(f"Points apres : {client_test.points_fidelite}")
    
    # Test 5 : Commande fidele (heritage multiple)
    print("\n\n" + "=" * 60)
    print("TEST 5 : COMMANDE FIDELE (HERITAGE MULTIPLE)")
    print("=" * 60 + "\n")
    
    client4 = Client("David Leroy", 1004, 25)
    
    print(f"Points de {client4.nom} AVANT : {client4.points_fidelite}")
    print()
    
    commande4 = CommandeFidele(client4)
    commande4.ajouter_boisson(Caramel(Lait(Cafe())))
    commande4.ajouter_boisson(Sucre(The()))
    commande4.ajouter_boisson(Cafe())
    
    # Affichage avant validation
    commande4.afficher()
    
    print()
    
    # Validation de la commande
    commande4.valider()
    
    print()
    
    # Affichage apres validation
    commande4.afficher()
    
    print(f"\nPoints de {client4.nom} APRES : {client4.points_fidelite}")
    
    
    # Test 6 : Polymorphisme
    print("\n\n" + "=" * 60)
    print("TEST 6 : POLYMORPHISME")
    print("=" * 60 + "\n")
    
    # Liste de commandes de types differents
    client5 = Client("Emma Bernard", 1005, 10)
    client6 = Client("Frank Dupont", 1006, 5)
    client7 = Client("Grace Martin", 1007, 80)
    
    commandes = [
        CommandeSurPlace(client5),
        CommandeEmporter(client6),
        CommandeFidele(client7)
    ]
    
    # Ajout d'une boisson a chaque commande
    for commande in commandes:
        commande.ajouter_boisson(Lait(Cafe()))
    
    # Affichage polymorphique
    print("Affichage de toutes les commandes :\n")
    for commande in commandes:
        commande.afficher()
        print()
    
    
    # Test 7 : Commande complete (exemple final)
    print("\n\n" + "=" * 60)
    print("TEST 7 : EXEMPLE COMPLET FINAL")
    print("=" * 60 + "\n")
    
    # Creation d'un client
    client_final = Client("Hugo Lefebvre", 2001, 0)
    print(f"Nouveau client : {client_final.nom}")
    print(f"Points initiaux : {client_final.points_fidelite}")
    print()
    
    # Creation de plusieurs boissons
    boisson1 = Caramel(Sucre(Lait(Cafe())))  # Cafe complet
    boisson2 = Sucre(The())                   # The sucre
    boisson3 = Cafe()                         # Cafe simple
    boisson4 = Lait(The())                    # The au lait
    
    # Creation d'une commande fidele
    commande_finale = CommandeFidele(client_final)
    
    # Ajout des boissons
    commande_finale.ajouter_boisson(boisson1)
    commande_finale.ajouter_boisson(boisson2)
    commande_finale.ajouter_boisson(boisson3)
    commande_finale.ajouter_boisson(boisson4)
    
    # Affichage de la commande
    commande_finale.afficher()
    
    print()
    
    # Validation de la commande
    commande_finale.valider()
    
    print()
    print(f"{client_final.nom} a maintenant {client_final.points_fidelite} points de fidelite !")
    
    
    # Test 8 : MRO (Method Resolution Order)
    print("\n\n" + "=" * 60)
    print("TEST 8 : METHOD RESOLUTION ORDER (MRO)")
    print("=" * 60 + "\n")
    
    print("Hierarchie des classes :\n")
    print(f"CommandeFidele MRO : {[c.__name__ for c in CommandeFidele.__mro__]}")
    print(f"CommandeSurPlaceFidele MRO : {[c.__name__ for c in CommandeSurPlaceFidele.__mro__]}")
    print(f"CommandeEmporterFidele MRO : {[c.__name__ for c in CommandeEmporterFidele.__mro__]}")