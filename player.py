import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.surf = pygame.image.load("select.png")
        self.surf = pygame.transform.scale(self.surf, (55, 55))
        self.rect = self.surf.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.x = x
        self.y = y

        self.speed = 6

    def update(self, keys):
        if keys[pygame.K_a] and self.x > 0:
            # decrement in x co-ordinate
            self.x -= self.speed
        # if left arrow key is pressed
        if keys[pygame.K_d] and self.x < 900:
            # increment in x co-ordinate
            self.x += self.speed
        # if left arrow key is pressed
        if keys[pygame.K_w] and self.y > 0:
            # decrement in y co-ordinate
            self.y -= self.speed
        # if left arrow key is pressed
        if keys[pygame.K_s] and self.y < 700:
            self.y += self.speed
        self.rect.centerx = round(self.x)
        self.rect.centery = round(self.y)
