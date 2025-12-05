from tkinter import *
#need to install on all machines
from tkmacosx import Button

# Create the main window
root = Tk()
root.title("thing")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="Red", background='red')
yellow_button = Button(root, text="yellow", background='yellow')
green_button = Button(root, text="green", background='green')

#Add a label
label = Label(root, text="this was changed!")

# Place widgets in window (with pack function!)
label.grid(rows = 1, column = 0)
red_button.pack(row = 2, column = 0)
yellow_button.pack(row = 3, column = 0)
green_button.pack(row = 4, column = 0)

# Start the GUI event loop
root.mainloop()