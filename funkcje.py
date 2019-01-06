import random
import time
import sys
from zmienne import *


def game_over():
    pass


def ruch(gdzie):
    if gdzie == 1:
        pass


def walka(mob, gracz, *boss):
    fajto = 1
    tura = 1
    blok = 0
    mana = 0
    super = 0
    jarek_ma_bica = False

    mob.hp = MOB_HP_MAX
    mob.sila = 1

    if gracz.xyz == 11: #jesli walczymy z jarkiem
        mob.hp = 1000
        mob.sila = 3
        jarek_ma_bica = True #zeby nie moc blokowac atakow jarka

    elif gracz.xyz == 10: #jesli walczymy z adriankiem
        mob.hp = 300
        mob.sila = 2

    print("\nWALKA!")

    while fajto: #walka
        if tura%2==1:   #gracz
            wybor = int(input("\nCo robisz? \n1-uderz \n2-blokuj"))
            if wybor == 1:
                atak = gracz.sila * random.randint(GRACZ_ATAK[0], GRACZ_ATAK[1])
                if super:
                    atak += super
                    super = 0
                mob.hp -= atak
                if mob.hp <= 0:
                    fajto = 0
                    print("\nPrzeciwnik pokonany! \nTwoje zdrowie po walce: {} \n".format(gracz.hp))
                    break
                mana += 1
            elif wybor == 2:
                if not jarek_ma_bica:
                    blok = 2
                else:
                    print("Jarek jest zbyt silny aby zablokować jego atak. ")

            else:
                print("???\n")
                continue

        else:   #przeciwnik
            if blok > 0:
                blok -= 1
                print("Przeciwnik zaatakował, ale zablokowałeś cios. ")
            else:
                atak = mob.sila * random.randint(MOB_ATAK[0], MOB_ATAK[1])
                gracz.hp -= atak
                if gracz.hp <= 0 and gracz.xyz == 11:
                    fajto = 0
                    break
                elif gracz.hp <=0:
                    fajto = 0
                    print("POLEGŁEŚ! MIAŁMLAND ZOSTAŁ SKAZANY NA KLĘSKĘ!")
                    time.sleep(5)
                    sys.exit()

        print("\nTwoje zdrowie: {} \nZdrowie przeciwnika: {} ".format(gracz.hp, mob.hp))
        tura += 1

    '''gracz.exp += tura * gracz.lvl * ILE_EXP

    #lvl_up
    while gracz.exp > LVL_UP_XP[gracz.lvl]:
        gracz.lvl_up()
        print("LEVEL UP! Obecny poziom: {} \n".format(gracz.lvl))'''

    return gracz.hp

def szansa_na_sukces(xyz):
    szansa = random.randint(0, 20-xyz)
    if szansa%3==1:
        return True
    else:
        return False


