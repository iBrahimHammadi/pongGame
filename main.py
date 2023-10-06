import pygame, sys

pygame.init()
clock = pygame.time.Clock()
width, height = 800, 600
#setting up the screen window
Screen = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('Pong Game')

#Creating the rectangles
ball = pygame.Rect(width/2-15,height/2-15 ,30,30)
player = pygame.Rect(width-20,height/2 -70,10,140)
opponent = pygame.Rect(10, height/2 -70, 10, 140)

light_grey = (200, 200, 200)
bg_color = pygame.Color('grey12')

#Creating the game loop
run = True
while run:
    # The event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    Screen.fill(bg_color)
    pygame.draw.rect(Screen, light_grey, player)
    pygame.draw.rect(Screen, light_grey, opponent)
    pygame.draw.ellipse(Screen, light_grey, ball)
    pygame.draw.aaline(Screen, light_grey, (width/2, 0), (width/2, height))
    #updating the window
    pygame.display.flip()
    clock.tick(60)

