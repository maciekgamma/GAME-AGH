from klasy import *
from random import randrange
from zmienne import *
from funkcje import *

def q1():
    print(" ")
    print("Dotarłeś do miasta, czas na zakupy.\nAby kupić miecz (siła 1) wybierz 1.\n"
          "Aby kupić topór (siła 1) wybierz 2.\nAby kupić młot (siła 1) wybierz 3.\n")
    w = int(input("Którą broń wybierasz? "))
    if w == 1:
        print("Zakupiłeś miecz (siła 1). Świetny wybór.")
    elif w == 2:
        print("Zakupiłeś miecz (siła 1). Świetny wybór.")
    elif w == 3:
        print("Zakupiłeś miecz (siła 1). Świetny wybór.")
    else:
        print("Widzę, że podjęcie decyzji przerosło twoje możliwości, dlatego wybrałem za Ciebie.\n"
                "Zakupiłeś gałąź sosny (siła 1).")
    print("Teraz masz już czym walczyć, jednak brak ci siły.\n"
                "Udaj się do lasu aby odbyć trening siłowy.\n"
                "Gdybyś trochę oberwał po drodze, udaj się do świątyni aby się uleczyć.")
    print("Zadanie: udaj się do lasu.")
    print(" ")

def q2(gracz):
    print(" ")
    print("Dotarłeś do lasu.")
    print("W celu wykonania serii wypisz liczby od 1 do 10.\nPamiętaj jednak, "
          "że możesz podać jedną liczbę na raz. Inaczej trening nie zostanie zaliczony.")
    y = input("Naciśnij ENTER aby unieść konar i wykonać serię 10 przysiadów.")
    a = input("Podaj liczbę: ")
    b = input("Podaj liczbę: ")
    c = input("Podaj liczbę: ")
    d = input("Podaj liczbę: ")
    e = input("Podaj liczbę: ")
    f = input("Podaj liczbę: ")
    g = input("Podaj liczbę: ")
    h = input("Podaj liczbę: ")
    i = input("Podaj liczbę: ")
    j = input("Podaj liczbę: ")
    if a == '1' and b == '2' and c == '3' and d == '4' and e == '5' and f == '6' and g == '7' and h == '8' and i == '9' and j == '10':
        print("Udało ci się wykonać 10 powtórzeń, twoja siła wzrosła o 1.")
        gracz.sila += 1
    else:
        print("Nie udało ci się wykonać 10 powtórzeń, spróbuj zwiększyć swoją siłe w inny sposób.")
    print("Wypadałoby zdobyć jakieś pożywienie.\nUdaj się na drogę leśną i nazbieraj tochę grzybów na zupę.\n"
            "Jeśli trochę oberwałeś wpierw udaj się do świątyni.")
    print("Zadanie: udaj się na ścieżkę leśną.")
    print(" ")

def q3(gracz):
    print(" ")
    print("Jesteś już na ścieżce, czas rozpocząć grzybobranie!")
    print("Kiedy zobaczysz parzystą liczbę, jest to grzyb jadalny. Zbierz bo wpisując: tak.\n"
          "Jednak kiedy liczba będzie nieparzysta, jest to grzyb trujący, nie zbieraj go wpisując: nie.\n"
          "Każdy trujący grzyb, który zbierzesz odejmie ci 10 hp. Powodzenia!")
    print("Zadanie: zbierz 10 grzybów jadalnych.")
    a = input("Naciśnij ENTER aby rozpocząć grzybobranie.")
    g = 0
    while g < 10:
        b = randrange(1,100)
        print("Grzyb:", b)
        d = input("Zebrać? (tak/nie) ")
        if b % 2 == 0 and d == "tak":
            g += 1
        elif b % 2 == 1 and d == "tak":
            print("Ten był trujący!")
            gracz.hp -= 10
            if gracz.hp <= 0:
                print("Strułeś się muchomorkami, umierasz.")
                time.sleep(5)
                sys.exit()
    else:
        print("Udało ci się zebrać 10 grzybów i przygotować wyśmienitą zupkę.")
        print("Okazało się, że grzyby te były magiczne.\nZyskałeś moc: widzenie w ciemności.") #zwiększyć siłę
        print("Zadanie: udaj się do jaskini.")
        print(" ")



