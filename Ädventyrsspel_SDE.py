import random as rand

class Player:
    strength = 0
    hp = 1
    inventory = []
    level = 1
    poäng = 9

    def __str__(self):
        return (f"""    Här är dina stats:
    Level: {self.level}
    Styrka: {self.strength}
    Hp: {self.hp}""")


class Item:
    def __init__(self, namn, strength_bonus):
        self.namn = namn
        self.strength_bonus = strength_bonus

plr = Player()


def prin(text):
    print("    " + text)


def print_item(item):
    prin(f"""Namn: {item.namn}
    Styrkeboost: {item.strength_bonus}
    """)

def main():
    while True:
        val = input("""
    Vad vill du göra?
    1: Välj dörr
    2: Kolla stats
    3: Kolla inventory
    --> """).replace(" ", "").replace(".", "")
        match(val):
            case("1"): dörr(); break
            case("2"): print(plr); break
            case("3"): inv(); break
            case(_): prin("Du måste skriva 1, 2 elller 3.")

def inv():
    if len(Player.inventory) == 0:
        prin("Ditt inventory är tomt!")
    else:
        prin("Här är vad som finns i ditt inventory:")
        for i in range(len(Player.inventory)):
            print_item(Player.inventory[i])


def endwin():
    if Player.hp == 0:
        prin("Du har nått noll Hp och förlorat spelet!")
    else:
        prin("Du har nått nivå tio och vunnit spelet! Waow!")
    while True:
        fråga = input("    Vill du spela igen? (Ja/Nej) --> ").lower().replace(" ", "").replace(".", "")
        match fråga:
            case("ja"): restart(); break
            case("nej"): return "stop"
            case(_): prin("Du måste svara med ja eller nej.")


def restart():
    prin("...startar om spelet...\n")
    Player.strength = 0
    Player.hp = 1
    Player.inventory = []
    Player.level = 1
    Player.poäng = 9


def poäng():
    print(plr)
    print(f"\n    Du har {Player.poäng} poäng över att spendera på dina stats!")
    a = 0
    while Player.poäng > 0:
        if a == 0: frg = "styrka"
        else: frg = "hp"
        while True:
            try:
                strf = int(input(f"    Hur många av dina poäng vill du sätta i {frg}? -->"))
                if strf < 0 or frg == "styrka" and strf >= Player.poäng:
                    prin(f"Du måste skriva ett tal från 1 till {Player.poäng-1}.")
                elif frg == "hp" and strf > Player.poäng:
                    prin(f"Du måste skriva ett tal från 1 till {Player.poäng}.")
                else:
                    Player.poäng -= strf
                    if a == 0:
                        Player.strength += strf
                    else:
                        Player.hp += strf
                    a += 1; break
            except ValueError:
                prin("Du måste skriva ett positivt heltal.")


dörrar = ["Stor stendörr", "Dörr med runor", "Metallgrind", "Gammal grind", "Drömmarnas dörr", "Träport", "Glasportal", "Stålport", "Hemlighetsfull lucka", "Betongport", "Rostig grind", "Träskdörr", "Valv dörr", "Glastunnel", "Rostig ståldörr", "Mörk gränd", "Gammal port", "Rosa dörr", "Tunneldörr", "Kuslig port"]

def dörr():
    for i in range(1, 4):
        prin(f"{i}. {rand.choice(dörrar)}")
    while True:
        val = input("    Vilken dörr vill du välja?").lower().replace(" ", "").replace(".", "")
        if val in {"1", "2", "3"}: break
        prin("Du måste skriva antingen 1, 2 eller 3.")
    rand.choice([monster, fälla, kista])()


monster_lista = ["Basilisk", "Cyklop", "Zombie", "Troll", "Spöke", "Golem", "Vampyr", "Varulv", "Gorgon", "Skelett", "Mimic", "Slime", "Spindel (Stor)", "Lindorm", "Häxa"]

def monster():
    total_strength = plr.strength
    for i in range(len(Player.inventory)):
        total_strength += Player.inventory[i].strength_bonus
    monster = Player()
    monster.level = rand.randint(1, plr.level+5)
    monster.strength = rand.randint(plr.level+3, plr.level+10)
    prin(f"""Du har träffat ett monster!!
    Namn: {rand.choice(monster_lista)}
    Level: {monster.level}
    Styrka: {monster.strength}
    ...ni börjar slåss...""")
    if monster.strength == total_strength:
        prin("Ni slogs hårt och länge men var lika starka så ingen vann. \n    Efter ett långt slagsmål drar du dig iväg utan stor skada.")
    elif monster.strength > total_strength:
        prin(f"Efter en kort fight krossades du av monstret. Ditt hp är nu {plr.hp-1}")
        plr.hp -= 1
    else:
        prin(f"Du kämpade hårt och lyckades äntligen ta kol på det förbaskade monstret!\n    Din level gick upp till {plr.level+1}!")
        plr.level += 1
        plr.poäng += 1


