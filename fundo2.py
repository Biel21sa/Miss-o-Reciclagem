import pygame
from pygame.locals import *
import sys 
import os
from random import randrange
from button import Button
import game


diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'assets')
diretorio_sons = os.path.join(diretorio_principal,'sons')

ALTURA = 600
LARGURA = 800

AZUL = ('#87CEEB')
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

pygame.font.init()
fonte = pygame.font.SysFont('Press Start 2P',40,False,False)

tela = pygame.display.set_mode((LARGURA,ALTURA))

pygame.display.set_caption('Missão Reciclagem')


sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'birds.png')).convert_alpha()


class Chao(pygame.sprite.Sprite):
    def __init__(self,pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.spriteChao = []
        self.spriteChao.append(pygame.image.load("assets/grass_block.png"))
        self.image = self.spriteChao[0]
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 62
        self.rect.x = pos_x * 64
        self.image =  pygame.transform.scale(self.image, (250/3,250/3))

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -=10

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_birds = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 83,7),(83,68))
            self.imagens_birds.append(img)

        self.index_lista = 0
        self.image = self.imagens_birds[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 500, 500)
        self.rect.x = LARGURA - randrange(30,400, 100)

    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.12
        self.image = self.imagens_birds[int(self.index_lista)]

        if self.rect.topleft[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(50, 300, 100)
        self.rect.x -=10

class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*83,0),(83,83))
        self.image = pygame.transform.scale(self.image, (83*1, 83*1))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(1, 100, 1)
        self.rect.x = LARGURA - randrange(30,400, 100)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(50, 300, 100)
        self.rect.x -=10


todas_as_sprites = pygame.sprite.Group()

for i in range (4):
    bird = Bird()
    todas_as_sprites.add(bird)

for i in range (3):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

todas_as_sprites.add(nuvem)

for i in range(1250*2//61):
    chao = Chao(i)
    todas_as_sprites.add(chao)
 ###botoes###
    def play():
        game.start_game(tela)
            
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        tela.fill("white")

        OPTIONS_TEXT = get_font(28).render("Aqui será a tela de opções.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 260))
        tela.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(390, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()
MENU_MOUSE_POS = pygame.mouse.get_pos()
####FIM BOTÕES###

relogio = pygame.time.Clock()
def main_menu():
    while True:
        relogio.tick(30)
        tela.fill(AZUL)
        titulo = ('Missão Reciclagem')
        texto_formatado = fonte.render(titulo, True,(255,255,255))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 330), 
                                text_input="PLAY", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400), 
                                text_input="OPTIONS", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 480), 
                                text_input="QUIT", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(tela)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        pygame.display.update()
        todas_as_sprites.draw(tela)
        tela.blit(texto_formatado,(275,150))
        todas_as_sprites.update()
        pygame.display.flip()
 
main_menu()