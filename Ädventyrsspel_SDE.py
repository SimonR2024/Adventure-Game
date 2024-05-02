import random as rand
import time

class Colors:                   #Detta är för att färga texten
    red = "\u001b[31m"
    yellow = "\u001b[33m"
    green = "\u001b[32m"
    reset = "\u001b[0m"


class Player:               #Detta är player-klassen som har de viktigaste statsen till spelaren
    strength = 0
    hp = 1
    inventory = []
    level = 1
    poäng = 9

    def __str__(self):      #för att lätt kunna skriva print(playernamn) för att 
        item_strength = 0
        for item in plr.inventory:
            item_strength += item.strength_bonus
        return (f"""    Här är dina stats:
    Level: {self.level}
    Styrka: {self.strength} (+{item_strength})
    Hp: {self.hp}""")


class Item:
    def __init__(self, namn, strength_bonus):
        self.namn = namn
        self.strength_bonus = strength_bonus

plr = Player()


def prin(text):
    print("    ", end="")
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.005)
    print(Colors.reset)


def print_item(item):
    prin(f"""Namn: {item.namn}
    Styrkeboost: {item.strength_bonus}""")

def main():
    while True:
        prin("""
    Vad vill du göra?
    1: Välj dörr
    2: Kolla stats
    3: Kolla inventory""")
        val = input("    --> ").replace(" ", "").replace(".", "")
        print("\n    ||----------||\n")
        match(val):
            case("1"): dörr(); break
            case("2"): print(plr); break
            case("3"): inv(); break
            case(_): prin(Colors.red + "> Du måste skriva 1, 2 elller 3.")

def inv():
    if len(plr.inventory) == 0:
        prin("Ditt inventory är tomt!")
    else:
        prin("Här är vad som finns i ditt inventory:")
        for i in range(len(plr.inventory)):
            print_item(plr.inventory[i])
            print()


def endwin():
    if plr.hp == 0:
        prin(Colors.red + ">Du har nått noll Hp och förlorat spelet!<")
    else:
        prin(Colors.green + "<Du har nått nivå tio och vunnit spelet! Waow!>")
    while True:
        fråga = input("    Vill du spela igen? (Ja/Nej) --> ").lower().replace(" ", "").replace(".", "")
        match fråga:
            case("ja"): restart(); break
            case("nej"): return "stop"
            case(_): prin(Colors.red + "> Du måste svara med ja eller nej.")


def restart():
    prin(Colors.yellow + "...startar om spelet...\n")
    plr.strength = 0
    plr.hp = 1
    plr.inventory = []
    plr.level = 1
    plr.poäng = 9


def poäng():
    print(plr)
    prin(f"{Colors.green}\n    Du har {plr.poäng} poäng över att spendera på dina stats!")
    fråga = "styrka"

    while plr.poäng > 0:
        try:
            prin(f"Hur många av dina poäng vill du sätta i {fråga}?")
            val = int(input("    --> ").replace(".", "").replace(" ", ""))
            if val >= 0 and val <= plr.poäng and fråga == "styrka":
                plr.strength += val; plr.poäng -= val; fråga = "hp"
            elif val >= 0 and val <= plr.poäng and fråga == "hp":
                plr.hp += val; plr.poäng -= val; fråga = "styrka"
            else:
                prin(f"{Colors.red}> Du måste skriva ett tal mellan 0 och {plr.poäng}.")
        except ValueError:
            prin(Colors.red + "> Du måste skriva ett positivt heltal.")
        

#--------------------------------------------------------------------------#
#Här är funktionen för dörrarna

dörrar = ["Stor stendörr", "Dörr med runor", "Metallgrind", "Gammal grind", "Drömmarnas dörr", "Träport", "Glasportal", "Stålport", "Hemlighetsfull lucka", "Betongport", "Rostig grind", "Träskdörr", "Valv dörr", "Glastunnel", "Rostig ståldörr", "Mörk gränd", "Gammal port", "Rosa dörr", "Tunneldörr", "Kuslig port"]

def dörr():
    for i in range(1, 4):
        prin(f"{i}. {rand.choice(dörrar)}")
    while True:
        prin("Vilken dörr vill du välja?")
        val = input("    --> ").lower().replace(" ", "").replace(".", "")
        if val in {"1", "2", "3"}: print("\n    ||----------||\n"); break
        prin(Colors.red + "Du måste skriva antingen 1, 2 eller 3.")
    rand.choice([skapa_monster, skapa_fälla, skapa_kista])()

#--------------------------------------------------------------------------#
#här är funktionen som definerar vad ett moster är och hur en fight kommer att utspela sig baserat på spelaren respektive monstrets styrka

monster_lista = ["Basilisk", "Cyklop", "Zombie", "Troll", "Spöke", "Golem", "Vampyr", "Varulv", "Gorgon", "Skelett", "Mimic", "Slime", "Spindel (Stor)", "Lindorm", "Häxa"]

