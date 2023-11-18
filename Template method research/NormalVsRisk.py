from abc import ABC, abstractmethod

# Clasa abstractă pentru Tensiunea Arterială
class TensiuneArterialaTemplate(ABC):
    @abstractmethod
    def introdu_valoare_sistolica(self):
        pass

    @abstractmethod
    def calculeaza_diastolica(self, sistolica):
        pass

    @abstractmethod
    def afiseaza_rezultat_tensiune_arteriala(self, sistolica, diastolica):
        pass

# Clasa concretă pentru aplicația Tensiune Arterială
class AplicatieTensiuneArteriala(TensiuneArterialaTemplate):
    def introdu_valoare_sistolica(self):
        return int(input("Introdu valoarea sistolica (90-200): "))

    def calculeaza_diastolica(self, sistolica):
        return sistolica / 2 + 10

    def afiseaza_rezultat_tensiune_arteriala(self, sistolica, diastolica):
        print("\nRezultat Tensiune Arteriala:")
        print(f"Tensiune Sistolica: {sistolica} mmHg")
        print(f"Tensiune Diastolica Calculata: {diastolica:.2f} mmHg")

        # Verifică intervalul și afișează rezultatele corespunzătoare
        if 90 <= sistolica <= 140 and 60 <= diastolica <= 80:
            print("\nTensiune Arteriala Normala:")
            print("Riscuri:")
            print(" - Riscuri mai scazute de afectiuni cardiovasculare.")
        elif sistolica < 90 and diastolica < 60:
            print("\nTensiune Arteriala Scăzută (Hipotensiune):")
            print("Riscuri:")
            print(" - Amețeli sau leșin.")
            print(" - Oboseală excesivă.")
            print(" - Dificultăți de concentrare.")
            print(" - Riscuri pentru persoanele cu tensiune arterială scăzută cronică pot include probleme cardiace sau hormonale.")
        elif sistolica >= 150 and diastolica >= 80:
            print("\nTensiune Arteriala Ridicată (Hipertensiune):")
            print("Riscuri:")
            print(" - Risc crescut de afecțiuni cardiovasculare, cum ar fi atacul de cord și accidentul vascular cerebral.")
            print(" - Risc crescut de boli renale.")
            print(" - Risc crescut de boli ale vaselor de sânge.")

# Clasa abstractă pentru IMC
class IMCTemplate(ABC):
    @abstractmethod
    def introdu_inaltimea(self):
        pass

    @abstractmethod
    def introdu_greutatea(self):
        pass

    @abstractmethod
    def calculeaza_imc(self, inaltime, greutate):
        pass

    @abstractmethod
    def afiseaza_rezultat_imc(self, imc):
        pass

# Clasa concretă pentru aplicația IMC
class AplicatieIMC(IMCTemplate):
    def introdu_inaltimea(self):
        return int(input("Înălțimea (50-220): "))

    def introdu_greutatea(self):
        return int(input("Greutatea (30-300): "))

    def calculeaza_imc(self, inaltime, greutate):
        return greutate / (inaltime / 100) ** 2

    def afiseaza_rezultat_imc(self, imc):
        print("\nRezultat IMC:")
        print(f"Indicele de Masă Corporală (IMC): {imc:.2f}")

        # Verifică intervalul și afișează rezultatele corespunzătoare
        if 18.5 <= imc <= 24.9:
            print("\nIMC Normal:")
            print("Riscuri:")
            print(" - Risc mai scăzut de boli cardiovasculare.")
            print(" - Risc redus de afecțiuni asociate greutății.")
        elif imc < 18.5:
            print("\nIMC Subponderal:")
            print("Riscuri:")
            print(" - Oboseală și slăbiciune.")
            print(" - Deficit nutrițional.")
            print(" - Risc crescut de osteoporoză și alte probleme de sănătate.")
        elif 25.0 <= imc <= 29.9:
            print("\nIMC Supraponderal:")
            print("Riscuri:")
            print(" - Risc crescut de boli cardiovasculare.")
            print(" - Risc crescut de diabet de tip 2.")
            print(" - Riscul unor afecțiuni legate de greutate.")
        elif imc >= 30.0:
            print("\nIMC Obez:")
            print("Riscuri:")
            print(" - Risc crescut de boli cardiovasculare, hipertensiune arterială și accident vascular cerebral.")
            print(" - Risc crescut de diabet de tip 2.")
            print(" - Risc crescut de afecțiuni musculo-scheletice și respiratorii.")

# Funcția principală a aplicației
def main():
    while True:
        print("\nNormal vs Risk")
        print("Opțiuni:")
        print("1. Tensiunea Arteriala")
        print("2. IMC (Indicele de masă corporală)")

        optiune = input("Alege opțiunea ta: ")

        if optiune == "1":
            aplicatie_tensiune_arteriala = AplicatieTensiuneArteriala()
            sistolica = aplicatie_tensiune_arteriala.introdu_valoare_sistolica()
            diastolica = aplicatie_tensiune_arteriala.calculeaza_diastolica(sistolica)
            aplicatie_tensiune_arteriala.afiseaza_rezultat_tensiune_arteriala(sistolica, diastolica)
        elif optiune == "2":
            aplicatie_imc = AplicatieIMC()
            inaltime = aplicatie_imc.introdu_inaltimea()
            greutate = aplicatie_imc.introdu_greutatea()
            imc = aplicatie_imc.calculeaza_imc(inaltime, greutate)
            aplicatie_imc.afiseaza_rezultat_imc(imc)
        else:
            print("Opțiune invalidă. Te rog să alegi 1 sau 2.")

if __name__ == "__main__":
    main()

