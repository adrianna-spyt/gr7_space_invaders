import os
import pygame

class gra():
    def __init__(self):
        #zmienna kontrolująca wyjście z gry
        self.running=True
        self.szerokosc_ekranu=900
        self.wysokosc_ekranu=600
        #włącza pygame
        pygame.init()
        #ustawia wielkość okna gry
        self.ekran=pygame.display.set_mode((self.szerokosc_ekranu,self.wysokosc_ekranu))
        #ustawia co jest w tle
        self.tlo=pygame.image.load("tlo.png")
        #blit = zmiana tego, co się wyświetla na ekranie UWAGA trzeba jeszcze ekran przeładować, aby się wyświetliło
        self.ekran.blit(self.tlo,(0,0))
        pygame.sprite.Sprite.__init__(self)
    def event(self):
        while self.running:
            self.ekran.blit(self.tlo,(0,0))
            gracz1.wyswietl()
            for i in range(3):
                for j in range(7):
                    przeciwnik.wyswietl(i,j)
            oslonki.wyswietl()
            pocisk.wyswietl()
            pygame.display.update()
            for event in pygame.event.get():
                #wychodzi z gry po kliknięciu X w prawym górnym rogu
                if event.type==pygame.QUIT:
                    self.running=False
                    break
                #jeśli wciśniesz jakiś przycisk
            przycisk = pygame.key.get_pressed()
            #jeśli wciśniesz escape, wychodzi z gry
            if przycisk[pygame.K_ESCAPE]:
                self.running=False
                break
            #jeśli klikniesz strzałkę w lewo
            elif przycisk[pygame.K_LEFT]:
                #żeby gracz nie mógł wyjść poza ekran
                if gracz1.pozycja_gracza_x>=10:
                    #współrzędna x gracza zmniejsza się o krok (czyli o ile się przesuwa), po czym wyświetla zaktualizowaną pozycję po zmniejszeniu zmiennej i odświeża ekran
                    #trzeba najpierw blitnąć tło, a potem wszystkie ikonki, bo inaczej stary obraz będzie widoczny
                    gracz1.pozycja_gracza_x-=1
                    gracz1.wyswietl()
                    pygame.display.update()
            #jeśli klikniesz strzałkę w prawo
            elif przycisk[pygame.K_RIGHT]:
                #żeby gracz nie mógł wyjść poza ekran
                if gracz1.pozycja_gracza_x<=self.szerokosc_ekranu-50:
                    #analogicznie do ruchu w lewo
                    gracz1.pozycja_gracza_x+=1
                    gracz1.wyswietl()
                    pygame.display.update()

            #jesli space to strzelamy
            elif przycisk[pygame.K_SPACE]:
                  self.pocisk_y-=self.pocisk_V
                  self.ekran.blit(self.tlo,(0,0))
                  gracz1.wyswietl()
                  for i in range(3):
                      for j in range(7):
                          przeciwnik.wyswietl(i,j)
                  oslonki.wyswietl()
                  pocisk.wyswietl()
                  pygame.display.update()
            #wyświetlamy wszystko

class gracz():
    def __init__(self):
        #ładuje obraz do zmiennej, której potem używamy do wyświetlania tego obrazu
        self.gracz=pygame.image.load("gracz.png")
        #wycina czarny kolor z bazowego obrazka (liczby oznaczają kolor czarny), więc zostaje przezroczyste tło i tylko sam statek
        #(zamiast tego można załadować png z przezroczystym tłem)
        #(UWAGA ważne żeby wszystkie obrazki były w takim samym formacie (png))
        self.gracz.set_colorkey((0,0,0))
        #ustawia współrzędne początkowe gracza
        self.pozycja_gracza_x=437
        self.pozycja_gracza_y=500
        #wyświetla obrazek gracza na współrzędnych wcześniej ustawionych
        spaceinvaders.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
    def wyswietl(self):
        spaceinvaders.ekran.blit(gracz1.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
class oslony():
    def __init__(self):
        self.oslony=pygame.image.load ("oslony.png")
        self.oslony.set_colorkey((0,0,0))
        self.pozycja_oslony1_x=25
        self.pozycja_oslony1_y=350
        self.pozycja_oslony2_x=245
        self.pozycja_oslony2_y=350
        self.pozycja_oslony3_x=470
        self.pozycja_oslony3_y=350
        self.pozycja_oslony4_x=685
        self.pozycja_oslony4_y=350
    def wyswietl(self):
        spaceinvaders.ekran.blit(self.oslony,(self.pozycja_oslony1_x, self.pozycja_oslony1_y))
        spaceinvaders.ekran.blit(self.oslony,(self.pozycja_oslony2_x, self.pozycja_oslony2_y))
        spaceinvaders.ekran.blit(self.oslony,(self.pozycja_oslony3_x, self.pozycja_oslony3_y))
        spaceinvaders.ekran.blit(self.oslony,(self.pozycja_oslony4_x, self.pozycja_oslony4_y))
class pociski():
    def __init__(self):
        #strzelanie
        self.pocisk=pygame.image.load("pocisk.png")
        self.pocisk.set_colorkey((0,225,0))
        self.pocisk_x=0
        self.pocisk_y=0
        self.pocisk_stan= "aktywny" #"niekatwny" gdy strzął zostanie wykonany
        self.pocisk_V= 1 #prędkość
    def wyswietl(self):
        spaceinvaders.ekran.blit(self.pocisk,(gracz1.pozycja_gracza_x,gracz1.pozycja_gracza_y))
    #def strzal(self,x,y):
        # self.pocisk_stan = "nieaktywny"
class przeciwnicy():
    def __init__(self):
        self.obraz_przeciwnicy=pygame.image.load("przeciwnik.png")
        self.obraz_przeciwnicy.set_colorkey((0,0,0))
        self.przec_pocz_x = 120 # początkowe miejsce pierwszego przeciwnika
        self.przec_pocz_y = 70
        self.odstep_rzedy = 100
        self.odstep_kolumny = 100
    def wyswietl(self,rzad,kolumna):
        # if i==1:
        #     self.przeciwnik_y = self.przec_pocz_y
        # else:
        #     self.przeciwnik_y = self.przec_pocz_y + 30*(i-1)
        # if j==1:
        #     self.przeciwnik_x = self.przec_pocz_x
        # else:
        #     self.przeciwnik_x = self.przec_pocz_x + 100*(j-1)
        self.przeciwnik_y = 70+self.odstep_rzedy*rzad
        self.przeciwnik_x = 120+self.odstep_kolumny*kolumna
        spaceinvaders.ekran.blit(self.obraz_przeciwnicy,(self.przeciwnik_x,self.przeciwnik_y))

if __name__=="__main__":
    spaceinvaders=gra()
    przeciwnik=przeciwnicy()
    gracz1=gracz()
    oslonki=oslony()
    pocisk=pociski()
    while spaceinvaders.running:
        spaceinvaders.event()
