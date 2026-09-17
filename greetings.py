# -*- coding: utf-8 -*-
# Příliš žluťoučký kůň úpěl ďábelské ódy - testovací pangram
"""_summary_
Na inputu jméno, příjmení. Na výstupu jeden ze 3 možných pozdravů včetně vstupních informací.
* jak vyčistit terminál
* jak skutečně zajistit náhodnost
* pozdrav podle denní doby
"""

##############################################################
### Jak vymazat terminál před opětovným spuštěním - cls pro Win, clear pro Unix-like systémy

import os

# Vymazání obrazovky terminálu (Windows)
os.system("cls")


##############################################################
### Základní verze - vždy stejná odpověď

# Získání jména a příjmení od uživatele
jmeno = input("Vojta")
prijmeni = input("Halmazňa")


# Generování pozdravu bez náhodného prvku a zobrazení v terminálu
print(f"Ahoj, {jmeno} {prijmeni}! Těší mě, že tě poznávám.")

##############################################################
### Rozšířená verze - pseudonáhodný výběr bez zamíchání
# vytvořit greetings jako list pozdravů

greetings = [f"Ahoj, {jmeno} {prijmeni}! Těší mě, že tě poznávám.",
             f"Zdravím tě, {jmeno} {prijmeni}! Jak se máš?",
             f"Zdar, {jmeno} {prijmeni}! Rád tě vidím."
             f"Bonjour, {jmeno} {prijmeni}! Comment ça va?"]

import random
print(random.choice(greetings))



import random



##############################################################
### Rozšířená verze - random seed()

# zamíchání, někdy se také používá s knihovnou time: inicializace seed pomocí time: random.seed(time.time())
# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání

random.seed()



##############################################################
### *verze - pozdrav podle denní doby

import datetime

