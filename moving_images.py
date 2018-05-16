from tkinter import *
import random

#code for moving images around

def roombg(img,cx,cy,w,h):
    nume = Label(image=img,bg='black',width=w, height=h).place(x=cx,y=cy)

def imageupdate(currentRoom,location,maplist,roomlist):
    if currentRoom != location:
        roombg(maplist,cx=1000,cy=0,w=190,h=190)
        roombg(roomlist,cx=1000,cy=0,w=700,h=400)

def imageswitch(currentRoom,location,maplist,roomlist):
    if currentRoom == location:
        roombg(maplist,cx=705,cy=0,w=190,h=190)
        roombg(roomlist,cx=0,cy=0,w=700,h=400)
