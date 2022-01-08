import tkinter as tk
from tkinter import ttk
import json


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

        for i in range(1000):
            self.objectsList.insert(tk.END, "Object " + str(i))
            self.assetsList.insert(tk.END, "Asset " + str(i))
            self.scenesList.insert(tk.END, "Scene " + str(i))

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


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
