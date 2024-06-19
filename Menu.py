import pygame
from pygame.locals import *
import sys
import os
from random import randrange
from button import Button
from player import Player
from platformClass import Platform
from collectible import CollectibleItem
from enemy import Enemy
from lixeiras import TrashCan

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'assets')
diretorio_sons = os.path.join(diretorio_principal, 'sons')

ALTURA = 600
LARGURA = 800

AZUL = ('#87CEEB')


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


pygame.font.init()
fonte = pygame.font.SysFont('Press Start 2P', 40, False, False)

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption('Missão Reciclagem')


sprite_sheet = pygame.image.load(os.path.join(
    diretorio_imagens, 'birds.png')).convert_alpha()


class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.spriteChao = []
        self.spriteChao.append(pygame.image.load("assets/grass_block.png"))
        self.image = self.spriteChao[0]
        self.rect = self.image.get_rect()
        self.rect.y = ALTURA - 62
        self.rect.x = pos_x * 64
        self.image = pygame.transform.scale(self.image, (250/3, 250/3))

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
        self.rect.x -= 10


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_birds = []
        for i in range(3):
            img = sprite_sheet.subsurface((i * 83, 8), (80, 76))
            self.imagens_birds.append(img)

        self.index_lista = 0
        self.image = self.imagens_birds[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 500, 500)
        self.rect.x = LARGURA - randrange(30, 400, 100)

    def update(self):
        if self.index_lista > 2.8:
            self.index_lista = 0
        self.index_lista += 0.12
        self.image = self.imagens_birds[int(self.index_lista)]

        if self.rect.topleft[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(50, 300, 100)
        self.rect.x -= 10


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((3*83, 0), (83, 83))
        self.image = pygame.transform.scale(self.image, (83*1, 83*1))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(1, 100, 1)
        self.rect.x = LARGURA - randrange(30, 400, 100)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = LARGURA
            self.rect.y = randrange(50, 300, 100)
        self.rect.x -= 10


todas_as_sprites = pygame.sprite.Group()

for i in range(4):
    bird = Bird()
    todas_as_sprites.add(bird)

for i in range(3):
    nuvem = Nuvens()
    todas_as_sprites.add(nuvem)

todas_as_sprites.add(nuvem)

for i in range(1250*2//61):
    chao = Chao(i)
    todas_as_sprites.add(chao)
 ### botoes###

 ####sons####
pygame.init()
vitoria_som = pygame.mixer.Sound('vitoria_som.wav')
colidiu_som = pygame.mixer.Sound('colisao.wav')
coletou_som = pygame.mixer.Sound('coletou.wav')
pulo_som = pygame.mixer.Sound('jump.wav')
musica_de_fundo = pygame.mixer.music.load('tema de fundo.mp3')
pygame.mixer.music.play(-1)
click_som = pygame.mixer.Sound('click.wav')
pygame.mixer.music.set_volume(0.5)
colidiu_som.set_volume(0.4)
vitoria_som.set_volume(0.1)



 ####fim sons####
def play():
    pygame.display.set_caption("Missão Reciclagem")
    # Variável para controlar o estado do jogo

    # Configurações da tela
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    buffer = pygame.Surface((screen_width, screen_height))
    aux = 0
    time = 0
    flag = 0

    # Cores
    blue = (170, 231, 253)

    # Configuração do FPS
    clock = pygame.time.Clock()
    fps = 60

    # Configuração do jogador
    player = Player(screen_width, screen_height, buffer)

    player_colidiu = False
    pisca = 0


    # Configuração das plataformas
    platforms = [
            Platform(0, screen_height - 500, 705, 15),
            Platform(80, screen_height - 400, 800, 15),
            Platform(0, screen_height - 300, 370, 15),
            Platform(450, screen_height - 300, 265, 15),
            Platform(400, screen_height - 200, 320, 15),
            Platform(0, screen_height - 200, 100, 15),
            Platform(170, screen_height - 200, 160, 15),
            Platform(70, screen_height - 100, 500, 15),
            Platform(650, screen_height - 100, 160, 15),
            Platform(0, screen_height - 4, 800, 15),
            Platform(760, screen_height - 450, 40, 15),
            Platform(0, screen_height - 350, 40, 15),
            Platform(760, screen_height - 250, 40, 15),
            Platform(760, screen_height - 150, 40, 15),
            Platform(0, screen_height - 50, 40, 15),
            Platform(550, screen_height - 100, 100, 15)
        # ... adicione mais plataformas conforme necessário ...
    ]

    # Lista de coordenadas dos itens colecionáveis (x, y)
    collectible_coordinates = [
            (150, 150),
            (250, 250),
            (350, 350),
            (450, 450),
            (350, 550),
            (100, 350),
            (350, 50),
            (350, 150),
            (150, 550),
            (550, 250)
        # Adicione mais coordenadas conforme necessário
    ]
    lixeiras = [
        TrashCan(500, 550, buffer, 0),
        TrashCan(550, 550, buffer, 1),
        TrashCan(600, 550, buffer, 2),
        TrashCan(650, 550, buffer, 3),
        TrashCan(700, 550, buffer, 4),
    ]

    # Configuração dos inimigos
    enemies = [
            Enemy(300, screen_height - 520, 300, 700, buffer, aux),
            Enemy(500, screen_height - 420, 400, 800, buffer, aux),
            Enemy(500, screen_height - 320, 450, 715, buffer, aux),
            Enemy(100, screen_height - 420, 80, 400, buffer, aux),
            Enemy(100, screen_height - 320, 0, 370, buffer, aux),
            Enemy(0, screen_height - 220, 0, 100, buffer, aux),
            Enemy(250, screen_height - 220, 170, 330, buffer, aux),
            Enemy(70, screen_height - 120, 80, 570, buffer, aux),
            Enemy(550, screen_height - 120, 550, 800, buffer, aux),
            Enemy(100, screen_height - 20, 0, 370, buffer, aux),
            Enemy(400, screen_height - 220, 400, 720, buffer, aux)
        # Adicione mais inimigos conforme necessário
    ]

    # Configuração dos itens colecionáveis
    collectible_items = [CollectibleItem(x, y, buffer, aux)
                        for x, y in collectible_coordinates]

    # Duração total do jogo em segundos
    total_seconds = 4000
    current_seconds = total_seconds

    # Configuração da fonte de texto
    font = pygame.font.Font(None, 36)
    text_color = (255, 255, 255)

    # Variável para controlar a pontuação do jogador
    score = 0

    
    running = True
    while running:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if player.y < 0:
            player.y = 0

        player.up_key(keys)
        player.left_key(keys)
        player.rigth_key(keys)

        for platform in platforms:
            has_platform_over = player.y + player.height >= platform.y
            verify_current_height = player.y + player.height <= platform.y + platform.height
            if has_platform_over and verify_current_height and player.x + player.width >= platform.x and player.x <= platform.x + platform.width:
                player.on_ground = True
                if player.y - player.height - player.delta < platform.y:
                    player.y = platform.y - player.height
                    player.jump_vel = 0

        # Atualize a posição dos inimigos
        for enemy in enemies:
            enemy.move()

        # Verifique a colisão com os inimigos
        for enemy in enemies:
            if enemy.check_collision(player):
                colidiu_som.play()
                player_colidiu = True
                score = 0  # Reduza a pontuação do jogador para zero
                # Restaure os itens colecionáveis aos seus lugares originais
                collectible_items = [CollectibleItem(
                    x, y, buffer, aux) for x, y in collectible_coordinates]

        # Verifique a colisão com os itens colecionáveis e colete-os
        items_to_remove = []
        for item in collectible_items:
            if item.check_collision(player):
                coletou_som.play()
                items_to_remove.append(item)
                score += 100  # Aumente a pontuação em 100 pontos

        # Remova os itens coletados da lista de itens colecionáveis
        for item in items_to_remove:
            collectible_items.remove(item)

        # Atualize o tempo restante
        current_seconds = max(0, current_seconds - 1)

        # Calcule minutos e segundos restantes
        minutes = current_seconds // 60
        seconds = current_seconds % 60

        buffer.fill(blue)

        for platform in platforms:
            platform.draw(buffer)

        for item in collectible_items:
            item.draw(buffer, aux)

        for i, lixeira in enumerate(lixeiras):
            lixeira.draw(buffer, i)

        LIXEIRA1 = get_font(20).render("1", True, "Black")
        LIXEIRA1_RECT = LIXEIRA1.get_rect(center=(525, 535))
        buffer.blit(LIXEIRA1, LIXEIRA1_RECT)

        LIXEIRA2 = get_font(20).render("2", True, "Black")
        LIXEIRA2_RECT = LIXEIRA2.get_rect(center=(575, 535))
        buffer.blit(LIXEIRA2, LIXEIRA2_RECT)

        LIXEIRA3 = get_font(20).render("3", True, "Black")
        LIXEIRA3_RECT = LIXEIRA3.get_rect(center=(625, 535))
        buffer.blit(LIXEIRA3, LIXEIRA3_RECT)

        LIXEIRA4 = get_font(20).render("4", True, "Black")
        LIXEIRA4_RECT = LIXEIRA4.get_rect(center=(675, 535))
        buffer.blit(LIXEIRA4, LIXEIRA4_RECT)

        LIXEIRA5 = get_font(20).render("5", True, "Black")
        LIXEIRA5_RECT = LIXEIRA5.get_rect(center=(725, 535))
        buffer.blit(LIXEIRA5, LIXEIRA5_RECT)

        for enemy in enemies:
            enemy.draw(buffer, aux)

        if player_colidiu:
            pisca = pisca + 1
            if pisca % 10:
                player.draw(buffer)
            if pisca > 70:
                player_colidiu = False
                pisca = 0

        if not player_colidiu:
            player.draw(buffer)

        # Exiba o tempo na tela
        time_text = font.render(
            f"Tempo: {minutes:02}:{seconds:02}", True, text_color)
        buffer.blit(time_text, (10, 10))

        # Exiba a pontuação na tela
        score_text = font.render(f"Pontuação: {score}", True, text_color)
        buffer.blit(score_text, (600, 10))

        ajuda = pygame.key.get_pressed()

        if ajuda[pygame.K_i] == True:
            help_tela = pygame.image.load("Screenshot_1.png")
            buffer.blit(help_tela, (400, 300))
        

        # Verifique a condição de derrota
        if current_seconds == 0:
            flag = flag + score
            while True:
                
                OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
                screen.fill("white")

                LOSS_TEXT = get_font(40).render("Você Perdeu!!!", True, "Black")
                LOSS_RECT = LOSS_TEXT.get_rect(center=(400, 260))
                screen.blit(LOSS_TEXT, LOSS_RECT)

                SCORE_TEXT = get_font(35).render(f"Pontuação: {flag}", True, "Black")
                SCORE_RECT = SCORE_TEXT.get_rect(center=(400, 360))
                screen.blit(SCORE_TEXT, SCORE_RECT)

                OPTIONS_BACK = Button(image=None, pos=(390, 460),
                                    text_input="Reiniciar", font=get_font(28), base_color="Black", hovering_color="Green")

                OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
                OPTIONS_BACK.update(screen)
                

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                            pygame.mixer.music.play()
                            main_menu()
                    
                    pygame.display.update()
                pygame.mixer.music.stop()
                
        key = pygame.key.get_pressed()
        
        # Verifique a condição de vitória
        if player.y == 556 and key[pygame.K_KP1] or player.y == 556 and key[pygame.K_KP2] or player.y == 556 and key[pygame.K_KP3] or player.y == 556 and key[pygame.K_KP4] or player.y == 556 and key[pygame.K_KP5]:
            if aux == 0 and key[pygame.K_KP1]:
                score = score + 100
            if aux == 1 and key[pygame.K_KP2]:
                score = score + 100
            if aux == 2 and key[pygame.K_KP3]:
                score = score + 100
            if aux == 3 and key[pygame.K_KP4]:
                score = score + 100
            if aux == 4 and key[pygame.K_KP5]:
                score = score + 100

            flag = flag + score

            condicao = True
            while condicao:
                pygame.mixer.music.stop()
                vitoria_som.play()
        
                OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

                screen.fill("white")

                WIN_TEXT = get_font(40).render("Você Ganhou!!!", True, "Black")
                WIN_RECT = WIN_TEXT.get_rect(center=(400, 260))
                screen.blit(WIN_TEXT, WIN_RECT)

                SCORE_TEXT = get_font(35).render(f"Pontuação: {flag}", True, "Black")
                SCORE_RECT = SCORE_TEXT.get_rect(center=(400, 360))
                screen.blit(SCORE_TEXT, SCORE_RECT)

                OPTIONS_BACK = Button(image=None, pos=(390, 460),
                                    text_input="Continuar", font=get_font(28), base_color="Black", hovering_color="Green")

                OPTIONS_MENU = Button(image=None, pos=(390, 660),
                                    text_input="Voltar ao menu", font=get_font(28), base_color="Black", hovering_color="Green")

                OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
                OPTIONS_MENU.changeColor(OPTIONS_MOUSE_POS)
                OPTIONS_BACK.update(screen)
                OPTIONS_MENU.update(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS) and aux != 4:
                            pygame.mixer.music.play()
                            condicao = False
                            collectible_items = [CollectibleItem(x, y, buffer, aux)
                        for x, y in collectible_coordinates]
                            score = 0
                            time = time + 300
                            player.x = 0
                            player.y = 0
                            aux = aux + 1
                            current_seconds = 3600 - time
                        elif OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS) and aux == 4:
                            pygame.mixer.music.play()
                            main_menu()
     


                pygame.display.update()
                pygame.display.flip()
        
        pygame.display.update()
        screen.blit(buffer, (0, 0))
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

def options():
    def imgT1():
        tela.blit(redT1,(ALTURA/2,LARGURA))

    def imgT2():
        tela.blit(redT1,(ALTURA/2,LARGURA))
        
    def imgT3():
        tela.blit(redT1,(ALTURA/2,LARGURA))
    imgL = 800/1.5
    imgA = 600/2
    imgT1 = (pygame.image.load('assets/Tutorial1.png'))
    redT1 = pygame.transform.scale(imgT1,(imgL,imgA))

    imgT2 = (pygame.image.load('assets/Tutorial2.png'))
    redT2 = pygame.transform.scale(imgT2,(imgL,imgA))

    imgT3 = (pygame.image.load('assets/Tutorial3.png'))
    redT3 = pygame.transform.scale(imgT3,(imgL,imgA))

    imgT4 = (pygame.image.load('assets/Tutorial4.png'))
    redT4 = pygame.transform.scale(imgT4,(imgL,imgA))

    #imgT5 = (pygame.image.load('assets/Tutorial5.png'))
    #redT5 = pygame.transform.scale(imgT5,(imgL,imgA))
    
    

    button_pressed = "button1"

    image_temp = redT1


    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        TUTORIAL_MOUSE_POS = pygame.mouse.get_pos()
        tela.fill("black")
        OPTIONS_TEXT = get_font(40).render("Como jogar", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 30))


        TUTORIAL_BUTTON1 = Button(image=pygame.image.load("assets/Tutorial Rect.png"), pos=(215, 500),
                            text_input="1", font=get_font(35), base_color="White", hovering_color="Green")

        TUTORIAL_BUTTON2 = Button(image=pygame.image.load("assets/Tutorial Rect.png"), pos=(350, 500),
                            text_input="2", font=get_font(35), base_color="White", hovering_color="Green")

        TUTORIAL_BUTTON3 = Button(image=pygame.image.load("assets/Tutorial Rect.png"), pos=(490, 500),
                            text_input="3", font=get_font(35), base_color="White", hovering_color="Green")
        
        TUTORIAL_BUTTON4 = Button(image=pygame.image.load("assets/Tutorial Rect.png"), pos=(650, 500),
                            text_input="4", font=get_font(35), base_color="White", hovering_color="Green")

        #TUTORIAL_BUTTON5 = Button(image=pygame.image.load("assets/Tutorial Rect.png"), pos=(675, 500),
                            #text_input="5", font=get_font(35), base_color="White", hovering_color="Green")

        OPTIONS_BACK = Button(image=None, pos=(85, 80), 
                        text_input="VOLTAR", font=get_font(20), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        TUTORIAL_BUTTON1.changeColor(TUTORIAL_MOUSE_POS)
        TUTORIAL_BUTTON2.changeColor(TUTORIAL_MOUSE_POS)
        TUTORIAL_BUTTON3.changeColor(TUTORIAL_MOUSE_POS)
        TUTORIAL_BUTTON4.changeColor(TUTORIAL_MOUSE_POS)
        #TUTORIAL_BUTTON5.changeColor(TUTORIAL_MOUSE_POS)
        TUTORIAL_BUTTON1.update(tela)
        TUTORIAL_BUTTON2.update(tela)
        TUTORIAL_BUTTON3.update(tela)
        TUTORIAL_BUTTON4.update(tela)
        #TUTORIAL_BUTTON5.update(tela)
        OPTIONS_BACK.update(tela)
        tela.blit(OPTIONS_TEXT, OPTIONS_RECT)
        img_atual = image_temp
        tela.blit(img_atual,(170,150))

        if(button_pressed == "button1"):
                img_atual = tela.blit(redT1,(170,150))
                

        if(button_pressed == "button2"):
                img_atual = tela.blit(redT2,(170,150))
                

        if(button_pressed == "button3"):
                img_atual = tela.blit(redT3,(170,150))
                

        if(button_pressed == "button4"):
                img_atual = tela.blit(redT4,(170,150))
                

        #if(button_pressed == "button5"):
                #img_atual = tela.blit(redT5,(170,150))
                

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TUTORIAL_BUTTON1.checkForInput(OPTIONS_MOUSE_POS):
                    button_pressed="button1"
                    click_som.play()
                if TUTORIAL_BUTTON2.checkForInput(OPTIONS_MOUSE_POS):
                    button_pressed="button2"
                    click_som.play()
                if TUTORIAL_BUTTON3.checkForInput(OPTIONS_MOUSE_POS):
                    button_pressed="button3"
                    click_som.play()
                if TUTORIAL_BUTTON4.checkForInput(OPTIONS_MOUSE_POS):
                    button_pressed="button4"
                    click_som.play()
                #if TUTORIAL_BUTTON5.checkForInput(OPTIONS_MOUSE_POS):
                    #button_pressed="button5"
                    #click_som.play()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click_som.play()
                    main_menu()
            pygame.display.update()

####FIM BOTÕES###

relogio = pygame.time.Clock()

def main_menu():
    while True:
        relogio.tick(30)
        tela.fill(AZUL)
        titulo = ('Missão Reciclagem')
        texto_formatado = fonte.render(titulo, True, (0, 0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 300),
                             text_input="Jogar", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 370),
                                text_input="Tutorial", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        MUTE_BUTTON = Button(image=pygame.image.load("assets/Mute Rect2.png"), pos=(50, 50),
                             text_input="", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 450),
                             text_input="Sair", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_som.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_som.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_som.play()
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
  
        
        todas_as_sprites.draw(tela)
        tela.blit(texto_formatado, (75, 150))
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(tela)
        todas_as_sprites.update()
        pygame.display.update()
        pygame.display.flip()
        
        


main_menu()
