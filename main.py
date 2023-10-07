import pygame, sys

def ball_animation():
    global ball_speed_x, ball_speed_y 
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.right >= width or ball.left <= 0:
        ball_speed_x *= -1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

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

#Adding the ball velocity
ball_speed_x = 5
ball_speed_y = 5
player_speed = 0

#Creating the game loop
run = True
while run:
    # The event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 5
            if event.key == pygame.K_UP:
                player_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 5
            if event.key == pygame.K_UP:
                player_speed += 5

    player_animation()
    ball_animation()

    Screen.fill(bg_color)
    pygame.draw.rect(Screen, light_grey, player)
    pygame.draw.rect(Screen, light_grey, opponent)
    pygame.draw.ellipse(Screen, light_grey, ball)
    pygame.draw.aaline(Screen, light_grey, (width/2, 0), (width/2, height))
    #updating the window
    pygame.display.flip()
    clock.tick(60)

