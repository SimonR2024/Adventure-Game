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

    def __str__(self):
        item_strength, item_hp, item_inv = 0, 0, 0

        for item in plr.inventory:
            item_strength += item.strength_bonus
            item_hp += item.hp_bonus
            item_inv += item.inv_bonus
        
        return (f"""    Här är dina stats:
    Level: {self.level}
    Styrka: {self.strength} +({item_strength})
    Hp: {self.hp} +({item_hp})
    Inventory storlek: 3 +({item_inv})""")


class Item:
    item_lista = []

    def __init__(self, namn, strength_bonus, hp_bonus, inv_bonus):
        self.namn = namn
        self.strength_bonus = strength_bonus
        self.hp_bonus = hp_bonus
        self.inv_bonus = inv_bonus
        self.item_lista.append(self)

a = Item("Widegrens svamp", 0, -2, 0)
b = Item("Fackla", 3, 0, 0)
c = Item("Istapp", 1, -1, 0)
d = Item("Ryggsäck", 0, 0, 2)
e = Item("Mjölner", 4, 0, 0)
f = Item("Drakens ande", 4, 3, 0)
g = Item("Katt (mjaow)", 2, 2, 0)
h = Item("Dammvippan", 1, 1, 0)
i = Item("Suddgummi", 1, 0, 0)
j = Item("P-böter", 0, -1, 0)
k = Item("Guldig delicatoboll", 0, 2, 0)
l = Item("Läderpiska", 2, 0, 0)
m = Item("Första förband", 0, 2, 0)
n = Item("Blyertspenna", 3, 0, 0)
o = Item("Mordisk blick", 1, 0, 0)
p = Item("Levi's byxor", 0, 1, 3)
q = Item("Mattebok", 2, 0, 0)
r = Item("Glasskärva", 2, -1, 0)
s = Item("Spidermanmask", 0, 1, 0)
t = Item("A4 papper", 2, -1, 0)
u = Item("Goon strumpa", 1, -1, 0)
v = Item("Digerdöden", 0, -99, 0)
w = Item("Jespers jawline", 2, -1, 0)
x = Item("Spjut", 2, 0, 0)
y = Item("Mammas sandal", 3, 1, 0)
z = Item("Surt regn", 1, -1, 0)
å = Item("Pappas bälte", 2, 0, 0)
ä = Item("Kappsäck", -1, 0, 2)
ö = Item("Fönsteröppnare", 3, 0, 0)

plr = Player()


def prin(text):
    print("    ", end="")
    for i in text:
        print(i, end="", flush=True)
        time.sleep(0.003)
    print(Colors.reset)


def print_item(item):
    prin(f"""Namn: {item.namn}
    Styrkeboost: {item.strength_bonus}
    Hpboost: {item.hp_bonus}
    Inv-boost: {item.inv_bonus}""")


def plr_inv():
    inv_size = 3
    for item in plr.inventory:
        inv_size += item.inv_bonus
    return inv_size


def plr_hp():
    hp = plr.hp
    for item in plr.inventory:
        hp += item.hp_bonus
    return hp
    

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
    if plr_hp() <= 0:
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
        if val in {"1", "2", "3"}: 
            print("\n    ||----------||\n"); break
        
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
    monster.strength = rand.randint(plr.level+4, round(plr.strength + weapon_strength/2)+plr.level+5)
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
#Här är en funktion för  och de olika senariosarna som han hända, dvs förlora 1 liv, förlora 1 item eller komma undan,

def skapa_fälla():
    match rand.randint(1, 3):
        case(1): prin(f"{Colors.red}Du blev fångad i en fälla!\n    Ditt hp gick ner till {plr.hp-1}"); plr.hp -= 1
        case(2): prin(Colors.green + "Du blev nästan fångad i en fälla, men kom snabbt undan!")
        case(3): 
            if len(plr.inventory) == 0:
                prin(Colors.yellow + "En fälla försökte ta ditt senaste item, men du är fattig!")
            else:
                prin(Colors.red + "En fälla tog ditt senaste item!")
                print_item(plr.inventory[len(plr.inventory)-1])
                prin(Colors.red + "har försvunnit!")
                del plr.inventory[len(plr.inventory)-1]
                
                while len(plr.inventory) > plr_inv():
                    prin(Colors.red + "> Du har för många items i ditt inventory!")
                    prin(f"{Colors.red}> {len(plr.inventory) - plr_inv()} items tas bort.")
                    
                    for i in range(len(plr.inventory) - plr_inv()):
                        del plr.inventory[len(plr.inventory-i-1)]


