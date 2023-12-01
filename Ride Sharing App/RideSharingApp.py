import random

class Mediator:
    def __init__(self):
        # Listele pentru a stoca clienți, scutere și mașini
        self.clients = []
        self.scooters = []
        self.cars = []

    def add_client(self, client):
        # Adaugă un client la lista de clienți a mediatorului
        self.clients.append(client)

    def add_scooter(self, scooter):
        # Adaugă un scuter la lista de scutere a mediatorului
        self.scooters.append(scooter)

    def add_car(self, car):
        # Adaugă o mașină la lista de mașini a mediatorului
        self.cars.append(car)

    def request_scooter(self, client, distance):
        # Obține scuterele disponibile care au încărcare suficientă și nu sunt ocupate
        available_scooters = [s for s in self.scooters if s.charge >= distance * 0.5 and not s.busy]
        if available_scooters:
            # Sortează scuterele după distanța față de locația clientului
            sorted_scooters = sorted(available_scooters, key=lambda s: abs(int(s.location[8:]) - client.location))
            # Returnează primele 3 opțiuni sau toate disponibile dacă sunt mai puține
            return sorted_scooters[:min(3, len(sorted_scooters))]
        return None

    def request_car(self, client, distance, comfort):
        # Obține mașinile disponibile care sunt libere și au confortul necesar
        available_cars = [c for c in self.cars if c.status == "free" and c.comfort >= comfort]
        if available_cars:
            # Sortează mașinile după distanța față de locația clientului
            sorted_cars = sorted(available_cars, key=lambda c: abs(int(c.location) - client.location))
            # Returnează primele 3 opțiuni sau toate disponibile dacă sunt mai puține
            return sorted_cars[:min(3, len(sorted_cars))]
        return None

class Client:
    def __init__(self, mediator):
        # Inițializează un client cu o locație aleatoare și fără scuter sau mașină
        self.mediator = mediator
        self.location = random.randint(1, 100)
        self.scooter = None
        self.car = None

    def request_scooter(self, distance):
        while True:
            # Obține opțiunile de scutere disponibile
            options = self.mediator.request_scooter(self, distance)
            if options:
                print("\nScooter options:")
                # Filtrare opțiuni pentru a afișa doar cele cu încărcare peste 50%
                valid_options = [scooter for scooter in options if scooter.charge > 50]
                if valid_options:
                    for i, scooter in enumerate(valid_options, start=1):
                        print(f"{i}. Scooter {scooter.id} at {scooter.location} - Charge: {scooter.charge}%")
                    choice = input("\nYour choice: ")
                    if choice.isdigit():
                        choice = int(choice)
                        if 1 <= choice <= len(valid_options):
                            self.scooter = valid_options[choice - 1]
                            print(f"\nClient received Scooter {self.scooter.id}.")
                            break
                        else:
                            print("Invalid choice. Please choose a valid option.")
                    else:
                        print("Invalid input. Please enter a number.")
                else:
                    print("No available scooters with over 50% charge.")
                    break
            else:
                print("No available scooters.")
                break

    def request_car(self, distance, comfort):
        while True:
            # Obține opțiunile de mașini disponibile
            options = self.mediator.request_car(self, distance, comfort)
            if options:
                print("\nCar options:")
                for i, car in enumerate(options, start=1):
                    print(f"{i}. {car.name} at {car.location} - Comfort: {car.comfort} - Status: {car.status}")
                choice = input("\nYour choice: ")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(options):
                        self.car = options[choice - 1]
                        self.car.status = "busy"
                        print(f"\nClient received {self.car.name}.")
                        break
                    else:
                        print("Invalid choice. Please choose a valid option.")
                else:
                    print("Invalid input. Please enter a number.")
            else:
                print("No available cars.")
                break

class Scooter:
    def __init__(self, id, location):
        # Inițializează un scuter cu un id, locație, încărcare și status
        self.id = id
        self.location = location
        self.charge = random.randint(40, 100)
        self.busy = False

class Car:
    def __init__(self, name, location, comfort):
        # Inițializează o mașină cu un nume, locație, confort și status
        self.name = name
        self.location = location
        self.status = random.choice(["free", "busy"])
        self.comfort = comfort

# Inițializează mediatorul
mediator = Mediator()

# Adaugă obiecte la mediator (scutere și mașini)
for i in range(1, 7):
    mediator.add_scooter(Scooter(i, f"Location{i}"))

mediator.add_car(Car("Dacia Logan", random.randint(1, 100), 1))
mediator.add_car(Car("Volkswagen Passat", random.randint(1, 100), 3))
mediator.add_car(Car("Skoda Octavia", random.randint(1, 100), 2))
mediator.add_car(Car("Dacia Stepway", random.randint(1, 100), 2))
mediator.add_car(Car("Kia xCeed", random.randint(1, 100), 4))
mediator.add_car(Car("Audi A6", random.randint(1, 100), 5))

# Inițializează un client
client = Client(mediator)

# Afișează detalii inițiale (scutere, mașini și locația clientului)
print("Initial Details:")
print("\nScooter details:")
for scooter in mediator.scooters:
    print(f"Scooter {scooter.id} at {scooter.location} - Charge: {scooter.charge}%")
print("\nCar details:")
for car in mediator.cars:
    print(f"{car.name} at {car.location} - Comfort: {car.comfort} - Status: {car.status}")
print("\nClient location:", client.location)

# Permite clientului să aleagă o locație și tipul de transport
location_choice = int(input("\nChoose location:\n1. Location 1\n2. Location 2\n3. Location 3\n4. Location 4\n5. Location 5\n6. Location 6\nYour Choice: "))
if 1 <= location_choice <= 6:
    client.location = location_choice * 20
    print("Updated client location:", client.location)
    transport_choice = int(input("\nChoose mode of transport:\n1. Scooters\n2. Cars\nYour Choice: "))
    if transport_choice == 1:
        client.request_scooter(30)
    elif transport_choice == 2:
        client.request_car(40, 3)
