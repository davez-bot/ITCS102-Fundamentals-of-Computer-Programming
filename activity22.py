shanks = ["Red Haired", "Emperor of the Sea", "Divine Purgatory"]
whitebeard = ["Strongest Man in the World", "Quake-Quake Fruit", "Quake Smash"]
mihawk = ["World's Strongest Swordsman", "Black Blade Yoru", "Thousand Slashes"]

ichigo = ["#1 Special Threat", "Tensa Zangetsu", "Getsuga Tensho"]
yamamoto = ["Captain Commander", "Zanka no Tachi", "Flame Purgatory"]
yhwach = ["Quincy King", "Schrift:A", "Almighty"]

gojo = ["Strongest Sorcerer of Today", "Infinite Void", "Hollow Purple"]
sukuna = ["Strongest Sorcerer in History", "Malevolent Shrine", "DIsmantle/Cleave"]
yuji = {"Strongest Sorcerer of Tomorrow", "Benevolent Shrine", "Convergent FIst"}

onepiece = {"Shanks": shanks, "Whitebeard": whitebeard, "Mihawk": mihawk}
bleach = {"Ichigo": ichigo, "Yamamoto": yamamoto, "Yhwach": yhwach}
jjk = {"Gojo": gojo, "Sukuna": sukuna, "Yuji": yuji}

shonen = {"One PIece": onepiece, "Bleach": bleach}
high_shonen = {"Jujutsu Kaisen": jjk}

anime = {"Old Anime": shonen, "New Anime": high_shonen}

print("--- 1. GOing down one level at a time ---")
print(anime["Old Anime"]["One Piece"]["Shanks"][1])

print()
print("--- 2. Loop level 1: Cagetories ---")
for category in anime:
    print(category)

print()
print("--- 3. Loop levels 1-2: categories and titles ---")
for category, titles in anime.items():
    print(category)
    for title in titles:
        print("  -", titles)

print()
print("--- 4. Loop ALL levels ---")
for category, titles in anime.items():
    print(Category)
    for title, characters in titles.items():
        print(" " + title)
        for name, info in characters.items():
            print("   " + name)
            print("     Description:", info[0])
            print("     Power:", info[1])

print()
print("--- 5. Count every character ---")
count = 0
for titles in anime.values():
    for characters in titles.values():
        for name in characters:
            count += 1
print("Total Characters:", count)

print()
print("--- 6. Search for a character ---")
search = "Rem"
found = False
for category, titles in anime.items():
    for title, characters in titles.item():
        if search in characters:
            print(search, "Is from", title, "(" + category + ")")
            print("Power", characters[search][1])
            found = True
if found == False:
    print(search, "not found.")
