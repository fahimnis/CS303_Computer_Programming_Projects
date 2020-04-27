#  File: Project1.py
#  Description: Project 1 Solution
#  Student's Name: Fahim N Islam
#  Student's UT EID: fni66
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: 4 / 20 / 20
#  Date Last Modified: 4 / 21 / 20

class Room():
    
    def __init__(self,name,north,east,south,west,up,down):
        # add your code here
        
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        

    def displayRoom(self):
        
        # add your code here
        
        print('Room name:',self.name)
        if self.north != None:
            print('{:<3s}{:<20s}{:}'.format('','Room to the north:',self.north))
        if self.east != None: 
            print('{:<3s}{:<20s}{:}'.format('','Room to the east:',self.east))
        if self.south != None:
            print('{:<3s}{:<20s}{:}'.format('','Room to the south:',self.south))
        if self.west != None:
            print('{:<3s}{:<20s}{:}'.format('','Room to the west:',self.west))
        if self.down != None:
            print('{:<3s}{:<20s}{:}'.format('','Room below:',self.down))
        if self.up != None:
            print('{:<3s}{:<20s}{:}'.format('','Room above:',self.up))
        print('\n')
        
        

def createRoom(roomData):
    # add your code here
    
    build = Room(roomData[0],roomData[1],roomData[2],
                 roomData[3],roomData[4],roomData[5],roomData[6])
    
    return build

def look():
    
    print('You are currently in the',current.name)

def getRoom(name):
    # add your code here
    
    for i in range (7):
        
        if name == floorPlan[i].name:
            
            return floorplan[i]

        
def move(direction):
    # add your code here
    
    New_Room = getattr(current,direction)
    
    if New_Room == None:
        
        print("You can't move in that direction.")
        
        return current
        
    else:
        
        print('You are now in the',New_Room)
        
        for i in range(7):
            if floorPlan[i].name == New_Room:
                
                return floorPlan[i] 

def displayAllRooms():
    # add your code here  
    
    for i in range(7):
        
        floorPlan[i].displayRoom()
        

##########################################################################
###     All code below this is given to you.  DO NOT EDIT IT unless    ###
###     you need to adjust the indentation to match the indentation    ###
###     of the rest of your code.                                      ###
##########################################################################
        
def loadMap():

    global floorPlan    # make the variable "floorPlan" a global variable
    
    room1 = ["Living Room","Dining Room",None,None,None,"Upper Hall",None]
    room2 = ["Dining Room",None,None,"Living Room","Kitchen",None,None]
    room3 = ["Kitchen",None,"Dining Room",None,None,None,None]
    room4 = ["Upper Hall","Bathroom","Small Bedroom","Master Bedroom",None,None,"Living Room"]
    room5 = ["Bathroom",None,None,"Upper Hall",None,None,None]
    room6 = ["Small Bedroom",None,None,None,"Upper Hall",None,None]
    room7 = ["Master Bedroom","Upper Hall",None,None,None,None,None]

    floorPlan = [createRoom(room1),createRoom(room2),createRoom(room3),createRoom(room4),createRoom(room5),createRoom(room6),createRoom(room7)]

def main():

    global current      # make the variable "current" a global variable
    
    loadMap()
    
    displayAllRooms()

    # TEST CODE:  walk around the house
    
    current = floorPlan[0]      # start in the living room
    look()                      # Living Room
    
    current = move("south")     # can't move this direction
    current = move("west")      # can't move this direction
    current = move("north")     # Dining Room
    current = move("south")     # Living Room
    current = move("up")        # Upper Hall
    look()                      # Upper Hall
    current = move("east")      # Small Bedroom
    current = move("east")      # can't move this direction
    current = move("west")      # Upper Hall
    current = move("south")     # Master Bedroom
    current = move("north")     # Upper Hall
    current = move("north")     # Bathroom
    current = move("south")     # Upper Hall
    look()                      # Upper Hall
    current = move("west")      # can't move this direction
    look()                      # still in the Upper Hall
    current = move("down")      # Living Room
    current = move("north")     # Dining Room
    current = move("west")      # Kitchen
    current = move("north")     # can't move this direction

main()
