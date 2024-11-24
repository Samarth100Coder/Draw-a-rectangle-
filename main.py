import pygame
pygame.init()
screen=pygame.display.set_mode((700,500))
colors={'red':pygame.Color('red'),
        'green':pygame.Color('green'),
        'blue':pygame.Color('blue'),
        'yellow':pygame.Color('yellow'),
        'white':pygame.Color('white')}  
current_color=colors['white']
x,y=30,30
clock=pygame.time.Clock() 
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x-=3
    if pressed[pygame.K_RIGHT]: x+=3
    if pressed[pygame.K_UP]: y-=3
    if pressed[pygame.K_DOWN]: y+=3

    x=min(max(0,x),650)
    y=min(max(0,x),450)
    if x==0: current_color=colors['blue']
    elif x==650: current_color=colors['yellow']
    elif y ==0: current_color=colors['red']
    elif y==450: current_color=colors['green']
    else: current_color=colors['white']

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(0,125,255), pygame.Rect(30,30,50,50))
    pygame.draw.circle(screen,(0,255,0),(150,150),50)
    pygame.draw.circle(screen,(0,0,255),(300,300),50,3)
    pygame.display.flip()
    clock.tick(90)
pygame.quit()