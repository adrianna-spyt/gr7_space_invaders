import os
import pygame

class gra():
    def __init__(self):
        self.running=True
        self.szerokosc_ekranu=900
        self.wysokosc_ekranu=600
        pygame.init()
        self.ekran=pygame.display.set_mode((self.szerokosc_ekranu,self.wysokosc_ekranu))
        self.tlo=pygame.image.load("tlo.png")
        self.ekran.blit(self.tlo,(0,0))
        self.gracz=pygame.image.load("gracz.png")
        self.gracz.set_colorkey((0,0,0))
        self.pozycja_gracza_x=450
        self.pozycja_gracza_y=500
        self.krok=10
        self.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
        pygame.display.update()
    def event(self):
        while self.running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                    break
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        self.running=False
                        break
                    elif event.key==pygame.K_LEFT:
                        if self.pozycja_gracza_x>=10:
                            self.pozycja_gracza_x-=self.krok
                            self.ekran.blit(self.tlo,(0,0))
                            self.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
                            pygame.display.update()
                    elif event.key==pygame.K_RIGHT:
                        if self.pozycja_gracza_x<=self.szerokosc_ekranu-50:
                            self.pozycja_gracza_x+=self.krok
                            self.ekran.blit(self.tlo,(0,0))
                            self.ekran.blit(self.gracz,(self.pozycja_gracza_x,self.pozycja_gracza_y))
                            pygame.display.update()
if __name__=="__main__":
    spaceinvaders=gra()
    spaceinvaders.event()

# def obraz(nazwa,colorkey=None,scale=1):
#     pelna_nazwa=os.path.join(data_dir,nazwa)
#     obraz=pg.image.load(pelna_nazwa)
#     rozmiar=obraz.get_size
#
# main_dir=os.path.split(os.path.abspath(gra.py))[0]
# data_dir=os.path.join(main_dir,"data")
