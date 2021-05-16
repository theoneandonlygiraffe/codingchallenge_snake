
from gamelogic.snake import Point, Snake
from bfs.field import Field

import random
import time


class SnakeGame(object):
    def __init__(self,width,height):

        self.width=width
        self.height=height
        
        self.snake=Snake(1,1)
        self.apple=Point(5,5)

        self.apple.x=random.randint(8,self.width-1)
        self.apple.y=random.randint(8,self.height-1)

        
        pass

    def run(self):
        FailCondition=False
        while not FailCondition:
            FailCondition=self.gameloop()
        
        self.deathscreen()
    
    def run_automated(self):
        FailCondition=False
        while not FailCondition:
            nextmove=self.makedecision()
            FailCondition=self.gameloop(nextmove)
            time.sleep(0.3)
        
        self.deathscreen()

    def gameloop(self,nextmove=None):

        #input
        if nextmove==None:
            validInput=False
            while not validInput:
                move=input(">")

                if move == "w" or move == "a" or move == "s" or move == "d":
                    validInput=True
                    
                else:
                    print("no valid Input :(")
                    validInput=False
        else:
            move=nextmove
            if move == "w" or move == "a" or move == "s" or move == "d":
                validInput=True
                
            else:
                print("no valid Input :(")
                validInput=False

                return False
        
        #move
        self.snake.move(move)

        #FailCondition
        FailCondition=self.testforfail()

        #Win (Apfel)
        if self.testforwin():
            self.snake.length=self.snake.length+1
            
            self.apple.x=random.randint(0,self.width)
            self.apple.y=random.randint(0,self.height)
            while not self.testifcellvalid(self.apple):
                self.apple.x=random.randint(0,self.width-1)
                self.apple.y=random.randint(0,self.height-1)
                

        #output
        self.output()
        print("-----------------------------------------------")
        self.output_debug()

        return FailCondition

    def extract_field(self):
        field=[]
        for r in range(self.height):
            newrow=[]
            for c in range(self.width):
                cell=0
                if c<0 or c >=self.width:
                    cell=-1
                if r<0 or r >=self.height:
                    cell=-1
                newrow.append(cell)
            field.append(newrow)
        for i in range(len(self.snake.body)):
            bodycell=self.snake.body[i]
            field[bodycell.x][bodycell.y]=i+1
        return field
    
    def makedecision(self):
        head=self.snake.body[-1]

        bfsfield=Field(self.extract_field())
        apple=[[self.apple.x,self.apple.y]]
        
        trace1=bfsfield.solve([head.x,head.y],[self.apple.x,self.apple.y])
        print("apple:",apple)
        print("snake:[",head.x,",",head.y,"]","len:",len(self.snake.body))
        print("trace:",trace1)
        
        if trace1:
            trace=apple+trace1
            
            print("path:",trace)
            print("path length:",len(trace))
            

            nextmove=trace[-2]
            snake=trace[-1]
            if nextmove[0]>snake[0]:
                return "d"
            elif nextmove[0]<snake[0]:
                return "a"
            elif nextmove[1]>snake[1]:
                return "s"
            elif nextmove[1]<snake[1]:
                return "w"
        else:
            print("no Path found! Can u do it better? (w,a,s,d)")
   

    



    def output(self):
        out=""
        for y in range(self.height):
            for x in range(self.width):
                cell_string=" "
                if self.apple.x==x and self.apple.y==y:
                    cell_string="X"
                for cell in self.snake.body:
                    if cell.x==x and cell.y ==y:
                        cell_string="#"
                        break
                out=out+cell_string  
            out=out+"\n"
        print(out)
    
    def output_debug(self):
        out_field=self.extract_field()
        out=""
        for y in range(self.height):
            for x in range(self.width):
                if out_field[x][y] == 0:
                    cell_string=" "
                else:
                    cell_string=str(out_field[x][y])
                    

                if self.apple.x==x and self.apple.y==y:
                    cell_string="X"
                
                if len(cell_string)<=1:
                    cell_string=" "+cell_string
                
                out=out+cell_string  
            out=out+"\n\n"
        print(out)


    def testforfail(self):
        head=self.snake.body[-1]
        for cell in self.snake.body[:-1]:
            if cell.x==head.x and cell.y == head.y:
                return True
        
        if head.x<0 or head.x >self.width:
            return True
        
        if head.y<0 or head.y >self.height:
            return True
        
        return False

    def testifcellvalid(self,point):
        head=point
        for cell in self.snake.body:
            if cell.x==head.x and cell.y == head.y:
                return False
        
        if head.x<0 or head.x >=self.width:
            return False
        
        if head.y<0 or head.y >=self.height:
            return False
        
        return True

    def testforwin(self):
        head=self.snake.body[-1]
        if self.apple.x==head.x and self.apple.y == head.y:
            return True

        return False

    def deathscreen(self):
        print("FailCondition")