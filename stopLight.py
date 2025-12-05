from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("stop light")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root, text="yellow", background='yellow')
green_button = Button(root, text="green", background='green')

#Add a label
label = Label(root, text="this was changed!")

# Place widgets in window (with pack function!)
label.grid(rows = 1, column = 2)
red_button.grid(row = 2, column = 4)
yellow_button.grid(row = 3, column = 6)
green_button.grid(row = 4, column = 8)

# Start the GUI event loop
root.mainloop()