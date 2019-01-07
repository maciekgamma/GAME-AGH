import random
from funkcje import *
from zmienne import *

class Gracz():
    def __init__(self, hp, sila, xyz):
        #self.lista = lista
        self.hp_max = GRACZ_HP_MAX
        self.hp = int(hp)
        self.sila = int(sila)
        #self.mana = 0
        #self.armor = 0
        #self.exp = 0
        #self.lvl = 1
        self.xyz = int(xyz)
        #self.magia = 5 #wartosc wzmocnienia ataku po uzyciu spella

    def info(self):
        pass

    def odpoczynek(self):
        self.hp += 20

    def dzban(self):
        print("banda ulryka")
        game_over()

    def spell(self):
        return self.magia

    def lvl_up(self):
        self.lvl += 1
        self.sila += 1
        self.hp = int(self.hp*1.1)

class Mob():
    def __init__(self):
        self.hp = MOB_HP_MAX
        self.sila = 1
