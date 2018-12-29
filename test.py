from pygame.locals import *
import pygame
import time
from random import randint
 
class Player:
    x = 0
    dx = 0
    y = 44
    dy = 1
    speed = 44
    
 
    def moveRight(self):
        self.x = self.x + self.speed
        self.dx = self.dx + 1
    def moveLeft(self):
        self.x = self.x - self.speed
        self.dx = self.dx - 1

    def moveUp(self):
        self.y = self.y - self.speed
        self.dy = self.dy - 1
    def moveDown(self):
        self.y = self.y + self.speed
        self.dy = self.dy + 1

class Maze:
    def __init__(self):
       self.M = 12
       self.N = 12
       self.maze = [1,1,1,1,1,1,1,1,1,1,1,1,
                    0,0,0,1,0,0,0,0,1,0,1,1,
                    1,0,1,1,0,1,1,1,0,0,0,1,
                    1,0,1,0,0,0,0,0,0,1,0,1,
                    1,0,0,0,0,1,0,0,1,0,0,1,
                    1,1,0,1,1,1,0,1,0,0,1,1,
                    1,0,0,0,0,1,0,0,0,0,0,1,
                    1,0,1,1,1,0,0,1,1,0,0,1,
                    1,0,0,0,0,0,1,0,0,1,0,1,
                    1,1,0,1,0,0,0,1,0,0,0,1,
                    1,0,0,0,0,1,0,0,0,1,0,0,
                    1,1,1,1,1,1,1,1,1,1,1,1]
 
    def draw(self,display_surf,image_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 44 , by * 44))
 
           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1
 
 
