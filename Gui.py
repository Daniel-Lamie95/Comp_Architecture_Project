#GUI code
#import the tkinter library
import tkinter as tk
from tkinter import messagebox
from project import assemble
#run the assembler
def run_assembler():
    try:
        assemble()
        messagebox.showinfo(
            "Success",
            "Assembly completed successfully.\n\n"
            "Files generated:\n"
            "output.txt\n"
            "output_binary.txt"
        )
    except Exception as error:
        messagebox.showerror(
            "Assembler Error",
            str(error)
        )

#main application window(main program screen)
window= tk.Tk()
#set window name to assembler simulator and width=600 and height=500
window.title("Assembler Simulator")
window.geometry("600x500")

title = tk.Label(window, text="Assembler Simulator", font=("Arial", 18))
#display the text on screen 
title.pack(pady=10)
#display description
description=tk.Label(window,text=("Write your assembly code inside input.asm\n""Then click Assemble"),font=("Arial",12))
description.pack()
#display assembly button
assemble_button=tk.Button(window,command=run_assembler,text="Assemble",width=20,height=2)
assemble_button.pack()
#run window
window.mainloop()
