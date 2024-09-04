import os
from tkinter import messagebox

def loadSettings():
    """
    Loads the last saved configuration
    Currently only gets the saved theme value
    """
    if os.path.exists("settings.neo"):
        with open("settings.neo", "r+") as settings:
            get_options = settings.read()
            if get_options == '':
                settings.write("0")
                return 0
            else:
                return int(get_options)
    

def loadNoteCount():
    """
    Loads the last saved number of notes
    """
    if os.path.exists("notecount.neo"):
        with open("notecount.neo", "r+") as notecount:
            get_count = notecount.read()
            if get_count == '':
                notecount.write("0")
                return 0
            else:
                return int(get_count)
    else:
        with open("notecount.neo", "w") as newNotes:
            newNotes.write("0")

def confirmClear():
    """
    Allows the user to confirm that they want to clear the list of notes
    Returns a boolean value depending on the option the user selected
    """
    clear_confirm = messagebox.askyesno("Clear Note List", "Are you sure you want to clear all saved notes?")
    return clear_confirm
