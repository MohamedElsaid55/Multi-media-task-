# mohamd elsaied mohamed elsaied 
import tkinter as tk
from tkinter import messagebox 
def on_button_click():
    print("Hello,I'am Mohamed")
root = tk.Tk()
root.title("GUI with python") 
root.geometry("300x150")         
my_button = tk.Button(
    master=root, 
    text="Button!",
    command=on_button_click
)
my_button.pack(pady=40)
root.mainloop()
print("GUI application closed.")