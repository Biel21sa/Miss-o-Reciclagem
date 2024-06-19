import pygame

class TrashCan:
    def __init__(self, x, y, screen, aux):
        self.x = x
        self.y = y
        self.width = 50  # Largura do item
        self.height = 50
        self.screen = screen
            

    def draw(self, screen, cor):
        if cor == 0:
            enemy_image = pygame.image.load("lixeira\sprite_0.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self.screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif cor == 1:
            enemy_image = pygame.image.load("lixeira\sprite_1.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self.screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif cor == 2:
            enemy_image = pygame.image.load("lixeira\sprite_2.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self.screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()
        
        elif cor == 3:
            enemy_image = pygame.image.load("lixeira\sprite_3.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self.screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif cor == 4:
            enemy_image = pygame.image.load("lixeira\sprite_4.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self.screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()