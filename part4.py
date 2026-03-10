from part1 import Boisson
from part2 import Cafe, The
from part3 import Lait, Sucre


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

class BoissonAvecCombinaison(Boisson):
    """
    Classe de base qui ajoute la capacité de combiner des boissons avec +
    """

    def __add__(self, other):
        """Permet de combiner deux boissons avec l'opérateur +"""
        if not isinstance(other, Boisson):
            return NotImplemented
        return BoissonCombinee(self, other)

class CafeCombinable(BoissonAvecCombinaison):
    """Café avec possibilité de combinaison"""

    def cout(self):
        return 2.0

    def description(self):
        return "Café simple"


class TheCombinable(BoissonAvecCombinaison):
    """Thé avec possibilité de combinaison"""

    def cout(self):
        return 1.5

    def description(self):
        return "Thé"


# Décorateurs combinables
class DecorateurBoissonCombinable(BoissonAvecCombinaison):
    """Décorateur de base avec possibilité de combinaison"""

    def __init__(self, boisson):
        self._boisson = boisson


class LaitCombinable(DecorateurBoissonCombinable):
    """Lait avec possibilité de combinaison"""

    def cout(self):
        return self._boisson.cout() + 0.5

    def description(self):
        return self._boisson.description() + ", Lait"


class SucreCombinable(DecorateurBoissonCombinable):
    """Sucre avec possibilité de combinaison"""

    def cout(self):
        return self._boisson.cout() + 0.2

    def description(self):
        return self._boisson.description() + ", Sucre"


# Test de la combinaison
if __name__ == "__main__":
    print("=" * 50)
    print("TEST DE LA COMBINAISON DE BOISSONS")
    print("=" * 50)

    # Création de boissons
    cafe = CafeCombinable()
    the = TheCombinable()

    # Combinaison simple
    menu1 = cafe + the
    print(f"\n {menu1.description()}")
    print(f"  Prix : {menu1.cout()}€")

    # Combinaison avec décorateurs
    cafe_lait = LaitCombinable(CafeCombinable())
    the_sucre = SucreCombinable(TheCombinable())

    menu2 = cafe_lait + the_sucre
    print(f"\n {menu2.description()}")
    print(f"  Prix : {menu2.cout()}€")

    # Combinaison complexe
    cafe_complet = SucreCombinable(LaitCombinable(CafeCombinable()))
    menu3 = cafe_complet + the
    print(f"\n {menu3.description()}")
    print(f"  Prix : {menu3.cout()}€") 