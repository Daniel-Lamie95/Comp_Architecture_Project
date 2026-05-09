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


window= tk.Tk()

window.title("Assembler Simulator")
window.geometry("600x500")

title = tk.Label(window, text="Assembler Simulator", font=("Arial", 18))

title.pack(pady=10)

description=tk.Label(window,text=("Write your assembly code inside input.asm\n""Then click Assemble"),font=("Arial",12))
description.pack()

assemble_button=tk.Button(window,command=run_assembler,text="Assemble",width=20,height=2)
assemble_button.pack()

window.mainloop()
