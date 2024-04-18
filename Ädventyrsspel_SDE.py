import random as rand

class Player:
    strength = 0
    hp = 1
    inventory = []
    level = 1
    poäng = 9

    def __str__(self):
        return (f"""\n    Här är dina stats:
    Level: {self.level}
    Styrka: {self.strength}
    Hp: {self.hp}""")


class Item:
    def __init__(self, namn, strength_bonus):
        self.namn = namn
        self.strength_bonus = strength_bonus

plr = Player()


def print_item(item):
    print(f"""    Namn: {Player.inventory[item].namn}
    Styrkeboost: {Player.inventory[item].strength_bonus}
    """)

def main():
    while True:
        try:
            val = int(input("""    Vad vill du göra?
    1: Välj dörr
    2: Kolla stats
    3: Kolla inventory
    --> """))
            break
        except ValueError:
            print("    Du måste skriva 1, 2 eller 3!")
    if val == 1:
        dörr()
    elif val == 2:
        print(plr)
    elif val == 3:
        inv()
    else:
        print("    Du måste skriva 1, 2 eller 3!")
        main()


def inv():
    if len(Player.inventory) == 0:
        print("\n    Ditt inventory är tomt!")
    else:
        print("\n    Här är vad som finns i ditt inventory:")
        for i in range(len(Player.inventory)):
            print_item(i)


def endwin():
    if Player.hp == 0:
        print("    Du har nått noll Hp och förlorat spelet!")
    else:
        print("    Du har nått nivå tio och vunnit spelet! Waow!")
    while True:
        fråga = input("    Vill du spela igen? (Ja/Nej) --> ").lower().replace(" ", "").replace(".", "")
        if fråga == "ja":
            restart()
            break
        elif fråga == "nej":
            return "stop"
        else:
            print("    Du måste svara med ja eller nej.")


def restart():
    print("    ...startar om spelet...\n")
    Player.strength = 0
    Player.hp = 1
    Player.inventory = []
    Player.level = 1
    Player.poäng = 9


def poäng():
    print(plr)
    print(f"    Du har {Player.poäng} poäng över att spendera på dina stats!")
    a = 0
    while Player.poäng > 0:
        if a == 0:
            frg = "styrka"
        else:
            frg = "hp"
        while True:
            try:
                strf = int(input(f"    Hur många av dina poäng vill du sätta i {frg}? -->"))
                if strf < 0 or frg == "styrka" and strf >= Player.poäng:
                    print(f"    Du måste skriva ett tal från 1 till {Player.poäng-1}.")
                elif frg == "hp" and strf > Player.poäng:
                    print(f"    Du måste skriva ett tal från 1 till {Player.poäng}.")
                else:
                    Player.poäng -= strf
                    if a == 0:
                        Player.strength += strf
                    else:
                        Player.hp += strf
                    a += 1; break
            except ValueError:
                print("    Du måste skriva ett positivt heltal.")
        

dörrar = ["Stor stendörr", "Dörr med runor", "Metallgrind", "Gammal grind", "Drömmarnas dörr", "Träport", "Glasportal", "Stålport", "Hemlighetsfull lucka", "Betongport", "Rostiga grind", "Träskdörr", "Valv dörr", "Glastunnel", "Rostig ståldörr", "Mörk gränd", "Gammal port", "Rosa dörr", "Tunneldörr", "Kuslig port"]

def dörr():
    for i in range(1, 4):
        print("    ", i, ". ", rand.choice(dörrar))
    while True:
        val = int(input("    Vilken dörr vill du välja?"))
        if val in {1, 2, 3}:
            break
        print("    Du måste skriva antingen 1, 2 eller 3.")
    randomval = rand.randint(1, 3)
    if randomval == 1:
        monster()
    elif randomval == 2:
        fälla()
    else:
        kista()


monster_lista = ["Basilisk", "Cyklop", "Zombie", "Troll", "Spöke", "Golem", "Vampyr", "Varulv", "Gorgon", "Skelett", "Mimic", "Slime", "Spindel (Stor)", "Lindorm", "Häxa"]

def monster():
    total_strength = plr.strength
    for i in range(len(Player.inventory)):
        total_strength += Player.inventory[i].strength_bonus
    monster = Player()
    monster.level = rand.randint(1, plr.level+5)
    monster.strength = rand.randint(plr.level+3, plr.level+10)
    print(f"""
    Du har träffat ett monster!!
    Namn: {rand.choice(monster_lista)}
    Level: {monster.level}
    Styrka: {monster.strength}
    ...ni börjar slåss...""")
    if monster.strength == total_strength:
        print("    Ni slogs hårt och länge men var lika starka så ingen vann. \n    Efter ett långt slagsmål drar du dig iväg utan stor skada.")
    elif monster.strength > total_strength:
        print(f"    Efter en kort fight krossades du av monstret. Ditt hp är nu {plr.hp-1}")
        plr.hp -= 1
    else:
        print(f"    Du kämpade hårt och lyckades äntligen ta kol på det förbaskade monstret!\n    Din level gick upp till {plr.level+1}!")
        plr.level += 1


def fälla():
    print(f"    Du blev fångad i en fälla!\n    Ditt hp gick ner till {plr.hp-1}")
    plr.hp -= 1


vapen = ["Skymningsklingan", "Eldpilbåge", "Frostspira", "Åskhammaren", "Drakens ande", "Mörkets dolk", "Solglansen", "Stjärnfallssvärdet", "Havets hämnd", "Jordbrytaren", "Luftvirket", "Skuggornas spjut", "Eldtungan", "Kristallkastaren", "Månstrålesvärdet", "Dimslöparen", "Blodmånen", "Tidsförvrängaren", "Själssläckaren", "Natthärjaren"]

def kista():
    item = Item(rand.choice(vapen), rand.randint(1, 3))
    if len(plr.inventory) > 5:
        print("    Du har hittat ett item!")
        Player.inventory.append(item) #ta bort detta sen och fråga om man vill lägga till


#--------------------------------------------------------------------------#

print("Välkommen till vårat äventyrsspel, gjort av Simon Remle, Emelie Gyllenberg och Daniel Furo.")

while True:
    fråga = input("Vill du ha en spel tutorial? (ja/nej) --> ").lower().replace(".", "").replace(" ", "")
    if not fråga in {"ja", "nej"}:
        print("Du måste skriva antingen ja eller nej.")
    elif fråga == "ja":
        print("""Spelet går ut på att du som modig äventyrare ska ta dig igenom olika rum i en håla, besegra moster och hitta skatter. 
När du når nivå 10 vinner du spelet.
De olika dörrarna kan leda till olika rum, ett rum som har ett moster som du ska besegra, ett annat har en fälla och det tredje har en skatt.
När du slåss emot monster kan två olika grejer hända; 
1: du besegrar mostret och går upp en level 
2: du förlorar mot mostret och förlorar 1 liv. 
Den som vinner avgörs av den som har mest styrke poäng.
Om du har otur går du in i ett rum med en fälla, fällan kommer att skada dig och du förlorar 1 liv.
Om du hittar en skatt kan den bestå av olika föremål, vapen som ger dig yttligare styrka eller om du har tur, mer liv.

Du kan max ha 5 vapen i ditt inventory, varje vapen har en styrkebonus som läggs samman i dina stats. Du kollar ditt inventory genom att trycka 3, därefter kan du välja vilka vapen du vill ha 
elluks ud mo rav
 """); break
    else:
        break


while True:
    if Player.level == 10 or Player.hp == 0:
        if endwin() == "stop":
            break
    elif Player.poäng > 0:
        poäng()
    main()


    









