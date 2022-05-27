import os
import pygame




# tworzę klasę Pocisk
class Pocisk(pygame.sprite.Sprite):
    # picture_pocisk = pygame.image.load("pocisk.png")# wczytanie pocisku
    # picture_pocisk = pygame.transform.scale(picture_pocisk, (5,5))#wymiar pocisku

# zawiera kilka dodatkowych funkcji przydatnych właśnie do tworzenia gier, można np tworzyć grupy.
    def __init__(self, pozycja_gracza_x, pozycja_pocisk,predkosc,stan): #mamy 4 parametry pocisku
        x=300 #na testy
        y=400 #na testy
        predkosc = 5 # na testy
        stan= "widoczna" #kiedy pocisk jest wystrzelony

        pygame.sprite.Sprite.__init__(self)
        # ^tak się robi z tym spritem po prostu
        pocisk_fot=self.pocisk=pygame.image.load("pocisk.png")
        self.pygame.transform.scale(pocisk_fot, (5,5))
        self.pocisk.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        # rect - wklejam przeciwnika do takiego kwadratu i to będzie jego pozycja,
        # od razu zakłada że x to poziome a y to pionowe
        self.rect.center = [self.pozycja_gracza_x, self.pozycja_gracza_y]
        # środkowa część będzie w później określonym x i y
        if stan==widoczna:
            self.ekran.blit(self.pocisk,(self.pozycja_gracza_x,self.pozycja_gracza_y))
        if event.key==pygame.K_SPACE:
            self.pozycja_pocisk=self.predkosc
            self.ekran.blit(self.tlo,(0,0))
            self.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_pocisk))
            pygame.display.update()

        #odświeża ekran, KONIECZNE ABY ZMIANY SIĘ POJAWIŁY
        pygame.display.update()

