class Kalkulaator:      #Klassi Kalkulaator loomine
    def liida(self, a, b):      #Funktsiooni liida defineerimine
        return a + b      #Mida programm väljastab funktsiooniga
    def lahuta(self, a , b):      #Funktsiooni lahuta defineerimine
        return a - b      #mida programm väljastab funktsiooniga
    def korruta(self, a, b):      #Funktsiooni korruta defineerimine
        return a * b      # mida programm väljastab funktsiooniga
    def jaga(self, a, b):      #Funktsiooni jaga defineerimine
        if b == 0:      #Tingimuslause, kui B=0, siis väljastab järgmise rea stringi
            return "Viga: Nulliga jagamine ei ole lubatud! "
        return a / b      #mida programm väljastab funktsiooniga
    def astenda(self, a, b):     #Funktsiooni astenda defineerimine
        return a ** b     #Mida programm väljastab funktsiooniga
    def ruutjuur(self, a):     #Funktsiooni ruutjuur defineerimine
        if a < 0:     #Tingimuslause, kui sisestatud arv on nullist väiksem, siis väljastab järgmise rea stringi
            return "Viga: Negatiivse arvuga ruutjuurt ei saa arvutada! "
        
oliver_kalkulaator = Kalkulaator()     #Kalkulaatori objekt

while True:     #Lõputu tsükkel kasutajaliidese loomiseks
    print("1: Liida")
    print("2: Lahuta")
    print("3: Korruta")
    print("4: Jaga")
    print("5: Astenda")
    print("6: Ruutjuur")
    print("7: Välju")
    
    valik = int(input("Vali tegevus: "))
#Veendumine, et kasutaja valis kehtiva valiku    
    if valik in (1, 2, 3, 4, 5, 6, 7):
        if valik == 7:     #Katkestab tsükkli
            break     #Lõpetab programmi
        if valik == 6:     #Katkestab tsükkli
            arv = int(input("Sisesta arv: "))
            print(arv, "ruutjuur on", oliver_kalkulaator.ruutjuur(arv))
        else:     #Kui kasutaja valik ei ole 6 ega 7, siis läheb tsükkel edasi
            arv1 = int(input("Sisesta esimene arv: "))     #Küsib kasutajalt esimese arvu
            arv2 = int(input("Sisesta teine arv: "))     #Küsib kasutajalt teise arvu
            
            if valik == 1:     #Kontrollib kasutaja tegevust ja lõpetab tsükkli kui tarvis
                print(arv1, "+", arv2, "=", oliver_kalkulaator.liida(arv1, arv2))     #Väljastab ekraanile esimese ja teise arvu läbi liida funktsiooni
            elif valik == 2:     #Kontrollib kasutaja tegevust ja lõpetab tsükkli kui tarvis
                print(arv1, "-", arv2, "=", oliver_kalkulaator.lahuta(arv1, arv2))     #Väljastab ekraanile esimese ja teise arvu läbi lahuta funktsiooni
            elif valik == 3:     #Kontrollib kasutaja tegevust ja lõpetab tsükkli kui tarvis
                print(arv1, "*", arv2, "=", oliver_kalkulaator.korruta(arv1, arv2))     #Väljastab ekraanile esimese ja teise arvu läbi korruta funktsiooni
            elif valik == 4:     #Kontrollib kasutaja tegevust ja lõpetab tsükkli kui tarvis
                print(arv1, "/", arv2, "=", oliver_kalkulaator.jaga(arv1, arv2))     #Väljastab ekraanile esimese ja teise arvu läbi jaga funktsiooni
            elif valik == 5:     #Kontrollib kasutaja tegevust ja lõpetab tsükkli kui tarvis
                print(arv1, "^", arv2, "=", oliver_kalkulaator.astenda(arv1, arv2))     #Väljastab ekraanile esimese ja teise arvu läbi astenda funktsiooni
    else:     #Kui tegevus ei vasta ühelegi, siis käivitub järgmine rida
        print("Vigane sisend")
                
        
            
                