import os
from tkinter import messagebox

def loadSettings():
    if os.path.exists("settings.neo"):
        with open("settings.neo", "r+") as settings:
            get_options = settings.read()
            if get_options == '':
                settings.write("0")
                return 0
            else:
                return int(get_options)
    

def loadTaskCount():
    if os.path.exists("tasks.neo"):
        with open("tasks.neo", "r+") as taskcount:
            get_count = taskcount.read()
            if get_count == '':
                taskcount.write("0")
                return 0
            else:
                return int(get_count)
    else:
        with open("settings.neo", "w") as newTasks:
            newTasks.write("0")

def confirmClear():
    clear_confirm = messagebox.askyesno("Clear Task List", "Are you sure you want to clear the task list?")
    return clear_confirm