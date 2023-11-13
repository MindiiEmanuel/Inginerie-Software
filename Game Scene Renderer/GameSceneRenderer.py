import turtle
import random

# Lista pentru a stoca instanțele de cercuri pentru verificarea coliziunilor
lista_cercuri = []

# Definirea clasei de bază Persoana
class Persoana:
    def __init__(self, nume, varsta, inaltime, greutate, iq, abilitati):
        self.nume = nume
        self.varsta = varsta
        self.inaltime = inaltime
        self.greutate = greutate
        self.iq = iq
        self.abilitati = abilitati

# Definirea claselor derivate Om și Elf care mostenesc clasa Persoana
class Om(Persoana):
    def __init__(self, nume, varsta, inaltime, greutate, iq, abilitati):
        super().__init__(nume, varsta, inaltime, greutate, iq, abilitati)

class Elf(Persoana):
    def __init__(self, nume, varsta, inaltime, greutate, iq, abilitati):
        super().__init__(nume, varsta, inaltime, greutate, iq, abilitati)

# Definirea clasei Continent
class Continent:
    def __init__(self, nume):
        self.nume = nume
        self.case = []  # Lista pentru a stoca instantele de case

    def adauga_casa(self, casa):
        self.case.append(casa)

# Definirea claselor pentru casele specifice fiecarui continent
class Casa:
    def __init__(self, material):
        self.material = material

class CasaCaramida(Casa):
    def __init__(self):
        super().__init__("caramida")

class CasaLemn(Casa):
    def __init__(self):
        super().__init__("lemn")

class CasaStuf(Casa):
    def __init__(self):
        super().__init__("stuf")

# Funcții pentru afișarea opțiunilor de regiune și caracter
def afiseaza_optiuni_regiuni():
    print("Alege regiunea:")
    print("1. Europa")
    print("2. Asia")
    print("3. Africa")

def afiseaza_optiuni_caracter():
    print("Creeaza personajul:")
    print("Alege tipul de caracter:")
    print("1. Om")
    print("2. Elf")

# Funcție pentru a prelua opțiunea utilizatorului
def preia_optiune():
    return input("Selecteaza optiunea ta: ")

# Funcție pentru a prelua o valoare întreagă într-un interval specificat
def preia_valoare_int(mesaj, limita_inferioara, limita_superioara):
    while True:
        try:
            valoare = int(input(mesaj))
            if limita_inferioara <= valoare <= limita_superioara:
                return valoare
            else:
                print(f"Te rog introdu o valoare între {limita_inferioara} și {limita_superioara}.")
        except ValueError:
            print("Te rog introdu o valoare validă.")

# Funcție pentru alegerea abilităților în funcție de tipul de caracter
def preia_abilitati(tip_caracter):
    print("Alege abilitati:")
    if tip_caracter == 1:  # Om
        print("1. Civil")
        print("2. Spadasin")
        print("3. Arcas")
        print("4. Cavaler")
        optiuni_valide = ["1", "2", "3", "4"]
    elif tip_caracter == 2:  # Elf
        print("1. Civil")
        print("2. Inventator")
        print("3. Magician")
        optiuni_valide = ["1", "2", "3"]

    while True:
        abilitate = input("Selecteaza abilitatea ta: ")
        if abilitate in optiuni_valide:
            return abilitate
        else:
            print("Te rog selecteaza o abilitate valida.")

# Funcție pentru crearea personajului în funcție de tipul ales
def creeaza_personaj(tip_caracter):
    nume = input("Nume: ")
    varsta_limita_superioara = 80 if tip_caracter == 1 else 300
    varsta = preia_valoare_int(f"Varsta (1-{varsta_limita_superioara}): ", 1, varsta_limita_superioara)

    if tip_caracter == 1:  # Om
        inaltime = preia_valoare_int("Inaltime (20-200): ", 20, 200)
        greutate = preia_valoare_int("Greutate (3-100): ", 3, 100)
        iq = preia_valoare_int("Iq (70-150): ", 70, 150)
        abilitate = preia_abilitati(tip_caracter)

        return Om(nume, varsta, inaltime, greutate, iq, [abilitate])

    elif tip_caracter == 2:  # Elf
        inaltime = preia_valoare_int("Inaltime (150-180): ", 150, 180)
        greutate = preia_valoare_int("Greutate (3-80): ", 3, 80)
        iq = preia_valoare_int("Iq (100-300): ", 100, 300)
        abilitate = preia_abilitati(tip_caracter)

        return Elf(nume, varsta, inaltime, greutate, iq, [abilitate])

# Funcție pentru desenarea casei pe baza materialelor specificate
def deseneaza_casa(casa):
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

