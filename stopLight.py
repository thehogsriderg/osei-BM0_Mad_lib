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
label.pack()
red_button.pack()
yellow_button.pack()
green_button.pack()

# Start the GUI event loop
root.mainloop()