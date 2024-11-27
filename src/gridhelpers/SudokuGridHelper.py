from gridhelpers.GameGridHelper import SquareGameFrame, GameEntryField

class SudokuGameFrame(SquareGameFrame):

    GRIDSIZE = 9

    def __init__(self, master, frame_height):
        self.initialize_game_frame(master, self.GRIDSIZE, frame_height)

    def set_game_field(self, i):
        self.game_field.append(SudokuEntryField(self, i//self.GRIDSIZE, i%self.GRIDSIZE, self.game_entry_dimension))


class SudokuEntryField(GameEntryField):

    def __init__(self, master, row, column, entry_dimensions):
        super().__init__(master, row, column, entry_dimensions)

    def callback(self, *args):

        if len(self.entry_variable.get()) > 1:
            self.entry_variable.set(self.entry_variable.get()[:1])
        if not self.entry_variable.get().isdigit():
            self.entry_variable.set("")
