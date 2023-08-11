import os
import requests
from bs4 import BeautifulSoup
from pyfiglet import Figlet
from colorama import init, Fore
from questionary import prompt, text

# Initialisation de Colorama pour la coloration du texte dans la console
init(autoreset=True)

# Fonction pour obtenir les noms de projets d'un utilisateur Replit
def get_repl_names():
    user_url = text("Entrez l'URL de l'utilisateur Replit : ").ask()

    response = requests.get(user_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    project_names = []
    for project in soup.find_all(class_='styles__title___28KRs'):
        project_names.append(project.text.strip())

    return project_names

# Fonction pour enregistrer les noms de projets dans un fichier
def save_names_to_file(project_names):
    with open('repl_projects.txt', 'w') as file:
        for name in project_names:
            file.write(name + '\n')

# Affichage stylisé du titre
def print_title(title):
    custom_fig = Figlet()
    print(Fore.CYAN + custom_fig.renderText(title))

# Programme principal
if __name__ == "__main__":
    print_title("Replit Project Grabber")

    project_names = get_repl_names()
    save_names_to_file(project_names)

    print(Fore.GREEN + f"{len(project_names)} projet(s) enregistré(s) dans repl_projects.txt.")