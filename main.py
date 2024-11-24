import pygame
pygame.init()
screen=pygame.display.set_mode((700,500))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,255), pygame.Rect(30,30,350,250))
    pygame.display.flip()