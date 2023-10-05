import pygame, sys

pygame.init()
clock = pygame.time.Clock()

#setting up the screen window
Screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Pong Game')

#Creating the game loop
run = True
while run:
    # The event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #updating the window
    pygame.display.flip()
    clock.tick(60)

