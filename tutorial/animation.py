"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import math
import random

def movelinear(x):
    m=1
    b=50
    y=m*x+b
    return y

def movetrig(x):
    speed = 5
    waviness=50
    center=200
    y=math.sin(x*speed)*waviness+center
    return y

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
rect_x = 50
rect_y = 50
rect_change_x = 5
rect_change_y = 5
move_change = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLACK)
 
    rect_x += rect_change_x;
 
    if (move_change):
        rect_y = movetrig(rect_x)
    else:
        rect_y = movelinear(rect_x) 
 
    edge = False
    if rect_x > 649 or rect_x < 0:
        rect_change_x = rect_change_x * -1
        edge = True
    if rect_y > 449 or rect_y < 0:
        rect_change_x = rect_change_x * -1
        edge = True
    
    if edge:
        move_change = not move_change
 
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])

     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()