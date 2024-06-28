""" 
Exercice 6 : Contrôle d'accès au laboratoire secret
Scénario :
Tu dois vérifier les codes d'accès des employés pour entrer dans un laboratoire secret. 
Écris une fonction qui prend une liste de codes et retourne une liste de booléens indiquant 
si chaque code est valide 
(un code est valide s'il contient exactement 6 chiffres).
"""

def verification_codes(codes):
    for code in codes:
        if code.isdigit() and len(code) == 6:
            print(f"{code} : code valide")
        else:
            print(f"{code} : code non valide")


codes = ["123456", "abcdef", "1234", "789101", "654321"]

verification_codes(codes)
