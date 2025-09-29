import pygame
from os.path import join
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self, dt):
         keys = pygame.key.get_pressed()
         self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
         self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
         self.direction = self.direction.normalize() if self.direction else self.direction
         self.rect.center += self.direction * self.speed * dt
         
        #  recent_keys = pygame.key.get_just_pressed()
        #  if recent_keys[pygame.K_SPACE]:
        #     print("Fire the Lasers!")

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image =  surf
        self.rect = self.image.get_frect(center = (randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)))
      
# general setup
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True
clock = pygame.time.Clock()

# plain surface
surf = pygame.Surface((100,200))
surf.fill('mediumseagreen')
x = 100
y = 150

# All Sprites
all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
# star = Star(all_sprites)
for i in range(20):
    Star(all_sprites, star_surf)
# player 
player = Player(all_sprites)

# meteor
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# laser
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (WINDOW_WIDTH - 1260, WINDOW_HEIGHT - 20))


# game start
while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# draw the game

    all_sprites.update(dt)

    # set game background color
    display_surface.fill('darkgrey')
    

    # draw meteor
    display_surface.blit(meteor_surf, meteor_rect)
    # draw laser
    display_surface.blit(laser_surf, laser_rect)
    # draw player
    all_sprites.draw(display_surface)


    pygame.display.update()
pygame.quit()
