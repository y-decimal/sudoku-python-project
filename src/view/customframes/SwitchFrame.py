import customtkinter as ctk

class SwitchFrame(ctk.CTkFrame):

    def __init__(self, master, rows, columns, sticky="ew", **kwargs):

        super().__init__(master, **kwargs)

        self.parent = master
        self.rows = rows
        self.columns = columns
    
        self.rowconfigure([i for i in range (0,rows)], weight=1)
        self.columnconfigure([i for i in range (0,columns)], weight=1)

        self.switches = []

        index = 0
        for i in range(0, self.rows):

            for j in range(0, self.columns):

                self.switches.append(ctk.CTkSwitch(self, text=f"Switch {i}-{j}", command=self.switch))
                self.switches[index].grid(row = i, column = j, padx=10, pady=10, sticky=sticky)
                index += 1

    def switch(self):
        print("Default switch function")
            