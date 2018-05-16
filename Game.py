### ULTIMATE MONSTER HUNTER ###
###  A PYTHON GAME MADE BY  ###
### GHELBERE VLADUT-GABRIEL ###
###     CONCEPT ART BY      ###
###      LIMITEDDATA        ###  

#importing the tkinter library (for the GUI) and the random library (for random values in the game)
from tkinter import *
import random

#Linked list for inventory
from classes import node
from classes import linked_list

#functions for background change
from moving_images import roombg
from moving_images import imageupdate
from moving_images import imageswitch

#Player & Monster classses for stats handling
from objects import *

#functions for image handling and text alignment in ending screens.
def popup(nume,titlu,size):
    nume.geometry(size)
    nume.title(titlu)
    nume.resizable(width=False , height=False)
    nume.configure(background='black')

#make the text print on the bottom of the last message
def textlabel(window,text,fg,cx,cy):
    Label(window, text=text, fg=fg, bg='black').place(x=cx,y=cy)

#scroll function
def scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=681,height=169,bg="black", borderwidth=0, highlightthickness=0,yscrollcommand=myscrollbar.set)
    canvas.yview_moveto(1)

#opening a window for GUI
mainWindow = Tk()

#scanning input and getting response
def inputPrint(event):
	#using the global variables
    global currentRoom
    moveText = move.get()
    moveText=moveText.lower().split()
    move.delete(0, END)
    if len(moveText) == 0:
        Label(frame,text="You need to use a command",fg="white",bg="black").pack(side=TOP)
    if len(moveText)>0:

        #code for moving
        if moveText[0] == 'go':
            if moveText[1] in rooms[currentRoom]:
                currentRoom=rooms[currentRoom][moveText[1]]
                location_var.set(currentRoom)
                response = Player.takeAction()
                health_var.set(Player.health)
                gold_var.set(Player.gold)
                if len(response)>0:
                    Label(frame,text=response,fg="white",bg="black").pack(side=TOP)
            elif moveText[1]!=rooms[currentRoom]:
                Label(frame,text="---------------\nYou can't go that way!",fg="white",bg="black").pack(side=TOP)
            
            #moving images
            imageupdate(currentRoom,'front of the manor',maplist["map1"],roomlist["room1"])
            imageupdate(currentRoom,'the main hall',maplist["map2"],roomlist["room2"])
            imageupdate(currentRoom,'the living room',maplist["map3"],roomlist["room3"])
            imageupdate(currentRoom,'the kitchen',maplist["map4"],roomlist["room4"])
            imageupdate(currentRoom,'the basement',maplist["map5"],roomlist["room5"])
            imageupdate(currentRoom,'the first floor hallway',maplist["map6"],roomlist["room6"])
            imageupdate(currentRoom,'the bathroom',maplist["map7"],roomlist["room7"])
            imageupdate(currentRoom,'the bedroom',maplist["map8"],roomlist["room8"])
            imageupdate(currentRoom,'the attic',maplist["map9"],roomlist["room9"])

		    #replacing images
            imageswitch(currentRoom,'front of the manor',maplist["map1"],roomlist["room1"])
            imageswitch(currentRoom,'the main hall',maplist["map2"],roomlist["room2"])
            imageswitch(currentRoom,'the living room',maplist["map3"],roomlist["room3"])
            imageswitch(currentRoom,'the kitchen',maplist["map4"],roomlist["room4"])
            imageswitch(currentRoom,'the basement',maplist["map5"],roomlist["room5"])
            imageswitch(currentRoom,'the first floor hallway',maplist["map6"],roomlist["room6"])
            imageswitch(currentRoom,'the bathroom',maplist["map7"],roomlist["room7"])
            imageswitch(currentRoom,'the bedroom',maplist["map8"],roomlist["room8"])
            imageswitch(currentRoom,'the attic',maplist["map9"],roomlist["room9"])

        if 'destructible' in rooms[currentRoom]:
            Label(frame,text=("---------------\n I see a demonic totem !"),fg="white",bg="black").pack(side=TOP)

        #code for taking items and medicine
        if moveText[0] == 'take' and 'item' in rooms[currentRoom] and moveText[1] in rooms[currentRoom]['item'] and moveText[1]==rooms[currentRoom]['item']:
            	#use medicine
                if 'item' in rooms[currentRoom] and moveText[1] in rooms[currentRoom]['item'] and rooms[currentRoom]['item']=='painkillers':
                    Label(frame,text="---------------\nYou gained 25 HP",fg="white",bg="black").pack(side=TOP)
                    Player.takeMedicine()
                    health_var.set(Player.health)
                    del rooms[currentRoom]['item']
                #take items
                else:
                    ll.add_node(rooms[currentRoom]['item'])
                    inventoryList = Listbox(mainWindow, bg='black', fg='white', height=9, borderwidth=0, highlightthickness=0)
                    inventoryList.place(x=740,y=235,anchor=NW)
                    ll.list_print(inventoryList)
                    if ll.find_node(rooms[currentRoom]['item']):
                        Label(frame,text="---------------\n"+(str(rooms[currentRoom]['item'])+" got !"),fg="white",bg="black").pack(side=TOP)
                    del rooms[currentRoom]['item']

        #tell the player what you see
        if 'item' in rooms[currentRoom]:
            Label(frame,text=("---------------\n I see "+rooms[currentRoom]['item']+" !"),fg="white",bg="black").pack(side=TOP)

        #code for destroying items
        if moveText[0] == 'burn':
            if 'destructible' in rooms[currentRoom] and moveText[1] in rooms[currentRoom]['destructible'] and ll.find_node('gasoline'):
                Player.burnedTotem()
                totems_var.set(Player.totems)
                del rooms[currentRoom]['destructible']

                if Player.totems==1:
                    Label(frame,text="---------------\nYou pour gasoline on the totem, take out your lighter and watch it burn\nYou have burned "+str(Player.totems)+"/3",fg="white",bg="black").pack(side=TOP)
                if Player.totems==2:
                    Label(frame,text="---------------\nYou hear screams coming from the beyond\nYou have burned "+str(Player.totems)+"/3",fg="white",bg="black").pack(side=TOP)
                if Player.totems==3:
                    Label(frame,text="---------------\nYou have burned "+str(Player.totems)+"/3\nFind the key and escape.",fg="white",bg="black").pack(side=TOP)
            elif 'destructible' in rooms[currentRoom] and moveText[1] in rooms[currentRoom]['destructible']:
                Label(frame,text="---------------\nYou don't have anything flamable",fg="white",bg="black").pack(side=TOP)
            elif 'destructible' not in rooms[currentRoom]:
            	Label(frame,text="---------------\nYou have nothing to destroy here !",fg="white",bg="black").pack(side=TOP)
            else:
                Label(frame,text="---------------\nCan't destroy "+moveText[1]+ ' !',fg="white",bg="black").pack(side=TOP)
        
        #ending1
        if moveText[0] == 'go':
            if moveText[1] == 'back' and currentRoom == 'the street' :
                popup_end1=Tk()
                popup(popup_end1,"Ending 1/3 - Coward !",'400x125')
                end1=Label(popup_end1,text="---------------\nYou got back in your car and run away, hoping you got better days ahead !,\n---------------\nGAME OVER\n---------------",fg='white',bg='black').pack(side=TOP)
                popup_end1.mainloop()

        #ending2
        if Player.health <= 0:
            popup_end2=Tk()
            popup(popup_end2,"Ending 2/3 - Killed by monsters",'400x125')
            end2=Label(popup_end2,text="---------------\nThe monsters killed you !\n---------------\nGAME OVER\n---------------",fg='white',bg='black').pack(side=TOP)
            popup_end2.mainloop()

        #ending3
        if Player.totems==3 and ll.find_node('key') and currentRoom=='the main hall':
            popup_end3=Tk()
            popup(popup_end3,"Ending 3/3 - Monster Hunter",'400x125')
            end3=Label(popup_end3,text="---------------\nThe madness has stoped, there is peace once again.\n---------------\nGAME OVER\n---------------\nIn your adventure you gained "+str(Player.gold)+ " gold \n and an extra 100 for honoring your contract\n Score: "+str((Player.gold*3)+100+Player.health),fg='white',bg='black').pack(side=TOP)
            popup_end3.mainloop()

