import pygame
import spritesheets

##
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')
##

sprite_sheet_image = pygame.image.load('assets/character_idle.png').convert_alpha()
sprite_sheet = spritesheets.SpriteSheet(sprite_sheet_image)

BLACK = (0, 0, 0)
###
BG = (50, 50, 50)
###

animation_list = []
animation_steps = [4, 4, 4, 4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for i in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 20, 30, 3, BG))
        step_counter += 1
    animation_list.append(temp_img_list)


#frame_0 = sprite_sheet.get_image(0, 20, 30, 3, BLACK)
#frame_1 = sprite_sheet.get_image(1, 20, 30, 3, BLACK)
#frame_2 = sprite_sheet.get_image(2, 20, 30, 3, BLACK)
#frame_3 = sprite_sheet.get_image(3, 20, 30, 3, BLACK)

##
run = True
while run:

	#update background
    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0

    screen.blit(animation_list[action][frame], (100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()