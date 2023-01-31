import pygame
import random
import copy
from vec2 import Vec2
from game_classes import GameObject
from character import Character
from screen import create_screen_and_canvas
from assets_loader import tile_img, bullet_enemy_animation_list, bullet_enemy_hand_img, flare_gun, enemy_bullet_img
from constants import TILE_SIZE, ANIMATION_FPS


class World:
    def __init__(self, width: int, height: int, player: Character, num_enemies: int):
        
        self.width = width
        self.height = height
        
        self.screen, self.canvas = create_screen_and_canvas()
        
        self.player = player
        
        self.offset = Vec2(int(-self.canvas.get_rect().width/2), int(-self.canvas.get_rect().height/2))
        
        self.floortiles: list[GameObject] = []
        for y in range(height):
            for x in range(width):
                self.floortiles.append(GameObject(Vec2(x*TILE_SIZE - TILE_SIZE*width/2, y*TILE_SIZE - TILE_SIZE*height/2), tile_img))
        
        self.enemies: list[Character] = []
        for i in range(num_enemies):
            self.spawn_gunner(Vec2(random.randint(- width * TILE_SIZE / 2, self.width * TILE_SIZE / 2), random.randint(- height * TILE_SIZE / 2, self.height * TILE_SIZE / 2)))
    
    def spawn_gunner(self, pos: Vec2):
        new_gun = copy.copy(flare_gun)
        new_gun.bullet_img = enemy_bullet_img
        new_gun.bullets = []
        self.enemies.append(Character(pos, Vec2(15, 25), 3, 3, bullet_enemy_animation_list, bullet_enemy_hand_img, new_gun))


    def out_of_bounds(self, object: GameObject) -> int:

        """Returns an integer with information about whether the object is out of bounds"""

        result = 0

        # West
        if (object.pos.x < self.floortiles[0].pos.x):
            result |= 8

        # East
        elif (object.pos.x + object.img.get_width() > self.floortiles[-1].pos.x + TILE_SIZE):
            result |= 2
        
        # North
        if (object.pos.y < self.floortiles[0].pos.y):
            result |= 1
        
        # South
        elif (object.pos.y + object.img.get_height() > self.floortiles[-1].pos.y + TILE_SIZE):
            result |= 4
        
        return result
    

    def fix_out_of_bounds(self, character: Character):
        character_out_of_bounds_result = self.out_of_bounds(character)

        if (character_out_of_bounds_result & 8):
            character.weapon.pos.x += abs(character.pos.x - self.floortiles[0].pos.x)
            character.pos.x = self.floortiles[0].pos.x
        
        elif (character_out_of_bounds_result & 2):
            character.weapon.pos.x -= abs(character.img.get_width() + character.pos.x - self.floortiles[-1].pos.x - TILE_SIZE)
            character.pos.x = self.floortiles[-1].pos.x - character.img.get_width() + TILE_SIZE

        if (character_out_of_bounds_result & 1):
            character.weapon.pos.y += abs(character.pos.y - self.floortiles[0].pos.y)
            character.pos.y = self.floortiles[0].pos.y
        
        elif (character_out_of_bounds_result & 4):
            character.weapon.pos.y -= abs(character.img.get_height() + character.pos.y - self.floortiles[-1].pos.y - TILE_SIZE)
            character.pos.y = self.floortiles[-1].pos.y - character.img.get_height() + TILE_SIZE


    def handle_input(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_w:
                    self.player.direction += Vec2(0, -1)

                case pygame.K_a:
                    self.player.direction += Vec2(-1, 0)

                case pygame.K_s:
                    self.player.direction += Vec2(0, 1)

                case pygame.K_d:
                    self.player.direction += Vec2(1, 0)

        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_w:
                    self.player.direction -= Vec2(0, -1)

                case pygame.K_a:
                    self.player.direction -= Vec2(-1, 0)

                case pygame.K_s:
                    self.player.direction -= Vec2(0, 1)

                case pygame.K_d:
                    self.player.direction -= Vec2(1, 0)
        

        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()

            # Scale mouse position to match position on canvas, not screen
            mouse_pos = Vec2(mouse_pos[0]*self.canvas.get_rect().width/self.screen.get_rect().width, mouse_pos[1]*self.canvas.get_rect().height/self.screen.get_rect().height)

            # Point weapon towards mouse
            self.player.point_weapon_towards(mouse_pos + self.offset)


        elif event.type == pygame.MOUSEBUTTONDOWN:
            match event.button:
                case 1: # Left click
                    self.player.weapon.shoot()


    def update(self, time, dt):
        # Change animation frame of player based on total elapsed time
        self.player.animation_frame = int((time * ANIMATION_FPS / 1000)) % 4

        if (self.player.direction.abs() > 0):
            self.player.animation_index = 4
        else:
            self.player.animation_index = 0

        # No need to update player and enemy weapon direction if player is standing still
        if (self.player.direction.abs() != 0):

            self.player.update(dt)

            player_out_of_bounds_pos_change = copy.deepcopy(self.player.pos)
            self.fix_out_of_bounds(self.player)
            player_out_of_bounds_pos_change -= self.player.pos
            
            self.offset += self.player.direction.normalized() * (dt * TILE_SIZE * self.player.speed / 1000) - player_out_of_bounds_pos_change

            for gunner in self.enemies:
                gunner.point_weapon_towards(self.player.pos + Vec2(self.player.img.get_width()/2, self.player.img.get_height()/2))

        for gunner in self.enemies:
            self.fix_out_of_bounds(gunner)
            gunner.animation_frame = int((time * ANIMATION_FPS / 1000)) % 4

            # gunner.weapon.shoot()
            gunner.weapon.update_bullets(dt)

            # Remove bullets from gunner which are out of bounds
            a = 0
            while a < len(gunner.weapon.bullets):
                if (self.out_of_bounds(gunner.weapon.bullets[a])):
                    del gunner.weapon.bullets[a]
                a += 1


        self.player.weapon.update_bullets(dt)
            

        # Remove bullets from player which are out of bounds
        a = 0
        while a < len(self.player.weapon.bullets):
            
            if self.out_of_bounds(self.player.weapon.bullets[a]):
                del self.player.weapon.bullets[a]
            else:
                a += 1

        # Remove bullets from player which hit an enemy
        a = 0
        while a < len(self.player.weapon.bullets):
            
            hit = False

            for i, enemy in enumerate(self.enemies):
                if self.player.weapon.bullets[a].collision(enemy):
                    self.player.weapon.bullets.pop(a)
                    hit = True
                    enemy.health -= 1
                    if self.enemies[i].health == 0:
                        self.enemies.pop(i)
                    break
            
            if not hit:
                a += 1

    
    def draw(self):

        # Fill background
        self.canvas.fill((50, 50, 50))

        # Draw all game objects
        for tile in self.floortiles:
            tile.draw(self.canvas, self.offset)
        
        for gunner in self.enemies:
            gunner.draw(self.canvas, self.offset)
            gunner.weapon.draw_bullets(self.canvas, self.offset)
        
        self.player.draw(self.canvas, self.offset)
        self.player.weapon.draw_bullets(self.canvas, self.offset)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = Vec2(mouse_pos[0]*self.canvas.get_rect().width/self.screen.get_rect().width, mouse_pos[1]*self.canvas.get_rect().height/self.screen.get_rect().height)

        # Draw resized image on screen
        self.screen.blit(pygame.transform.scale(self.canvas, self.screen.get_rect().size), (0, 0))
        