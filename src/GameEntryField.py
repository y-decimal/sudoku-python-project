import customtkinter as ctk
from abc import ABC, abstractmethod

class GameEntryField(ABC):

            def __init__(self, master, row, column, window_height):      

                self.entry_variable = ctk.StringVar()       

                self.entry = ctk.CTkEntry(master, 
                                 width= window_height, 
                                 height = window_height, 
                                 font = ("Arial", 20), 
                                 textvariable=self.entry_variable, 
                                 justify="center"
                                )

                self.entry.grid(row=row, column=column, sticky="nsew")
                
                self.entry_variable.trace_add("write", self.callback)

            @abstractmethod
            def callback(self , *args):
                pass

            # def callback(self, *args):

            #     if len(self.entry_variable.get()) > 1:
            #         self.entry_variable.set(self.entry_variable.get()[:1])

            #     if not self.entry_variable.get().isdigit():
            #         self.entry_variable.set("")

               