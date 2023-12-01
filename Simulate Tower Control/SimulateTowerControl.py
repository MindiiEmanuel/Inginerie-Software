import random

# Clasa Mediator care gestionează interacțiunea dintre obiecte
class Mediator:
    def __init__(self):
        # Lista de avioane înregistrate și condițiile meteorologice
        self.airplanes = []
        self.weather = {"visibility": random.randint(50, 100), "wind_speed": random.randint(0, 90)}

    # Metodă pentru înregistrarea unui avion în sistem
    def register_airplane(self, airplane):
        self.airplanes.append(airplane)

    # Metodă pentru verificarea condițiilor de aterizare bazate pe vreme
    def check_landing_conditions(self):
        if self.weather["visibility"] < 75 and self.weather["wind_speed"] > 75:
            print("Imposibilitate de aterizare. Vreme nefavorabilă.")
            print("Dirijare spre cel mai apropiat aeroport.")
            return False
        else:
            print("Posibilitate de aterizare. Vreme favorabilă.")
            return True

    # Metodă pentru a ateriza avioanele înregistrate
    def land_airplanes(self):
        for airplane in self.airplanes:
            if self.check_landing_conditions():
                airplane.land()

# Clasa care reprezintă un avion
class Airplane:
    def __init__(self, name):
        self.name = name
        self.technical_issues = random.choice([True, False])
        self.fuel_level = random.randint(20, 100)
        self.distance_to_airport = random.randint(10, 100)

    # Metodă pentru a ateriza avionul
    def land(self):
        print(f"{self.name} avion în raza Aeroportului")

# Funcție pentru generarea de avioane
def generate_airplanes():
    airplane_names = ["Airbus a350", "Boeing 737", "Boeing 787", "Boeing 777", "Embraer e190"]
    airplanes = [Airplane(name) for name in airplane_names]
    return airplanes

# Funcție pentru afișarea informațiilor despre avion
def display_airplane_info(airplane, index):
    issues = "Cu probleme tehnice." if airplane.technical_issues else "Fără probleme tehnice."
    time_to_land = (index - 1) * 15  # Timpul estimat de aterizare în minute
    print(f"{index}. {airplane.name} cu distanța de {airplane.distance_to_airport} km, "
          f"combustibil {airplane.fuel_level}%, {issues}, Aterizare acceptată în {time_to_land} min.")

# Funcția principală a programului
def main():
    tower_control = Mediator()

    print("Air Traffic Control Simulator")
    print(f"Vizibilitate: {tower_control.weather['visibility']}%, Vânt: {tower_control.weather['wind_speed']} km/h")

    # Verificarea condițiilor meteorologice pentru posibilitatea de aterizare
    if tower_control.weather["visibility"] < 75 and tower_control.weather["wind_speed"] > 75:
        print("Imposibilitate de aterizare. Vreme nefavorabilă.")
        print("Dirijare spre cel mai apropiat aeroport.")
    else:
        # Generarea avioanelor și înregistrarea lor în sistem
        airplanes = generate_airplanes()
        for airplane in airplanes:
            tower_control.register_airplane(airplane)

        # Aterizarea avioanelor înregistrate
        tower_control.land_airplanes()

        # Afisarea avioanelor înregistrate și solicitarea utilizatorului pentru sortare
        print("\nAvioane în raza turnului care cer să aterizeze:")
        for index, airplane in enumerate(airplanes, start=1):
            display_airplane_info(airplane, index)

        user_decision = input("Sortare priorități de aterizare avioane? (y/n): ")
        if user_decision.lower() == 'y':
            # Sortarea avioanelor în funcție de criterii specifice
            print("\nTopul de aterizare:")
            sorted_airplanes = sorted(
                airplanes,
                key=lambda x: (
                    not x.technical_issues,
                    x.fuel_level < 5,
                    x.technical_issues and x.fuel_level < 5,
                    x.distance_to_airport
                )
            )
            for index, airplane in enumerate(sorted_airplanes, start=1):
                display_airplane_info(airplane, index)

# Verificare dacă scriptul este executat direct
if __name__ == "__main__":
    main()
