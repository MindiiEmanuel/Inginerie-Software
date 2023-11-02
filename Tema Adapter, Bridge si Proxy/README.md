Adapter

Definiție
Pattern-ul Adapter este unul dintre cele 23 de modele de proiectare identificate de GOF (Gang of Four) și este folosit pentru a conecta două interfețe incompatibile. Acesta convertește interfața unei clase în alta interfață pe care clientul o așteaptă. În acest fel, se permite colaborarea între clase cu interfețe diferite.
Când folosim Adapter?
•	Atunci când trebuie să conectăm o componentă nouă la o aplicație existentă cu interfețe incompatibile.
•	Când avem nevoie să folosim o clasă existentă, dar interfața acesteia nu se potrivește cu cea de care avem nevoie.
•	Pentru a permite colaborarea între clase care nu pot lucra împreună din cauza interfețelor incompatibile.
•	Este util în situațiile în care dorim să reutilizăm o clasă existentă, dar nu putem face modificări la aceasta pentru a se potrivi cu cerințele actuale. 
Unde se folosește Adapter?
•	Integrarea componentelor software existente care au interfețe incompatibile.
•	Crearea unor module software independente care trebuie să interacționeze cu alte module existente.
•	În proiectarea orientată pe obiecte, pentru a permite comunicarea între clase cu interfețe diferite.
•	În programarea hardware, pentru a permite conectarea dispozitivelor cu interfețe incompatibile.
•	În dezvoltarea aplicațiilor web, pentru a permite integrarea diferitelor servicii și API-uri cu interfețe diferite.
•	În dezvoltarea jocurilor, pentru a facilita comunicarea între diferite componente ale jocului.
De ce se folosește Adapter?
•	Integrarea: Adapterul facilitează integrarea componentelor software existente care au interfețe incompatibile sau diferite.
•	Reutilizarea: Prin intermediul adapterului, se pot reutiliza componente vechi cu interfețe neactualizate.
•	Flexibilitate: Utilizarea adapterului face ca adăugarea și schimbarea componentelor într-un sistem să fie mai flexibilă, deoarece se pot adapta la interfețe deja existente.
•	Extensibilitate: Adapterul permite adăugarea de noi funcționalități sau comportamente la interfețe existente fără a afecta codul sursă existent.
•	Conectivitate: Este utilizat pentru conectarea dispozitivelor hardware sau software cu interfețe incompatibile, permițându-le să comunice și să lucreze împreună.
•	Simplificarea complexității: Prin intermediul adapterului, se poate simplifica interacțiunea și comunicarea între componente sau module care au interfețe diferite.
Avantaje:
•	Reutilizarea componentelor existente: Adapterul permite reutilizarea componentelor cu interfețe neactualizate într-un mediu nou fără a afecta funcționalitatea acestuia.
•	Flexibilitate: Folosind adapterul, este posibilă adăugarea de noi funcționalități sau comportamente la interfețele existente fără a modifica codul sursă.
•	Extensibilitate: Adapterul permite extinderea funcționalității aplicațiilor fără a afecta codul deja existent.
•	Interoperabilitate: Folosind adapterul, se poate asigura interacțiunea între componente sau sisteme cu interfețe diferite sau incompatibile.
Dezavantaje:
•	Complexitate: Utilizarea adapterului poate introduce un grad suplimentar de complexitate în proiectul software, în special atunci când este necesară gestionarea unor interfețe multiple.
•	Overhead: Adăugarea adapterului poate introduce o anumită penalizare de performanță, deoarece implică adăugarea unui strat intermediar suplimentar între componente.
•	Dependență: Adapterul poate duce la crearea unei dependențe între componente care pot complica testarea și întreținerea sistemului.
•	Dificultatea de înțelegere: Utilizarea unui număr mare de adaptoare într-un proiect poate face dificilă înțelegerea fluxului de date și interacțiunile între componente.

Bridge

