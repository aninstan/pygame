import pygame
from vec2 import Vec2
import animation
from spritesheet import SpriteSheet
from game_classes import Weapon
from character import Character
from constants import WEAPON_ROTATE_RESOLUTION


tile_img = pygame.image.load("assets/floortile2.png")

player_sprite_sheet_image = pygame.image.load('assets/character_animations.png')
player_sprite_sheet = SpriteSheet(player_sprite_sheet_image)
player_animation_list = animation.AnimationList(player_sprite_sheet, [4, 4, 4, 4, 4, 4, 4, 4], 20, 30)
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

bullet_img = pygame.image.load("./assets/bullet.png")


gun = Weapon(Vec2(0, 0), Vec2(31, -7), 15, rotated_gun_array, bullet_img)
flare_gun = Weapon(Vec2(0, 0), Vec2(10, -5), 15, rotated_flare_gun_array, bullet_img)

player = Character(Vec2(-10, -15), Vec2(16, 26), 6, player_animation_list, player_hand_img, flare_gun)
