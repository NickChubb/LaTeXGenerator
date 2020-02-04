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

#---Global Variables---#

report_fields = ["Author", "Title", "Sub-title", "Class"]
note_fields = ["Author", "Class", "Lecture"]
cl_fields = ["Name", "Company"]

fields_array = [report_fields, note_fields, cl_fields]

entries = {}

#------Make Fields------#

def makefields(contframe, root, button_index):

    #delete frame
    #make new frame
    #populate new frame

    entries.clear()

    if contframe.winfo_children() != 0:
        for widget in contframe.winfo_children():
            widget.destroy()


        #entries.clear()
        

    for field in fields_array[button_index.get() - 1]:
        print(field)
        row = Frame(contframe)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, 
                 fill=X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, 
                 expand=YES, 
                 fill=X)

        entries[field] = ent

    print(entries)


#----Generate LaTeX----#

def generate(auth, tit, subtit):

    folder_title = tit + "-- Report"
    
    cwd = os.getcwd()
    os.chdir("..")
    os.mkdir(folder_title)
    os.chdir(folder_title)
    os.mkdir("src")
    os.mkdir("img")
    os.mkdir("tex")

    

#--------Main--------#
def main():
    

    #Setting up GUI
    root = Tk()

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

    btnGen = Button(generateFrame, text="Generate")
    btnGen.pack(anchor=E)

    entryFrame.pack()

    generateFrame.pack()
    
    
    root.mainloop()

    '''

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

    
    ttk.Button(mainframe, text="Generate", command=lambda: generate(author, title_input, subtitle)).grid(column=4, row=11, sticky=E)
    root.mainloop()

    '''




if __name__ == "__main__":
    main()
