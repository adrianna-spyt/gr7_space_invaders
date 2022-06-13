import os
import pygame
import math
from pygame.rect import *
from pygame.locals import *

def odswiez():
    gracz1.wyswietl()
    oslonki.wyswietl()
    przeciwnik.przesuwanie_przeciwnikow()
    przeciwnik.wyswietl()
    pocisk.pozycja_strzal()
    pygame.display.update()
class gra():
    def __init__(self):
        self.running=True
        self.szerokosc_ekranu=900
        self.wysokosc_ekranu=600
        pygame.init()
        pygame.mixer.init()
        self.ekran=pygame.display.set_mode((self.szerokosc_ekranu,self.wysokosc_ekranu))
        self.ekranname=pygame.display.set_caption("Space Invaders")
        self.tlo=pygame.image.load("tlo.png")
        self.ekran.blit(self.tlo,(0,0))
        pygame.mixer.music.load("muzyka.mp3")
        pygame.mixer.music.play(-1)
        self.punkty=0
        self.font = pygame.font.SysFont("Arial",36)
    def event(self):
        while self.running:
            self.ekran.blit(self.tlo,(0,0))
            wynik = self.font.render("Punkty: " + str(self.punkty),True, (225,225,225))
            spaceinvaders.ekran.blit(wynik,(60,20))
            odswiez()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                    break
            przycisk = pygame.key.get_pressed()
            if przycisk[pygame.K_ESCAPE]:
                self.running=False
                break
            elif przycisk[pygame.K_LEFT]:
                if gracz1.pozycja_gracza_x>=10:
                    gracz1.pozycja_gracza_x-=1
                    gracz1.wyswietl()
            elif przycisk[pygame.K_RIGHT]:
                if gracz1.pozycja_gracza_x<=self.szerokosc_ekranu-50:
                    gracz1.pozycja_gracza_x+=1
                    gracz1.wyswietl()
            if przycisk[pygame.K_SPACE]:
                pocisk.pocisk_stan="start"
                pocisk.pozycja_strzal()
            elif pocisk.pocisk_stan=="start":
                tablica_rectow=[]
                for i in range(len(przeciwnik.tablica_przeciwnikow)):
                    tablica_rectow.append(przeciwnik.tablica_przeciwnikow[i][2])
                for i in range(len(tablica_rectow)):
                    usun=pygame.Rect.colliderect(pocisk.pociskrect,tablica_rectow[i])
                    if usun==True:
                        przeciwnik.tablica_przeciwnikow.remove(przeciwnik.tablica_przeciwnikow[i])
                        self.punkty+=10
                        pocisk.tablica_pociski.remove(pocisk.tablica_pociski[0])
                        pocisk.tablica_pociski.remove(pocisk.tablica_pociski[1])
                        pocisk.pocisk_stan="stop"
                        break
            if przeciwnik.tablica_przeciwnikow==False:
                self.ekran.blit(self.tlo,(0,0))
                wynik = self.font.render("Punkty: " + str(self.punkty),True, (225,225,225))
                spaceinvaders.ekran.blit(wynik,(60,20))


                 # pocisk.kolizja()
            #póżniej gdy tablica przeciwników będzie pusta
            elif self.punkty==210:
                self.wynik = self.font.render("Punkty: 210" ,True, (225,225,225))
                self.wiadom=self.font.render("Wygrał_ś!" ,True, (225,225,225))
                self.font = pygame.font.SysFont("Arial",100)
                spaceinvaders.ekran.blit(self.wiadom,(200,230))
                pygame.display.update()
            #wykrywanie kolizji
            #wyświetlamy wszystkoself.celny_strzal=pocisk.kolizja(self,pocisk.pozycja_pocisk_x,przeciwnicy.tablica_przeciwnikow[i],pocisk.pozycja_pocisk_y,70)

