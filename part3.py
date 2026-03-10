from part1 import Boisson
from part2 import Cafe, The


class DecorateurBoisson(Boisson):
    """
    Classe décorateur de base.
    Cette classe reçoit une boisson existante et pourra modifier son comportement.
    """

    def __init__(self, boisson):
        self._boisson = boisson


class Lait(DecorateurBoisson):
    """Ajoute du lait à une boisson"""

    def cout(self):
        return self._boisson.cout() + 0.5

    def description(self):
        return self._boisson.description() + ", Lait"


class Sucre(DecorateurBoisson):
    """Ajoute du sucre à une boisson"""

    def cout(self):
        return self._boisson.cout() + 0.2

    def description(self):
        return self._boisson.description() + ", Sucre"


# Test des décorateurs
if __name__ == "__main__":
    print("=" * 50)
    print("TEST DES DÉCORATEURS")
    print("=" * 50)

    # Café simple
    boisson = Cafe()
    print(f"\n {boisson.description()}")
    print(f" Prix : {boisson.cout()}€")

    # Café avec lait
    boisson = Lait(boisson)
    print(f"\n {boisson.description()}")
    print(f" Prix : {boisson.cout()}€")

    # Café avec lait et sucre
    boisson = Sucre(boisson)
    print(f"\n{boisson.description()}")
    print(f"Prix : {boisson.cout()}€")

    print("\n" + "=" * 50)

    # Thé avec sucre seulement
    the_sucre = Sucre(The())
    print(f"\n {the_sucre.description()}")
    print(f" Prix : {the_sucre.cout()}€")