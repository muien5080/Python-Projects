import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import ttk
import os

# ------------------ Main Window ------------------ #
root = tk.Tk()
root.title("Advanced Text Editor")
root.geometry("900x600")

current_file = None
current_font_family = "Arial"
current_font_size = 12

# ------------------ Functions ------------------ #

def update_title(name=None):
    if name:
        root.title(f"{name} - Advanced Text Editor")
    else:
        root.title("Untitled - Advanced Text Editor")

def new_file():
    global current_file
    text_area.delete(1.0, tk.END)
    current_file = None
    update_title()

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        current_file = file_path
        update_title(os.path.basename(file_path))

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(text_area.get(1.0, tk.END))
    else:
        save_as()

def save_as():
    global current_file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        current_file = file_path
        save_file()
        update_title(os.path.basename(file_path))

def exit_app():
    root.quit()

# ------------------ Theme ------------------ #

def set_theme(theme):
    themes = {
        "Light": ("black", "white"),
        "Dark": ("white", "#2b2b2b"),
        "Blue": ("white", "#1e3d59")
    }
    fg, bg = themes.get(theme, ("black", "white"))
    text_area.config(fg=fg, bg=bg, insertbackground=fg)

# ------------------ Font Controls ------------------ #

def change_font_family(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_area.config(font=(current_font_family, current_font_size))

def change_font_size(event=None):
    global current_font_size
    current_font_size = int(font_size.get())
    text_area.config(font=(current_font_family, current_font_size))

# ------------------ Find ------------------ #

def find_text():
    text_area.tag_remove("highlight", "1.0", tk.END)
    search = simpledialog.askstring("Find", "Enter text to find:")
    if search:
        start_pos = "1.0"
        while True:
            start_pos = text_area.search(search, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            end_pos = f"{start_pos}+{len(search)}c"
            text_area.tag_add("highlight", start_pos, end_pos)
            start_pos = end_pos
        text_area.tag_config("highlight", background="yellow", foreground="black")

# ------------------ Status Bar ------------------ #

def update_status(event=None):
    text = text_area.get(1.0, tk.END)
    words = len(text.split())
    chars = len(text) - 1
    status_bar.config(text=f"Words: {words} | Characters: {chars}")

# ------------------ UI Setup ------------------ #

# Toolbar Frame
toolbar = tk.Frame(root)
toolbar.pack(fill="x")

# Font Family Dropdown
font_family = ttk.Combobox(toolbar, values=["Arial", "Calibri", "Times New Roman", "Courier"])
font_family.set(current_font_family)
font_family.pack(side="left", padx=5)
font_family.bind("<<ComboboxSelected>>", change_font_family)

# Font Size Dropdown
font_size = ttk.Combobox(toolbar, values=[8, 10, 12, 14, 16, 18, 20, 24])
font_size.set(current_font_size)
font_size.pack(side="left", padx=5)
font_size.bind("<<ComboboxSelected>>", change_font_size)

# Theme Dropdown
theme_box = ttk.Combobox(toolbar, values=["Light", "Dark", "Blue"])
theme_box.set("Light")
theme_box.pack(side="left", padx=5)
theme_box.bind("<<ComboboxSelected>>", lambda e: set_theme(theme_box.get()))

# Text Area
text_area = tk.Text(root, wrap="word", undo=True)
text_area.pack(fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(side="right", fill="y")
scrollbar.config(command=text_area.yview)
text_area.config(yscrollcommand=scrollbar.set)

# Status Bar
status_bar = tk.Label(root, text="Words: 0 | Characters: 0", anchor="e")
status_bar.pack(fill="x", side="bottom")

text_area.bind("<KeyRelease>", update_status)

# ------------------ Menu ------------------ #

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

edit_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text_area.edit_undo, accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", command=text_area.edit_redo, accelerator="Ctrl+Y")
edit_menu.add_command(label="Find", command=find_text, accelerator="Ctrl+F")

# Keyboard Shortcuts
root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())
root.bind("<Control-f>", lambda e: find_text())
root.bind("<Control-z>", lambda e: text_area.edit_undo())
root.bind("<Control-y>", lambda e: text_area.edit_redo())

update_title()
set_theme("Light")
root.mainloop()