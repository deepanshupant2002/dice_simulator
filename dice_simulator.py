import random
import tkinter as tk

root = tk.Tk()
root.title("DICE")
root.geometry("400x300")

label  = tk.Label(root,font = ("verdana",200),fg = "red",text = "")

def dice():
    num =["\u2680","\u2681","\u2682","\u2683","\u2684","\u2685"]
    label.configure(text = f"{random.choice(num)}")
    label.pack()
    
box = tk.Button(root,font=("verdana",15),text="ROLL DICE",bg="yellow",command=dice)
box.pack()



root.mainloop()