Definiție
Bridge este un design pattern structural care permite separarea unei ierarhii de clase în două ierarhii separate - o ierarhie de abstractizare și o ierarhie de implementare. Acesta promovează încapsularea, agregarea și delegarea pentru a permite modificări fără a afecta alte clase din aceeași ierarhie. Ideea din spatele acestui pattern este de a separa o clasă mare sau o interfață care are mai multe responsabilități în clase separate care se pot modifica independent unul de celălalt.
Principalele componente sunt: Abstracțiunea, Implementarea și Rafinarea abstracției. 
Când folosim Bridge?
•	Când dorim să evităm legarea permanentă între implementare și abstracțiune.
•	Când o modificare în abstracție ar trebui să afecteze doar abstracția, fără a afecta implementarea.
•	Când dorim să extindem o clasă în mai multe dimensiuni independente.
•	Când dorim să evităm o ierarhie extinsă a claselor în favoarea unei ierarhii de obiecte mai mici și mai simple.
Unde se folosește Bridge?
•	Când avem o ierarhie de clase și dorim să evităm o legătură permanentă între implementare și abstractizare.
•	Când o schimbare într-o clasă ar trebui să afecteze doar clasa respectivă, fără a afecta alte clase.
•	Când dorim să extindem o clasă în două dimensiuni independente.
•	Când evităm o ierarhie de clasă mare și complexă în favoarea unei ierarhii mai simple și mai ușor de gestionat.
De ce se folosește Bridge?
•	Decuplarea: Bridge permite decuplarea unei abstracții de implementarea sa, permițându-le să evolueze independent. Aceasta înseamnă că modificările într-o parte a ierarhiei nu vor afecta cealaltă parte, permițând o mai mare flexibilitate și extensibilitate în dezvoltare.
•	Extensibilitatea: Bridge facilitează extinderea ierarhiilor de clasă, deoarece noi tipuri de abstracții și implementări pot fi adăugate fără a afecta codul existent. Acest lucru face ca sistemul să fie mai ușor de extins și de gestionat în viitor.
•	Abordare modulară: Prin utilizarea Bridge, putem să avem o abordare modulară a proiectării software, permițând ca componentele sistemului să fie modificate sau înlocuite fără a afecta întregul sistem. Această abordare modulară poate duce la un design mai clar și mai ușor de înțeles.
•	Reutilizarea codului: Bridge facilitează reutilizarea codului, deoarece o implementare poate fi asociată cu mai multe abstracții. Aceasta promovează principiile dezvoltării software care favorizează reutilizarea și refactorizarea codului.
Avantaje:
•	Separarea completă a interfeței de implementare.
•	Extensibilitatea și flexibilitatea crescute.
•	Decuplarea: Bridge elimină cuplajul strâns dintre abstracție și implementare.
•	Reutilizarea codului: Deoarece o implementare poate fi asociată cu mai multe abstracții, Bridge promovează reutilizarea și refactorizarea codului.
Dezavantaje:
•	Complexitatea suplimentară: Introducerea pattern-ului Bridge poate adăuga complexitate suplimentară proiectului. Dacă nu este utilizat corect, poate duce la creșterea complexității sistemului.
•	Costul suplimentar: Implementarea pattern-ului Bridge poate duce la costuri suplimentare de dezvoltare și de întreținere a sistemului. Aceste costuri trebuie luate în considerare atunci când se decide utilizarea Bridge într-un proiect.
•	Abstracții și implementări suplimentare: Adăugarea de abstracții și implementări suplimentare poate duce la creșterea numărului de clase și interacțiuni în cadrul proiectului, ceea ce poate face sistemul mai greu de gestionat și de înțeles.

Proxy

