from tkinter import *
from moving_images import roombg 

currentRoom='front of the manor'

rooms = {
    #bottom floor
    'front of the manor':
    {
        'forward' : 'the main hall',
        'back' : 'the street'
    },
    'the street':{}, #Ending_1
    'the main hall':
    {
        'forward' :'the first floor hallway',
        'left':'the living room',
        'right':'the kitchen'
    },
    'the living room':
    {
        'back': 'the main hall',
        'item' : 'key'
    },
    'the kitchen':
    {
        'forward':'the basement',
        'back':'the main hall',
        'item':'gasoline'
    },
    'the basement':
    {
        'back':'the kitchen',
        'destructible':'totem'
    },
    #1st floor
    'the first floor hallway':
    {
        'forward':'the attic',
        'back':'the main hall',
        'left':'the bathroom',
        'right':'the bedroom'
    },
    'the bathroom':
    {
        'back':'the first floor hallway',
        'item':'painkillers'
    },
    'the bedroom':
    {
        'back':'the first floor hallway',
        'destructible':'totem'
    },
    #attic
        'the attic':
    {
        'back':'the first floor hallway',
        'destructible':'totem'
    }
}

#instructions_output
introduction='''===============
ULTIMATE MONSTER HUNTER
===============
Story:
You are a monster hunter.
You travel the land and take contracts for gold.
You heard about one particular haunted house near a swamp.
You decide to take the matter in your own hands.
===============
Instructions:
~ Find the three demonic totems inside the house and burn them.
~ Find the key and escape before the creatures get you !
===============
Commands:
go [dirrection] (ex. forward,back,left,right)
take [item] (ex. key,gasoline,painkillers)
burn [object] (ex. totem)
===============
You see the house and walk to the door...
'''

#image lists
roomlist={
"room1":PhotoImage(file="./rooms/room1.png"),
"room2":PhotoImage(file="./rooms/room2.png"),
"room3":PhotoImage(file="./rooms/room3.png"),
"room4":PhotoImage(file="./rooms/room4.png"),
"room5":PhotoImage(file="./rooms/room5.png"),
"room6":PhotoImage(file="./rooms/room6.png"),
"room7":PhotoImage(file="./rooms/room7.png"),
"room8":PhotoImage(file="./rooms/room8.png"),
"room9":PhotoImage(file="./rooms/room9.png"),}

maplist ={
"map1":PhotoImage(file="./map/room1.png"),
"map2":PhotoImage(file="./map/room2.png"),
"map3":PhotoImage(file="./map/room3.png"),
"map4":PhotoImage(file="./map/room4.png"),
"map5":PhotoImage(file="./map/room5.png"),
"map6":PhotoImage(file="./map/room6.png"),
"map7":PhotoImage(file="./map/room7.png"),
"map8":PhotoImage(file="./map/room8.png"),
"map9":PhotoImage(file="./map/room9.png"),}

#load the intro image
roombg(roomlist["room1"],cx=0,cy=0,w=700,h=400)
roombg(maplist["map1"],cx=705,cy=0,w=190,h=190)