def fälla():
    tal = rand.randint(1, 3)
    match tal:
        case(1): prin(f"Du blev fångad i en fälla!\n    Ditt hp gick ner till {plr.hp-1}"); plr.hp -= 1
        case(2): prin("Du blev nästan fångad i en fälla, men kom snabbt undan!")
        case(3): 
            if len(Player.inventory > 0):
                prin(f"En fälla tog ditt senaste item!\n{print_item(Player.inventory[len(Player.inventory)-1])}\n    har försvunnit.")
                del Player.inventory[len(Player.inventory)-1]
            else:
                prin("En fälla försökte ta ditt senaste item, men du är fattig!")


vapen = ["Skymningsklingan", "Eldpilbåge", "Frostspira", "Åskhammaren", "Drakens ande", "Mörkets dolk", "Solglansen", "Stjärnfallssvärdet", "Havets hämnd", "Jordbrytaren", "Luftvirket", "Skuggornas spjut", "Eldtungan", "Kristallkastaren", "Månstrålesvärdet", "Dimslöparen", "Blodmånen", "Tidsförvrängaren", "Själssläckaren", "Natthärjaren"]

def kista():
    item = Item(rand.choice(vapen), rand.randint(1, 3))
    if len(plr.inventory) < 5:
        prin("Du har hittat ett item!\n    Eftersom ditt inventory inte är fullt läggs det i ditt inventory!")
        print_item(item)
        Player.inventory.append(item)
    else:
        prin("Ditt inventory är fullt! Vill du byta ut något för det du hittade?")
        prin(f"Här är itemet du hittade:\n{print_item(item)}")
        prin("Här är ditt inventory, skriv 1, 2, 3, 4 eller 5 för det item du vill byta ut.\n    Om du inte vill byta ut något, skriv 6.")
        for i in range(5):
            prin(f"{i+1}. ")
            print_item(Player.inventory[i])
        while True:
            val = input("--> ").replace(" ", "").replace(".", "")
            match(val):
                case("1" | "2" | "3" | "4" | "5"):
                    Player.inventory[int(val)-1] = item; break
                case("6"):
                    prin("Ingenting hände."); break
                case(_): prin("Du måste skriva 1, 2, 3, 4, 5 eller 6.")


#--------------------------------------------------------------------------#

print("Välkommen till vårat äventyrsspel, gjort av Simon Remle, Emelie Gyllenberg och Daniel Furo.")

while True:
    fråga = input("Vill du ha en spel tutorial? (ja/nej) --> ").lower().replace(".", "").replace(" ", "")
    if not fråga in {"ja", "nej"}:
        print("Du måste skriva antingen ja eller nej.")
    elif fråga == "ja":
        print("""Spelet går ut på att du som modig äventyrare ska ta dig igenom olika rum i en håla, besegra moster och hitta skatter. 
När du når nivå 10 vinner du spelet.
Du väljer att gå in i en dörr genom att trycka 1, däreter får du välja mellan tre olika dörrar genom att trycka 1,2 eller 3.
De olika dörrarna kan leda till olika rum, ett rum som har ett moster som du ska besegra, ett annat har en fälla och det tredje har en skatt.
När du slåss emot monster kan två olika grejer att hända; 
1: du besegrar mostret och går upp en level 
2: du förlorar mot mostret och förlorar 1 liv. 
Den som vinner avgörs av den som har mest styrke poäng.
Om du har otur går du in i ett rum med en fälla, fällan kommer att skada dig och du förlorar 1 liv.
Om du hittar en skatt kan den bestå av olika föremål, vapen som ger dig yttligare styrka eller om du har tur, mer liv.

Du kan max ha 5 vapen i ditt inventory, varje vapen har en styrkebonus som läggs samman i dina stats, du kan kolla dina stats genom att tycka 2, och du kollar ditt inventory genom att trycka 3. 
Om du har för många vapen i ditt inventory så måste du välja ett att slänga, detta kommer att påvrka din styrkebonus, så välj noga!

Lycka till på ditt äventyr!! :D
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


    









