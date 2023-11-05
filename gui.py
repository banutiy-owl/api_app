import webbrowser
import tkinter as tk
from api_endpoints import *


def open_webpage():
    webbrowser.open('http://localhost:5000/books')

root = tk.Tk()
root.title("Desktop App")

button = tk.Button(root, text="Open Books Page", command=open_webpage)
button.pack(pady=20)

root.mainloop()