import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True

# plain surface
surf = pygame.Surface((100,200))
surf.fill('mediumseagreen')
x = 100
y = 150

# player 
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4))
player_direction = 1

# star
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)) for i in range(20)]

# meteor
meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# laser
laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (WINDOW_WIDTH - 1260, WINDOW_HEIGHT - 20))



# game start
while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# draw the game
    # set game background color
    display_surface.fill('darkgrey')
    # draw stars in random int locations on background
    for pos in star_positions:
        display_surface.blit(star_surf,pos)

    # draw meteor
    display_surface.blit(meteor_surf, meteor_rect)
    # draw laser
    display_surface.blit(laser_surf, laser_rect)
    
    # player movement
    player_rect.x +=player_direction * 0.4
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction *= -1
   
    # draw player
    display_surface.blit(player_surf, player_rect)
    pygame.display.update()
pygame.quit()