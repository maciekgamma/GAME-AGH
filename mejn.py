from klasy import *
from funkcje import *
from klesty import *
from zmienne import *

print("Witaj w krainie Miałmland.\nRządzi nią okrutny dyktator, którego musisz pokonać. Czy podołasz wyzwaniu?")

wybor = input("Naciśnij ENTER by rozpocząć przygodę! ")
print(" ")

if not wybor == "plmd":
    gracz = Gracz()
    mob = Mob()
    q = 1
    jaskinia = True
    super_moc = False
    print("Na początek udaj się do miasta aby zakupić broń do walki z przeciwnikami.")
    print("Zadanie: udaj się do miasta.")

    while gracz:
        #jesli ciezko ranny to mozliwosc odpoczynku by sie wyleczyc

        if gracz.xyz == 1: #start
            print("Znajdujesz się na starcie.")
            gdzie = input("Możesz udać się na polanę lub na ścieżkę do lasu. Jaka jest twa decyzja? (sciezka/polana) ")
            if gdzie=='polana':
                gracz.xyz = 2
            elif gdzie=='sciezka':
                gracz.xyz = 3
            else:
                print("Nie możesz udać się w to miejsce (sprawdź poprawność pisowni lub opcje przyjść na mapie).")

        elif gracz.xyz == 2: #polana
            if szansa_na_sukces(gracz.xyz) == True and q > 1:
                walka(mob, gracz)
            print("Znajdujesz się na polanie.")

            #quest

            gdzie = input("Możesz udać się do miasta lub na ścieżkę do lasu. Jaka jest twa decyzja? (miasto/sciezka) ")
            if gdzie=='miasto':
                gracz.xyz = 6
            elif gdzie=='sciezka':
                gracz.xyz = 3
            else:
                print("Nie możesz udać się w to miejsce (sprawdź poprawność pisowni lub opcje przyjść na mapie).")

        elif gracz.xyz == 3: #sciezka do lasu
            if szansa_na_sukces(gracz.xyz) == True and q > 1:
                walka(mob, gracz)
            if q == 3:
                q3(gracz)
                q = 4
            print("Znajdujesz się na leśnym trakcie.")
            gdzie = input("Możesz udać się na polanę lub do lasu. Jaka jest twa decyzja? (polana/las) ")
            if gdzie=='polana':
                gracz.xyz = 2
            elif gdzie=='las':
                gracz.xyz = 4
            else:
                print("Nie możesz udać się w to miejsce (sprawdź poprawność pisowni lub opcje przyjść na mapie).")

        elif gracz.xyz == 4: #las
            if szansa_na_sukces(gracz.xyz) == True and q > 2:
                walka(mob, gracz)
            if q == 2:
                q2(gracz)
                q = 3
            print("Znajdujesz się w lesie.")
            gdzie = input("Możesz udać się nad sadzawkę lub na ścieżkę do lasu. Jaka jest twa decyzja? (sadzawka/sciezka) ")
            if gdzie=='sadzawka':
                gracz.xyz = 5
            elif gdzie=='sciezka':
                gracz.xyz = 3
            else:
                print("Nie możesz udać się w to miejsce (sprawdź poprawność pisowni lub opcje przyjść na mapie).")

        elif gracz.xyz == 5: #sadzawka
            if szansa_na_sukces(gracz.xyz) == True and q > 1:
                walka(mob, gracz)
            print("Znajdujesz się nad sadzawką, która niestety wyschła.")
            gdzie = input("Możesz udać się na pola pszenżyta lub do lasu. Jaka jest twa decyzja? (pola/las) ")
            if gdzie=='pola' or gdzie=="pole":
                gracz.xyz = 8
            elif gdzie=='las':
                gracz.xyz = 4
            else:
                print("Nie możesz udać się w to miejsce (sprawdź poprawność pisowni lub opcje przyjść na mapie).")

        elif gracz.xyz == 6: #miasto
            if q == 1:
                q1()
                q = 2
            print("Znajdujesz się w mieście.")
            gdzie = input("Możesz udać się na polanę lub na pola lub do świątyni lub na tajemną drogę. Jaka jest twa decyzja? (polana/pola/swiatynia/droga) ")
            if gdzie=='polana':
                gracz.xyz = 2
            elif gdzie=='pola' or gdzie=="pole":
                gracz.xyz = 8
            elif gdzie=='swiatynia':
                leczenie(gracz)
                print("Twoje hp:", gracz.hp, "/", gracz.hp_max)
                gracz.xyz = 6
            elif gdzie=='droga':
                gracz.xyz = 10
            else:
                print("Nie możesz udać się w to miejsce (sprawdź poprawność pisowni lub opcje przyjść na mapie).")

        elif gracz.xyz == 7: #swiatynia easter-egg
            pass
        elif gracz.xyz == 8: #pola pszenzyta
            if szansa_na_sukces(gracz.xyz) == True and q > 1:
                walka(mob, gracz)
            print("Znajdujesz się na polach pszenżyta.")
            if jaskinia:
                gdzie = input("Możesz udać się nad sadzawkę, do miasta lub to mrocznej jaskini. Jaka jest twa decyzja? (sadzawka/miasto/jaskinia) ")
                if gdzie == 'sadzawka':
                    gracz.xyz = 5
                elif gdzie == 'miasto':
                    gracz.xyz = 6
                elif gdzie == 'jaskinia':
                    gracz.xyz = 9
                    jaskinia = False
                else:
                    print("Nie możesz udać się w to miejsce (sprawdź poprawność pisowni lub opcje przyjść na mapie).")
            else:
                gdzie = input("Możesz udać się nad sadzawkę lub do miasta. Jaka jest twa decyzja? (sadzawka/miasto) ")
                if gdzie=='sadzawka':
                    gracz.xyz = 5
                elif gdzie=='miasto':
                    gracz.xyz = 6
                else:
                    print("Nie możesz udać się w to miejsce (sprawdź poprawność pisowni lub opcje przyjść na mapie).")

        elif gracz.xyz == 9: #jaskinia
            if q < 4:
                print("W jaskini jest zbyt ciemno, żebyś mógł do niej wejść.")
            elif q == 4:
                super_moc = skrzynia()
                q = 5
            else:
                print("Jaskinia się zawaliła, nie możesz do niej wejść.")
            gracz.xyz = 8

        elif gracz.xyz == 10: #droga
            if q == 5:
                print("Udało ci się dostać na drogę, jednak natknąłeś się na kota Adrianka, który strzeże mejścia do zamku.\n"
                      "Atakuje Cię!")
                gracz.hp = walka(mob, gracz, "adrianek")
                print("Udało ci się pokonać kota Adrianka, udajesz się do zamku.")
                gracz.xyz = 11
            else:
                print("Ta droga jest zamknięta, spróbuj innym razem.")
                gracz.xyz = 6

        elif gracz.xyz == 11: #zamek i ogolnie tutaj juz nie ma odwrotu, ostatnia petla i koniec gry
            print("\n\nStajesz przed zamkową bramą. ZAMKNIĘTE! No tak, można było to przewidzieć.\n")
            print("K.: Psst! Ej ty! Tak, do ciebie mówię! Nie wpuścili cie do zamku? Nie ciebie jednego.\n"
                  "Najpierw zapraszją z ofertą pracy, a potem "
                  "nie, nie wejdziesz! I konczysz żeniąc się z jakąś wieśniaczką!")
            print("Ty: Nie ma żadnego sposobu?")

            zamek = input("K.: Nie ma, ale moŻesz przyłączyć się do kociej brygady, mimo że nie masz ku temu absolutnie żadnego powodu (tak/nie)")
            if zamek == "tak":
                print("K.: Coż... nie spodziewałem sie takiej odpowiedzi. Skoro jednak, witamy w naszych szeregach!\n Udaj sie do szefa po swoj bitewny parasol")
                print("Decydując się przejść na stronę kota, SKAZAŁEŚ MIAŁMLAND NA ZAGŁADĘ!")
                time.sleep(5)
                sys.exit()
            elif zamek == "nie":
                print("Nim zdażyłes udzielić tajemniczemu nieznajomemu odpowiedzi, zaatakował cie wściekły kot Jarek!")
                gracz.hp = walka(mob, gracz, "jarek")
                gracz.xyz = 0
                print("\nNagle kot Jaarek polewa sie skisłym mlekiem, odzyskując wszystkie siły witalne!\nTo koniec - myślisz.\n"
                      "Glos zza ściany: Nikt nie spodziewa sie hiszpańskiej inkwizycji!\n"
                      "Rozjuszony inkwizytor wbiega na salę i jednym cięciem pozbawia kota ogona!")
            if super_moc: #jesli mamy super moc ze skrzyni
                print("Nagle przypominasz sobie o tajemniczych runach z jaskini!\n"
                      "Wyjmujesz je i sam nie wiesz jak, ale odczytujesz je!\nSkutkuje to pojawieniem się w twojej dłoni "
                      "POTĘŻNEGO miecza, którym przecinasz kota na pół!\nZWYCIĘSTWO! MIAŁMLAND ZOSTAŁ WYZWOLONY!")
                time.sleep(5)
                sys.exit()
            else: #jesli nie mamy mocy
                print("Niestety nie masz pojęcia co się właśnie stało więc całkowicie zapomniałeś o jakimkolwiek niebezpieczeństwie!\n"
                      "Kot Jarek wykorzystuje ten moment, rzuca ci się do gardła i całkowicie go rozrywa!\n"
                      "POLEGŁEŚ! MIAŁMLAND POZOSTAŁ POD DYKTATURĄ JARKA NA WIEKI WIEKÓW!")
                time.sleep(5)
                sys.exit()

        else:
            pass
