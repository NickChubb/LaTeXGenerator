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
from tkinter import messagebox

from datetime import date

#---Global Variables---#

report_fields = ["Author", "Title", "Sub-title", "Class"]
note_fields = ["Author", "Class", "Lecture"]
cl_fields = ["Name", "Company"]

fields_array = [report_fields, note_fields, cl_fields]

entries = {}

def makeReport():
    return

def makeNotes():
    return

def makeCL():
    return

#------Make Folder------#

def makeFolder(folder_title):
    
    cwd = os.getcwd()
    os.chdir("..")
    os.mkdir(folder_title)
    os.chdir(folder_title)
    os.mkdir("src")
    os.mkdir("img")
    os.mkdir("tex")

#------Make Fields------#

def makefields(contframe, root, button_index):

    #delete frame
    #make new frame
    #populate new frame

    entries.clear()

    if contframe.winfo_children() != 0:
        for widget in contframe.winfo_children():
            widget.destroy()

        

    for field in fields_array[button_index.get() - 1]:
        print(field)
        row = Frame(contframe)
        lab = Label(row, width=10, text=field+": ", anchor='w')
        ent = Entry(row)
        
        row.pack(side=TOP, 
                 fill=X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, 
                 expand=YES, 
                 fill=X)

        entries[field] = ent


#----Generate LaTeX----#

def generate(ents, btn_num):

    for entry in ents:
        if ents[entry].get() == "":

            #Throw error message if fields blank
            messagebox.showinfo("ERROR", "ERROR: No fields may be left blank")

            return

        

    if btn_num == 1:

        makeReport()

    elif btn_num == 2:

        makeNotes()

    elif btn_num == 2:

        makeCL()
        
    

#--------Main--------#
def main():
    

    #Setting up GUI
    root = Tk()

    root.geometry('300x300')

    root.title("LaTeX Generator v1.0")

    entryFrame = Frame(root)
    generateFrame = Frame(root)
    
    v = IntVar()

    Label(root, text="Choose your project type:", padx=20, pady=10).pack()

    btnReport = Radiobutton(root, text="Report", variable=v, value=1, command= lambda: makefields(entryFrame, root, v))
    btnReport.pack(anchor=W)

    btnNotes = Radiobutton(root, text="Notes", variable=v, value=2, command= lambda: makefields(entryFrame, root, v))
    btnNotes.pack(anchor=W)
    
    btnCL = Radiobutton(root, text="Cover Letter", variable=v, value=3, command= lambda: makefields(entryFrame, root, v))
    btnCL.pack(anchor=W)

    btnGen = Button(generateFrame, text="Generate", command = lambda: generate(entries, v.get()))
    btnGen.pack(anchor=E)

    entryFrame.pack()

    generateFrame.pack()
    
    
    root.mainloop()




if __name__ == "__main__":
    main()
