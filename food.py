import pygame

class Food(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super(Food, self).__init__()
        self.surf = pygame.image.load(image)
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        self.x = x
        self.y = y
        self.rect.centerx = x
        self.rect.centery = y

        self.gravitiy = 3

    def update(self):
        self.y += self.gravitiy
        self.rect.centery = round(self.y)

        if self.y > 805:
            self.kill()

    def Move(self, x, y):
        self.x = x
        self.y = y
        self.rect.centerx = round(self.x)
        self.rect.centery = round(self.y)
