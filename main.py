# Imports
from tkinter import *
import tkinter as tk
import sys
import os


class dos_gui:

  def quitgui(self):
    print("Quit called!")
    sys.exit(0)

  def __init__(self):
    self.root = tk.Tk()
    self.root.title("DOS GUI")
    self.mainframe = tk.Frame(self.root)
    self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    self.root.columnconfigure(0, weight=1)
    self.root.rowconfigure(0, weight=1)
    self.toolsTextVar = StringVar(value="DOS Tools")
    self.toolsBtn = tk.Button(self.mainframe,
                              textvariable=self.toolsTextVar,
                              command=self.tools).grid(row=0,
                                                       column=0,
                                                       sticky=(W, E))
    self.dos_docsTextVar = StringVar(value="DOS Documentation")
    self.dos_docsBtn = tk.Button(self.mainframe,
                                 textvariable=self.dos_docsTextVar,
                                 command=self.dos_docs).grid(row=1,
                                                             column=0,
                                                             sticky=(W, E))
    self.quitButton = tk.Button(self.mainframe,
                                text='Quit',
                                command=self.quitgui).grid(row=2,
                                                           column=0,
                                                           sticky=(W, W))
    self.instanceLabel = tk.Label(
        self.mainframe, text='Current Instance --> ').grid(row=3,
                                                           column=0,
                                                           sticky=(W, E))
    #self.existenceButton = tk.Button(self.mainframe, text='Existence', command=self.existence)
    #self.exempButton = tk.Button(self.mainframe, text='Exemplification', command=self.exemp)
    #self.optimizeButton = tk.Button(self.mainframe, text='(Omni)optimization', command=self.optimize)
    self.instanceInfo = StringVar(value="No Instance Detected")
    self.instanceText = tk.Label(self.mainframe,
                                 textvariable=self.instanceInfo).grid(
                                     row=3, column=1, sticky=(W, E))
    self.root.mainloop()

  def dos_docs(self):
    print("dos_docs called")

  def tools(self):
    print("tools called")


#driver code
gui = dos_gui()