#--------------------------------------------------------------------------#             
#här är vapen/inventory/kist funktionen, där man kan plocka upp vapen och om man hittar många får man välja att byta ut ett vapen mot ett annat.

def skapa_kista():
    item = rand.choice(Item.item_lista)
    
    if len(plr.inventory) < plr_inv():
        prin(Colors.green + "Du har hittat ett item!\n    Eftersom ditt inventory inte är fullt läggs det i ditt inventory!")
        print_item(item)
        plr.inventory.append(item)
    else:
        prin(Colors.yellow + "Ditt inventory är fullt! Vill du byta ut något för det du hittade?")
        prin("Här är itemet du hittade:")
        print_item(item)
        prin("\n    Här är ditt inventory, skriv numret för det item du vill byta ut.\n    Om du inte vill byta ut något, skriv 0.")
        
        for i in range(plr_inv()):
            prin(f"{i+1}.")
            print_item(plr.inventory[i])
            print()
        
        while True:
            try:
                val = int(input("    --> "))
                if val == 0:
                    prin(Colors.yellow + "Ingenting hände."); break
                elif val in range(plr_inv()+1):
                    prin(Colors.yellow + "Dina items byttes ut.")
                    plr.inventory[val-1] = item; break
                else:
                    prin(f"{Colors.red}> Du måste skriva ett tal mellan 0 och {plr_inv()}.")
            except ValueError:
                prin(Colors.red + "> Du måste skriva ett positivt heltal.")


#--------------------------------------------------------------------------#
#Här är en introduktion/tutorial till spelet.

print("Välkommen till vårat äventyrsspel, gjort av Simon Remle, Emelie Gyllenberg och Daniel Furo.")

while True:
    fråga = input("    Vill du ha en spel tutorial? (ja/nej) --> ").lower().replace(".", "").replace(" ", "")
    if not fråga in {"ja", "nej"}:
        prin(Colors.red + "> Du måste skriva antingen ja eller nej.")
    elif fråga == "ja":
        prin("""Spelet går ut på att du som modig äventyrare ska ta dig igenom olika rum i en håla, besegra moster och hitta skatter. 
    När nivå 10 uppnås vinner du spelet.
    Du väljer att gå in i en dörr genom att trycka 1, däreter får du välja mellan tre olika dörrar genom att trycka 1,2 eller 3.
    De olika dörrarna kan leda till olika rum, ett rum som har ett moster som du ska försöka besegra, ett annat har en fälla och det tredje har en skatt.
    När du slåss emot monster kan två olika grejer att hända; 
    1: du besegrar mostret och går upp en level 
    2: du förlorar mot mostret och förlorar 1 liv. 
    Den som vinner avgörs av den som har mest styrke poäng.
    Om du har otur går du in i ett rum med en fälla, fällan kan skada dig och ta 1 liv, den kan även ta en sak från ditt inventory eller kan du smita utan att ta skada.
    Om du hittar en skatt kan den bestå av olika föremål, saker som ger dig yttligare styrka, mer liv eller ger mer plats i inventoryt.

    Du kan max ha 3 saker i ditt inventory, varje sak har en styrkebonus, hpbonus eller inventorybonus som läggs samman i dina stats. 
    Du kan kolla dina stats genom att tycka 2, och du kollar ditt inventory genom att trycka 3. 
    Om du har för många saker i ditt inventory så måste du välja ett att slänga, detta kommer att påvrka dina sammanlagda stats, så välj noga!

    Lycka till på ditt äventyr!! :D
    """); break
    else: break


while True:
    if plr.level >= 10 or plr_hp() <= 0:
        if endwin() == "stop":
            break
    if plr.poäng > 0:
        poäng()
    main()


    









