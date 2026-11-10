import tkinter as tk
from tkinter import messagebox
import webbrowser

root = tk.Tk()
root.title("Roblox Cheat GUI")
root.geometry("400x500")
label = tk.Label(root, text="Roblox Cheat GUI", font=("Arial", 24))
label.pack(pady=20)

def button_bomber():
    
    messagebox.askretrycancel("Roblox Cheat GUI", "Something went wrong.") 
    webbrowser.open("https://youtube.com")


button = tk.Button(root, text="Inject into Roblox", command=button_bomber)
button.pack(pady=10)

root.mainloop()