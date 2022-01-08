import tkinter as tk
from tkinter import ttk

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
        
        # #make properties fram on the right
        # self.propertiesFrame = ttk.Frame(root)
        # self.propertiesFrame.place(x=1152-200, y=48, width=200, height=600)
        # self.nameLabel = ttk.Label(self.propertiesFrame, text="Name:")
        # self.nameLabel.place(x=0, y=0, width=100, height=20)
        # self.nameEntry = ttk.Entry(self.propertiesFrame)
        # self.nameEntry.place(x=100, y=0, width=100, height=20)
        # self.nameEntry.insert(0, "Object")
        # self.xLabel = ttk.Label(self.propertiesFrame, text="X:")
        # self.xLabel.place(x=0, y=20, width=100, height=20)
        # self.xEntry = ttk.Entry(self.propertiesFrame)
        # self.xEntry.place(x=100, y=20, width=100, height=20)
        # self.xEntry.insert(0, "0")
        # self.yLabel = ttk.Label(self.propertiesFrame, text="Y:")
        # self.yLabel.place(x=0, y=40, width=100, height=20)
        # self.yEntry = ttk.Entry(self.propertiesFrame)
        # self.yEntry.place(x=100, y=40, width=100, height=20)
        # self.yEntry.insert(0, "0")
        # self.widthLabel = ttk.Label(self.propertiesFrame, text="Width:")
        # self.widthLabel.place(x=0, y=60, width=100, height=20)
        # self.widthEntry = ttk.Entry(self.propertiesFrame)
        # self.widthEntry.place(x=100, y=60, width=100, height=20)
        # self.widthEntry.insert(0, "0")
        # self.heightLabel = ttk.Label(self.propertiesFrame, text="Height:")
        # self.heightLabel.place(x=0, y=80, width=100, height=20)
        # self.heightEntry = ttk.Entry(self.propertiesFrame)
        # self.heightEntry.place(x=100, y=80, width=100, height=20)
        # self.heightEntry.insert(0, "0")
        # self.scaleLabel = ttk.Label(self.propertiesFrame, text="Scale:")
        # self.scaleLabel.place(x=0, y=100, width=100, height=20)
        # self.scaleEntry = ttk.Entry(self.propertiesFrame)
        # self.scaleEntry.place(x=100, y=100, width=100, height=20)
        # self.scaleEntry.insert(0, "1")
        
        self.itemsnotebook = ttk.Notebook(root)
        self.itemsnotebook.place(relx=0.01, rely=0.01, relwidth=0.15, relheight=0.98)
        self.objectsTab = ttk.Frame(self.itemsnotebook)
        self.itemsnotebook.add(self.objectsTab, text="Objects")
        self.objectsList = tk.Listbox(self.objectsTab)
        self.objectsList.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.assetsTab = ttk.Frame(self.itemsnotebook)
        self.itemsnotebook.add(self.assetsTab, text="Assets")
        self.assetsList = tk.Listbox(self.assetsTab)
        self.assetsList.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.scenesTab = ttk.Frame(self.itemsnotebook)
        self.itemsnotebook.add(self.scenesTab, text="Scenes")
        self.scenesList = tk.Listbox(self.scenesTab)
        self.scenesList.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.editorTabs = ttk.Notebook(root)
        self.editorTabs.place(relx=0.17, rely=0.01, relwidth=0.68, relheight=0.98)
        
        self.canvasTab = ttk.Frame(self.editorTabs)
        self.editorTabs.add(self.canvasTab, text="Canvas")
        self.canvas = tk.Canvas(self.canvasTab)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.runtimeTab = ttk.Frame(self.editorTabs)
        self.editorTabs.add(self.runtimeTab, text="Runtime")
        self.runtimeCodeEditor = tk.Text(self.runtimeTab, wrap="none")
        self.runtimeCodeEditor.place(x=0, y=0, relwidth=0.98, relheight=0.98)
        self.runtimeCodeEditorXScroll = tk.Scrollbar(self.runtimeTab, orient="horizontal", command=self.runtimeCodeEditor.xview)
        self.runtimeCodeEditorXScroll.place(x=0, rely=0.98, relwidth=1)
        self.runtimeCodeEditor.configure(xscrollcommand=self.runtimeCodeEditorXScroll.set)
        self.runtimeCodeEditorYScroll = tk.Scrollbar(self.runtimeTab, orient="vertical", command=self.runtimeCodeEditor.yview)
        self.runtimeCodeEditorYScroll.place(relx=0.98, y=0, relheight=1)
        self.runtimeCodeEditor.configure(yscrollcommand=self.runtimeCodeEditorYScroll.set)
        
        self.initTab = ttk.Frame(self.editorTabs)
        self.editorTabs.add(self.initTab, text="Init")
        self.initCodeEditor = tk.Text(self.initTab, wrap="none")
        self.initCodeEditor.place(x=0, y=0, relwidth=0.98, relheight=0.98)
        self.initCodeEditorXScroll = tk.Scrollbar(self.initTab, orient="horizontal", command=self.initCodeEditor.xview)
        self.initCodeEditorXScroll.place(x=0, rely=0.98, relwidth=1)
        self.initCodeEditor.configure(xscrollcommand=self.initCodeEditorXScroll.set)
        self.initCodeEditorYScroll = tk.Scrollbar(self.initTab, orient="vertical", command=self.initCodeEditor.yview)
        self.initCodeEditorYScroll.place(relx=0.98, y=0, relheight=1)
        self.initCodeEditor.configure(yscrollcommand=self.initCodeEditorYScroll.set)
        
        self.propertiesFrame = ttk.Frame(root)
        self.propertiesFrame.place(relx=0.85, rely=0.01, relwidth=0.15, relheight=0.98)
        self.PropertiesLabel = ttk.Label(self.propertiesFrame, text="Properties")
        self.PropertiesLabel.place(x=0, y=0, width=100, height=20)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()