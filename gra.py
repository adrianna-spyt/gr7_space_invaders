import os
import pygame
import math
pygame.mixer.init()

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
        #muzyka w grze
        self.muzyka=pygame.mixer.Sound("muzyka.mp3")
        self.muzyka.play(-1)
        self.strzal_m=pygame.mixer.Sound("shot.mp3")
        #punkty gracza
        self.punkty=0
        #życia gracza
        self.zycia=3
        self.font = pygame.font.SysFont("Arial",36)


        pygame.sprite.Sprite.__init__(self)
    def event(self):
        while self.running:
            self.ekran.blit(self.tlo,(0,0))
            #ekran pnktow
            wynik = self.font.render("Punkty: " + str(self.punkty),True, (225,225,225))
            spaceinvaders.ekran.blit(wynik,(60,20))
            zycie = self.font.render("Życia: " + str(self.zycia),True, (225,225,225))
            spaceinvaders.ekran.blit(zycie,(700,20))
            gracz1.wyswietl()
            oslonki.wyswietl()
            przeciwnik.przesuwanie_przeciwnikow()
            przeciwnik.wyswietl()
            pocisk.pozycja_strzal()

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
                  pocisk.pocisk_stan="start"
                  self.strzal_m.play(0)
                  pocisk.pozycja_strzal()
                  gracz1.wyswietl()
                  przeciwnik.przesuwanie_przeciwnikow()
                  przeciwnik.wyswietl()
                  oslonki.wyswietl()
                 # pocisk.kolizja()
                  pygame.display.update()
            #póżniej gdy tablica przeciwników będzie pusta
            elif self.punkty=="100":
                wynik = self.font.render("Punkty: " ,True, (225,225,225))
                spaceinvaders.ekran.blit(wynik,(150,150))
            #wykrywanie kolizji
            elif pocisk.pocisk_stan=="start":
                self.celny=pocisk.kolizja(pocisk.pozycja_pocisk_x,170,pocisk.pozycja_pocisk_y,350)#wspolrzedne na testy, funkcja dziala
                if self.celny==True:#jesli trafiono w przeciwnika
                    self.punkty+=1
                    spaceinvaders.ekran.blit(pocisk.pocisk_st,(pocisk.pozycja_pocisk_x,pocisk.pozycja_pocisk_y))
                pygame.display.update()

    

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
        self.pocisk_st=pygame.image.load("pocisk_st.png")
        self.pocisk_st.set_colorkey((0,225,0))
        self.pocisk_stan= "stop" #"niekatwny" gdy strzął zostanie wykonany
        self.pocisk_V= 3  #prędkość
        self.pozycja_pocisk_y=gracz1.pozycja_gracza_y
        self.pozycja_pocisk_x=gracz1.pozycja_gracza_x


    def pozycja_strzal(self):
         if self.pocisk_stan=="start":
             spaceinvaders.ekran.blit(pocisk.pocisk,(pocisk.pozycja_pocisk_x,pocisk.pozycja_pocisk_y))
             #self.pocisk_wyswietl=True
             self.pozycja_pocisk_y-=self.pocisk_V
         if self.pocisk_stan=="stop":
             self.pozycja_pocisk_x=gracz1.pozycja_gracza_x+13
         if self.pozycja_pocisk_y<50:
             self.pocisk_stan="stop"
             self.pozycja_pocisk_y=gracz1.pozycja_gracza_y

    def kolizja(self,x,x1,y,y1):
        self.odleglosc=math.sqrt((math.pow(x-x1,2))+(math.pow(y-y1,2)))
        if self.odleglosc<100:
            return True

class przeciwnicy():
    def __init__(self):
        self.obraz_przeciwnicy=pygame.image.load("przeciwnik.png")
        self.obraz_przeciwnicy.set_colorkey((0,0,0))
        self.przec_pocz_x = 0 # początkowe miejsce pierwszego przeciwnika
        self.przec_pocz_y = 70
        self.odstep_rzedy = 100
        self.odstep_kolumny = 100
        self.kierunek = 1 # +1 będzie szedł w prawo, a -1 będzie szedł w lewo
        self.granica = 650 # ustaliłam sobie taką granicę, jako wyznacznik dla jakiej wartości dalej ma zmianić kierunek


    def wyswietl(self):
        for i in range(len(self.tablica_przeciwnikow)):
            spaceinvaders.ekran.blit(self.obraz_przeciwnicy, (self.tablica_przeciwnikow[i][0], self.tablica_przeciwnikow[i][1]))

    def generowanie_przeciwnikow(self, kolumny, rzedy):
        self.tablica_przeciwnikow = []
        for kazdy in range(rzedy):
            for wszystkie in range(kolumny):
                self.tablica_przeciwnikow.append([self.przec_pocz_x + (self.odstep_kolumny * wszystkie), self.przec_pocz_y + (self.odstep_rzedy * kazdy)] )
                #print(self.tablica_przeciwnikow)
    def przesuwanie_przeciwnikow(self):
        if self.granica > 5700:
            self.kierunek = -1
        if self.granica < 700:
            self.kierunek = 1
        if self.kierunek == 1:
            for i in range(len(self.tablica_przeciwnikow)):
                self.tablica_przeciwnikow[i][0]+=1
                self.granica += 1
        if self.kierunek == -1:
            for i in range(len(self.tablica_przeciwnikow)):
                self.tablica_przeciwnikow[i][0]-=1
                self.granica -= 1




if __name__=="__main__":
    spaceinvaders=gra()
    przeciwnik=przeciwnicy()
    gracz1=gracz()
    oslonki=oslony()
    pocisk=pociski()
    przeciwnik.generowanie_przeciwnikow(7, 3)
    while spaceinvaders.running:
        spaceinvaders.event()
