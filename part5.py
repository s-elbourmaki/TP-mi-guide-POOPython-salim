from dataclasses import dataclass

@dataclass
class Client:
    """
    Représente un client du café.
    Utilise @dataclass pour générer automatiquement __init__, __repr__, __eq__
    """
    nom: str
    numero: int
    points_fidelite: int


# Test de la dataclass
if __name__ == "__main__":
    print("=" * 50)
    print("TEST DE LA CLASSE CLIENT")
    print("=" * 50)

    # Création de clients
    client1 = Client("Alice", 1001, 50)
    client2 = Client("Bob", 1002, 120)
    client3 = Client("Alice", 1001, 50)

    # Affichage automatique grâce à __repr__
    print(f"\n Client 1 : {client1}")
    print(f" Client 2 : {client2}")
    print(f" Client 3 : {client3}")

    # Comparaison automatique grâce à __eq__
    print(f"\n client1 == client2 : {client1 == client2}")
    print(f" client1 == client3 : {client1 == client3}")

    # Modification des points de fidelité
    print(f"\n Points de {client1.nom} avant : {client1.points_fidelite}")
    client1.points_fidelite += 10
    print(f" Points de {client1.nom} après : {client1.points_fidelite}")