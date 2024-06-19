import pygame
import sys
from player import Player
from platformClass import Platform
from collectible import CollectibleItem
from enemy import Enemy
from button import Button

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)


# Inicialização do Pygame
pygame.init()

def start_game(screen):
    pygame.display.set_caption("Missão Reciclagem")
    # Variável para controlar o estado do jogo

    # Configurações da tela
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Cores
    blue = (170, 231, 253)

    # Configuração do FPS
    clock = pygame.time.Clock()
    fps = 60

    # Configuração do jogador
    player = Player(screen_width, screen_height)
    
    player_colidiu = False
    pisca = 0

    # Configuração das plataformas
    platforms = [
        Platform(0, screen_height - 500, 705, 10),
        Platform(80, screen_height - 400, 800, 10),
        Platform(0, screen_height - 300, 370, 10),
        Platform(450, screen_height - 300, 265, 10),
        Platform(400, screen_height - 200, 320, 10),
        Platform(0, screen_height - 200, 100, 10),
        Platform(170, screen_height - 200, 160, 10),
        Platform(70, screen_height - 100, 500, 10),
        Platform(650, screen_height - 100, 160, 10),
        Platform(0, screen_height - 4, 800, 10),
        Platform(750, screen_height - 450, 50, 10),
        Platform(0, screen_height - 350, 50, 10),
        Platform(750, screen_height - 250, 50, 10),
        Platform(750, screen_height - 150, 50, 10),
        Platform(0, screen_height - 50, 50, 10)
        # ... adicione mais plataformas conforme necessário ...
    ]

    # Lista de coordenadas dos itens colecionáveis (x, y)
    collectible_coordinates = [
        (150, 150),
        (250, 250),
        (350, 350),
        (450, 450),
        (550, 550),
        (100, 350),
        (350, 50),
        (350, 150),
        (150, 550),
        (550, 250)
        # Adicione mais coordenadas conforme necessário
    ]

    # Configuração dos inimigos
    enemies = [
        Enemy(100, screen_height - 530, 30, 30, 100, 300),
        Enemy(500, screen_height - 430, 30, 30, 400, 700),
        # Adicione mais inimigos conforme necessário
    ]

    # Configuração dos itens colecionáveis
    collectible_items = [CollectibleItem(x, y) for x, y in collectible_coordinates]

    # Duração total do jogo em segundos
    total_seconds = 500
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
                player_colidiu = True
                score = 0  # Reduza a pontuação do jogador para zero
                collectible_items = [CollectibleItem(x, y) for x, y in collectible_coordinates]  # Restaure os itens colecionáveis aos seus lugares originais
    
        
        # Verifique a colisão com os itens colecionáveis e colete-os
        items_to_remove = []
        for item in collectible_items:
            if item.check_collision(player):
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

        screen.fill(blue)

        for platform in platforms:
            platform.draw(screen)

        for item in collectible_items:
            item.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        if player_colidiu:
            pisca = pisca + 1
            if pisca % 10:
                player.draw(screen)
            if pisca > 50:
                player_colidiu = False
                pisca = 0
                
        if not player_colidiu:
            player.draw(screen)
        # player.draw(screen)

        # Exiba o tempo na tela
        time_text = font.render(f"Tempo: {minutes:02}:{seconds:02}", True, text_color)
        screen.blit(time_text, (10, 10))

        # Exiba a pontuação na tela
        score_text = font.render(f"Pontuação: {score}", True, text_color)
        screen.blit(score_text, (600, 10))

        # Verifique a condição de derrota
        if current_seconds == 0 and len(collectible_items) > 0:
            jogo = True
            while jogo == True:
                OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

                screen.fill("white")

                OPTIONS_TEXT = get_font(40).render("Você Perdeu!!!", True, "Black")
                OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 260))
                screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

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
                            jogo = False
    
                pygame.display.update()
                current_seconds = 500


        # Verifique a condição de vitória
        if len(collectible_items) == 0:
            jogo = True
            while jogo == True:
                OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

                screen.fill("white")

                OPTIONS_TEXT = get_font(40).render("Você Ganhou!!!", True, "Black")
                OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(400, 260))
                screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

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
                            jogo = False
    
                pygame.display.update()
                current_seconds = 500
                
        pygame.display.update()

    pygame.quit()
    sys.exit()
