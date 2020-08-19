import tkinter as tk
from tkinter import *
import tkinter.messagebox

window = tk.Tk()
window.title("TTT")
window.resizable(0, 0)
window.geometry("250x300")
c = tk.Canvas(window, height=250, width=250, bg="white")
turn = 0
flag = 0

def board():
    l1 = c.create_line(85, 5, 85, 245)
    l2 = c.create_line(170, 5, 170, 245)
    l3 = c.create_line(5, 85, 245, 85)
    l4 = c.create_line(5, 170, 245, 170)

    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    b1 = tk.Button(window, text="", width=11, height=5, bg="white", bd=0, command=lambda: flip(b1))
    b2 = tk.Button(window, text="", width=11, height=5, bg="white", bd=0, command=lambda: flip(b2))
    b3 = tk.Button(window, text="", width=11, height=5, bg="white", bd=0, command=lambda: flip(b3))
    b4 = tk.Button(window, text="", width=11, height=5, bg="white", bd=0, command=lambda: flip(b4))
    b5 = tk.Button(window, text="", width=11, height=5, bg="white", bd=0, command=lambda: flip(b5))
    b6 = tk.Button(window, text="", width=11, height=5, bg="white", bd=0, command=lambda: flip(b6))
    b7 = tk.Button(window, text="", width=11, height=5, bg="white", bd=0, command=lambda: flip(b7))
    b8 = tk.Button(window, text="", width=11, height=5, bg="white", bd=0, command=lambda: flip(b8))
    b9 = tk.Button(window, text="", width=11, height=5, bg="white", bd=0, command=lambda: flip(b9))

    c1 = c.create_window(43, 43, window=b1)
    c2 = c.create_window(127, 43, window=b2)
    c3 = c.create_window(212, 43, window=b3)
    c4 = c.create_window(43, 127, window=b4)
    c5 = c.create_window(127, 127, window=b5)
    c6 = c.create_window(212, 127, window=b6)
    c7 = c.create_window(43, 212, window=b7)
    c8 = c.create_window(127, 212, window=b8)
    c9 = c.create_window(212, 212, window=b9)

    c.pack()

    b = tk.Button(window, text="Reset", command=resetBoard)
    b.pack()
    b.place(x=105, y=265)

    global x, o
    x = tk.Label(text="X")
    x.pack()
    x.place(x=55, y=265)

    o = tk.Label(text="O")
    o.pack()
    o.place(x=180, y=265)

    window.mainloop()

def checkWin():
    if (b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X") or \
        (b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X") or \
        (b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X") or \
        (b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X") or \
        (b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X") or \
        (b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X") or \
        (b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X") or \
        (b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"):
            tkinter.messagebox.showinfo("TTT", "Player 1 wins!")
            disableButtons()
            resetBoard()

    elif (b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O") or \
        (b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O") or \
        (b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O") or \
        (b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O") or \
        (b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O") or \
        (b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O") or \
        (b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O") or \
        (b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O"):
            tkinter.messagebox.showinfo("TTT", "Player 2 wins!")
            disableButtons()
            resetBoard()

    else:
        checkTie()


def checkTie():
    global flag
    if flag == 9:
        tkinter.messagebox.showinfo("TTT", "It's a tie")
        resetBoard()

def flip(button):
    global turn, flag
    flag += 1
    if turn == 0:
        button["text"] = "X"
        #x["font"] = "normal"
    else:
        button["text"] = "O"
    button["state"] = DISABLED
    turn = (turn + 1) % 2
    checkWin()


def resetBoard():
    global c
    c.destroy()
    c = tk.Canvas(window, height=250, width=250, bg="white")
    global turn, flag
    turn = flag = 0
    board()


def disableButtons():
    b1["state"] = DISABLED
    b2["state"] = DISABLED
    b3["state"] = DISABLED
    b4["state"] = DISABLED
    b5["state"] = DISABLED
    b6["state"] = DISABLED
    b7["state"] = DISABLED
    b8["state"] = DISABLED
    b9["state"] = DISABLED

board()