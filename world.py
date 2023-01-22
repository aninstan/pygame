import pygame
from vec2 import Vec2
from game_classes import GameObject
from character import Character
from screen import create_screen_and_canvas
from assets_loader import tile_img
from constants import TILE_SIZE


class World:
    def __init__(self, width: int, height: int, player: Character):
        self.width = width
        self.height = height
        self.player = player
        self.screen, self.canvas = create_screen_and_canvas()
        self.offset = Vec2(int(-self.canvas.get_rect().width/2), int(-self.canvas.get_rect().height/2))
        self.floortiles: list[GameObject] = []
        for y in range(height):
            for x in range(width):
                self.floortiles.append(GameObject(Vec2(x*TILE_SIZE - TILE_SIZE*width/2, y*TILE_SIZE - TILE_SIZE*height/2), tile_img))


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

            # Scale mouse pos to match position on canvas, not screen
            mouse_pos = Vec2(mouse_pos[0]*self.canvas.get_rect().width/self.screen.get_rect().width, mouse_pos[1]*self.canvas.get_rect().height/self.screen.get_rect().height)

            # Point weapon towards mouse
            self.player.weapon.direction = Vec2(self.offset.x + mouse_pos.x - self.player.weapon.pos.x - self.player.weapon.tip_offset.x, self.offset.y + mouse_pos.y - self.player.weapon.pos.y - self.player.weapon.tip_offset.y)


        elif event.type == pygame.MOUSEBUTTONDOWN:
            match event.button:
                case 1: # Left click
                    self.player.weapon.shoot()


    
    def draw(self):

        # Fill background
        self.canvas.fill((50, 50, 50))

        # Draw all game objects
        for tile in self.floortiles:
            tile.draw(self.canvas, self.offset)
        
        self.player.draw(self.canvas, self.offset)
        self.player.weapon.draw_bullets(self.canvas, self.offset)

        # Draw resized image on screen
        self.screen.blit(pygame.transform.scale(self.canvas, self.screen.get_rect().size), (0, 0))
        