def skrzynia():
    szyfr = [0, 1, 2, 3]
    for x in szyfr:
        szyfr[x] = random.randint(0, 3)

    print("\nWidzisz tajemniczą skrzynię. Jest ona zamknięta, a do jej otwarcia potrzebny jest kod. \n"
          "Na szczęście dwie z czterech cyfr są wpisane, dlatego wystarczy, że odgadniesz dwa. \n"
          "Jest w niej jednak zamontowany skomplikowany mechanizm krasnoludów, który zmienia szyfr po 3 nieudanych próbach otwarcia. \n")
    licznik = 0
    wybor = "tak"
    while wybor=="tak":
        wybor = input("Czy chcesz spróbować zgadnąć kod? (tak/nie) \n")

        if wybor=="nie":
            print("\nWyszedłeś z jaskini, która zaraz po tym zawaliła się. Nie możesz już do niej wrócić. \n")
            print("Powietrze wypełniające jaskinię natchnęło cię wiedzą.\nIntuicja podpowiada Ci, abyś udał się "
                  "na drogę wiodącą do zamku.")
            print("Zadanie: udaj się na drogę do zamku.")
            break
        elif wybor=="prosze_drodzy_tworcy_pokazcie_mi_kod":
            print("Kod: [{}], [{}], [{}], [{}]".format(szyfr[0], szyfr[1], szyfr[2], szyfr[3]))
        else:
            print("Kod: [*], [*], [{}], [{}] \n".format(szyfr[2], szyfr[3]))

        jeden = int(input("Podaj pierwszą cyfrę kodu. \n"))
        dwa = int(input("Podaj drugą cyfrę kodu. \n"))

        if jeden==szyfr[0] and dwa==szyfr[1]:
            print("Gratulacje! Udało Ci się otworzyć skrzynię! \nW środku znalazłeś tajemnicze runy, "
                  "których nie rozumiesz, ale może kiedyś uda ci się je odczytać.")
            ucieczka = input("Nagle czujesz, że ziemia zaczyna drżeć. Jaskinia zaraz się zawali! Uciekasz? (tak/nie) \n")

            if ucieczka=="tak":
                print("Udało Ci się uciec na chwilę przed zawaleniem jaskini. Nie możesz już do niej wrócić. \n")
                print("Powietrze wypełniające jaskinię natchnęło cię wiedzą.\nIntuicja podpowiada Ci, abyś udał się "
                      "na drogę wiodącą do zamku.")
                print("Zadanie: udaj się na drogę do zamku.")
                return True

            else:
                print("\nZamiast uciekać postanowiłeś usiąść i podziwiać spróchniałe dno skrzyni. \n"
                      "Jaskinia zawaliła się. \n"
                      "Nie żyjesz. \n")
                wyjscie = input("Dziękujemy za grę. \n"
                                "Naciśnij ENTER aby zakończyć \n")
                time.sleep(5)
                sys.exit()

        else:
            print("Kod nie działa. \n")


def leczenie(gracz):
    print("Powolnym krokiem wkradasz się do świątyni. Obcy nie są tu mile widziani,\nwięc masz tylko jedną próbę, aby uprosić boga o uzdrowienie.\n")
    print("Twoje hp:", gracz.hp, "/", gracz.hp_max)
    wybor = input("Czy chcesz się pomodlić?(tak/nie)")
    if wybor == 'tak':
        print("Spokojnie siadasz na zimnej posadzce świątyni, gotowy, by w każdej chwili wybiec z budyku.\nNagle słyszysz głos z góry: 'em', 'am', 'olt', brzmią sylaby.\nBóg oczekuje, że ułożysz z nich słowa modlitwy. ")
        sylaby = ['em', 'am', 'olt']
        szansa = 0
        punkty = 0
        while szansa < 5:
            syl =  random.randint(0,2)
            twoj_ruch = input("Podaj sylabę:")
            if twoj_ruch in sylaby and twoj_ruch==sylaby[syl]:
                punkty += 1
                szansa += 1
                print("Wyczuwasz, że bóg jest zadowolony.")
            else:
                print("Bóg jest wściekły!")
                szansa += 1
        if punkty == 0:
            print("Bóg jest zawiedziony twoją modlitwą i w ramach kary, wywołuje rany na twoim ciele")
            gracz.hp -= 10
        elif punkty == 1:
            gracz.hp +=50
            print("Bóg uleczył twoje rany")
        elif punkty == 2:
            gracz.hp += 120
            print("Bóg uleczył twoje rany")
        elif punkty == 3:
            gracz.hp += 250
            print("Bóg uleczył twoje rany")
        elif punkty == 4:
            gracz.hp += 400
            print("Bóg uleczył twoje rany")
        elif punkty == 5:
            gracz.hp = gracz.hp_max
        if gracz.hp > gracz.hp_max:
            gracz.hp = gracz.hp_max
        punkty = 0
        szansa = 0
        print("Wściekły kapłan wyrzuca Cię za profanację")
    else:
        print("Wściekły kapłan wyrzuca Cię za profanację")

