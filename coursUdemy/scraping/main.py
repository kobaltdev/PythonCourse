from bs4 import BeautifulSoup
import os

script_dir = os.path.dirname(__file__)
rel_path = "site_recette/recette.html"
abs_file_path = os.path.join(script_dir, rel_path)
print(abs_file_path)

f = open(abs_file_path, "r")
html_content = f.read()
f.close()



soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1")
desc = soup.find("p", class_="description")

print("titre H1 :", titre_h1.text)
print("description :", desc.text)

# pour isoler un element non unique, si on a plusieurs balises avec le même type, même nom etc.
# on peut extraire en plusieurs parties
# Exemple avec la même description, qui se trouve dans le div 'centre'

div_centre = soup.find_all("div", class_="centre") # on récupère les éléments parents
desc2 = div_centre[1].find("p") # on cherche directement dans l'élément parent

print("description récupérée via le parent :", desc2)

# rechercher l'attribut / la source de l'image

div_info = soup.find("div", class_="info")
src_image = div_info.contents[1]

print("Le src de l'image est :", src_image["src"])

