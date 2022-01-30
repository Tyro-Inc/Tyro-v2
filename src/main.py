import tkinter as tk
from tkinter import ttk
import json
from objects import *
from tkinter import filedialog, colorchooser, font, messagebox
import random
import json
import shutil
from time import sleep
import sys
import os

class App:
    def __init__(self, root):
        # Initialize the root window
        root.title("Tyro Engine")
        width = 1152
        height = 648
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        self.root = root

        styles = json.load(open("config.json"))
        root.configure(background=styles["core"]["background"])

        s = ttk.Style()
        s.theme_use("default")
        s.configure(
            "TNotebook.Tab",
            background=styles["notebook"],
            foreground=styles["text"]["text"],
        )
        s.configure("TNotebook", background=styles["notebook"])
        s.configure("TFrame", background=styles["notebook"])
        s.configure(
            "TLabel", background=styles["notebook"], foreground=styles["text"]["text"]
        )
        s.map("TNotebook.Tab", background=[("selected", styles["tabs"])])

        self.itemsnotebook = ttk.Notebook(root)
        self.itemsnotebook.place(relx=0.01, rely=0.01, relwidth=0.15, relheight=0.98)

        self.objectsTab = ttk.Frame(self.itemsnotebook)
        self.itemsnotebook.add(self.objectsTab, text="Objects")
        self.objectsList = tk.Listbox(
            self.objectsTab,
            background=styles["lists"],
            foreground=styles["text"]["text"],
            selectmode=tk.SINGLE,
        )
        self.objectsList.bind("<<ListboxSelect>>", self.displayProperties)
        self.objectsList.place(x=0, y=0, relwidth=1, relheight=1)
        self.objectsListYScroll = tk.Scrollbar(self.objectsTab, orient=tk.VERTICAL)
        self.objectsListYScroll.place(relx=0.9, rely=0, relheight=1, relwidth=0.1)
        self.objectsList.configure(yscrollcommand=self.objectsListYScroll.set)
        self.objectsListYScroll.configure(command=self.objectsList.yview)

        self.assetsTab = ttk.Frame(self.itemsnotebook)
        self.itemsnotebook.add(self.assetsTab, text="Assets")
        self.assetsList = tk.Listbox(
            self.assetsTab,
            background=styles["lists"],
            foreground=styles["text"]["text"],
            selectmode=tk.SINGLE,
        )
        self.assetsList.place(x=0, y=0, relwidth=1, relheight=1)
        self.assetsListYScroll = tk.Scrollbar(self.assetsTab, orient=tk.VERTICAL)
        self.assetsListYScroll.place(relx=0.9, rely=0, relheight=1, relwidth=0.1)
        self.assetsList.configure(yscrollcommand=self.assetsListYScroll.set)
        self.assetsListYScroll.configure(command=self.assetsList.yview)

        self.scenesTab = ttk.Frame(self.itemsnotebook)
        self.itemsnotebook.add(self.scenesTab, text="Scenes")
        self.scenesList = tk.Listbox(
            self.scenesTab,
            background=styles["lists"],
            foreground=styles["text"]["text"],
            selectmode=tk.SINGLE,
        )
        self.scenesList.place(x=0, y=0, relwidth=1, relheight=1)
        self.scenesListYScroll = tk.Scrollbar(self.scenesTab, orient=tk.VERTICAL)
        self.scenesListYScroll.place(relx=0.9, rely=0, relheight=1, relwidth=0.1)
        self.scenesList.configure(yscrollcommand=self.scenesListYScroll.set)
        self.scenesListYScroll.configure(command=self.scenesList.yview)

        # for i in range(1000):
        #     self.objectsList.insert(tk.END, "Object " + str(i))
        #     self.assetsList.insert(tk.END, "Asset " + str(i))
        #     self.scenesList.insert(tk.END, "Scene " + str(i))

        self.editorTabs = ttk.Notebook(root)
        self.editorTabs.place(relx=0.17, rely=0.01, relwidth=0.67, relheight=0.98)

        self.canvasTab = ttk.Frame(self.editorTabs)
        self.editorTabs.add(self.canvasTab, text="Canvas")
        self.canvas = tk.Canvas(self.canvasTab, background="#ffffff")
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        self.initTab = ttk.Frame(self.editorTabs)
        self.editorTabs.add(self.initTab, text="Init")
        self.initCodeEditor = tk.Text(
            self.initTab,
            wrap="none",
            background=styles["text"]["background"],
            foreground=styles["text"]["text"],
            font=("Consolas", 20),
        )
        self.initCodeEditor.place(x=0, y=0, relwidth=0.98, relheight=0.98)
        self.initCodeEditorXScroll = tk.Scrollbar(
            self.initTab, orient="horizontal", command=self.initCodeEditor.xview
        )
        self.initCodeEditorXScroll.place(x=0, rely=0.98, relwidth=1)
        self.initCodeEditor.configure(xscrollcommand=self.initCodeEditorXScroll.set)
        self.initCodeEditorYScroll = tk.Scrollbar(
            self.initTab, orient="vertical", command=self.initCodeEditor.yview
        )
        self.initCodeEditorYScroll.place(relx=0.981125, y=0, relheight=1)
        self.initCodeEditor.configure(yscrollcommand=self.initCodeEditorYScroll.set)

        self.runtimeTab = ttk.Frame(self.editorTabs)
        self.editorTabs.add(self.runtimeTab, text="Runtime")
        self.runtimeCodeEditor = tk.Text(
            self.runtimeTab,
            wrap="none",
            background=styles["text"]["background"],
            foreground=styles["text"]["text"],
            font=("Consolas", 20),
        )
        self.runtimeCodeEditor.place(x=0, y=0, relwidth=0.98, relheight=0.98)
        self.runtimeCodeEditorXScroll = tk.Scrollbar(
            self.runtimeTab, orient="horizontal", command=self.runtimeCodeEditor.xview
        )
        self.runtimeCodeEditorXScroll.place(x=0, rely=0.98, relwidth=1)
        self.runtimeCodeEditor.configure(
            xscrollcommand=self.runtimeCodeEditorXScroll.set
        )
        self.runtimeCodeEditorYScroll = tk.Scrollbar(
            self.runtimeTab, orient="vertical", command=self.runtimeCodeEditor.yview
        )
        self.runtimeCodeEditorYScroll.place(relx=0.981125, y=0, relheight=1)
        self.runtimeCodeEditor.configure(
            yscrollcommand=self.runtimeCodeEditorYScroll.set
        )

        self.propertiesFrame = ttk.Frame(root)
        self.propertiesFrame.place(relx=0.85, rely=0.01, relwidth=0.15, relheight=0.98)
        self.PropertiesLabel = ttk.Label(self.propertiesFrame, text="Properties")
        self.PropertiesLabel.place(x=0, y=0, width=100, height=20)
        
        # Initialize the Menu bar
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)

        self.addobjectmenu = tk.Menu(self.menu)
        self.filemenu = tk.Menu(self.menu)

        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.menu.add_cascade(label="Add Object", menu=self.addobjectmenu)

        self.addobjectmenu.add_command(
            label="Image", command=lambda: self.addImage(""), accelerator="Ctrl+I")
        self.addobjectmenu.add_command(
            label="Rectangle", command=lambda: self.addRectangle(""), accelerator="Ctrl+R")
        self.addobjectmenu.add_command(
            label="Ellipse", command=lambda: self.addEllipse(""), accelerator="Ctrl+E")
        self.addobjectmenu.add_command(
            label="Line", command=lambda: self.addLine(""), accelerator="Ctrl+L")
        self.addobjectmenu.add_command(
            label="Text", command=lambda: self.addText(""), accelerator="Ctrl+T")

        self.root.bind("<Control-i>", self.addImage)
        self.root.bind("<Control-r>", self.addRectangle)
        self.root.bind("<Control-e>", self.addEllipse)
        self.root.bind("<Control-l>", self.addLine)
        self.root.bind("<Control-t>", self.addText)
        self.objects = {}
        
        
    def addImage(self, arg):
        """
        Ask the user to select an image and then adds it to the project
        """
        image = filedialog.askopenfilename(
            initialdir="/",
            title="Select file",
            filetypes=(("png files", "*.png"), ("all files", "*.*")),
        )
        if image != "":
            ID = str(random.randint(1000, 10000))
            imgname = image.split("/")[-1]
            imgname = f"{imgname.split('.')[0]}_{ID}"
            self.objects[imgname] = CanvasObject(id=ID, name=imgname, path=image, type="image", x=0, y=0, scale=1, 
                                                    width=100, height=100, canvas=self.canvas)
            self.root.image = self.objects[imgname].image
            self.objects[imgname].draw()
            self.objectsList.insert(tk.END, imgname)

    def addRectangle(self, arg):
        """
        Creates a new rectangle object and adds it to the project
        """
        ID = str(random.randint(1000, 10000))
        self.objects["rectangle_" + str(ID)] = CanvasObject(id=ID, name="rectangle_" + str(ID), canvas=self.canvas, 
                                                            x=0, y=0, width=100, height=100, scale=1, fill="#999999",
                                                            type="rectangle")
        self.objects["rectangle_" + str(ID)].draw()
        self.objectsList.insert(tk.END, "rectangle_" + str(ID))

    def addEllipse(self, arg):
        """
        Creates a new Ellipse object and adds it to the project
        """
        ID = str(random.randint(1000, 10000))
        self.objects["ellipse_" + str(ID)] = CanvasObject(id=ID, name="ellipse_" + str(ID), canvas=self.canvas, 
                                                            x=0, y=0, width=100, height=100, scale=1, fill="#999999",
                                                            type="ellipse")
        self.objects["ellipse_" + str(ID)].draw()
        self.objectsList.insert(tk.END, "ellipse_" + str(ID))

    def addLine(self, arg):
        """
        Creates a new Line object and adds it to the project
        """
        ID = str(random.randint(1000, 10000))
        self.objects["line_" + str(ID)] = CanvasObject(id=ID, name="line_" + str(ID), canvas=self.canvas, 
                                                            x=0, y=0, width=100, height=100, scale=1, fill="#999999",
                                                            type="line", thickness=5)
        self.objects["line_" + str(ID)].draw()
        self.objectsList.insert(tk.END, "line_" + str(ID))

    def addText(self, arg):
        """
        Creates a new Text object and adds it to the project
        """
        ID = str(random.randint(1000, 10000))
        self.objects["text_" + str(ID)] = CanvasObject(id=ID, name="text_" + str(ID), canvas=self.canvas, 
                                                            x=0, y=0, width=100, height=100, scale=1, fill="#999999",
                                                            type="text", fontSize=18, text="Text", font="Consolas")
        self.objects["text_" + str(ID)].draw()
        self.objectsList.insert(tk.END, "text_" + str(ID))
    
    def displayProperties(self, arg):
        try:
            self.currentItem = self.objectsList.get(self.objectsList.curselection())
            currentItem = self.currentItem
            currentItem = self.objects[currentItem].__dict__
            props = []
            self.propElements = {}
            for key in currentItem.keys():
                props.append([key, currentItem[key]])
            y=0.05
            for item in self.propertiesFrame.winfo_children():
                item.destroy()
            for propert, value in props:
                if propert not in ["canvas", "id", "canvasObject", "type", "image"]:
                    self.propElements[propert] = {}
                    self.propElements[propert]["label"] = ttk.Label(self.propertiesFrame, text=propert)
                    self.propElements[propert]["value"] = tk.StringVar()
                    self.propElements[propert]["value"].set(value)
                    self.propElements[propert]["entry"] = tk.Entry(self.propertiesFrame, textvariable=self.propElements[propert]["value"])
                    self.propElements[propert]["label"].place(relx=0, rely=y, relwidth=0.5, relheight=0.05)
                    self.propElements[propert]["entry"].place(relx=0.5, rely=y, anchor="nw", relwidth=0.5, relheight=0.05)
                    self.propElements[propert]["entry"].bind("<Return>", self.updateObject)
                    y+=0.05
            self.PropertiesLabel = ttk.Label(self.propertiesFrame, text="Properties")
            self.PropertiesLabel.place(x=0, y=0, width=100, height=20)
        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)
    
    def updateObject(self, arg):
        try:
            currentItem = self.currentItem
            for keys in self.propElements.keys():
                try:
                    self.objects[currentItem].__dict__[keys] = int(self.propElements[keys]["value"].get())
                except:
                    self.objects[currentItem].__dict__[keys] = self.propElements[keys]["value"].get()
                self.objects[currentItem].update()
                GameObject = self.objects[currentItem]
                del self.objects[currentItem]
                self.objects[GameObject.name] = GameObject
                
                self.objectsList.delete(0, tk.END)
                for i in self.objects.keys():
                    self.objectsList.insert(tk.END, i)
        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
