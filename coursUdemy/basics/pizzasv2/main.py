class Pizza:
    # On utilise un booleen pour signifier qu'une pizza est vegetarienne ou non

    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def afficherPizza(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = "- VEGETARIENNE"
        print(f"Pizza : {self.nom}, prix : {self.prix}€ {veg_str}")
        print(f"Ingrédients : {", ".join(self.ingredients)}")
        print()


class PizzaPersonnalisee(Pizza):

    # Pour le prix, la pizza personnalisée est à 7 € de base
    # Chaque ingrédient supplémentaire augmente son prix 1.20 €
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1.2
    # On crée aussi un index global qui va permettre d'ajouter autant de personnalisé
    # Sans passer l'index dans la construction de l'objet
    NUMERO = 0

    def __init__(self):
        # !!! ATTENTION bien afficher ce paramètre en premier !!!
        # En effet, on en a besoin pour demanderIngredient()
        # On va venir incrémenter la variable de classe à chaque création d'objet
        PizzaPersonnalisee.NUMERO += 1
        # on passe alors ce numero au self
        self.numero = PizzaPersonnalisee.NUMERO
        # on modifie le nom pour la pizza personnalisé directement dans le constructeur
        super().__init__("Personnalisée " + str(self.numero), 0, [])
        self.demanderIngredient()  # on appelle la fonction de cette classe enfant
        self.calculPrix()


    def demanderIngredient(self):
        # afficher ingrédients pour la pizza personnalisée numero xx
        print("-----")
        print(f"Ingredient(s) pour la pizza perso numero {self.numero}")
        print("-----")
        nb_ingredient_max = 5
        # pour boucler de manière infinie, et on cassera la boucle avec un return dans une condition
        while True:
            # Définition du nombre max d'ingrédients
            if len(self.ingredients) > (nb_ingredient_max - 1):
                return
            ingredient = input(f"Ajoutez un ingredient (max {nb_ingredient_max}) (ENTER pour finir) : ")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)   # ajout de l'ingrédient saisi à la liste
            # utilisation de join pour formater la sortie
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculPrix(self):
        self.prix = self.PRIX_DE_BASE + (self.PRIX_PAR_INGREDIENT * len(self.ingredients))




pizzas = [Pizza("4 fromages", 8.50, ("brie", "emmental", "comté", "parmesan"), True),
          Pizza("Calzone", 10.50, ("jambon", "tomates", "oeufs")),
          Pizza("Hawaienne", 11.50, ("tomates", "oignons", "poivrons", "poulet")),
          Pizza("Savoyarde", 9, ("lardons", "reblochon", "patates", "oignons"), True),
          PizzaPersonnalisee(),
          PizzaPersonnalisee(),
          ]

for p in pizzas:
    print()
    print("Liste des pizzas : ")
    print()
    p.afficherPizza()




# ------- TRIS ------------

# def tri(e):
#     return len(e.ingredients)
#
#
# pizzas.sort(key=tri, reverse=False)
# for p in pizzas:
#     p.afficherPizza()

# print("toutes les pizzas")
# print()
# for p in pizzas:
#     p.afficherPizza()
#
# print("-----------")
# print("uniquement les vegetariennes :")
# print()
# for p in pizzas:
#     if p.vegetarienne:
#         p.afficherPizza()
#
# print("-----------")
# print("uniquement les non-vegetariennes :")
# print()
# for p in pizzas:
#     if not p.vegetarienne:
#         p.afficherPizza()
#
# print("-----------")
# print("uniquement contenant de la tomate :")
# print()
# for p in pizzas:
#     if "tomates" in p.ingredient:
#         p.afficherPizza()
#
# print("-----------")
# print("uniquement a moins de 10€ :")
# print()
# for p in pizzas:
#     if p.prix < 10:
#         p.afficherPizza()
