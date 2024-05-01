from tkinter import messagebox
from tkinter import filedialog
import random as r

def task_import():
    try:
        import_file = filedialog.askopenfile(title="Select Task File", filetypes=[("Notera Tasks", ".ntrt")])
        the_content = import_file.read()
        messagebox.showinfo("The Content", the_content)
    except AttributeError:
        pass

def task_export():
    try:
        export_file = filedialog.asksaveasfile(title="Export Task File", filetypes=[("Notera Tasks", ".ntrt")], initialfile="New Task File", defaultextension=".ntrt")
        content = f"Okie This Works! {r.randint(0,99)}"
        export_file.write(content)
    except AttributeError:
        pass