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

    '''
    print("========================================")
    print("|| Welcome to my LaTeX Generator v1.0 ||")
    print("========================================")
    print("Type 'e' at any point to exit...")
    
    cwd = os.getcwd()
    os.chdir("..")
    os.mkdir("New Report")
    os.mkdir("New Report/src")
    os.mkdir("New Report/img")
    os.mkdir("New Report/tex")
    

    #Recruiter Name
    text_in = input("Author: ")
    recruiter_name = text_in if text_in != "e" else sys.exit()

    #Company Name
    text_in = input("Enter Name of Company: ")
    company_name = text_in if text_in != "e" else sys.exit()

    #Company Address
    text_in = input("Enter Company Address: ")
    company_address = text_in if text_in != "e" else sys.exit()

    #set today's date
    today_date = date.today().strftime("%B %d, %Y")


    #make folder architecture
    #eventually -> chose target folder

    cwd = os.getcwd()
    cwd.chdir("..")
    os.mkdir("New Report")
    
    
    #copy folder
    new_folder = "%s -- Cover Letter" % company_name
    new_file = company_name + "_cover_letter.tex"
    os.mkdir(new_folder)
    shutil.copy("templates/template.tex", new_folder + "/" + new_file)

    #
    
    with fileinput.FileInput(new_folder + "/" + new_file, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("<DATE>", today_date), end='')
        for line in file:
            print(line.replace("<RECRUITER_NAME>", recruiter_name), end='')
    '''

if __name__ == "__main__":
    main()
