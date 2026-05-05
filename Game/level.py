import pygame
import random
from gamesprite import GameSprite

class Level:
    def loadMeteors(self, s_w, s_h, spriteSheet):
        meteors = []
        for row in range(2):
            for col in range(2):
                rect = pygame.Rect(col * s_w, row * s_h, s_w, s_h)
                image = pygame.Surface((s_w, s_h), pygame.SRCALPHA)
                image.blit(spriteSheet, (0, 0), rect)
                mask = pygame.mask.from_surface(image)
                if mask.count() > 500: 
                    meteors.append(image)
        return meteors

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        try:
            spriteSheet = pygame.image.load("Game/bigbrownmeteorspritesheet.png").convert_alpha()
            spriteSheet2 = pygame.image.load("Game/biggraymeteorsspritesheet.png").convert_alpha()
        except Exception as e:
            print(f"Error loading images: {e}")
            spriteSheet = pygame.Surface((410, 160))
            spriteSheet.fill((139, 69, 19))
            spriteSheet2 = pygame.Surface((410, 160))
            spriteSheet2.fill((128, 128, 128))

        s_w, s_h = 102, 80
        self.bigBrownMeteors = self.loadMeteors(s_w, s_h, spriteSheet)
        self.bigGrayMeteors = self.loadMeteors(s_w, s_h, spriteSheet2)

        self.meteorfield_list = pygame.sprite.Group()

        meteorRange = 60 # how many times we going to randomly place meteors
        total_depth = -4500 # how long the meteor field is vertically
        threshold = -2200  # half the distance of the vertical scrolling

        for i in range(meteorRange):
            new_y = random.randint(total_depth, -100)
            
            if new_y > threshold:
                image = random.choice(self.bigBrownMeteors)
            else:
                image = random.choice(self.bigGrayMeteors)

            new_meteor = GameSprite(image, s_w, s_h)
            new_meteor.radius = 40
            new_meteor.shrink_radius(0.85)

            # spread them out horizontally so that it is a little easier to fly through the meteor field
            new_meteor.rect.x = random.randint(-50, self.screen_width - s_w + 50)
            new_meteor.rect.y = new_y
            
            self.meteorfield_list.add(new_meteor)

    def shift_world(self, shift_x, shift_y):
        for meteor in self.meteorfield_list:
            meteor.rect.y += shift_y
            meteor.rect.x += shift_x 

            if meteor.rect.top > self.screen_height:
                # Re-apply wide horizontal spread on respawn
                meteor.rect.x = random.randint(-50, self.screen_width - meteor.rect.width + 50)
                
                # pick the area where the brown meteors will be vs. gray meteors will be randomly
                if meteor.image in self.bigBrownMeteors:
                    meteor.rect.y = random.randint(-2200, -100)
                else:
                    # gray is further in
                    meteor.rect.y = random.randint(-4500, -2201)
            
            elif meteor.rect.bottom < -4500:
                meteor.rect.y = self.screen_height

    def draw(self, screen):
        self.meteorfield_list.draw(screen)
