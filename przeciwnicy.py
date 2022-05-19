import os
import pygame

picture_przeciwnik1 = pygame.image.load("przeciwnik1.png")
picture_przeciwnik1 = pygame.transform.scale(picture, (20,20))

wiersze = 3
kolumny = 5

# tworzę klasę Przeciwnicy
class Przeciwnicy(pygame.sprite.Sprite):
# te sprite to są takie moduły do zarządzania obiektami w grze i przyspieszają i ułatwiają działanie klasy.
# zawiera kilka dodatkowych funkcji przydatnych właśnie do tworzenia gier, można np tworzyć grupy.
    def __innit__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # ^tak się robi z tym spritem po prostu
        self.gracz=pygame.image.load("przeciwnik1.png")
        self.gracz.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        # rect - wklejam przeciwnika do takiego kwadratu i to będzie jego pozycja,
        # od razu zakłada że x to poziome a y to pionowe
        self.rect.center = [x, y]
        # środkowa część będzie w później określonym x i y

# teraz aby mi się załadował przeciwnik muszę go zupdateować
    def update(self):
        pass
        # to będe robić dopiero przy ruchu


# tworzę sobie grupę przeciwników, póki co pustą
przeciwnik_group = pygame.sprite.Group()

# teraz wygeneruję przeciwników w takich odstępach jakich chcę. Wcześniej napisałam ile będzie kolumn a ile wierszy
def create_przeciwnicy():
    for wiersz in range(wiersze):
        for item in range(kolumny):
            przeciwnik = Przeciwnicy(200 + item * 100, 100 + wiersz * 70 )
            # dla x: (200 -> nie będzie się zaczynać od lewego górnego tylko trochę od ekranu.
            # Następnie będzie wstawiony obiekt przeciwnik, który będzie * 100, czyli będzie co 100 odstępu)
            # dla y: będzie się zaczynać trochę poniżej krawędzi i co 70

            # po każdym wygenerowanym przeciwniku, dodaję go do grupy
            przeciwnik_group.add(przeciwnik)

create_przeciwnicy()

przeciwinik_group.update()
przeciwnik_group.draw(screen)
