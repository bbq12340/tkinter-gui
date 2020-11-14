# 아직 이해 안감...
import tkinter as tk
import subprocess as sub
p = sub.Popen('./script',stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()

root = tk.Tk()
text = tk.Text(root)
text.pack()
text.insert(tk.END, output)
root.mainloop()