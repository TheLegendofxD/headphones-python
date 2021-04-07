#!/usr/bin/env python3
from playsound import playsound
import tkinter
from os import sep
import webbrowser
from sys import argv

# HTML-URL
url = "https://legendxd.000webhostapp.com/projects/headphone-tester/index"
version = "1.1"
date = "March 16 2021"

def left():
	playsound("sounds" + sep + "beep-left.wav")
def both():
	playsound("sounds" + sep + "beep-both.wav")
def right():
	playsound("sounds" + sep + "beep-right.wav")
   

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

try: # Not the best solution but it does work... so...
    if(argv[1] == "web" or argv[1] == "w"):
        webbrowser.open_new_tab(url)
    elif(argv[1] == "version" or argv[1] == "v"):
        print(f"The_Legend_of_xD's Headphone-Tester v{version}\nBuild-Date:{date}")
    else:
        gui()
except:
    gui()