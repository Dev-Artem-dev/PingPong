from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x,size_y,player_speed):
        super().__init__()

        #images
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed

        #rect
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

#window
window = display.set_mode((500, 500))
display.set_caption("Ping Pong")
window.fill((152, 251, 152))

#sprites
racketr = Player("Снимок.JPG", 10, 100, 20, 100, 1)
racketl = Player("Снимок.JPG", 410, 100, 20, 100, 1)
ball = Player("Снимок.JPG", 410, 100, 20, 100, 1)

#game cycle
game = True
finish = False
clock = time.Clock()
FPS = 61

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    #update
    if finish != True:
        window.fill((152, 251, 152))

        racketr.update_r()
        racketl.update_l()

        racketr.reset()
        racketl.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)


#end