import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """
 
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(WHITE)
        return image

def main():
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    
    pygame.display.set_caption("Move Stick Figure")
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    done = False
    x = y = 50
    pygame.mouse.set_visible(0)
    background_image = pygame.image.load("tutorial/ch11/backdrop.jpeg").convert()
    left_player_image = SpriteSheet("tutorial/ch11/playerspritesheet.png").get_image(0,0,50,50);
    right_player_image = SpriteSheet("tutorial/ch11/playerspritesheet.png").get_image(50,0,50,50);
    player_image = left_player_image
    walk_sound = pygame.mixer.Sound("tutorial/ch11/walk.ogg")
    while not done:
        # --- Main event loop 
        for event in pygame.event.get():

            prevx = x
            prevy = y

            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 3
                    player_image = left_player_image
                elif event.key == pygame.K_RIGHT:
                    x += 3
                    player_image = right_player_image
                elif event.key == pygame.K_UP:
                     y -= 3
                elif event.key == pygame.K_DOWN:
                     y += 3
                walk_sound.play()
            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                walk_sound.play()
                
        screen.blit(background_image, [0, 0])
    
        screen.blit(player_image, [x,y])
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    
        # --- Limit to 60 frames per second
        clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    main()