class App:
 
    windowWidth = 530
    windowHeight = 530
    player = 0
    monster1 = 0
    monster2 = 0
    monster3 = 0
    uwin = False
    ulose = False
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.monster1 = Player()
        self.monster2 = Player()
        self.monster3 = Player()
        self.maze = Maze()

        self.monster1.dx = 11
        self.monster1.dy = 10
        self.monster1.x = 484
        self.monster1.y = 440

        self.monster2.dx = 1
        self.monster2.dy = 10
        self.monster2.x = 44
        self.monster2.y = 440

        self.monster3.dx = 4
        self.monster3.dy = 1
        self.monster3.x = 176
        self.monster3.y = 44

        
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Maze (Sara Sanjabi)')
        self._running = True
        self._image_surf = pygame.image.load("player.png").convert()
        self._block_surf = pygame.image.load("block.png").convert()
        self._youWin_surf = pygame.image.load("you-win.png").convert()
        self._youLose_surf = pygame.image.load("you-lose.png").convert()
        self._monster_surf = pygame.image.load("monster.png").convert()

 
    def on_render(self):
        if(self.uwin == True):
            self._display_surf.blit(self._youWin_surf,(0,0))
        elif(self.ulose == True):
            self._display_surf.blit(self._youLose_surf,(0,0))

        else:  
            self._display_surf.fill((255,255,255))
            self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
            self._display_surf.blit(self._monster_surf,(self.monster1.x, self.monster1.y))
            self._display_surf.blit(self._monster_surf,(self.monster2.x, self.monster2.y))
            self._display_surf.blit(self._monster_surf,(self.monster3.x, self.monster3.y))
            self.maze.draw(self._display_surf, self._block_surf)
            
        pygame.display.flip()
 


    def move_monster1(self):
        lastx = self.monster1.dx
        lasty = self.monster1.dy
        move = randint(0, 4)
        if(move == 0 and
           self.maze.maze[self.monster1.dx+(12*(self.monster1.dy))+1]!=1 and
           lastx != self.monster1.dx+1):

            lastx = self.monster1.dx
            lasty = self.monster1.dy
            self.monster1.moveRight()
        elif(move == 1 and
           self.maze.maze[self.monster1.dx+(12*(self.monster1.dy))-1]!=1 and
           lastx != self.monster1.dx-1):

            lastx = self.monster1.dx
            lasty = self.monster1.dy
            self.monster1.moveLeft()
        if(move == 2 and
           self.maze.maze[self.monster1.dx+(12*(self.monster1.dy-1))]!=1 and
           lastx != self.monster1.dy-1):

            lastx = self.monster1.dx
            lasty = self.monster1.dy
            self.monster1.moveUp()
        if(move == 3 and
           self.maze.maze[self.monster1.dx+(12*(self.monster1.dy+1))]!=1 and
           lastx != self.monster1.dy+1):

            lastx = self.monster1.dx
            lasty = self.monster1.dy
            self.monster1.moveDown()

    def move_monster2(self):
        lastx = self.monster2.dx
        lasty = self.monster2.dy
        move = randint(0, 4)
        if(move == 0 and
           self.maze.maze[self.monster2.dx+(12*(self.monster2.dy))+1]!=1 and
           lastx != self.monster2.dx+1):

            lastx = self.monster2.dx
            lasty = self.monster2.dy
            self.monster2.moveRight()
        elif(move == 1 and
           self.maze.maze[self.monster2.dx+(12*(self.monster2.dy))-1]!=1 and
           lastx != self.monster2.dx-1):

            lastx = self.monster2.dx
            lasty = self.monster2.dy
            self.monster2.moveLeft()
        if(move == 2 and
           self.maze.maze[self.monster2.dx+(12*(self.monster2.dy-1))]!=1 and
           lastx != self.monster2.dy-1):

            lastx = self.monster2.dx
            lasty = self.monster2.dy
            self.monster2.moveUp()
        if(move == 3 and
           self.maze.maze[self.monster2.dx+(12*(self.monster2.dy+1))]!=1 and
           lastx != self.monster2.dy+1):

            lastx = self.monster2.dx
            lasty = self.monster2.dy
            self.monster2.moveDown()

            
    def move_monster3(self):
        lastx = self.monster3.dx
        lasty = self.monster3.dy
        move = randint(0, 4)
        if(move == 0 and
           self.maze.maze[self.monster3.dx+(12*(self.monster3.dy))+1]!=1 and
           lastx != self.monster3.dx+1):

            lastx = self.monster3.dx
            lasty = self.monster3.dy
            self.monster3.moveRight()
        elif(move == 1 and
           self.maze.maze[self.monster3.dx+(12*(self.monster3.dy))-1]!=1 and
           lastx != self.monster3.dx-1):

            lastx = self.monster3.dx
            lasty = self.monster3.dy
            self.monster3.moveLeft()
        if(move == 2 and
           self.maze.maze[self.monster3.dx+(12*(self.monster3.dy-1))]!=1 and
           lastx != self.monster3.dy-1):

            lastx = self.monster3.dx
            lasty = self.monster3.dy
            self.monster3.moveUp()
        if(move == 3 and
           self.maze.maze[self.monster3.dx+(12*(self.monster3.dy+1))]!=1 and
           lastx != self.monster3.dy+1):

            lastx = self.monster3.dx
            lasty = self.monster3.dy
            self.monster3.moveDown()
    
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            time.sleep(0.2)
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            
            if (keys[K_RIGHT]):                
                if (self.maze.maze[self.player.dx+(12*(self.player.dy))+1]!=1):
                    self.player.moveRight()

            if (keys[K_LEFT]):
                if (self.maze.maze[self.player.dx+(12*(self.player.dy))-1]!=1):
                    self.player.moveLeft()
                
            if (keys[K_UP]):
                if (self.maze.maze[self.player.dx+(12*(self.player.dy-1))]!=1):
                    self.player.moveUp()
                
            if (keys[K_DOWN]):
                if (self.maze.maze[self.player.dx+(12*(self.player.dy+1))]!=1):
                    self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
           
            if(self.player.dx == 11 and self.player.dy == 10):
                self.uwin = True

            if(self.player.dx == self.monster1.dx and self.player.dy == self.monster1.dy):
                self.ulose = True
            if(self.player.dx == self.monster2.dx and self.player.dy == self.monster2.dy):
                self.ulose = True
            if(self.player.dx == self.monster3.dx and self.player.dy == self.monster3.dy):
                self.ulose = True
                
            self.move_monster1()
            self.move_monster2()
            self.move_monster3()




            self.on_render()

 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
