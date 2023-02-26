import pygame
import sys

#spaceship class
class Base(pygame.sprite.Sprite):
    def __init__(self,width,height,position_x,position_y,direction,color):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.pos_x = position_x
        self.pos_y = position_y
        if(direction=='L'):
            self.image=pygame.image.load("D:\Alans-Folder\Miscellaneous\\test_game\\resourses\\resourses\\1 right.png")
            
        else:
            self.image=pygame.image.load("D:\Alans-Folder\Miscellaneous\\test_game\\resourses\\resourses\\1 left.png")
            
        self.rect = self.image.get_rect()
        #self.rect.center= [self.pos_x,self.pos_y]
    
    def poschng(self,x,y):
        self.pos_x=x
        self.pos_y=y
    def update(self):
        self.rect.center= [self.pos_x,self.pos_y]

#da Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self,direc,x,y):
        super().__init__()
        if(direc==1):
            self.image = pygame.image.load("D:\\Alans-Folder\\Miscellaneous\\test_game\\resourses\\resourses\\bulletR.png")
            
        elif(direc==-1):
            self.image = pygame.image.load("D:\\Alans-Folder\\Miscellaneous\\test_game\\resourses\\resourses\\bulletL.png")
            
        elif(direc==0):
            self.image = pygame.image.load("D:\\Alans-Folder\\Miscellaneous\\test_game\\resourses\\resourses\\bulletU.png")
            
        self.rect = self.image.get_rect()
        self.x=x
        self.y=y
        self.direc=direc
    def update(self):
        if(self.direc==0):
            self.rect.center=pygame.mouse.get_pos()
        else:
            pygame.sprite.spritecollide(ship_2,bullet_r,True)
            pygame.sprite.spritecollide(ship_1,bullet_l,True)
            self.x = self.x + self.direc*10 #bullet speed
            self.rect.center=[self.x,self.y]

#basic game window
pygame.init()
clock =pygame.time.Clock()
screen = pygame.display.set_mode((1440,810))  
done = True  
border=80
screen_bg=pygame.image.load("D:\\Alans-Folder\\Miscellaneous\\test_game\\resourses\\resourses\\space_bg.png")


#the actual spaceships
ship_1 = Base(50,100,150,405,'R',(255,150,255))
ship_2 = Base(50,100,1290,405,'L',(150,255,100))
horspeed=1
upspeed=2

ship_group = pygame.sprite.Group()
ship_group.add(ship_1)
ship_group.add(ship_2)
bullet_l= pygame.sprite.Group()
bullet_r= pygame.sprite.Group()
bullets=[]
bulletr=0
bulletl=0
ofset=1
spawnspeed=1

#ship positions
pos_1_x=150
pos_1_y=405
pos_2_x=1290
pos_2_y=405
activityCheck=0
    
while done:
    pygame.display.flip()
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            done = False
            break
    bulletr = bulletr+spawnspeed
    bulletl = bulletl+spawnspeed
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_w])and(pos_1_y>border):
        pos_1_y=pos_1_y - upspeed
        #print('"{}" key pressed'.format(key_name))
        
    if(keys[pygame.K_s])and(pos_1_y<810-border):
        pos_1_y=pos_1_y + upspeed
        #print('"{}" key pressed'.format(key_name))
        
    if(keys[pygame.K_a])and(pos_1_x>border):
        pos_1_x =pos_1_x  -  horspeed
        #print('"{}" key pressed'.format(key_name))
        
    if(keys[pygame.K_d])and(pos_1_x<700-border):
        pos_1_x= pos_1_x + horspeed
        #print('"{}" key pressed'.format(key_name))
        
    if(keys[pygame.K_k])and(pos_2_y<810-border):
        pos_2_y = pos_2_y + upspeed
        #print('"{}" key pressed'.format(key_name))
        
    if(keys[pygame.K_i])and(pos_2_y>border):
        pos_2_y=pos_2_y - upspeed
        #print('"{}" key pressed'.format(key_name))
        
    if(keys[pygame.K_j])and(pos_2_x>700+border):
        pos_2_x = pos_2_x - horspeed
        #print('"{}" key pressed'.format(key_name))
        
    if(keys[pygame.K_l])and(pos_2_x<1440-border):
        pos_2_x = pos_2_x + horspeed
        #print('"{}" key pressed'.format(key_name))
        
    if(keys[pygame.K_q])and(bulletr>=100):
        bullets.append(Bullet(1,pos_1_x+ofset,pos_1_y))
        bulletr=0
        bullet_r.add(bullets[len(bullets)-1])
        
    if(keys[pygame.K_u])and(bulletl>=100):
        bullets.append(Bullet(-1,pos_2_x-ofset,pos_2_y))
        bulletl=0
        bullet_l.add(bullets[len(bullets)-1])
        
    ship_1.poschng(pos_1_x,pos_1_y)
    ship_2.poschng(pos_2_x,pos_2_y)
#                while (True):
#                   if(event.type == pygame.KEYUP):
#                        break
#                    if(activityCheck==1)and(pos_1_y>border)and(pos_1_y<810-border):
#                        pos_1_y=pos_1_y - 1
#                    if(activityCheck==2)and(pos_1_y>border)and(pos_1_y<810-border):
#                        pos_1_y = pos_1_y + 1
#                    if(activityCheck==3)and(pos_1_x>border)and(pos_1_x<700-border):
#                        pos_1_x = pos_1_x  - 1
#                    if(activityCheck==4)and(pos_1_x>border)and(pos_1_x<700-border):
#                        pos_1_y = pos_1_x + 1
#                    if(activityCheck==-1)and(pos_2_y>border)and(pos_2_y<810-border):
#                        pos_2_y = pos_2_y + 1
#                    if(activityCheck==-2)and(pos_2_y>border)and(pos_2_y<810-border):
#                        pos_2_y = pos_2_y  - 1
#                    if(activityCheck==-3)and(pos_2_x>700+border)and(pos_2_x<1440-border):
#                        pos_2_x = pos_2_x  - 1
#                    if(activityCheck==-4)and(pos_2_x>700+border)and(pos_2_x<1440-border):
#                        pos_2_y = pos_2_x + 1
#                    screen.blit(screen_bg,(0,0))
#                    ship_group.draw(screen)
#                    ship_group.update()
#                    bullet_g.draw(screen)
#                    bullet_g.update()
#                    pygame.display.flip()
        
    for p in bullet_r:
        if(p.x>1440)or(p.x<0):
            bullet_r.remove(p)    
    for p in bullet_l:
        if(p.x>1440)or(p.x<0):
            bullet_l.remove(p)
    screen.blit(screen_bg,(0,0))
    ship_group.draw(screen)
    ship_group.update()
    bullet_l.draw(screen)
    bullet_l.update()
    bullet_r.draw(screen)
    bullet_r.update()
    pygame.display.flip()
    clock.tick(60)
