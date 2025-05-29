##################################
##          Projekt_1           ##
##  do Engeto online akademie   ##
##          Štěpán Výšek        ##
##        vysek@centrum.cz      ##
##################################

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

texts_len = list(range(1, len(TEXTS)+1))    #  pocet bloku textu

stat_words =        0       # pocet slov
stat_first_upp =    0       # pocet slov s prvnim velkym pismenem
stat_upper =        0       # pocet slov velkymi 
stat_lower =        0       # pocet slov malymi
stat_num_cnt =      0       # pocet cisel
stat_num_sum =      0       # suma vsech cisel       

stat_words_len =   {}       # dict pro pocty slov o delce x

oddelovac = 47

# telo programu
# -----------------------------------------------------------

# prihlaseni uzivatele
print("=" * oddelovac, "Vitej v Textovem analyzatoru".center(oddelovac), "=" * oddelovac, sep = "\n")
print("Zadej sve prihlasovaci udaje:")
user = input(" uzivatel: ")
password = input(" heslo: ")
print("-" * oddelovac)

if accounts.get(user) == password:
    print(f"Uspesne zalogovan. Vitej uzivateli {user} !".center(oddelovac))
elif user in accounts.keys():
    print("Zadal jsi neplatne heslo!")
    print("Ukoncuji program.....")
    exit()
else:
    print("Neregistrovany uzivatel!")
    print("Ukoncuji program.....")
    exit()
print("-" * oddelovac)

# zadani volby bloku textu
print("Mas na vyber ze 3 bloku textu (ukazky):")
for x in texts_len:
    print("  ", x, " - \"", TEXTS[x-1][0:36], "...\"", sep="")
print()
print(" Zadej svoji volbu - pouze cisla", texts_len, ": ", end=""); text_block = input()

if not text_block.isnumeric():
    print("Spatna volba, nutne cislo", "Ukoncuji program.....", sep="\n")
    exit()
elif int(text_block) not in texts_len:
    print("Spatna volba, neni ve vyberu", "Ukoncuji program.....", sep="\n")
    exit()
else:
    text_block = int(text_block)

# zpracovani bloku textu
text_to_process = TEXTS[text_block-1].split()  # rozdeleni textu pred zpracovanim na list
stat_words = len(text_to_process)
for word in text_to_process:
    for x in (",","."):                     # vycisteni textu od "," a "."
        word = word.replace(x,"")

    if not stat_words_len.get(len(word)):   # cetnost delek slov
        stat_words_len[len(word)] = 1
    else:
        stat_words_len[len(word)] += 1

    if word.isnumeric():                    # pocet slov mala/velka ...
        stat_num_cnt += 1
        stat_num_sum += int(word)
    elif word[0].islower():
        stat_lower += 1
    elif word[1].isupper():
        stat_upper += 1
    else:
        stat_first_upp += 1

# Zobrazeni vysledku
print("-" * oddelovac, "Vysledky vypoctu:".center(oddelovac), "-" * oddelovac, sep = "\n")
print("{:<38} : {:>6}".format(" Pocet slov v textu ", stat_words))
print("{:<38} : {:>6}".format(" Pocet slov s prvnim velkym pismenem ", stat_first_upp))
print("{:<38} : {:>6}".format(" Pocet slov velkymi pismeny ", stat_upper))
print("{:<38} : {:>6}".format(" Pocet slov malymi pismeny ", stat_lower))
print("{:<38} : {:>6}".format(" Pocet cisel v textu ", stat_num_cnt))
print("{:<38} : {:>6}".format(" Suma vsech cisel v textu ", stat_num_sum))

# tabulka vyskytu & delky slov
stat_words_len_sort = dict(sorted(stat_words_len.items()))
print("-" * oddelovac, "Pocty slov o ruzne delce".center(oddelovac), "-" * oddelovac, sep = "\n")
print("|Delka|", " " * 10, " graf ", " " * 12, "|", "Pocet|")
print("-" * oddelovac)
for x in stat_words_len_sort:
    y = stat_words_len_sort[x]
    print("|", "{:>3} | {:<30}".format(x, "*" * y),"|", "{:>4} |".format(y))
print("-" * oddelovac)