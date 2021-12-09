from color import Color
from parser_x import parser
import random
import tkinter as tk
from rhombus import Rhombus

class Cube(object):
    """
    definition and manipulation of a cube class in a isometric plan
    """
    nmemb = 0
    def __init__(self, position: list, color: Color, options):
        self.__position = position
        self.__color = color
        self.__options = options
        self.__rhombus= {"sup":Rhombus(), }
        Cube.nmemb += 1

    @staticmethod
    def number_of_cubes():
        return nmemb;

    @classmethod
    def create_cube(cls, event, canvas):
        dict_col = parser()
        col_names = list(dict_col.keys())
        choice = random.choice(col_names)
        choice = dict_col[choice]
        res =  cls(position=[0,event.x, event.y], color=Color(*choice),
                   options="xd" )
        res.display_cube(canvas)
        return res


    def display_cube(self, canvas):
        l = 50;
        a_x = self.__position[1]
        a_y = self.__position[2]
        big_diag = 100
        small_diag = 50
        dis = small_diag
        b_x = a_x+big_diag/2
        b_y = a_y+small_diag/2
        c_x = a_x
        c_y = a_y+small_diag
        d_x = a_x-big_diag/2
        d_y = a_y+small_diag/2

        color = self.__color.to_hex_rgb()
        shaded_1 = self.__color.shade_color(0.25)
        shaded_2 = shaded_1.shade_color(0.25).to_hex_rgb()
        shaded_1 = shaded_1.to_hex_rgb()


        canvas.create_polygon(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y,
                            fill=color, outline="black", width=2, tags="rhombus")

        canvas.create_polygon(d_x, d_y, c_x, c_y, c_x, c_y+dis, d_x, d_y+dis,
                            fill=shaded_1, outline="black", width=2, tags="rhombus")

        canvas.create_polygon(c_x, c_y, b_x, b_y, b_x, b_y+dis, c_x, c_y+dis,
                            fill=shaded_2, width=2,outline="black", tags="rhombus")


