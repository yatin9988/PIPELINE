import pygame
pygame.init()
screen=pygame.display.set_mode([800,600])
pygame.display.set_caption("SMILEY")
pic=pygame.image.load("smiley.png")
pic=pygame.transform.scale(pic,(100,100))
keep_going=True
picx=0
picy=0
speedx=5
speedy=5
black=(0,0,0)
count=0
yatin=pygame.time.Clock()
while keep_going:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keep_going=False
    yatin.tick(150)        
    screen.blit(pic,(picx,picy))
    pygame.display.update()
    picx+=speedx
    picy+=speedy
    if picx<=0 or picx + pic.get_width()>=800:
        speedx=-speedx
        count=count+1
    if picy<=0 or picy + pic.get_height()>=600:
        speedy=-speedy
        count=count+1
print(count)        
pygame.quit()        
    
