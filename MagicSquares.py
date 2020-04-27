#  File: MagicSquares.py
#  Description: Hw 13
#  Student's Name: Fahim Noor Islam
#  Student's UT EID: fni66
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created:4 / 21 / 20
#  Date Last Modified:4 / 21 / 20

class MagicSquare():
    
    def __init__(self,side):
        
        self.sideLength = side
        
        #Make an empty 1-D list
        grid = []
        
        for i in range(self.sideLength):
            #Make n more lists 
            
            rows  = []
            
            for j in range(self.sideLength):
                #Fill the second set with zeros
                
                rows.append(0)
             
            #Insert the rows of zeros into the first list to make
            # a list of lists
            grid.append(rows)
        
        i = 1 #start with i = 1
        row = i - 1 #get the first row
        column = self.sideLength//2 #get the center column
            
        grid[row][column] = i
        
        for count in range(2,self.sideLength**2+1):
            
            if i%self.sideLength == 0:
                
                row += 1
                
                if row > (self.sideLength-1):
                    
                    row = 0
                    i = count #increment i
                    grid[row][column] = i
                    
                else:
                    i = count #increment i            
                    grid[row][column] = i      
            else:
                
                row -= 1
                column += 1
        
                if row < 0:
                    
                    row = self.sideLength - 1
                    
                    if column > (self.sideLength - 1):
                        
                        column = 0
                        i = count #increment i
                        grid[row][column] = i
                      
                    else:
                        i = count #increment i
                        grid[row][column] = i
                         
                elif column > (self.sideLength-1):
                    
                    column = 0
                    
                    if row < 0:
                        
                        row = self.sideLength - 1
                        i = count #increment i
                        grid[row][column] = i
              
                    else:
                        i = count #increment i
                        grid[row][column] = i        
                else:
                    i = count #increment i
                    grid[row][column] = i
            
        self.grid = grid
                          
    def display(self):

        for row in self.grid :
            for column in row:  
                print('{:>5}'.format(column),end = '')
            print()
            
        print('\n')

def main():
    
    for i in range(1,14,2):
        print('Magic Square of size',i)
        print()
        Square = MagicSquare(i)
        Square.display()

main()