class gracz():
    def __init__(self):
        self.gracz=pygame.image.load("gracz.png")
        self.gracz.set_colorkey((0,0,0))
        self.pozycja_gracza_x=437
        self.pozycja_gracza_y=500
        spaceinvaders.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
    def wyswietl(self):
        spaceinvaders.ekran.blit(gracz1.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
class oslony():
    def __init__(self):
        self.oslony=pygame.image.load ("oslony.png")
        self.oslony.set_colorkey((0,0,0))
        self.pozycja_oslony1_x=30
        self.pozycja_oslony1_y=350
        self.pozycja_oslony2_x=265
        self.pozycja_oslony2_y=350
        self.pozycja_oslony3_x=500
        self.pozycja_oslony3_y=350
        self.pozycja_oslony4_x=735
        self.pozycja_oslony4_y=350
    def wyswietl(self):
        spaceinvaders.ekran.blit(self.oslony,(self.pozycja_oslony1_x, self.pozycja_oslony1_y))
        spaceinvaders.ekran.blit(self.oslony,(self.pozycja_oslony2_x, self.pozycja_oslony2_y))
        spaceinvaders.ekran.blit(self.oslony,(self.pozycja_oslony3_x, self.pozycja_oslony3_y))
        spaceinvaders.ekran.blit(self.oslony,(self.pozycja_oslony4_x, self.pozycja_oslony4_y))

class pociski():
    def __init__(self):
        self.pocisk=pygame.image.load("pocisk.png")
        self.pocisk.set_colorkey((0,225,0))
        self.pocisk_stan= "stop" #"niekatwny" gdy strzął zostanie wykonany
        self.pocisk_V= 3  #prędkość
        self.pozycja_pocisk_y=gracz1.pozycja_gracza_y
        self.pozycja_pocisk_x=gracz1.pozycja_gracza_x+7
        self.rect = self.pocisk.get_rect(x=0,y=0)
        self.tablica_pociski=[]
        self.tablica_pociski.append(self.pozycja_pocisk_x)
        self.tablica_pociski.append(self.pozycja_pocisk_y)
    def pozycja_strzal(self):
         if self.pocisk_stan=="start":
             self.tablica_pociski=[]
             self.tablica_pociski.append(self.pozycja_pocisk_x)
             self.tablica_pociski.append(self.pozycja_pocisk_y)
             spaceinvaders.ekran.blit(self.pocisk,(self.tablica_pociski[0],self.tablica_pociski[1]))
             self.pozycja_pocisk_y-=self.pocisk_V
             self.tablica_pociski[1]=self.pozycja_pocisk_y
             self.pociskrect=Rect(self.pozycja_pocisk_x,self.pozycja_pocisk_y,self.rect.width,self.rect.height)
             self.tablica_pociski.append(pygame.draw.rect(spaceinvaders.ekran,przeciwnik.kolor_life,self.pociskrect,width=2))
         if self.pocisk_stan=="stop":
             self.pozycja_pocisk_x=gracz1.pozycja_gracza_x+7
             self.pozycja_pocisk_y=gracz1.pozycja_gracza_y
             self.tablica_pociski.append(self.pozycja_pocisk_x)
             self.tablica_pociski.append(self.pozycja_pocisk_y)
         if self.pozycja_pocisk_y<50:
             self.pocisk_stan="stop"
             self.pozycja_pocisk_y=gracz1.pozycja_gracza_y
             self.rect.y=gracz1.pozycja_gracza_y #pozycja Y na stop
    def wyswietl(self):
        spaceinvaders.ekran.blit(self.pocisk,(self.tablica_pociski[0],self.tablica_pociski[1]))


        # for i in range (len(przeciwnicy.przesuwanie_przeciwnikow))
        #
        #    punkt+=1
        #if self.pozycja_pocisk_y==70 or self.pozycja_pocisk_y==170 or self.pozycja_pocisk_y==240:


        # self.pocisk_stan = "nieaktywny"
class przeciwnicy():
    def __init__(self):
        self.obraz_przeciwnicy=pygame.image.load("przeciwnik.png")
        self.obraz_przeciwnicy.set_colorkey((0,0,0))
        self.przec_pocz_x = 0
        self.przec_pocz_y = 70
        self.odstep_rzedy = 100
        self.odstep_kolumny = 100
        self.kierunek = 1 # +1 będzie szedł w prawo, a -1 będzie szedł w lewo
        self.granica = 650
        self.rect = self.obraz_przeciwnicy.get_rect(x=0,y=0)
        self.kolor_life = pygame.Color(50,255,200)
        self.kolor_dead = pygame.Color(255,0,0)
        self.widoczny = True

    def wyswietl(self):
        for i in range(len(self.tablica_przeciwnikow)):
            spaceinvaders.ekran.blit(self.obraz_przeciwnicy, (self.tablica_przeciwnikow[i][0], self.tablica_przeciwnikow[i][1]))
            self.tablica_przeciwnikow[i][2]
            pygame.draw.rect(spaceinvaders.ekran, self.kolor_life ,self.tablica_przeciwnikow[i][2], width=4)
    def generowanie_przeciwnikow(self, kolumny, rzedy):
        self.tablica_przeciwnikow = []
        for kazdy in range(rzedy):
            for wszystkie in range(kolumny):
                self.tablica_przeciwnikow.append([self.przec_pocz_x + (self.odstep_kolumny * wszystkie), self.przec_pocz_y + (self.odstep_rzedy * kazdy)] )
                #print(self.tablica_przeciwnikow)
        for i in range(len(self.tablica_przeciwnikow)):
            newRect = Rect(self.tablica_przeciwnikow[i][0], self.tablica_przeciwnikow[i][1], self.rect.width, self.rect.height)
            self.tablica_przeciwnikow[i].append(newRect)
    def przesuwanie_przeciwnikow(self):
        if self.granica > 5700:
            self.kierunek = -1
        if self.granica < 700:
            self.kierunek = 1
        if self.kierunek == 1:
            for i in range(len(self.tablica_przeciwnikow)):
                self.tablica_przeciwnikow[i][0]+=1
                newRect = Rect(self.tablica_przeciwnikow[i][0], self.tablica_przeciwnikow[i][1], self.rect.width, self.rect.height)
                self.tablica_przeciwnikow[i][2]=(Rect(self.tablica_przeciwnikow[i][0], self.tablica_przeciwnikow[i][1], self.rect.width, self.rect.height))
            self.granica+=21
        if self.kierunek == -1:
            for i in range(len(self.tablica_przeciwnikow)):
                self.tablica_przeciwnikow[i][0]-=1
                newRect = Rect(self.tablica_przeciwnikow[i][0], self.tablica_przeciwnikow[i][1], self.rect.width, self.rect.height)
                self.tablica_przeciwnikow[i][2]=(Rect(self.tablica_przeciwnikow[i][0], self.tablica_przeciwnikow[i][1], self.rect.width, self.rect.height))
            self.granica -= 21


if __name__=="__main__":
    all_colliders = []
    spaceinvaders=gra()
    przeciwnik=przeciwnicy()
    gracz1=gracz()
    oslonki=oslony()
    pocisk=pociski()
    przeciwnik.generowanie_przeciwnikow(7, 3)
    while spaceinvaders.running:
        spaceinvaders.event()
