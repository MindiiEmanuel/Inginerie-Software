# Inginerie-Software
Singleton

I.	 Definiție
Singleton este un șablon de proiectare software care este folosit pentru asigura că o clasă are doar o instanță și că există un punct global de acces. Ideea de bază este de a permite o singură instanță a unei clase să existe în întregul ciclu de viață al unei aplicații și este util deoarece ajută ca aceeași resursă pentru mai multe obiecte. În singleton constructorul este privat așadar obiectul nu poate fi instanțiat în afara obiectului. Acest pattern este folosit adesea în situații în care este important să avem un punct centralizat de control
II.	Când folosim Singleton?
Singleton-ul este folosit în situații în care avem nevoie de o singură instanță a unei clase care să fie disponibilă în întreaga aplicație.
III.	Unde se folosește Singleton?
1.	Gestionarea conexiunii la baza de date
2.	Managerul de fișiere de configurare:
3.	Obiecte de tip cache
4.	Obiecte de tip registru
5.	Logger
IV.	De ce se folosește Singleton?
Singleton-ul este utilizat în programare pentru a asigura că o anumită clasă are o singură instanță și că toate apelurile ulterioare către acea clasă vor fi îndreptate către aceeași instanță. Astfel, Singleton-ul facilitează accesul global la o anumită instanță a unei clase și coordonează acțiunile între diferite părți ale unei aplicații.
V.	Avantaje:
1.	Controlul asupra instanței: Asigură că o clasă are o singură instanță, ceea ce poate fi util în situații în care este necesară o coordonare strictă a acțiunilor.
2.	Acces global ușor: Oferă acces global la instanța respectivă, permițând apeluri simple din întreaga aplicație.
3.	Utilizare eficientă a resurselor: Împiedică crearea mai multor instanțe, ceea ce poate duce la o utilizare ineficientă a resurselor.
4.	Creșterea performanței: Poate contribui la creșterea performanței, deoarece obiectul Singleton este creat o singură dată și este reutilizat în întreaga aplicație.
VI.	Dezavantaje:
1.	Crearea cuplajelor strânse: Poate duce la crearea unor cuplaje strânse între clase, ceea ce face codul mai greu de testat și de întreținut.
2.	Dificultatea extinderii: Extinderea unui Singleton poate fi dificilă, deoarece necesită modificări la nivelul clasei Singleton și poate afecta alte părți ale aplicației.
3.	Probleme de concurență: Implementările slabe ale Singleton-ului pot duce la probleme de concurență într-o aplicație cu fire multiple, deoarece mai multe fire pot încerca să acceseze și să modifice instanța Singleton în același timp.
VII.	Cazuri Speciale:
1.	Singleton leneș (Lazy Singleton): Această abordare implică amânarea creării instanței până în momentul în care este necesară prima dată. Aceasta poate îmbunătăți performanța în cazul în care crearea instanței este costisitoare sau consumatoare de resurse.
2.	Singleton sincronizat: Pentru aplicațiile care utilizează fire multiple și necesită o instanță Singleton, se poate utiliza o implementare sincronizată a Singleton-ului pentru a evita problemele de concurență. Acest lucru asigură că mai multe fire nu pot accesa simultan instanța Singleton.
3.	Singleton dublu blocat (Double Checked Singleton): Acesta este o variantă a Singleton-ului sincronizat, care verifică dacă instanța a fost deja creată înainte de a bloca resursele. Acest lucru poate îmbunătăți performanța în cazul aplicațiilor cu un număr mare de fire.
4.	Singleton static: În limbaje de programare precum Java, Singleton-ul poate fi implementat folosind variabile și blocuri statice pentru a asigura că instanța este creată o singură dată. Aceasta elimină nevoia de gestionare manuală a Singleton-ului.
5.	Singleton cu inițializare pe thread-uri: Aceasta este o abordare specializată a Singleton-ului care se asigură că fiecare fir primește o instanță Singleton separată. Este utilă în anumite situații în care fiecare fir necesită o instanță Singleton independentă.
