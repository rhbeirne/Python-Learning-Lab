
import pygame
import random

# 1. Initialize Pygame
pygame.init()

# 2. Setup the "Stage"
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() # This library tool controls our FPS

# 3. The Player (A simple Rectangle)
# pygame.Rect(x, y, width, height)
player = pygame.Rect(375, 275, 50, 50)
player_color = (0, 128, 255) # A nice Azure Blue

# 4. The Game Loop
running = True
while running:
    # Check for "Events" (like clicking the X)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # DRAWING PHASE
    screen.fill((30, 30, 30)) # Dark Gray Background
    
    # Draw the player square
    pygame.draw.rect(screen, player_color, player)
    
    # Update the display
    pygame.display.flip()
    
    # Keep the game running at 60 Frames Per Second
    clock.tick(60)

pygame.quit()