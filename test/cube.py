import tkinter as tk
import display_plan as dp
import random
from parser_x import parser

class Cube(object):
    """
    definition and manipulation of a cube class in a isometric plan
    """
    nmemb = 0
    def __init__(self, position: list, options):
        self.__position = position
        self.__options =  options
        Cube.nmemb += 1

    @staticmethod
    def number_of_cubes():
        return nmemb;

if __name__ == "__main__" :
   # root = tk.Tk()
   # root.title("plan")

   # canvas = tk.Canvas(root, bg="white")
   # canvas.pack(side="top", expand=True, fill="both")
   # canvas.bind(sequence="<ButtonPress-1>", func=display_cube)
   # root.attributes("-zoomed", True)
   # root.mainloop()

   a  = Cube("a", "b ")
   b = Cube("a", "b")
   print(Cube.nmemb)
   l = [255,255,255]
   col = Color(*l)
   print(col)


colors = list(parser().keys())
def display_cube(event=None):
    print("ok")
    l = 50;
    a_x = event.x
    a_y = event.y
    big_diag = 100
    small_diag = 50
    b_x = a_x+big_diag/2
    b_y = a_y+small_diag/2
    c_x = a_x
    c_y = a_y+small_diag
    d_x = a_x-big_diag/2
    d_y = a_y+small_diag/2
    dis = dp.distance(a_x, a_y, b_x, b_y)

    color_choice = random.choice(colors)
    rgb_list = (parser()[color_choice])
    s1 = shade_color(rgb_list, 0.5)
    s2 = shade_color(s1, 0.5)
    s1 = rgb_to_hex_rgb(s1)
    s2 = rgb_to_hex_rgb(s2)

    canvas.create_polygon(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y,
                          fill=color_choice, outline="black", width=2, tags="rhombus")

    canvas.create_polygon(d_x, d_y, c_x, c_y, c_x, c_y+dis, d_x, d_y+dis,
                          fill=s2, outline="black", width=2, tags="rhombus")

    canvas.create_polygon(c_x, c_y, b_x, b_y, b_x, b_y+dis, c_x, c_y+dis,
                          fill=s1, width=2,outline="black", tags="rhombus")

    return
