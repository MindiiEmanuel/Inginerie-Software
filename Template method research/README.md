Template

Definiție 
Patternul de proiectare Template este un tip de design pattern comportamental care definesc schelete pentru algoritmi într-o metodă și îi lasă implementarea anumitor pași să fie furnizată de subclase. Acest pattern este utilizat pentru a stabili un schelet pentru o anumită operație și pentru a permite subclaselor să modifice anumite pași ai acestei operații fără a schimba structura generală a acesteia.
Principalele componente ale patternului Template includ:
1.	Metodă Template (Template Method):
Definește scheletul algoritmului într-o metodă, având anumite pași implementați în mod concret și alții lăsați sub formă de stubs (metode fără implementare sau cu implementare implicită).
2.	Metode Concrete (Concrete Methods):
Sunt metodele care implementează pașii specifici în algoritmul general definit de metoda șablon.
3.	Metode Hook (Hook Methods):
Sunt metodele opționale care pot fi suprascrise sau nu de către subclase. Ele permit subclaselor să influențeze sau să extindă comportamentul algoritmului fără a modifica întreaga structură.

Când se folosește?
1.	Structura algoritmului este constantă, dar anumite etape pot varia:
Dacă există o structură generală sau un schelet de algoritm care rămâne constant, dar anumite pași sau detalii pot varia în implementările concrete, atunci patternul Template este util.
2.	Evitarea duplicării de cod:
Atunci când există porțiuni de cod care se repetă în mai multe locuri ale unei ierarhii de clase, Template permite plasarea acestora într-o metodă de șablon, evitând astfel duplicarea.
3.	Permiterea extinderii fără a modifica structura generală:
Template oferă un mod de extindere a unui algoritm fără a modifica structura acestuia. Prin furnizarea de metode "hook", subclasele pot influența sau extinde anumite părți ale algoritmului fără a schimba metoda de șablon însăși.
4.	Definirea unei interfețe la nivel înalt pentru o anumită operație:
Template oferă o interfață sau un contract la nivel înalt pentru o anumită operație, lăsând detaliile specifice subclaselor. Aceasta poate îmbunătăți claritatea și coerența codului.
5.	Crearea unor schelete pentru algoritmi reutilizabili:
Atunci când există necesitatea de a defini o structură de algoritm care poate fi reutilizată în mai multe contexte, Template poate oferi un schelet pe care îl pot urma diferite implementări concrete.

Unde se folosește?
1.	Framework-uri pentru dezvoltarea aplicațiilor:
Multe framework-uri sau biblioteci de dezvoltare a aplicațiilor utilizează patternul Template pentru a oferi o structură de bază sau un schelet pentru diferite componente. Aceasta permite dezvoltatorilor să extindă și să modifice comportamentul fără a schimba structura generală.
2.	Biblioteci grafice și UI:
În dezvoltarea interfețelor grafice sau a bibliotecilor grafice, se pot folosi șabloane pentru a defini modul în care evenimentele, desenarea sau manipularea obiectelor trebuie gestionate. Subclasele pot apoi implementa comportamente specifice.
3.	Gestionarea resurselor și conexiunilor:
În cazul manipulării resurselor (cum ar fi conexiunile la baze de date sau fișiere), se poate utiliza un șablon pentru a defini pașii comuni, cum ar fi deschiderea și închiderea resurselor, iar detaliile specifice pot fi implementate în subclase.
4.	Proiectarea algoritmilor de procesare a datelor:
În contextul prelucrării datelor, patternul Template poate fi folosit pentru a defini pașii comuni ai unui algoritm (cum ar fi citirea datelor, procesarea și salvarea rezultatelor), iar pașii specifici pot fi implementați în subclase.
5.	Metodele de execuție ale unor programe:
În limbaje de programare precum C++, șablonul este adesea folosit în metodele run ale claselor pentru a defini scheletul execuției programului. Subclasele pot apoi să își definească comportamentul specific în cadrul acestei metode.
6.	Generarea de rapoarte sau documente:
În sistemele care generează rapoarte sau documente, patternul Template poate fi folosit pentru a defini structura generală a documentului, iar subclasele pot furniza implementarea detaliată a anumitor secțiuni sau elemente.

De ce se folosește?
•	Reutilizarea codului
•	Definirea unei structuri generale
•	Extensibilitate
•	Claritate și coerență
•	Implementarea detaliilor specifice în subclase
•	Consistență a interfeței
•	Gestionarea pașilor comuni ai algoritmilor
•	Evitarea duplicării de cod

Pro vs cons
Avantaje (Pros) ale Patternului Template:
1.	Reutilizarea Codului
2.	Claritatea și Coerența Codului
3.	Extensibilitate
4.	Consistență a Interfeței
5.	Gestionarea Detaliilor Specifice

Dezavantaje (Cons) ale Patternului Template:
1.	Inflexibilitate în Modificarea Structurii
2.	Clase Cu o Singură Metodă
3.	Probleme de Mentenanță
4.	Riscul de Violare a Încapsulării
5.	Complexitatea Crește cu Numărul de Subclase

Normal vs Risk.
Acest cod folosește modelul Template Pattern prin intermediul claselor abstracte (TensiuneArterialaTemplate și IMCTemplate) și claselor concrete (AplicatieTensiuneArteriala și AplicatieIMC) care implementează aceste șabloane. Iată cum funcționează și de ce se consideră un exemplu de Template Pattern:

Clasa Abstractă - TensiuneArterialaTemplate și IMCTemplate:

Aceste clase abstracte definesc metode abstracte care reprezintă pașii algoritmului general (introdu_valoare_sistolica, calculeaza_diastolica, afiseaza_rezultat_tensiune_arteriala, introdu_inaltimea, introdu_greutatea, calculeaza_imc, afiseaza_rezultat_imc).
Clasa Concretă - AplicatieTensiuneArteriala și AplicatieIMC:

Aceste clase concrete extind clasele abstracte și implementează detaliile specifice ale fiecărui pas al algoritmului.
De exemplu, AplicatieTensiuneArteriala implementează metodele pentru introducerea valorii sistolice, calculul diastolicei și afișarea rezultatelor specifice tensiunii arteriale.
Metoda Template (main):

Funcția main acționează ca o metodă template. Ea conține logica generală a aplicației, inclusiv bucla continuă care permite utilizatorului să aleagă între cele două opțiuni (tensiune arterială sau IMC).
Când utilizatorul alege o opțiune, se creează o instanță a clasei corespunzătoare (AplicatieTensiuneArteriala sau AplicatieIMC) și sunt apelați pașii algoritmului (metodele abstracte) prin intermediul metodelor concrete.
În concluzie, acest cod ilustrează modelul Template Pattern prin separarea logicii generale a aplicației de detaliile specifice ale fiecărui pas al algoritmului în clasele concrete care implementează interfața abstractă. Astfel, se asigură o structură flexibilă și ușor de întreținut pentru extinderea și modificarea funcționalității.
