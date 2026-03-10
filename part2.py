from part1 import Boisson


class Cafe(Boisson):
    """Représente un café simple"""

    def cout(self):
        return 2.0

    def description(self):
        return "Café simple"


class The(Boisson):
    """Représente un thé"""

    def cout(self):
        return 1.5

    def description(self):
        return "Thé"


# Test des boissons concrètes
if __name__ == "__main__":
    print("=" * 50)
    print("TEST DES BOISSONS CONCRÈTES")
    print("=" * 50)

    # Création d'un café
    boisson1 = Cafe()
    print(f"\n {boisson1.description()}")
    print(f"Prix : {boisson1.cout()}€")

    # Création d'un thé
    boisson2 = The()
    print(f"\n {boisson2.description()}")
    print(f" Prix : {boisson2.cout()}€")