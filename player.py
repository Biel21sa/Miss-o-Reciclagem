import pygame
pygame.init()
pulo_som = pygame.mixer.Sound('jump.wav')
pulo_som.set_volume(1)
class Player:
    def __init__(self, screen_width, screen_height, screen:pygame.Surface):
        self._screen = screen
        self.width = 32
        self.height = 40
        self.x = 30
        self.y = 30
        self.vel = 3  # Velocidade diminuída
        self.jump_vel = 0  # Inicialmente, definir a velocidade de pulo como 0
        self.gravity = 0.5  # Gravidade
        self.on_ground = True
        self.delta = -7
        self._direction = None
        self._movimentation = {
            "imagem":0,
            "contador":0,
            "movimentando": False
        }

        self._movimentationR = {
            "imagem":3,
            "contador":0,
            "movimentando": False
        }

        self._movimentationL = {
            "imagem":6,
            "contador":0,
            "movimentando": False
        }

    def verify_movR(keys):
        return (keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_LEFT] or keys[pygame.K_a])

    def verify_movL(keys):
        return (keys[pygame.K_UP] or keys[pygame.K_SPACE]
                or keys[pygame.K_RIGHT] or keys[pygame.K_d])

    def verify_mov(keys):
        return (keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_LEFT] or keys[pygame.K_a]
                or keys[pygame.K_RIGHT] or keys[pygame.K_d])

    def up_key(self, keys):
        if keys[pygame.K_UP] and self.on_ground or keys[pygame.K_SPACE] and self.on_ground:
            pulo_som.play()
            self.jump_vel = self.delta  # Iniciar o pulo
        
        if(Player.verify_mov(keys)):
            self._movimentation["movimentando"] = True
        else:
            self._movimentation["movimentando"] = False

        if (Player.verify_movR(keys)):
            self._movimentationR["movimentando"] = True
        else:
            self._movimentationR["movimentando"] = False 

        if (Player.verify_movL(keys)):
            self._movimentationL["movimentando"] = True
        else:
            self._movimentationL["movimentando"] = False

        self.jump_vel += self.gravity
        self.y += self.jump_vel

    def left_key(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.vel
            self._direction = "left"

        if(Player.verify_mov(keys)):
            self._movimentation["movimentando"] = True
        else:
            self._movimentation["movimentando"] = False

        if (Player.verify_movR(keys)):
            self._movimentationR["movimentando"] = True
        else:
            self._movimentationR["movimentando"] = False 
        
        if (Player.verify_movL(keys)):
            self._movimentationL["movimentando"] = True
        else:
            self._movimentationL["movimentando"] = False

        if self.x < 0:
            self.x = 0
        elif self.x > 800 - self.width:
            self.x = 800 - self.width

        if self.y >= 600 - self.height:
            self.y = 600 - self.height
            self.jump_vel = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def rigth_key(self, keys):
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.vel
            self._direction = "rigth"

        if(Player.verify_mov(keys)):
            self._movimentation["movimentando"] = True
        else:
            self._movimentation["movimentando"] = False

        if (Player.verify_movR(keys)):
            self._movimentationR["movimentando"] = True
        else:
            self._movimentationR["movimentando"] = False 

        if (Player.verify_movL(keys)):
            self._movimentationL["movimentando"] = True
        else:
            self._movimentationL["movimentando"] = False

        if self.x < 0:
            self.x = 0
        elif self.x > 800 - self.width:
            self.x = 800 - self.width

        if self.y >= 600 - self.height:
            self.y = 600 - self.height
            self.jump_vel = 0
            self.on_ground = True
        else:
            self.on_ground = False

    def draw(self, screen):
        if self._direction == None:
            if self._movimentation["movimentando"] == True or self._movimentation["imagem"] == 0:
                person_image = pygame.image.load("personagem\sprite_0.png").convert_alpha()
                scaled_image = pygame.transform.scale(person_image, (self.width, self.height))
                if self._movimentation["contador"] > 10:
                     self._movimentation["imagem"] = 1
                     self._movimentation["contador"] = 0
            elif self._movimentation["imagem"] == 1:
                person_image = pygame.image.load("personagem\sprite_1.png").convert_alpha()
                scaled_image = pygame.transform.scale(person_image, (self.width, self.height))
                if self._movimentation["contador"] > 10:
                     self._movimentation["imagem"] = 0
                     self._movimentation["contador"] = 0
        
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()

        elif self._direction == 'left':
            if self._movimentationL["movimentando"] == True or self._movimentationL["imagem"] == 6:
                person_image = pygame.image.load("personagem\sprite_6.png").convert_alpha()
                scaled_image = pygame.transform.scale(person_image, (self.width, self.height))
                if self._movimentationL["contador"] > 7:
                    self._movimentationL["imagem"] = 7
                    self._movimentationL["contador"] = 0
            elif self._movimentationL["imagem"] == 7:
                person_image = pygame.image.load("personagem\sprite_7.png").convert_alpha()
                scaled_image = pygame.transform.scale(person_image, (self.width, self.height))
                if self._movimentationL["contador"] > 7:
                    self._movimentationL["imagem"] = 6
                    self._movimentationL["contador"] = 0
           
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()
            self._direction = None

        elif self._direction == "rigth":
            if self._movimentationR["movimentando"] == True or self._movimentationR["imagem"] == 3:
                person_image = pygame.image.load("personagem\sprite_3.png").convert_alpha()
                scaled_image = pygame.transform.scale(person_image, (self.width, self.height))
                if self._movimentationR["contador"] > 7:
                    self._movimentationR["imagem"] = 4
                    self._movimentationR["contador"] = 0
            elif self._movimentationR["imagem"] == 4:
                person_image = pygame.image.load("personagem\sprite_4.png").convert_alpha()
                scaled_image = pygame.transform.scale(person_image, (self.width, self.height))
                if self._movimentationR["contador"] > 7:
                    self._movimentationR["imagem"] = 3
                    self._movimentationR["contador"] = 0
            
            self._screen.blit(scaled_image, (self.x, self.y))
            pygame.display.flip()
            self._direction = None
        self._movimentation["contador"] = self._movimentation["contador"] + 1
        self._movimentationL["contador"] = self._movimentationL["contador"] + 1
        self._movimentationR["contador"] = self._movimentationR["contador"] + 1