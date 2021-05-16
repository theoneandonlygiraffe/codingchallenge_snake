
class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    


class Snake(object):
    def __init__(self,x,y):
        self.body=[]
        self.body.append(Point(x,y))
        self.length=1

    def move(self,move):

        newhead=Point(self.body[-1].x,self.body[-1].y)
        if move == "w":
            newhead.y=newhead.y-1


            pass
        elif move == "a":

            newhead.x=newhead.x-1

            pass
        elif move == "s":

            newhead.y=newhead.y+1

            pass
        elif move == "d":

            newhead.x=newhead.x+1

            pass
        
        

        self.body.append(newhead)
        if len(self.body)>self.length:
            del(self.body[0])

        
        
        
        return False

