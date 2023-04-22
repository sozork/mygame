from pygame import *

run = True
player_speed = 0
clock = time.Clock()
fps = 30

window = display.set_mode((700, 500))
display.set_caption("game")
bg = transform.scale(image.load("images/fon.jpg") , (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speedd, player_w, player_h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speedd
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = player_w
        self.height = player_h
        global player_speed
        player_speed = player_speedd

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    

    def update(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 355:
            self.rect.y += self.speed

class Player2(GameSprite):
    

    def update(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 355:
            self.rect.y += self.speed

player = Player("images/palka.png", 10, 210, 5, 20, 80)
player2 = Player2("images/palka.png", 670, 210, 5, 20, 80)
class Ball(GameSprite):
    
    speed_x = player_speed
    speed_y = player_speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x <= 0:
            self.rect.x = 1
            self.speed_x = self.speed_x*-1
        if self.rect.x >= 640:
            self.rect.x = 639
            self.speed_x = self.speed_x*-1
        if self.rect.y <= 0:
            self.rect.y = 1
            self.speed_y = self.speed_y*-1
        if self.rect.y >= 440:
            self.rect.y = 439
            self.speed_y = self.speed_y*-1
        
        
            

ball = Ball("images/ball.png", 350, 250, 2, 60, 60)

while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    
    if sprite.collide_rect(ball, player):
        ball.rect.x += 10
        ball.speed_x = ball.speed_x*-1
        ball.speed_y = ball.speed_y*-1

    if sprite.collide_rect(ball, player2):
        ball.rect.y += 10
        ball.speed_x = ball.speed_x*-1
        ball.speed_y = ball.speed_y*-1
        

    window.blit(bg, (0, 0))

    player.reset()
    player.update()
    ball.reset()
    ball.update()
    player2.reset()
    player2.update()

    


    display.update()
    clock.tick(fps)     