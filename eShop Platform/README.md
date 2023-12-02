eShop Platform

În continuare, voi face o trecere detaliată a fiecărei părți a codului.
1.	Autentificarea și utilizatorii:
Clasa AuthManager gestionează autentificarea utilizatorilor și este implementată folosind un Singleton pattern. Ea are o listă simplă de utilizatori (owner și client) cu parole asociate.
Clasa User reprezintă un utilizator, având un nume de utilizator, un rol (vânzător sau client) și un buget opțional pentru clienți.
2.	Bugetul:
Clasa BudgetFacade furnizează o interfață simplificată pentru gestionarea bugetului. Utilizează metode precum get_budget, add_money și subtract_money pentru a gestiona bugetul și afișează bugetul pentru clienți.
Clasa UserBudget reprezintă bugetul unui client și implementează operațiile de adăugare și scădere de bani.
3.	Stocul:
Clasa Stock reprezintă stocul de produse și are metode pentru afișarea stocului și completarea acestuia.
Clasele StockCompletionStrategy, AutomaticCompletionStrategy și BudgetUpdateStrategy implementează o strategie pentru completarea stocului.
4.	Adăugarea de produse:
Clasa AddProductState reprezintă starea de adăugare a unui nou produs în stoc. Utilizatorul poate introduce diferite comenzi (ID, NAME, PRICE, QUANTITY) pentru a specifica detaliile produsului.
Odată ce utilizatorul alege să salveze (S), produsul este adăugat la stoc.
5.	Acțiunile vânzătorului:
Clasa SellerActions conține metode pentru afișarea stocului, adăugarea de produse, configurarea promoțiilor și afișarea bugetului. Aceasta folosește și strategii pentru completarea stocului.
Interfața SellerInterface și clasele SellerOptions reprezintă strategiile pentru afișarea opțiunilor vânzătorului.
6.	Acțiunile clientului:
Clasa ClientActions conține metode pentru autentificarea clientului, afișarea bugetului, plasarea comenzilor și gestionarea coșului de cumpărături.
Interfața ClientInterface și clasa ClientOptions reprezintă strategiile pentru afișarea opțiunilor clientului.
7.	Meniuri și interfață:
Clasa UserMenu este un context care utilizează strategiile pentru a afișa opțiunile vânzătorului sau clientului.
UserMenu este folosit pentru a afișa meniul și a gestiona interacțiunea cu utilizatorul.
8.	Platforma eShop:
Clasa eShopPlatform este clasa principală care inițializează autentificarea, bugetul, stocul și acțiunile utilizatorilor. Ea rulează aplicația într-un buclă principală, permițând utilizatorilor să aleagă între rolul de vânzător și client.
9.	Rularea aplicației:
La final, se creează o instanță a clasei eShopPlatform și se rulează metoda run() pentru a începe aplicația.
Este important să menționăm că acest cod poate servi drept schelet pentru o aplicație de comerț electronic mai complexă și poate fi extins și personalizat în funcție de cerințe. Este o implementare bine structurată și utilizează diverse concepte de programare orientată pe obiect (OO) și design patterns.

Pattern-urile folosite: 

1.	Singleton Pattern:
Clasa AuthManager este implementată ca un singleton. Acest pattern asigură că există o singură instanță a clasei AuthManager și oferă un punct global de acces la această instanță.
 
2.	Strategy Pattern:
Interfața StockCompletionStrategy și clasele concrete AutomaticCompletionStrategy și BudgetUpdateStrategy implementează un pattern de strategie. Acest pattern permite schimbarea comportamentului la runtime.
Clasa Stock utilizează o strategie pentru a completa stocul, în funcție de alegerea utilizatorului.
 
3.	State Pattern:
Clasa AddProductState implementează un pattern de stare pentru gestionarea diferitelor stări în timpul adăugării unui produs la stoc. Acest pattern permite unui obiect să-și schimbe comportamentul în funcție de starea internă.
 
4.	Observer Pattern:
Deși nu este evident în cod, relațiile între diferitele clase și obiecte, precum BudgetFacade, UserBudget, Stock, SellerActions, și ClientActions, pot să implice un fel de comunicare bazată pe observatori.
