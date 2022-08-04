import pygame

class Cart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Cart, self).__init__()
        self.surf = pygame.image.load("cart.png")
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.rect = self.surf.get_rect()
        self.x = x
        self.y = y
        self.rect.centerx = round(self.x)
        self.rect.centery = round(self.y)
