import customtkinter as ctk

class ButtonFrame(ctk.CTkFrame): 

    def __init__(self, master, rows, columns, **kwargs):

        super().__init__(master, **kwargs)

        self.parent = master
        self.rows = rows
        self.columns = columns
    
        self.rowconfigure([i for i in range (0,rows)], weight=1)
        self.columnconfigure([i for i in range (0,columns)], weight=1)

        self.buttons = []

        self.index = 0
        for i in range(0, self.rows):

            for j in range(0, self.columns):

                # self.buttons.append(GridButton(self, i, j))

                self.buttons.append(ctk.CTkButton(self, text=f"Button {i}-{j}", command=lambda: print("Button not implemented yet")))
                self.buttons[self.index].grid(row = i, column = j, padx=10, pady=10, sticky="ew")
                self.index += 1
                
