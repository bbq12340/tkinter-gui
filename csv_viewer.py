import tkinter as tk
from tkinter import ttk
import pandas as pd

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.read_data()
        self.create_widget()

    def read_data(self):
        self.df = pd.read_csv('sample_input/sample.csv', encoding='utf-8-sig', index_col="업체명")

    def set_tree(self):
        for c in self.df.columns:
            self.tree.column(c, stretch=tk.NO, width=50)
            self.tree.heading(c, text=c)
        for i in list(self.df.index):
            row=[]
            for j in self.df.columns:
                row.append(self.df.loc[i,j])
            self.tree.insert("", tk.END, text=i, values=row)
        return
        
    def create_widget(self):
        scrollx = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        scrolly = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.tree = ttk.Treeview(self, columns=list(self.df.columns), height='150', xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx["command"] = self.tree.xview
        scrolly["command"] = self.tree.yview
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)
        self.set_tree()
        self.tree.pack()

root = tk.Tk()
root.wm_geometry('400x400')
app = Application(master=root)
app.mainloop()