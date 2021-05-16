class Field(object):
    def __init__(self,field_in):
        self.cols=len(field_in[0])
        self.rows=len(field_in)

        self.field=field_in

    def get_neighbours(self,x,y,start):
        out=[]
        offsetsx=[-1,1,0,0]
        offsetsy=[0,0,-1,1]
        for i in range(0,len(offsetsx)):
            cellx=x + offsetsx[i]
            celly=y + offsetsy[i]
            if self.testifcellinframe(cellx,celly):
                if self.field[cellx][celly] ==0:
                    out.append([cellx,celly])
                else:
                    mintimesteps=abs(cellx-start[0])+abs(celly-start[1])

                    if mintimesteps > self.field[cellx][celly]:
                        out.append([cellx,celly])

        return out

    def testifcellinframe(self,x,y):
        if x<0 or x >=self.cols:
            return False
        
        if y<0 or y >=self.rows:
            return False
 
        return True
    
    def solve(self,start,end):

        visited = [] # List to keep track of visited nodes.
        queue = []    #Initialize a queue

        parents=[]
        for row in range(self.rows):
            newrow=[]
            for col in range(self.cols):
                newrow.append(None)
            parents.append(newrow) 

        visited.append(start)
        queue.append(start)

        while queue:
            s = queue.pop(0) 
            #print (s, end = " ") 

            x=s[0]
            y=s[1]
            for neighbour in self.get_neighbours(x,y,start):
                if neighbour not in visited:
                    #print(neighbour)
                    visited.append(neighbour)
                    queue.append(neighbour)
                    #self.field[neighbour[0]][neighbour[1]].parent=[x,y]
                    parents[neighbour[0]][neighbour[1]]=[x,y]
                    #parent[x][y]=
                    #print(self.field[x][y].parent)


                    #backtrace
                    
                    if neighbour == end:
                        trace=[]
                        #print("ende gefunden",neighbour)
                        #parent=self.field[neighbour[0]][neighbour[1]].parent
                        parent=parents[neighbour[0]][neighbour[1]]
                        #print(parent)
                        while parent:
                            
                            trace.append(parent)
                            #print(parent)
                            #parent=self.field[parent[0]][parent[1]].parent
                            parent=parents[parent[0]][parent[1]]
                            
                        return trace


        
