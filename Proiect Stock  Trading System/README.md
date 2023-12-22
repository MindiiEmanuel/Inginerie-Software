Singleton Pattern:
Utilizare: Se asigură că o clasă are o singură instanță și oferă un punct de acces global la această instanță.
Exemplu: User clasă folosește Singleton Pattern pentru a avea o singură instanță a utilizatorului autentificat.
 
Memento Pattern:
Utilizare: Captura stării interne ale unui obiect fără a dezvălui detaliile interne și permite restaurarea ulterioară a stării.
Exemplu: AuthMemento este folosit pentru a salva și restaura starea utilizatorului.
 
Observer Pattern:
Utilizare: Definește o relație unu-la-mulți între obiecte, astfel încât atunci când un obiect se schimbă starea, toți dependenții să fie notificați și actualizați automat.
Exemplu: Clasele TransactionObserver, SearchObserver, BuyObserver, și SellObserver sunt observatori care reacționează la evenimente de tranzacție.
 
 
Fac o trecere detaliată a fiecărei părți a codului.
Clasa AuthMemento:
Scop: Această clasă este parte a pattern-ului de Memento și are rolul de a stoca starea unui obiect User într-un moment dat.
Metode: __init__(self, user): Constructorul primește un obiect user și stochează informațiile relevante într-o instanță Memento.
Clasa User:
Scop: Această clasă implementează Singleton pattern pentru a asigura existența unei singure instanțe a utilizatorului.
Metode:
•	get_instance(cls): Metoda de clasă pentru a obține instanța utilizatorului (Singleton).
•	__init__(self): Constructorul inițializează proprietățile utilizatorului.
•	reset_authentication(self): Resetează starea de autentificare a utilizatorului.
•	create_memento(self): Creează un obiect AuthMemento pentru starea curentă a utilizatorului.
•	restore_from_memento(self, memento): Restaurează starea utilizatorului la cea stocată într-un obiect AuthMemento.
•	add_to_portfolio(self, stock_name, stock_symbol, quantity, price): Adaugă o tranzacție în portofoliu.
•	display_portfolio(self): Afișează portofoliul utilizatorului.
•	sell_transaction(self, transaction): Realizează o tranzacție de vânzare.
•	Alte metode auxiliare pentru funcționalitățile specifice.
Clasa TransactionHistory:
Scop: Această clasă gestionează istoricul tranzacțiilor.
Metode:
•	add_transaction(self, event): Adaugă un obiect TransactionEvent în istoric.
•	display_history(self): Afișează istoricul tranzacțiilor utilizatorului.
Clasa TransactionEvent:
Scop: Această clasă reprezintă un eveniment de tranzacție, folosit în istoric și pentru a notifica observatorii.
Atribute:
•	action: Tipul de acțiune (cumpărare sau vânzare).
•	stock_name: Numele stocului.
•	stock_symbol: Simbolul stocului.
•	quantity: Cantitatea tranzacționată.
•	price: Prețul tranzacției.
•	timestamp: Timestamp-ul tranzacției.
Clasa TransactionObserver:
Scop: Această clasă definește o interfață pentru observatori.
Metode: update(self, event): Metodă care va fi implementată de clasele concrete ale observatorilor.
Clasa TransactionManager:
Scop: Această clasă gestionează observatorii și notifică acești observatori despre evenimentele de tranzacții.
Metode:
•	add_observer(cls, observer): Adaugă un observator în listă.
•	remove_observer(cls, observer): Elimină un observator din listă.
•	notify_observers(cls, event): Notifică toți observatorii despre un eveniment de tranzacție.
Clasa StockListCommand:
Scop: Această clasă gestionează comanda pentru a afișa lista de stocuri disponibile.
Atribute: _stocks: Dicționar care conține informații despre stocurile disponibile.
Clasa SearchCommand:
Scop: Această clasă gestionează comanda de căutare a stocurilor.
Metode: execute(self, transaction_manager): Implementează logica comenzii de căutare.
Clasa SearchObserver:
Scop: Această clasă reprezintă un observator pentru acțiunile de căutare.
Clasa BuyObserver:
Scop: Această clasă reprezintă un observator pentru acțiunile de cumpărare.
Clasa SellObserver:
Scop: Această clasă reprezintă un observator pentru acțiunile de vânzare.
Clasa TradingCommand:
Scop: Această clasă gestionează comanda de tranzacționare (cumpărare și vânzare).
Metode:
•	sell_transaction(self, transaction_manager): Implementează logica pentru tranzacția de vânzare.
•	buy_transaction(self): Implementează logica pentru tranzacția de cumpărare.
•	is_valid_strategy(self, strategy_sl): Verifică dacă strategia introdusă în tranzacție este validă.
Clasa HistoryCommand:
Scop: Această clasă gestionează comanda pentru afișarea istoricului tranzacțiilor.
Funcția main:
Scop: Funcția principală care inițializează obiecte, adaugă observatori, și gestionează logica principală a interacțiunii cu utilizatorul.