Definiție
Pattern-ul Proxy este un pattern structural care permite crearea unui obiect intermediar care acționează ca înlocuitor pentru un alt obiect sau pentru o resursă costisitoare. Acesta controlează accesul la obiectul real, permițând efectuarea unor operații suplimentare înainte sau după accesarea acestuia. Astfel, Proxy-ul oferă o reprezentare locală sau un placeholder pentru un obiect din altă parte, cum ar fi un fișier, un obiect complex sau o conexiune la un serviciu.
Când folosim Proxy?
•	Încărcare întârziată (lazy loading) a resurselor costisitoare, cum ar fi imagini sau alte date de pe server, pentru a îmbunătăți performanța aplicațiilor web.
•	Controlul și gestionarea accesului la obiecte sensibile sau restricționate, cum ar fi fișierele sau datele confidențiale.
•	Cache-ul datelor pentru a îmbunătăți performanța și a reduce timpul de acces la resursele recurente.
•	Gestionarea cererilor și monitorizarea obiectelor din sistem, pentru a urmări și înregistra interacțiunile cu acestea.
•	Implementarea accesului la obiecte de la distanță, cum ar fi servicii web sau API-uri externe, pentru a controla cererile și a oferi o interfață simplificată pentru utilizatorii locali.
Unde se folosește Proxy?
•	Încărcarea întârziată a resurselor, cum ar fi imaginile și fișierele multimedia, pentru a optimiza performanța aplicațiilor web.
•	Controlul accesului la obiecte sau informații sensibile, gestionarea permisiunilor și securității într-un sistem.
•	Cache-ul datelor pentru a îmbunătăți performanța prin reducerea timpului de acces la resursele recurente.
•	Redirecționarea cererilor și gestionarea traficului pentru a optimiza resursele și a îmbunătăți performanța.
•	Protejarea unui obiect sau a unei resurse prin oferirea unei interfețe de securitate sau de filtrare a accesului.
De ce se folosește Proxy?
•	Controlul accesului: Proxy-ul poate reglementa și monitoriza accesul la un obiect, permițând sau refuzând anumite cereri în funcție de anumite criterii sau permisiuni.
•	Încărcare întârziată (lazy loading): Acesta poate fi folosit pentru a încărca resursele doar atunci când sunt necesare, reducând astfel timpul de încărcare inițială.
•	Securitatea: Proxy-ul poate adăuga straturi suplimentare de securitate în jurul unui obiect, protejându-l astfel de accesul neautorizat sau utilizarea necorespunzătoare.
•	Cache: Poate fi utilizat pentru a stoca temporar datele, facilitând astfel accesul rapid la resursele comune și reducând cererile repetate către resurse externe.
•	Redirecționarea cererilor: Proxy-ul poate gestiona și redirecționa cererile către servere sau servicii diferite, optimizând astfel traficul și performanța.
Avantaje:
•	Securitate îmbunătățită: Proxy-ul poate oferi un strat suplimentar de securitate, permițând controlul accesului și validarea cererilor înainte de a ajunge la obiectul real.
•	Încărcare întârziată (lazy loading): Proxy-ul poate încărca resursele doar atunci când sunt necesare, economisind astfel resursele sistemului și îmbunătățind timpul de răspuns al aplicației.
•	Gestionarea și controlul accesului la resurse: Proxy-ul poate gestiona accesul la resursele critice și poate oferi o interfață de securitate pentru a valida cererile și a bloca accesul neautorizat.
•	Cache: Poate oferi un mecanism de cache pentru a stoca date temporare și a îmbunătăți astfel performanța prin reducerea cererilor repetate către resurse externe.
Dezavantaje:
•	Complexitatea suplimentară: Utilizarea unui Proxy poate adăuga complexitate în codul unei aplicații, ceea ce poate duce la o gestionare mai dificilă și la o creștere a costurilor de dezvoltare.
•	Overhead suplimentar: Proxy-ul poate adăuga un overhead suplimentar în timpul de execuție al aplicației, deoarece există un strat intermediar între client și obiectul real, ceea ce poate duce la o scădere a performanței în anumite cazuri.
•	Puncte unice de eșec: Introducerea unui Proxy poate duce la apariția unor puncte unice de eșec în aplicație, în cazul în care Proxy-ul în sine nu este gestionat sau implementat corespunzător.

