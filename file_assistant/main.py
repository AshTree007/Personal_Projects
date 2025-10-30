from tkinter import *
from tkinter import ttk
from utils import old_file, organizer,scanner
import os

root = Tk()
root.title("File Assistant")

assistant = ttk.Frame(root, padding=20)
assistant.grid(column=2, row=1, stick=(N,E,W,S))

#######treeview########
files = scanner.scan_folder(f"/{os.path.abspath(os.curdir).split("/")[1]}")
tree = ttk.Treeview(root)
tree.grid(column=1, row = 1 )
nodes = {}

for full_path in sorted(files.keys()):
    parts = [p for p in full_path.split(os.sep) if p]

    parent_key = ""
    for part in parts:
        node_key = parent_key + os.sep + part if parent_key else part

        if node_key not in nodes:
            parent_id = nodes.get(parent_key, "")
            item_id = tree.insert(parent_id, "end", text=part, open=False)
            nodes[node_key] = item_id

        parent_key = node_key

for child in tree.get_children():
    tree.item(child, open=True)
#########


def select():
    selected_item = tree.selection()[0]  
    parts = []
    while selected_item:
        part = tree.item(selected_item, "text")
        parts.insert(0, part)
        selected_item = tree.parent(selected_item)

    full_path = os.path.join(*parts)
    print(f"{full_path}/")
    return f"/{full_path}/"

def old(path):
    old_files = [x.split("/")[-1] for x in old_file.find_old_files(path)]
    x = 2
    old_display = ttk.Frame(root)
    old_display.grid(column=3, row =1)
    ttk.Label(old_display, text="Old Files:").grid(column=0, row=0)
    for files in old_files:
        ttk.Label(old_display, text = files).grid(column=0, row=x)
        x+=1

ttk.Label(assistant, text="Welcome to File Assistant", anchor="center").grid(column=1, row=0, sticky="NEW")
ttk.Button(assistant, text="Scan for old", command = lambda: old(select())).grid(column=0, row=2)
ttk.Button(assistant, text="Sort this folder", command = lambda: organizer.organize_file(select())).grid(column=2, row=2)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()