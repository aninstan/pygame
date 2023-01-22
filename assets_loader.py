import pygame
from spritesheet import SpriteSheet
from animation import AnimationList


tile_img = pygame.image.load("assets/testtile20px.png")

player_sprite_sheet_image = pygame.image.load('assets/character_animations.png')
player_sprite_sheet = SpriteSheet(player_sprite_sheet_image)
player_animation_list = AnimationList(player_sprite_sheet, [4, 4, 4, 4, 4, 4, 4, 4])

ak47_img = pygame.image.load("assets/ak47.png")

duo_img = pygame.image.load("./assets/buffed_bird_yes.png")
