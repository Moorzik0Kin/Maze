import pygame

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

player = GameSprite('hero.png', 5, 420, 4)
monster = GameSprite('cyborg.png', 620, 280, 2)
final = GameSprite('treasure.png', 580, 420, 0)


wall1=pygame.Rect(250,150,25,400)
wall2=pygame.Rect(250,150,25,400)






game = True
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
# pygame.mixer.music.play()

color_wall=(0,200,0)
speed=3
fi=0
mo="l"

while game:
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

    if fi!=80 and mo=="l":
        monster.rect.x-=1.8
        fi+=1
    if fi!=-80 and mo=="r":
        monster.rect.x+=1.8
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
    pygame.draw.rect(window, color_wall,wall1)

    pygame.display.update()
    clock.tick(60)