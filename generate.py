#-----generate.py-----#
#
# This is the main py
# file that generates
# the LaTeX files
#
# To-Do --> GUI!!!
#
#---------------------#

#----Dependencies----#
import sys
import fileinput
import os
import shutil
import pylatex

from tkinter import *
from tkinter import ttk

from datetime import date

def generate():
    cwd = os.getcwd()
    os.chdir("..")
    os.mkdir("New Report")
    os.mkdir("New Report/src")
    os.mkdir("New Report/img")
    os.mkdir("New Report/tex")

#--------Main--------#
def main():

    #Setting up GUI
    root = Tk()
    author_input = StringVar()
    title_input = StringVar()
    subtitle_input = StringVar()

    root.title("LaTeX Generator")

    mainframe = ttk.Frame(root, padding="3 3 12 12")

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    

    ttk.Label(mainframe,
              text="Please enter the following info to generate your LaTeX Project...").grid(columnspan=2, column=3, row=1, sticky=W)

    ttk.Label(mainframe, text="Project Type: ").grid(column=3,
                                                     row=3, sticky=E)
    
    project_type = ttk.Combobox(mainframe,
                                values = ["report", "notes"],
                                state="readonly").grid(column=4,
                                                           row=3, sticky=W)


    ttk.Label(mainframe, text="Author: ").grid(column=3, row=5, sticky=E)
    author = ttk.Entry(mainframe,
                       textvariable = author_input).grid(column=4,
                                                     row=5, sticky=W)

    
    ttk.Label(mainframe, text="Title: ").grid(column=3, row=7, sticky=E)
    title = ttk.Entry(mainframe,
                      textvariable = title_input).grid(column=4,
                                                       row=7, sticky=W)

    
    ttk.Label(mainframe, text="Sub-Title: ").grid(column=3, row=9, sticky=E)
    subtitle = ttk.Entry(mainframe,
                         textvariable = subtitle_input).grid(column=4,
                                                             row=9, sticky=W)

    
    ttk.Button(mainframe, text="Generate", command=generate).grid(column=4, row=11, sticky=E)
    root.mainloop()




if __name__ == "__main__":
    main()
