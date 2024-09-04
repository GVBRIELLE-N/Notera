import tkinter as tk
import random as r
import datetime as dt
from tkinter import messagebox
from datetime import datetime as ddt
from config.themes import *
from config.import_export import *
from config.settings import *
from config.footer import rFooter
from tools.espee import *
from tkinter import *
from tkinter import ttk
import os

global options
global task_count
            
def configureTheme():
    for wid in main_bg.winfo_children():
        if isinstance(wid, Button):
            wid.configure(relief=theme[options].relief, foreground=theme[options].button_fg, background=theme[options].button_bg,
                        activebackground=theme[options].button_bg_active, activeforeground=theme[options].button_fg, height=theme[options].height, borderwidth=theme[options].border_width,
                        font=(theme[options].font_main, 12))

def loadWidgets():
    global task_count
    for i in range(task_count):
        new_button_test = Button(main_bg, text=f"Note #{i+1}")
        new_button_test.pack(fill='x', pady='1', before=button_new_task)
        configureTheme()
    if task_count == 5:
        button_new_task.pack_forget()

def showAbout():
    """
    Display information about Notera
    """
    messagebox.showinfo("Notera - Alpha", "Notera Prototype Ver. 1\n\nDeveloped by LEOTHERA")

def restartProgram():
    """
    Destroys window and runs a shell script to rerun the program with applied changes
    """
    win_main.destroy()
    os.system("./runnotera.sh")

def getButtonName():
    global task_count
    t_count = loadNoteCount()
    with open("notecount.neo", "r+") as note_number:
        t_count = int(note_number.read())
        if t_count > 6:
            note_number.write("0")
        else:
            t_count += 1
            with open("notecount.neo", "w") as new_number:
                if t_count > 6:
                    new_number.write("0")
                else:
                    new_number.write(str(t_count))
    if t_count <= 6:
        new_button_test = Button(main_bg, text=f"Note #{t_count}")
        new_button_test.pack(fill='x', pady='1', before=button_new_task)
        configureTheme()
        if t_count == 5:
            button_new_task.pack_forget()

def changeTheme():
    main_bg.config(background=theme[options].bg)
    main_footer.config(background=theme[options].footer_bg)
    text_date.config(foreground=theme[options].fg, background=theme[options].bg, font=(theme[options].font_main, 12))
    text_footer.config(foreground=theme[options].fg_footer, background=theme[options].footer_bg, font=(theme[options].font_main, 10))
    text_footer_time.config(foreground=theme[options].fg_footer, background=theme[options].footer_bg, font=(theme[options].font_main, 10))
    configureTheme()    

def setTheme():
    """
    Changes the UI theme
    """
    global options
    chosen_theme = theme_var.get()
    with open("settings.neo", "w") as theme_setting:
        theme_setting.write(str(chosen_theme))
    options = loadSettings()
    changeTheme()

def updateTime():
    """
    Ensures the time and date displayed matches your current time
    """
    today = str(ddt.now())
    text_date.config(text=f"{today[0:10]}")
    text_footer_time.config(text=f"{today[11:16]}")
    win_main.after(100, updateTime)

def removeNotes():
    """
    Clears the list of notes created
    """
    remove = confirmClear()
    if remove:
        with open("notecount.neo", "w") as note_val:
            note_val.write("0")
        for wid in main_bg.winfo_children():
            if isinstance(wid, Button):
                wid.pack_forget()
        button_new_task.pack(fill='x', pady='1')
    else:
        pass

options = loadSettings()
task_count = loadNoteCount()
theme = {0:darkTheme, 1: lightTheme, 2:retroTheme, 3:simsTheme, 4:pipTheme, 5:nokiaTheme}

#Main Window
win_main = tk.Tk()
win_main.title("Notera - Alpha Build")
win_main.geometry('320x380')
win_main.resizable(False, False)
win_main.minsize('320', '380')
win_main.option_add('*tearOff', False)
theme_var = IntVar()
theme_var.set(options)

#Menubar and options
menu_main       = Menu(win_main)
menu_file       = Menu(menu_main, name='menu_file')
menu_options    = Menu(menu_main, name='menu_options')

options_theme   = Menu(menu_options, name='options_theme')

menu_main.add_cascade(menu=menu_file, label="File")
menu_main.add_cascade(menu=menu_options, label="Options")

menu_file.add_command(label="Import Notes Backup", command=note_import)
menu_file.add_command(label="Export Notes Backup", command=note_export)
menu_file.add_separator()
menu_file.add_command(label="Clear Notes", command=removeNotes)
menu_file.add_separator()
menu_file.add_command(label="About", command=showAbout)

menu_options.add_cascade(menu=options_theme, label="Set Theme")

#----------------------------Themes Menu-------------------------------------------------
options_theme.add_radiobutton(label='Dark', variable=theme_var, value=0, command=setTheme)
options_theme.add_radiobutton(label='Light', variable=theme_var, value=1, command=setTheme)
options_theme.add_radiobutton(label='Retromantic95', variable=theme_var, value=2, command=setTheme)
options_theme.add_radiobutton(label='Sul Sul', variable=theme_var, value=3, command=setTheme)
options_theme.add_radiobutton(label='Vault Kid', variable=theme_var, value=4, command=setTheme)
options_theme.add_radiobutton(label='Yes, Kia', variable=theme_var, value=5, command=setTheme)


#Frames
main_bg = Frame(win_main, background=theme[options].bg)
main_bg.pack(side=TOP, fill='both', expand=True)
main_bg.pack_propagate(0)

main_footer = Frame(win_main, background=theme[options].footer_bg, height='20')
main_footer.pack(side=BOTTOM, fill='x', anchor=S)

#Main Frame Widgets

text_date = Label(main_bg, text="00 - 00 - 0000", foreground=theme[options].fg, background=theme[options].bg, font=(theme[options].font_main, 12))
text_date.pack(side=TOP, pady='4')

button_new_task = Button(main_bg, text="+ New", command=getButtonName)
button_new_task.pack(fill='x', pady='1')

configureTheme()

#Footer Frame Widgets
text_footer = Label(main_footer, text=rFooter, foreground=theme[options].fg_footer, background=theme[options].footer_bg, font=(theme[options].font_main, 10))
text_footer.pack(side=LEFT, anchor=SW)

text_footer_time = Label(main_footer, text="00:00", foreground=theme[options].fg_footer, background=theme[options].footer_bg, font=(theme[options].font_main, 10))
text_footer_time.pack(side=RIGHT, anchor=SE)

if __name__ == "__main__":
    win_main['menu'] = menu_main
    loadWidgets()
    updateTime()
    win_main.mainloop()