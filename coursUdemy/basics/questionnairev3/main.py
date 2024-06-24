# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# classe Question :
#   - poserQuestion
#   - demanderReponse
#
# Question : titre: str, choix (str), bonne reponse: str
# Autres données : reponse_user, score_user
#
# classe Questionnaire
# - questions    (Question)
# - lancerQuestionnaire()

class Question:

    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

    def poserQuestion(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i + 1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utilisateur(1, len(self.choix))
        if self.choix[reponse_int - 1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")

        print()
        return resultat_response_correcte


    def demander_reponse_numerique_utilisateur(mini, maxi):
        reponse_str = input("Votre réponse (entre " + str(mini) + " et " + str(maxi) + ") : ")
        try:
            reponse_int = int(reponse_str)
            if mini <= reponse_int <= maxi:
                return reponse_int
            print("ERREUR : Vous devez rentrer un nombre entre", mini, "et", maxi)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utilisateur(mini, maxi)


class Questionnaire:
    score = 0

    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        for question in self.questions:
            if question.poserQuestion():
                Questionnaire.score += 1
        print("Score final :", Questionnaire.score, "sur", len(self.questions))


liste_question = (
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
)

q1 = Questionnaire(liste_question)
q1.lancer()






