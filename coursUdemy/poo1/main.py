class EtreVivant:
    ESPECE = "(Etre vivant non reconnu)"

    def afficher_infos_etre_vivant(self):
        print("Info type etre vivant : " + self.ESPECE)


class Chat(EtreVivant):
    ESPECE = "Mamifère félin"

class Personne(EtreVivant):

    ESPECE = "Humain"

    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        self.age = age
        if nom == "": # prévoir le cas d'un nom vide
            self.nom = self.demanderNom()

    def sePresenter(self):
        # Cas de l'âge non passé
        if self.age == 0:
            print(f"Bonjour, je m'appelle {self.nom}")
        else:
            print(f"Bonjour, je m'appelle {self.nom} et j'ai {self.age} ans.")
            if self.estMajeur():
                print("Je suis donc majeur")
            else:
                print("Je suis donc mineur")
        print(f"Espèce : {Personne.ESPECE}")

    def estMajeur(self):
        if self.age >= 18:
            return True
        return False

    def demanderNom(self):
        self.nom = input("Quel est votre nom ? = ")
        return self.nom


class Etudiant(Personne):

    def __init__(self, nom: str, age: int, etudes: str):
        super().__init__(nom, age)
        self.etudes = etudes

    def sePresenter(self):
        super().sePresenter()
        print(f"Mes études : {self.etudes}")

# ---- UTILISATION

liste_personnes = [Personne("jean", 30), Personne("paul", 15), Personne("Zoe", 20)]


for personne in liste_personnes:
    personne.sePresenter()

liste_personnes[0].afficher_infos_etre_vivant()

chat1 = Chat()
chat1.afficher_infos_etre_vivant()

etre1 = EtreVivant()
etre1.afficher_infos_etre_vivant()

etudiant1 = Etudiant("jojo", 22, "Ecole d'ingé")
etudiant1.afficher_infos_etre_vivant()
etudiant1.sePresenter()

