import pygame
pygame.init() #initializing python

#some colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
vel = 0.3


#bottom paddle (player 1) variables
x = 200
y = 450
width = 100
height = 10
#player 1




# create window to open the game
win_width =  500
win_height = 500
size = (win_width,win_height) # define the window size
win_display = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")

#player 2 variables (top player)
x_2 = 200
y_2 = 50
width_2 = 100
height_2 = 10
#player 2


#ball
red = (255, 0, 0)
ball_rad = 6
ball_x = 250
ball_y = 250
ball_speed = 1
ball_speed_x = ball_speed
ball_speed_y = ball_speed
del_x = 3;
del_y = 3
circle_width = ball_rad *2
circle_height = circle_width
#ball

game_not_done = True

while game_not_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_not_done = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < win_width - width - vel:
        x += vel
    if keys[pygame.K_a] and x_2 > vel:
            x_2 -= vel
    if keys[pygame.K_d] and x_2 < win_width - width_2 - vel:
        x_2 += vel
    win_display.fill(black)
    #draw both paddles
    pygame.draw.rect(win_display, white, [round(x), round(y), round(width), round(height)]) #bottom paddle
    pygame.draw.rect(win_display,white,[round(x_2),round(y_2),round(width_2),round(height_2)]) #top paddle


    #ball movement

    del_x = ball_x + ball_speed_x
    del_y = ball_y + ball_speed_y
    if del_y < 0: #if ball reaches top of window screen
        if del_x > (0.5 * win_width): # if ball goes off from the right side
            ball_speed_x = abs(ball_speed_x)
        else:
            ball_speed_x = -abs(ball_speed_x)
        ball_x = int(0.5 * width)
        ball_y = int(0.5* height)
    elif del_y > height: #if ball reaches bottom of window screen
        if del_x > (0.5 * win_width):
            ball_speed_x = abs(ball_speed_x)
        else:
            ball_speed_x = -abs(ball_speed_x)
            ball_x = int(0.5 * width)
            ball_y = int(0.5 * height)
    if del_x < 0: #if it hits left boundary
        ball_speed_x = abs(ball_speed_x)
    elif del_x > width: # if it hits right boundary
        ball_speed_x = -abs(ball_speed_x)
    pygame.draw.circle(win_display,red,[ball_x,ball_y], ball_rad)


    #check for collisions off paddle

    if ball_x < x + circle_width and ball_x + width > x and ball_y < y + circle_height and height + ball_y > y:
        ball_x = y_2 + height_2
        ball_speed_y = abs(ball_speed_y)




    #refresh the screen
    pygame.display.update()










