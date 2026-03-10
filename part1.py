from abc import ABC, abstractmethod


class Boisson(ABC):
    """
    Classe abstraite représentant une boisson générique.
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


# Test de la classe abstraite
if __name__ == "__main__":
    # Cette ligne provoquera une erreur car on ne peut pas instancier une classe abstraite
    try:
        boisson = Boisson()
    except TypeError as e:
        print(f"Erreur attendue : {e}")
        print("On ne peut pas créer d'instance de Boisson directement")