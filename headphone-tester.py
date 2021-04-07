#!/usr/bin/env python3
from playsound import playsound
import tkinter
from os import sep
import webbrowser
from sys import argv

# HTML-URL
url = "https://legendxd.000webhostapp.com/projects/headphone-tester/index"
version = "1.2"
date = "April 7 2021"

# Define Sound-Functions
def left():
	playsound("sounds" + sep + "beep-left.wav")
def both():
	playsound("sounds" + sep + "beep-both.wav")
def right():
	playsound("sounds" + sep + "beep-right.wav")
   
# GUI
def gui():
    root = tkinter.Tk()
    root.title("Headphones")
    root.resizable(width=False, height=False)
    
    buttonLeft = tkinter.Button(root, text="Left", command=left)
    buttonBoth = tkinter.Button(root, text="Both", command=both)
    buttonRight = tkinter.Button(root, text="Right", command=right)
    buttonLeft.grid(row=0,column=0)
    buttonBoth.grid(row=0,column=1)
    buttonRight.grid(row=0,column=2)
    
    root.mainloop()

# Parse args
try: # Not the best solution but it does work... so...
    if(argv[1] == "web" or argv[1] == "w"):
        webbrowser.open_new_tab(url)
    elif(argv[1] == "version" or argv[1] == "v"):
        print(f"The_Legend_of_xD's Headphone-Tester v{version}\nBuild-Date: {date}")
    elif(argv[1] == "right" or argv[1] == "r"):
    	right()
    elif(argv[1] == "left" or argv[1] == "l"):
    	left()
    elif(argv[1] == "both" or argv[1] == "b"):
    	both()
    else:
        gui()
except:
    gui()
