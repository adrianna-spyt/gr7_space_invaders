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
        #ładuje obraz do zmiennej, której potem używamy do wyświetlania tego obrazu
        self.gracz=pygame.image.load("gracz.png")
        #wycina czarny kolor z bazowego obrazka (liczby oznaczają kolor czarny), więc zostaje przezroczyste tło i tylko sam statek
        #(zamiast tego można załadować png z przezroczystym tłem)
        #(UWAGA ważne żeby wszystkie obrazki były w takim samym formacie (png))
        self.gracz.set_colorkey((0,0,0))
        #ustawia współrzędne początkowe gracza
        self.pozycja_gracza_x=450
        self.pozycja_gracza_y=500
        #ustawia o ile przesuwa się gracz przy każdym kliknięciu
        self.krok=10
        #wyświetla obrazek gracza na współrzędnych wcześniej ustawionych
        self.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
        #odświeża ekran, KONIECZNE ABY ZMIANY SIĘ POJAWIŁY
        pygame.display.update()
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
        self.ekran.blit(self.oslony,(self.pozycja_oslony1_x, self.pozycja_oslony1_y))
        self.ekran.blit(self.oslony,(self.pozycja_oslony2_x, self.pozycja_oslony2_y))
        self.ekran.blit(self.oslony,(self.pozycja_oslony3_x, self.pozycja_oslony3_y))
        self.ekran.blit(self.oslony,(self.pozycja_oslony4_x, self.pozycja_oslony4_y))
        pygame.display.update()
    def event(self):
        while self.running:
            for event in pygame.event.get():
                #wychodzi z gry po kliknięciu X w prawym górnym rogu
                if event.type==pygame.QUIT:
                    self.running=False
                    break
                #jeśli wciśniesz jakiś przycisk
                elif event.type==pygame.KEYDOWN:
                    #jeśli wciśniesz escape, wychodzi z gry
                    if event.key==pygame.K_ESCAPE:
                        self.running=False
                        break
                    #jeśli klikniesz strzałkę w lewo
                    elif event.key==pygame.K_LEFT:
                        #żeby gracz nie mógł wyjść poza ekran
                        if self.pozycja_gracza_x>=10:
                            #współrzędna x gracza zmniejsza się o krok (czyli o ile się przesuwa), po czym wyświetla zaktualizowaną pozycję po zmniejszeniu zmiennej i odświeża ekran
                            #trzeba najpierw blitnąć tło, a potem wszystkie ikonki, bo inaczej stary obraz będzie widoczny
                            self.pozycja_gracza_x-=self.krok
                            self.ekran.blit(self.tlo,(0,0))
                            self.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
                            self.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
                            self.ekran.blit(self.oslony,(self.pozycja_oslony1_x, self.pozycja_oslony1_y))
                            self.ekran.blit(self.oslony,(self.pozycja_oslony2_x, self.pozycja_oslony2_y))
                            self.ekran.blit(self.oslony,(self.pozycja_oslony3_x, self.pozycja_oslony3_y))
                            self.ekran.blit(self.oslony,(self.pozycja_oslony4_x, self.pozycja_oslony4_y))
                            pygame.display.update()
                    #jeśli klikniesz strzałkę w prawo
                    elif event.key==pygame.K_RIGHT:
                        #żeby gracz nie mógł wyjść poza ekran
                        if self.pozycja_gracza_x<=self.szerokosc_ekranu-50:
                            #analogicznie do ruchu w lewo
                            self.pozycja_gracza_x+=self.krok
                            self.ekran.blit(self.tlo,(0,0))
                            self.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
                            self.ekran.blit(self.oslony,(self.pozycja_oslony1_x, self.pozycja_oslony1_y))
                            self.ekran.blit(self.oslony,(self.pozycja_oslony2_x, self.pozycja_oslony2_y))
                            self.ekran.blit(self.oslony,(self.pozycja_oslony3_x, self.pozycja_oslony3_y))
                            self.ekran.blit(self.oslony,(self.pozycja_oslony4_x, self.pozycja_oslony4_y))
                            pygame.display.update()
#to nie wiem w sumie czemu, ale w poradnikach tak piszą, żeby działało XD
if __name__=="__main__":
    #spaceinvaders jako instancja klasy gra
    spaceinvaders=gra()
    #uruchamiamy metodę gry jaką są eventy
    spaceinvaders.event()
#jakby co, to pytajcie <3
