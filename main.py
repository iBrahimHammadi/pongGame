import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.right >= width:
        opponent_score += 1
        ball_restart()
        pygame.mixer.Sound.play(score_sound)
    if ball.left <= 0:
        player_score += 1
        ball_restart()
        pygame.mixer.Sound.play(score_sound)
    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.Sound.play(hitting_sound)
        ball_speed_x *= -1

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = ((width/2),(height/2))
    ball_speed_x *= random.choice((-1,1))
    ball_speed_y *= random.choice((-1,1))

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

def opponent_animation():
    if opponent.top < ball.y:
        opponent.bottom += opponent_speed
    if opponent.bottom > ball.y:
        opponent.top -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= height:
        opponent.bottom = height
    

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

#Adding the velocity
ball_speed_x = 5 * random.choice((-1,1))
ball_speed_y = 5 * random.choice((-1,1))
player_speed = 0
opponent_speed = 5

#Adding the Score variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32) 

#importing the ball sounds
score_sound = pygame.mixer.Sound('score.wav')
hitting_sound = pygame.mixer.Sound('hitting.wav')
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
    opponent_animation()

    Screen.fill(bg_color)
    pygame.draw.rect(Screen, light_grey, player)
    pygame.draw.rect(Screen, light_grey, opponent)
    pygame.draw.ellipse(Screen, light_grey, ball)
    pygame.draw.aaline(Screen, light_grey, (width/2, 0), (width/2, height))

    #Drawing the text on the display screen
    player_text = game_font.render(f"{player_score}",False, light_grey )
    Screen.blit(player_text, (width/2 + 20, height/2))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    Screen.blit(opponent_text, (width/2 - 40, height/2))

    #updating the window
    pygame.display.flip()
    clock.tick(60)

