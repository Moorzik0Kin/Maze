import pygame
pygame.init()

from time import sleep
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

width, height = 700, 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze")
background = pygame.transform.scale(pygame.image.load("background.jpg"), (width, height))

final = GameSprite('treasure.png', 600, 400, 0)
monster = GameSprite('cyborg.png', 470, 430, 2)
player = GameSprite('hero.png', 5, 420, 4)


wall1=pygame.Rect(250,150,25,400)
wall2=pygame.Rect(0,300,130,25)
wall3=pygame.Rect(125,150,350,25)
wall4=pygame.Rect(600,150,100,25)
wall5=pygame.Rect(400,150,25,75)
wall6=pygame.Rect(675,0,25,330)
wall7=pygame.Rect(400,320,300,25)
wall8=pygame.Rect(250,0,450,25)
wall9=pygame.Rect(250,475,100,25)
wall10=pygame.Rect(300,125,25,25)
wall11=pygame.Rect(450,25,25,25)

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11]


game = True
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
# pygame.mixer.music.play()
kick = pygame.mixer.Sound("kick.ogg")
money = pygame.mixer.Sound("money.ogg")

color_wall=(0,200,0)
speed=3
fi=0
mo="l"

font=pygame.font.Font(None, 20)
hello = font.render("Prees F for speed 2x. And D for 1x", True, (0, 160, 0))
text = pygame.Rect(430, 325, 100, 100)
while game:
    pygame.draw.rect(window, color_wall, text)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
        
    key =pygame.key.get_pressed()
    if key[pygame.K_LEFT] and player.rect.x>0:
        player.rect.x-=speed
    if key[pygame.K_RIGHT] and player.rect.x<630:
        player.rect.x+=speed
    if key[pygame.K_DOWN] and player.rect.y<430:
        player.rect.y+=speed
    if key[pygame.K_UP] and player.rect.y>0:
        player.rect.y-=speed
    if key[pygame.K_f]:
        speed=6
    if key[pygame.K_d]:
        speed=3

    if fi!=80 and mo=="l":
        monster.rect.y-=0.6
        fi+=1
    if fi!=-80 and mo=="r":
        monster.rect.y+=0.6
        fi-=1
    
    if fi==80:
        fi=0
        mo="r"
    if fi==-80:
        fi=0
        mo="l"


    window.blit(background,(0, 0))
    player.draw()
    monster.draw()
    final.draw()
    # pygame.draw.rect(window, color_wall,wall1)
    # pygame.draw.rect(window, color_wall,wall2)
    for j in walls:
        pygame.draw.rect(window, color_wall,j)
        if player.rect.colliderect(j):
            kick.play(3)
            sleep(2)
            game=False
    
    window.blit(hello, (430, 325))
    if player.rect.colliderect(monster):
        kick.play()
        sleep(3.0)
        game=False
    if player.rect.colliderect(final):
        money.play()
        sleep(3.0)
        game=False

    pygame.display.update()
    clock.tick(60)
