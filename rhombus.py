import tkinter as tk
from color import Color

def create_rhombus(color, orientation, *args, **kwargs):
    start_x, start_y = args
    points = [start_x, start_y, start_x+BIG_DIAG/2,
              start_y+SMALL_DIAG/2, start_x, start_y+SMALL_DIAG,
              start_x-BIG_DIAG/2, start_y+SMALL_DIAG/2]
    rhombus = Rhombus(color, orientation, *points, **kwargs)


class Rhombus():
    BIG_DIAG = None
    SMALL_DIAG = None
    all_rhombus = {}
    def change_color(self, event=None):
        canvas.itemconfigure(self.__id, fill="#2bfafa")

    def reset_color(self, event=None):
        canvas.itemconfigure(self.__id, fill=self.__color.to_hex_rgb())

    @property
    def orientation(self):
        return self.__orientation

    def __init__(self, color, orientation, *args, **kwargs):
        """
        Create a rhombus based on the start point and the big diagonal [2:1] prop
        """
        self.__canvas = canvas
        self.__color = color
        self.__orientation = orientation
        print(self.__orientation)
        self.__id = canvas.create_polygon(*args, **kwargs, outline="black",
                                           fill=self.__color.to_hex_rgb(),
                                           width=2)
        self.all_rhombus[self.__id] = self
        if "rhombus" not in canvas.gettags(self.__id):
            canvas.addtag_withtag( "rhombus", self.__id)
        canvas.tag_bind(self.__id, sequence="<Enter>", func=lambda event :self.change_color(event))
        canvas.tag_bind(self.__id, sequence="<Leave>", func=lambda event :self.reset_color(event))




def create_plan(size):
    p = Plan(size)

def distance(x_0: int, y_0: int, x_1: int, y_1:int):
    return ((x_0-x_1)**2+(y_0-y_1)**2)**0.5


if __name__ == "__main__" :
    root = tk.Tk()
    root.title("plan")
    canvas = tk.Canvas(root, bg="white")
    canvas.bind(sequence="<ButtonPress-1>", func= create_cube)
    canvas.pack(side="top", expand=True, fill="both")
    button = tk.Button(root, text="display plan", command=lambda: create_plan(7), takefocus=True)
    button.pack(side="top")
    root.attributes("-zoomed", True)
    root.mainloop()
