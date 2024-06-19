import pygame

class Enemy:
    def __init__(self, x, y, left_bound, right_bound, screen:pygame.Surface, aux):
        self.aux = aux
        self._screen = screen
        self.x = x
        self.y = y
        self.width = 26
        self.height = 20
        self.vel = 2.4  # Velocidade do inimigo
        self.left_bound = left_bound  # Limite esquerdo de movimento
        self.right_bound = right_bound  # Limite direito de movimento
        self.direction = 1  # Direção inicial (1 para direita, -1 para esquerda)
        self._movimentation = {
            "imagem":0,
            "contador":0,
        }

    def move(self):
        # Verifique os limites e mude de direção, se necessário
        if self.x <= self.left_bound:
            self.direction = 1
        elif self.x + self.width >= self.right_bound:
            self.direction = -1

        # Atualize a posição do inimigo com base na direção
        self.x += self.vel * self.direction

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
        if aux == 0:
            self.vel = 2.6
        elif aux == 1:
            self.vel = 2.8
        elif aux == 2:
            self.vel = 3.0
        elif aux == 3:
            self.vel = 3.2
        elif aux == 4:
            self.vel = 3.4
        if self._movimentation["imagem"] == 0:
            enemy_image = pygame.image.load("inimigo\sprite_0.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            if self._movimentation["contador"] > 5:
                    self._movimentation["imagem"] = 1
                    self._movimentation["contador"] = 0
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))

        elif self._movimentation["imagem"] == 1:
            enemy_image = pygame.image.load("inimigo\sprite_1.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            if self._movimentation["contador"] > 5:
                    self._movimentation["imagem"] = 2
                    self._movimentation["contador"] = 0
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif self._movimentation["imagem"] == 2:
            enemy_image = pygame.image.load("inimigo\sprite_2.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            if self._movimentation["contador"] > 5:
                    self._movimentation["imagem"] = 3
                    self._movimentation["contador"] = 0
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif self._movimentation["imagem"] == 3:
            enemy_image = pygame.image.load("inimigo\sprite_3.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            if self._movimentation["contador"] > 5:
                    self._movimentation["imagem"] = 4
                    self._movimentation["contador"] = 0
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif self._movimentation["imagem"] == 4:
            enemy_image = pygame.image.load("inimigo\sprite_4.png").convert_alpha()
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            if self._movimentation["contador"] > 5:
                    self._movimentation["imagem"] = 0
                    self._movimentation["contador"] = 0
            scaled_image = pygame.transform.scale(enemy_image, (self.width, self.height))
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()        

        self._movimentation["contador"] = self._movimentation["contador"] + 1
