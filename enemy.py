import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load(image)
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect()
        self.x = x
        self.y = y
        self.rect.centerx = x
        self.rect.centery = y

        self.gravitiy = 2

    def update(self):
        self.y += self.gravitiy
        self.rect.centery = round(self.y)

        if self.y > 805:
            self.kill()
