from tkinter import *
import turtle

turtle.goto(0, 0)

window = Tk()

def forward(event):
    turtle.forward(10)
    
def left(event):
    turtle.left(10)

def backward(event):
    turtle.backward(10)
    
def right(event):
    turtle.right(10)
    
def clear(event):
    turtle.clear()
    
window.bind("<Up>", forward)
window.bind("<Left>", left)
window.bind("<Down>", backward)
window.bind("<Right>", right)
window.bind("<c>", clear)
window.mainloop()