from loading_assets import *

#window bar
popup(mainWindow,"ULTIMATE MONSTER HUNTER",'900x600')

#input bar
move = Entry(mainWindow, bg='black',fg='white',width=117)
move.place(x=0,y=600,anchor=SW)
move.bind('<Return>',inputPrint)

#inventory
inv=PhotoImage(file="./frames/InventoryFrame.png")
roombg(inv,cx=705,cy=195,w=190,h=205)

#inventoryTitleText
textlabel(window=mainWindow,text='INVENTORY',fg="brown",cx=765,cy=219)
#inventory_list
ll = linked_list()
inventoryList = Listbox(mainWindow, bg='black', fg='white', height=9, borderwidth=0, highlightthickness=0)
inventoryList.place(x=740,y=240,anchor=NW)

#status_Bar
stat=PhotoImage(file="./frames/statusFrame.png")
roombg(stat,cx=705,cy=405,w=190,h=190)

#status_Location
location_var=StringVar()
location_var.set(currentRoom)
textlabel(window=mainWindow,text='LOCATION: ',fg="cyan",cx=770,cy=422)
Label(mainWindow, textvariable=(location_var), fg='cyan', bg='black').place(x=750,y=442, anchor=NW)

#status_HP
health_var=StringVar()
health_var.set(Player.health)
textlabel(window=mainWindow,text='HEALTH: ',fg="red",cx=775,cy=462)
Label(mainWindow, textvariable=(health_var), fg='red', bg='black').place(x=793,y=482, anchor=NW)

#status_gold
gold_var=StringVar()
gold_var.set(Player.gold)
textlabel(window=mainWindow,text='GOLD: ',fg="yellow",cx=780,cy=502)
Label(mainWindow, textvariable=(gold_var), fg='yellow', bg='black').place(x=793,y=522, anchor=NW)

#status_Totems
totems_var=StringVar()
totems_var.set(Player.totems)
textlabel(window=mainWindow,text='TOTEMS: ',fg="green",cx=775,cy=542)
Label(mainWindow, textvariable=(totems_var), fg='green', bg='black').place(x=795,y=562, anchor=NW)

#scroll_bar
myframe=Frame(mainWindow,width=50,height=100,bg="black")
myframe.place(x=0,y=405)
canvas=Canvas(myframe)
frame=Frame(canvas,bg="black")
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left",expand=True)
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",scroll)

#load the introduction
Label(frame,text=introduction,fg="white",bg="black").pack(side=TOP)

#keep program running
mainWindow.mainloop()