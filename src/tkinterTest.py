import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hello, World!")

# set relative size and aspect ratio
relativesize = 0.5
minimumSize = 0.5
aspectRatio = 5/4

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#set the window size relative to the screen size
window_height = int(screen_height*relativesize)
window_width = int(window_height*aspectRatio)

# find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# set the minimum size of the window
root.minsize(int(window_width*minimumSize), int(window_height*minimumSize))

root.configure(bg="#181819")
root.iconbitmap('./assets/images/sudoku.ico')

message = tk.Label(root, text="Hello, World!", font=("Helvetica", 24), background="#181a1b", foreground="white")


button = ttk.Button(root, text="Click me!", command=lambda: print("Hello, World!"))

messageButBetter = ttk.Label(root, text="Hello, World! But better tho", font=("Helvetica", 24), background="#1a1a33", foreground="white")

coolBox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])

message.pack()
messageButBetter.pack()
coolBox.pack()
button.pack()
root.mainloop()