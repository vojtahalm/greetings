
# vymazání terminálu

import os
import random


# Vymazání obrazovky terminálu (Windows)
os.system("cls")

### Základní verze - vždy stejná odpověď
# Získání jména a příjmení od uživatele

jmeno = input("Vojta")
prijmeni = input("Halmazňa")


# Generování pozdravu bez náhodného prvku a zobrazení v terminálu
#    print(f"Ahoj, {jmeno} {prijmeni}! Těší mě, že tě poznávám.")

### Rozšířená verze - pseudonáhodný výběr bez zamíchání
# vytvořit greetings jako list pozdravů

greetings = [f"Ahoj, {jmeno} {prijmeni}! Těší mě, že tě poznávám.",
             f"Zdravím tě, {jmeno} {prijmeni}! Jak se máš?",
             f"Zdar, {jmeno} {prijmeni}! Rád tě vidím."
             f"Bonjour, {jmeno} {prijmeni}! Comment ça va?"]


print(random.choice(greetings))

# Rozšířená verze - random seed()

# side effect provedení v této části kódu má za následek i zamíchání volby při opětovném volání


# *verze - pozdrav podle denní doby
from datetime import datetime
hodina = datetime.now().hour

if 5 <= hodina < 11:
    print(f"Dobré ráno, {jmeno} {prijmeni}! Je {hodina} hodin. ")
elif 11 <= hodina < 17:
    print(f"Kvalitní den přeji, {jmeno} {prijmeni}! Je {hodina} hodin. ")
else:
    print(f"Klidný večer nebo noc, {jmeno} {prijmeni}! Je {hodina} hodin. ")