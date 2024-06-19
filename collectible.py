import pygame

class CollectibleItem:
    def __init__(self, x, y, screen, aux):
        self.aux = 0
        self._screen = screen
        self.x = x
        self.y = y
        self.width = 26  # Largura do item
        self.height = 26  # Altura do item
        self.color = (255, 0, 0)  # Cor do item

    def check_collision(self, player):
        if (
            self.x < player.x + player.width
            and self.x + self.width > player.x
            and self.y < player.y + player.height
            and self.y + self.height > player.y
        ):
            return True
        return False

    def draw(self, screen, aux):
        #pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        if aux == 0:
            enemy_image = pygame.image.load("garrafa_plastica.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif aux == 1:
            enemy_image = pygame.image.load("Lata.metal.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif aux == 2:
            enemy_image = pygame.image.load("Papel.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif aux == 3:
            enemy_image = pygame.image.load("vidro.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif aux == 4:
            enemy_image = pygame.image.load("organico.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()
