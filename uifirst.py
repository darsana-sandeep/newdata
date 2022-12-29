from tkinter import *
import tkinter as tk
from tkinter import filedialog as fd
from cv2 import line
from matplotlib import markers
from matplotlib.animation import FuncAnimation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm


class Browse(tk.Frame):
    """ Creates a frame that contains a button when clicked lets the user to select
    a file and put its filepath into an entry.
    """


    def __init__(self, master, initialdir='', filetypes=()):
        super().__init__(master)
        self.filepath = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes
        
        self._create_widgets()
        self._display_widgets()

    def _create_widgets(self):
        self.user_name = tk.Label(self,text = "Predictive Maintanance",fg='white',bg="red",font=("bold", 20))
        self._entry = tk.Entry(self, textvariable=self.filepath, font=("bold", 10))
        self._button = tk.Button(self, text="Browse...",bg="white",fg="black", command=self.browse)
        
    def _display_widgets(self):  
        self.user_name.pack()      
        self._entry.pack(fill='both', expand=True)
        self._button.pack(fill='y')
        

    
    def browse(self):
        self.filepath.set(fd.askopenfilename(initialdir=self._initaldir,
                                             filetypes=self._filetypes))
        var=pd.read_excel(self.filepath.get())
        print(var)
        self._buttonlive = tk.Button(self, text="Live Grapgh...",bg="white",fg="black", command=self.live)
        self._buttoncustom = tk.Button(self, text="Custom Grapgh...",bg="white",fg="black", command=self.live)
        self._buttongraph = tk.Button(self, text="Static Grapgh...",bg="white",fg="black", command=self.static1)
        self._buttonlive.pack(fill='y')
        self._buttoncustom.pack(fill='y')
        self._buttongraph.pack(fill='y')


    def animate(self,i):
        df = pd.read_excel(self.filepath.get(),engine='openpyxl') # only for xlsx files

#print(df.to_string())
#print(df.columns)
        X= df.iloc[-10:-1, :2].values
        p=pd.DataFrame(X)
        print(p.to_string())
        print(p.columns)
        y=p[1].to_numpy()
        x=p[0].to_numpy()
        upper=458
        lower=452
        plt.cla()
        plt.axhline(y = 458,label ='Upper Limit-458', color = 'r', linestyle = '-')
        plt.axhline(y = 455, label ='Tolerance-455',color = 'g', linestyle = '-')
        plt.axhline(y = 452,label ='Lower Limit-452', color = 'r', linestyle = '-')
        plt.legend(loc ='upper left')
        for x1,x2,y1,y2 in zip(x,x[1:],y,y[1:]):
            if y2<upper and y2>lower:
                plt.plot([x1,x2],[y1,y2],'g')
            elif y2>upper or y2 <lower:
                plt.plot([x1,x2],[y1,y2],'r')

    def live(self):
        

        plt.xlabel("Time")
        plt.ylabel("Input V")
        ani=FuncAnimation(plt.gcf(),self.animate,interval=1000)


        plt.show()

    def static1(self):
        df = pd.read_excel(self.filepath.get(),engine='openpyxl',header=3) # only for xlsx files
        print(df)

#print(df.to_string())
#print(df.columns)
        X= df.iloc[4:28, :2].values
        p=pd.DataFrame(X)
        print(p.to_string())
        print(p.columns)
        y=df["Input V"].to_numpy()
        x=p[0].to_numpy()
        upper=458
        lower=452
        plt.cla()
        plt.axhline(y = 458,label ='Upper Limit-458', color = 'r', linestyle = '-')
        plt.axhline(y = 455, label ='Tolerance-455',color = 'g', linestyle = '-')
        plt.axhline(y = 452,label ='Lower Limit-452', color = 'r', linestyle = '-')
        plt.legend(loc ='upper left')
        for x1,x2,y1,y2 in zip(x,x[1:],y,y[1:]):
            if y2<upper and y2>lower:
                plt.plot([x1,x2],[y1,y2],'g')
            elif y2>upper or y2 <lower:
                plt.plot([x1,x2],[y1,y2],'r')  
        plt.xlabel("Time")
        plt.ylabel("Input V")
        
                             

        plt.show()
              
   

root = tk.Tk()
labelfont = ('times', 10, 'bold')
root.geometry("500x500")
filetypes = (
        ('Excel', '*.xlsx'),
        ("All files", "*.*")
    )

file_browser = Browse(root, initialdir=r"E:\infopark_solutions",filetypes=filetypes)
file_browser.pack(fill='y')
root.mainloop()