import pygame
from gamesprite import GameSprite
import random

class Level:
    def __init__(self):
        self.meteors = []

        spriteSheet = pygame.image.load("Game/bigbrownmeteorspritesheet.png").convert_alpha()
        
        # make meteors sprites
        level = []

        start_x = 0
        start_y = 0
        end_x   = 819
        end_y   = 259
        s_w = 205
        s_h = 80
        for row in range(100):
            for col in range(100):
                x = start_x + s_w * ((col+1) % 2) 
                y = start_y + s_h * ((row+1) % 2)
                meteor = GameSprite(spriteSheet,s_w,s_h,(x,y,s_w,s_h))
                self.meteors.append(meteor)
                level.append([0+(col*row+col)*random.randint(200,400),500])

 
        # Go through the array above and add platforms
        self.meteorfeild_list = pygame.sprite.Group()
        for platform in level:
            meteor = self.meteors[random.randint(0,len(self.meteors)-1)]
            meteor.rect.x = platform[0]
            meteor.rect.y = platform[1]
            #plant.player = self.player
            self.meteorfeild_list.add(meteor)

        # How far this world has been scrolled left/right
        self.world_shift = 0

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.meteorfeild_list.update()
        #self.enemy_list.update()
 
    def draw(self, screen):
        # Draw everything on this level.
        self.meteorfeild_list.draw(screen)
        #self.enemy_list.draw(screen)
 
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
 
        # Go through all the sprite lists and shift
        for floorItems in self.meteorfeild_list:
            floorItems.rect.x += shift_x
 
        #for enemy in self.enemy_list:
            #enemy.rect.x += shift_x