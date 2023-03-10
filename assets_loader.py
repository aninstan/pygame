import pygame
from vec2 import Vec2
import animation
from spritesheet import SpriteSheet
from game_classes import Weapon
from character import Character
from constants import WEAPON_ROTATE_RESOLUTION


tile1_img = pygame.image.load("assets/floortile1.png")
tile2_img = pygame.image.load("assets/floortile2.png")

player_sprite_sheet_image = pygame.image.load('assets/character_animations.png')
player_sprite_sheet = SpriteSheet(player_sprite_sheet_image)
player_animation_list = animation.AnimationList(player_sprite_sheet, [4, 4, 4, 4, 4, 4, 4, 4], 20, 21)
player_hand_img = pygame.image.load("assets/hand.png")

bullet_enemy_sprite_sheet_image = pygame.image.load("assets/bullet_enemy_animation.png")
bullet_enemy_sprite_sheet = SpriteSheet(bullet_enemy_sprite_sheet_image)
bullet_enemy_animation_list = animation.AnimationList(bullet_enemy_sprite_sheet, [4], 17, 30)
bullet_enemy_hand_img = pygame.image.load("assets/bullet_enemy_hand.png")

gun_img = pygame.image.load("assets/gun.png")
rotated_gun_array = animation.create_rotated_image_array(gun_img, Vec2(13, 12), WEAPON_ROTATE_RESOLUTION)

flare_gun_img = pygame.image.load("assets/flare_gun.png")
flipped_flare_gun_img = pygame.transform.flip(flare_gun_img, False, True)
rotated_flare_gun_array = animation.create_rotated_image_array(flare_gun_img, Vec2(2, 5), WEAPON_ROTATE_RESOLUTION)

player_bullet_img = pygame.image.load("./assets/bullet.png")
enemy_bullet_img = pygame.image.load("./assets/enemy_bullet.png")

gun = Weapon(Vec2(0, 0), Vec2(31, -7), 15, rotated_gun_array, player_bullet_img)
player_flare_gun = Weapon(Vec2(0, 0), Vec2(10, -5), 15, rotated_flare_gun_array, player_bullet_img)

player = Character(Vec2(-10, -15), Vec2(16, 17), 6, 3, 300, player_animation_list, player_hand_img, player_flare_gun)

pygame.font.init()
font_location = "./assets/Grand9KPixel.ttf"
font24 = pygame.font.Font(font_location, 24)
font82 = pygame.font.Font(font_location, 82)