# Funcția principală a jocului
def joc():
    print("Game Scene Renderer")

    # Alegerea regiunii
    afiseaza_optiuni_regiuni()
    optiune_regiune = int(preia_optiune())

    # Crearea personajului în funcție de tipul ales
    afiseaza_optiuni_caracter()
    tip_caracter = int(preia_optiune())
    personaj = creeaza_personaj(tip_caracter)

    # Afișarea caracteristicilor personajului
    print("\nCaracteristici personaj creat:")
    print(f"Nume: {personaj.nume}")
    print(f"Varsta: {personaj.varsta}")
    print(f"Inaltime: {personaj.inaltime}")
    print(f"Greutate: {personaj.greutate}")
    print(f"Iq: {personaj.iq}")
    print(f"Abilitati: {', '.join(personaj.abilitati)}")

    # Crearea instanțelor de continent
    europa = Continent("Europa")
    asia = Continent("Asia")
    africa = Continent("Africa")

    # Adaugarea caselor la fiecare continent
    europa.adauga_casa(CasaCaramida())
    asia.adauga_casa(CasaLemn())
    africa.adauga_casa(CasaStuf())

    # Desenarea hărții cu casele și personajele specificate pentru fiecare regiune
    turtle.speed(2)

    if optiune_regiune == 1:  # Europa
        for casa in europa.case:
            deseneaza_casa(casa)

        # Afisare case galbene (caramida) si personaje
        for _ in range(6):
            turtle.penup()
            turtle.color("yellow")
            turtle.shape("square")
            turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
            turtle.stamp()

        # Afisare nume personaje si abilitati
        for nume, abilitate, culoare in [("Athos", "Spadasin", "blue"), ("Porthos", "Arcas", "blue"),
                                         ("Aramis", "Cavaler", "blue"), ("Caigwyn", "Civil", "green"),
                                         ("Inagwyai", "Inventator", "green"), ("Wynnala", "Magician", "green")]:
            turtle.penup()
            turtle.color(culoare)
            turtle.shape("circle")
            turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
            turtle.goto(turtle.xcor(), turtle.ycor() - 10)
            turtle.write(f"{nume}\nAbilitate: {abilitate}", align="center", font=("Arial", 8, "normal"))
            # Salvează poziția noii instanțe de cerc pentru verificarea coliziunii
            lista_cercuri.append(turtle.clone())

    elif optiune_regiune == 2:  # Asia
        turtle.penup()
        turtle.goto(-150, 0)
        turtle.pendown()
        for casa in asia.case:
            deseneaza_casa(casa)

        # Afisare case maro (lemn) si personaje
        for _ in range(6):
            turtle.penup()
            turtle.color("brown")
            turtle.shape("square")
            turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
            turtle.stamp()

        # Afisare nume personaje si abilitati
        for nume, abilitate, culoare in [("Athos", "Spadasin", "blue"), ("Porthos", "Arcas", "blue"),
                                         ("Aramis", "Cavaler", "blue"), ("Caigwyn", "Civil", "green"),
                                         ("Inagwyai", "Inventator", "green"), ("Wynnala", "Magician", "green")]:
            turtle.penup()
            turtle.color(culoare)
            turtle.shape("circle")
            turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
            turtle.goto(turtle.xcor(), turtle.ycor() - 10)
            turtle.write(f"{nume}\nAbilitate: {abilitate}", align="center", font=("Arial", 8, "normal"))
            # Salvează poziția noii instanțe de cerc pentru verificarea coliziunii
            lista_cercuri.append(turtle.clone())

    elif optiune_regiune == 3:  # Africa
        turtle.penup()
        turtle.goto(150, 0)
        turtle.pendown()
        for casa in africa.case:
            deseneaza_casa(casa)

        # Afisare case gri (lemn) si personaje
        for _ in range(6):
            turtle.penup()
            turtle.color("gray")
            turtle.shape("square")
            turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
            turtle.stamp()

        # Afisare nume personaje si abilitati
        for nume, abilitate, culoare in [("Athos", "Spadasin", "blue"), ("Porthos", "Arcas", "blue"),
                                         ("Aramis", "Cavaler", "blue"), ("Caigwyn", "Civil", "green"),
                                         ("Inagwyai", "Inventator", "green"), ("Wynnala", "Magician", "green")]:
            turtle.penup()
            turtle.color(culoare)
            turtle.shape("circle")
            turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
            turtle.goto(turtle.xcor(), turtle.ycor() - 10)
            turtle.write(f"{nume}\nAbilitate: {abilitate}", align="center", font=("Arial", 8, "normal"))
            # Salvează poziția noii instanțe de cerc pentru verificarea coliziunii
            lista_cercuri.append(turtle.clone())

# Adăugarea personajului jucător pe hartă
personaj = turtle.Turtle()
personaj.shape("circle")
personaj.color("red")
personaj.penup()
personaj.speed(0)

# Definirea funcțiilor de mișcare pentru personajul jucător
def muta_sus():
    y = personaj.ycor()
    personaj.sety(y + 20)
    verificare_coliziune()

def muta_jos():
    y = personaj.ycor()
    personaj.sety(y - 20)
    verificare_coliziune()

def muta_stanga():
    x = personaj.xcor()
    personaj.setx(x - 20)
    verificare_coliziune()

def muta_dreapta():
    x = personaj.xcor()
    personaj.setx(x + 20)
    verificare_coliziune()

# Asocierea funcțiilor de mișcare cu tastatura
turtle.listen()
turtle.onkey(muta_sus, "Up")
turtle.onkey(muta_jos, "Down")
turtle.onkey(muta_stanga, "Left")
turtle.onkey(muta_dreapta, "Right")

# Funcție pentru verificarea coliziunii personajului cu celelalte personaje
def verificare_coliziune():
    for cerc in lista_cercuri:
        if personaj.distance(cerc) < 20:  # Distanta la care consideram coliziunea
            print("Coliziune cu alt personaj!")

# Rularea funcției principale
joc()

# Asigurarea afișării ferestrei până când utilizatorul închide fereastra
turtle.done()
