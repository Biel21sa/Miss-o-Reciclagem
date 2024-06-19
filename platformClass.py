import pygame

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self, screen):
        plataform_image = pygame.image.load("Plataform_edit.png").convert_alpha()
        i = 0
        image_width = 42
        while(i <= self.width):
            scaled_image = pygame.transform.scale(plataform_image, (image_width, self.height))
            screen.blit(scaled_image, (self.x+i, self.y))
            i = i + image_width

        # pygame.draw.rect(screen, (35, 160, 38), (self.x, self.y, self.width, self.height))