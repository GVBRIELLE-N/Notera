from tkinter import messagebox
from tkinter import filedialog
import random as r

def note_import():
    try:
        import_file = filedialog.askopenfile(title="Select Backup File", filetypes=[("Notera Notes Backup", ".ntrt")])
        the_content = import_file.read()
        messagebox.showinfo("The Content", the_content)
    except AttributeError:
        pass

def note_export():
    try:
        export_file = filedialog.asksaveasfile(title="Export Backup File", filetypes=[("Notera Notes Backup", ".ntrt")], initialfile="New Notes Backup", defaultextension=".ntrt")
        content = f"Okie This Works! {r.randint(0,99)}"
        export_file.write(content)
    except AttributeError:
        pass