import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.delay_time = tk.DoubleVar()
        self.create_widgets()
        

    def create_widgets(self):
        #Label
        self.filename_label = tk.Label(self, text="")
        self.filename_label.grid(row=0, column=1)

        self.request_label = tk.Label(self, text='요청 파일명:')
        self.request_label.grid(row=0, column=0)

        self.delay_time_label = tk.Label(self, text="딜레이 (초)")
        self.delay_time_label.grid(row=1, column=0)

        #Button
        self.search_btn = tk.Button(self, text='파일 탐색', command=self.add_file)
        self.search_btn.grid(row=3, column=0, pady=5)

        #Entry
        self.delay_time_entry = tk.Entry(self, width=7, textvariable=self.delay_time)
        self.delay_time_entry.grid(row=1, column=1)

        #ProgressBar
        self.progress = Progressbar(self,orient=tk.HORIZONTAL,length=150)
        self.progress.grid(row=2,column=0,columnspan=2,pady=5)
    
    def add_file(self):
        filename = filedialog.askopenfilename(initialdir='./list', title='파일 탐색', filetypes=[("text files", "*.txt")])
        self.filename_label.config(text=f"{filename.split('/')[-1]}")
        self.FILENAME = filename
        

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.title('InputSample')
root.geometry('250x150')
app = Application(master=root)
app.mainloop()
