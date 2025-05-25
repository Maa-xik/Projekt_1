##################################
##          Projekt_1           ##
##                              ##
##          Stepan Vysek        ##
##        vysek@centrum.cz      ##
##                              ##
##################################


# import ppotrebnych knihoven
# -----------------------------------------------------------
import pprint
#import time

# promenne
# -----------------------------------------------------------
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

accounts = {
    "bob":      "123",
    "ann":      "pass123",
    "mike":     "password123",
    "liz":      "pass123"
}

# telo programu
# -----------------------------------------------------------

# prihlaseni uzivatele
print("="*40); print("      Vitej v Textovem analyzatoru")
print("-"*40); print("Zadej sve prihlasovaci udaje:")
#print(" uzivatel: ", end=""); user = input()
#print(" heslo: ", end=""); password = input()
print("-"*40)

#if accounts.get(user) == password:
#    print("Uspesne zalogovan. Vitej uzivateli", user,"!")
#elif user in accounts.keys():
#    print("Zadal jsi neplatne heslo!")
#    print("Ukoncuji program.....")
#    exit()
#else:
#    print("Neregistrovany uzivatel!")
#    print("Ukoncuji program.....")
#    exit()
print("-"*40)

# zadani volby bloku textu
print("Mas na vyber ze 3 bloku textu (ukazky):\n")

text_pocet = ("1", "2", "3")
for x in text_pocet:
    print(x, " - \"",TEXTS[int(x)-1][0:40],"...\"", sep="")
print()
#print("Zadej svoji volbu (pouze cisla 1-3): ", end=""); text_block = input()
text_block = "1"

if text_block not in text_pocet:
    print("Spatna volba")
    print("Ukoncuji program.....")
    exit()
print("-"*40)

# zpracovani bloku textu
print("Jedeeeeem, pracujem s textem")

text_to_process = TEXTS[int(textblock)-1][:-1].split()  # rozdeleni textu na list a odebrani tecky

print(text_to_process)
print(len(text_to_process))

stats_words = len(text_to_process)


    








