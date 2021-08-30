import tkinter as tk
from tkinter import *
import random
import os


win = tk.Tk()
mycolor2 ='#103447'
mycolor3='#d61a1a'
win.configure(bg=mycolor2, borderwidth=5)
win.geometry("650x550")
win.title("Number Guessing Game")

result = StringVar()
chances = IntVar()
chances1 = IntVar()
choice = IntVar()
no = random.randint(1, 20)
result.set("Guess a number between 1 to 20 ")
chances.set(5)
chances1.set(chances.get())


def fun():
    chances1.set(chances.get())
    if chances.get() > 0:

        if choice.get() > 20 or choice.get() < 0:     #our entered choice
            result.set("You just lost 1 Chance")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())

        elif no == choice.get():
            result.set("Congratulation YOU WON!!!")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())

        elif no > choice.get():
            result.set("Your guess was too low: Guess a number higher ")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())
        elif no < choice.get():
            result.set(
                "Your guess was too High: Guess a number Lower ")
            chances.set(chances.get() - 1)
            chances1.set(chances.get())
    else:
        result.set(
            "Game Over You Lost")


def restart():
    no = random.randint(1, 20)
    result.set("Guess a number between 1 to 20 ")
    chances.set(5)
    chances1.set(chances.get())


ent1 = Entry(win, textvariable=choice, width=3, #our entered choice
             font=('Ubuntu', 50), relief=GROOVE)
ent1.place(relx=0.5, rely=0.3, anchor=CENTER)

ent2 = Entry(win, textvariable=result, width=50, #displays result
             font=('Courier', 15), relief=GROOVE)
ent2.place(relx=0.5, rely=0.7, anchor=CENTER)

ent3 = Entry(win, text=chances1, width=2,  #chances left
             font=('Ubuntu', 24), relief=GROOVE)
ent3.place(relx=0.61, rely=0.85, anchor=CENTER)

msg = Label(win, text='Guess a number between 1 to 20 ', #heading
            font=("Courier", 25), relief=GROOVE)
msg.place(relx=0.5, rely=0.09, anchor=CENTER)

msg2 = Label(win, text='Remaining Chances',   #normal text
             font=("Courier", 25), relief=GROOVE)
msg2.place(relx=0.3, rely=0.85, anchor=CENTER)

try_no = Button(win, width=8, text='TRY', font=(   #try button
    'Courier', 25), command=fun, relief=GROOVE)
try_no.place(relx=0.5, rely=0.5, anchor=CENTER)

stop = tk.Button(win, text='stop', width=40, command=win.destroy,  #stop button
                 bg=mycolor3,pady=10, activebackground="red", relief=GROOVE)
stop.place(relx=0.25, rely=1, anchor=S)
reset = tk.Button(win, text='Restart', width=40, command=restart,pady=10,borderwidth=3, #restart button
                  bg="steel blue", activebackground="red", relief=GROOVE)
reset.place(relx=.75, rely=1, anchor=S)


win.mainloop()