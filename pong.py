import pygame,random
pygame.init()
WIDTH = 1200
HEIGHT = 600

VEL = 10
ball_vel = 16

ballx_vel = ball_vel
bally_vel = random.randint(-ball_vel//2,ball_vel//2)

WHITE = "#ffffff"

font = pygame.font.SysFont("arial",40,True,)

score1 = 0
score2 = 0

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")

pygame.draw.rect(screen,WHITE,(WIDTH//2+3,0,6,HEIGHT))

pad1 = HEIGHT//2-50
pad2 = HEIGHT//2-50

ballx,bally = WIDTH//2+8,HEIGHT//2-8

def draw_pads():
    rect1 = pygame.Rect(10,pad1,10,100)
    rect2 = pygame.Rect(WIDTH-20,pad2,10,100)
    pygame.draw.rect(screen,WHITE,rect1)
    pygame.draw.rect(screen,WHITE,rect2)
    return rect1,rect2

def draw_ball():
    ball_rect = pygame.Rect(ballx,bally,16,16)
    pygame.draw.rect(screen,"#ff0000",ball_rect,border_radius=16)
    return ball_rect

def draw_score():
    text1 = font.render(str(score1),True,WHITE)
    text2 = font.render(str(score2),True,WHITE)
    screen.blit(text1,(WIDTH//4-(text1.get_width()//2),50))
    screen.blit(text2,(3*WIDTH//4-(text2.get_width()),50))

def reset():
    global ballx_vel,bally_vel,score1,score2,pad1,pad2,ballx,bally

    ballx_vel = ball_vel
    bally_vel = 0
    score1 = 0
    score2 = 0
    pad1 = HEIGHT//2-50
    pad2 = HEIGHT//2-50
    ballx,bally = WIDTH//2+8,HEIGHT//2-8

def AI(player = 1):
    #paddley,bally,ballx,opponent_paddley
    global pad1,pad2
    if player == 1:
        if bally < pad1+70 and pad1 >=0:
            pad1 -= VEL

        elif bally > pad1+70 and pad1+100 <= HEIGHT:
            pad1 += VEL

    else:
        if bally < pad2+30 and pad2 >=0:
            pad2 -= VEL

        elif bally > pad2+30 and pad2+100 <= HEIGHT:
            pad2 += VEL

paddle1, paddle2 = draw_pads()
ball = draw_ball()
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                reset()
    
    ballx += ballx_vel
    bally += bally_vel 
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and pad2>0 :
        pad2 -= VEL
    if keys[pygame.K_DOWN] and pad2<HEIGHT-100:
        pad2 += VEL

    if keys[pygame.K_w] and pad1>0:
        pad1 -= VEL
    if keys[pygame.K_s] and pad1<HEIGHT-100:
        pad1 += VEL

    if ballx< 3*WIDTH//4:
        AI()
    #if ballx > WIDTH//4:
    #   AI(2)

    screen.fill("#000000")
    pygame.draw.rect(screen,WHITE,(WIDTH//2+2,0,4,HEIGHT))
    ball = draw_ball()
    paddle1, paddle2 = draw_pads()
    draw_score()
    pygame.display.update()        

    if ballx <= 0:
        score2 += 1
        ballx,bally = WIDTH//2+8,HEIGHT//2-8
        ballx_vel = -ball_vel
        bally_vel = random.randrange(-ball_vel//2,ball_vel//2)
        pad1 = HEIGHT//2-50
        pad2 = HEIGHT//2-50
    elif ballx >= WIDTH:
        score1 += 1
        ballx,bally = WIDTH//2+8,HEIGHT//2-8
        ballx_vel = ball_vel
        bally_vel = random.randrange(-ball_vel//2,ball_vel//2)
        pad1 = HEIGHT//2-50
        pad2 = HEIGHT//2-50
    

    if bally <= 5:
        bally_vel *= -1

    if bally >= HEIGHT-20:
        bally_vel *= -1

    if ball.colliderect(paddle2):
        ballx_vel = -ball_vel
        diff = (bally+8) - (pad2+50)
        bally_vel = diff / (50/ball_vel)


    if ball.colliderect(paddle1):
        ballx_vel = ball_vel
        diff = (bally+8) - (pad1+50)
        bally_vel = diff / (50/ball_vel)

pygame.quit()