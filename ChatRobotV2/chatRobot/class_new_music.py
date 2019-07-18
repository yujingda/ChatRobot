import tkinter
import os
from musicTree import TreeWindows
#from lyric import Lyric
#from musicButton import MusicButton
import sys, time

win = tkinter.Tk()
win.title("音乐播放器")
# win.geometry("950x700+300+100")
win.geometry("230x300")
path = "./music"

frameL = tkinter.Frame(win)
frameL.pack(fill=tkinter.Y, side=tkinter.LEFT)

# frameR = tkinter.Frame(win)
# frameR.pack(fill=tkinter.Y, side=tkinter.RIGHT)

#ly = Lyric(frameR)
#ly.vis()
treeWin = TreeWindows(frameL, path)
#button = MusicButton(frameR, path)

win.mainloop()