def skapa_monster():
    weapon_strength = 0
    for item in plr.inventory:
        weapon_strength += item.strength_bonus
    monster = Player()
    monster.level = rand.randint(1, plr.level+5)
    monster.strength = rand.randint(plr.level+3, round(plr.strength + weapon_strength/2)+5)
    prin(f"""Du har träffat ett monster!!
    Namn: {rand.choice(monster_lista)}
    Level: {monster.level}
    Styrka: {monster.strength}
    ...ni börjar slåss...""")
    if monster.strength == plr.strength + weapon_strength:
        prin(Colors.yellow + "Ni slogs hårt och länge men var lika starka så ingen vann. \n    Efter ett långt slagsmål drar du dig iväg utan stor skada.")
    elif monster.strength > plr.strength + weapon_strength:
        prin(f"{Colors.red}Efter en kort fight krossades du av monstret. Ditt hp är nu {plr.hp-1}.")
        plr.hp -= 1
    else:
        prin(f"{Colors.green}Du kämpade hårt och lyckades äntligen ta kol på det förbaskade monstret!\n    Din level gick upp till {plr.level+1}!")
        plr.level += 1
        plr.poäng += 1

#--------------------------------------------------------------------------#
#här är en funktion för  och de olika senariosarna som han hända, dvs förlora 1 liv, förlora 1 item eller komma undan,

def skapa_fälla():
    match rand.randint(1, 3):
        case(1): prin(f"{Colors.red}Du blev fångad i en fälla!\n    Ditt hp gick ner till {plr.hp-1}"); plr.hp -= 1
        case(2): prin(Colors.green + "Du blev nästan fångad i en fälla, men kom snabbt undan!")
        case(3): 
            if len(plr.inventory) > 0:
                prin(Colors.red + "En fälla tog ditt senaste item!")
                print_item(plr.inventory[len(plr.inventory)-1])
                prin(Colors.red + "har försvunnit!")
                del plr.inventory[len(plr.inventory)-1]
            else:
                prin(Colors.yellow + "En fälla försökte ta ditt senaste item, men du är fattig!")
                
#--------------------------------------------------------------------------#             
#här är vapen/inventory/kist funktionen, där man kan plocka upp 5 vapen och om man hittar fler får man välja att byta ut ett vapen mot ett annat.

vapen = ["Skymningsklingan", "Eldpilbåge", "Frostspira", "Åskhammaren", "Drakens ande", "Mörkets dolk", "Solglansen", "Stjärnfallssvärdet", "Havets hämnd", "Jordbrytaren", "Luftvirket", "Skuggornas spjut", "Eldtungan", "Kristallkastaren", "Månstrålesvärdet", "Dimslöparen", "Blodmånen", "Tidsförvrängaren", "Själssläckaren", "Natthärjaren"]

def skapa_kista():
    item = Item(rand.choice(vapen), rand.randint(1, 3))
    if len(plr.inventory) < 5:
        prin(Colors.green + "Du har hittat ett item!\n    Eftersom ditt inventory inte är fullt läggs det i ditt inventory!")
        print_item(item)
        plr.inventory.append(item)
    else:
        prin(Colors.yellow + "Ditt inventory är fullt! Vill du byta ut något för det du hittade?")
        prin("Här är itemet du hittade:")
        print_item(item)
        prin("\n    Här är ditt inventory, skriv 1, 2, 3, 4 eller 5 för det item du vill byta ut.\n    Om du inte vill byta ut något, skriv 6.")
        for i in range(5):
            prin(f"{i+1}.")
            print_item(plr.inventory[i])
            print()
        while True:
            val = input("    --> ").replace(" ", "").replace(".", "")
            match(val):
                case("1" | "2" | "3" | "4" | "5"):
                    prin(Colors.yellow + "Dina items byttes ut.")
                    plr.inventory[int(val)-1] = item; break
                case("6"):
                    prin("Ingenting hände."); break
                case(_): prin(Colors.red + "> Du måste skriva 1, 2, 3, 4, 5 eller 6.")


#--------------------------------------------------------------------------#
#Här är en introduktion/tutorial till spelet.
print("Välkommen till vårat äventyrsspel, gjort av Simon Remle, Emelie Gyllenberg och Daniel Furo.")

while True:
    fråga = input("    Vill du ha en spel tutorial? (ja/nej) --> ").lower().replace(".", "").replace(" ", "")
    if not fråga in {"ja", "nej"}:
        prin(Colors.red + "> Du måste skriva antingen ja eller nej.")
    elif fråga == "ja":
        prin("""Spelet går ut på att du som modig äventyrare ska ta dig igenom olika rum i en håla, besegra moster och hitta skatter. 
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
    else: break


while True:
    if plr.level >= 10 or plr.hp <= 0:
        if endwin() == "stop":
            break
    if plr.poäng > 0:
        poäng()
    main()


    









