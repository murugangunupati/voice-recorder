import tkinter as tk
from tkinter import *
import recorder 

window = Tk()#creating window
window.geometry('700x300')#geomtry of window
window.title('TechVidvan')#title to window
Label(window,text="Click on Start To Start Recording",font=('bold',20)).pack()#label

rec = recorder.Recorder(channels=2)
running = None

def start():
    global running

    if running is not None:
        print('already running')
    else:
        running = rec.open('untitled.flac', 'wb')
        running.start_recording()
    Label(window,text='Recording has started').pack()

def stop():
    global running

    if running is not None:
        running.stop_recording()
        running.close()
        running = None
        Label(window,text='Recording has stoped').pack()
    else:
        print('not running')


Button(window,text='Start',bg='green',command=start,font=('bold',20)).pack()#create a button
Button(window,text='Stop',bg='green',command=stop,font=('bold',20)).pack()#create a button

window.mainloop()