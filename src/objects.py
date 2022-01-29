import tkinter as tk
from tkinter import ttk
import PIL
from PIL import Image as img, ImageTk
import json



class CanvasObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        if self.type == "image":
            self.image = img.open(self.path)
            self.image = self.image.resize((int(self.width*self.scale), int(self.height*self.scale)), PIL.Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.image)
        self.draw()
    
    def moveX(self, x):
        self.x += x
    
    def moveY(self, y):
        self.y += y
    
    def changeWidth(self, width):
        self.width = width
    
    def changeHeight(self, height):
        self.height = height
    
    def changeScale(self, scale):
        self.scale = scale
        
    def draw(self):
        if self.type == "image":
            self.canvasObject = self.canvas.create_image(self.x, self.y, image=self.image, anchor="nw")
        elif self.type == "text":
            self.canvasObject = self.canvas.create_text(self.x, self.y, text=self.text, font=(self.font, self.fontSize), fill=self.fill, anchor="nw")
        elif self.type == "rectangle":
            self.canvasObject = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill)
        elif self.type == "ellipse":
            self.canvasObject = self.canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill)
        elif self.type == "line":
            self.canvasObject = self.canvas.create_line(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.fill, width=self.thickness)
    
    def update(self):
        self.canvas.delete(self.id)
        self.draw()