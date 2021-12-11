from color import Color
from parser_x import parser
import random
import tkinter as tk
from rhombus import Rhombus

def create_cube(event=None):
    id_curr = canvas.find_withtag("current")[0]

    print(">>>>>>>>", canvas.gettags(id_curr))
    relative_pos = canvas.gettags(id_curr)[0]
    relative_pos = [int(x) for x in relative_pos.split(' ')]
    color = Color.random_col()
    rhombus = Rhombus.all_rhombus[id_curr]
    orientation = (rhombus.all_rhombus[id_curr].orientation)
    if orientation == "sup":
        relative_pos[0] += 1
    elif orientation == "right":
        relative_pos[1] += 1
    elif orientation == "left":
        relative_pos[2] += 1

    cube = Cube(relative_pos, color, "xd")


class Cube(object):
    """
    definition and manipulation of a cube class in a isometric plan
    """
    all_cubes = {}
    nmemb = 0

    @staticmethod
    def position_from_relative_points(height, x_pos, y_pos):
        # cube_edge = distance(A_x, A_y, C_x, C_y)
        small_diag = SMALL_DIAG
        big_diag = small_diag*2
        res_x = A_x
        res_y = A_y
        for _ in range(x_pos):
            res_x += big_diag/2
            res_y += small_diag/2
        for _ in range(y_pos):
            res_x -= big_diag/2
            res_y += small_diag/2
        for _ in range(height+1):
            res_y -= small_diag
        return res_x, res_y


    def __init__(self, position: list, color: Color, options):
        self.__position = position
        self.__color = color
        self.__options = options
        self.display_cube()
        if self.nmemb == 0:
            Cube.bind()
        Cube.nmemb += 1

    @staticmethod
    def bind():
        canvas.tag_bind("cube", sequence="<ButtonPress-3>",
                        func=Cube.erase_cube)
    @staticmethod
    def erase_cube(event=None):
        id_curr = canvas.find_withtag("current")
        pos = canvas.gettags(id_curr)[0]
        ids = Cube.all_cubes.pop(tuple((int(x)) for x in pos.split(' ')))
        for id_curr in canvas.find_withtag(pos):
            canvas.delete(id_curr)

    @staticmethod
    def number_of_cubes():
        return nmemb;

    def painter_algorithm(self):
        all_positions = list(self.all_cubes.keys())
        all_positions.sort()
        print(all_positions)
        for i in range(1,len(all_positions)):
            str_lower = " ".join([str(x) for x in all_positions[i-1]])
            str_upper = " ".join([str(x) for x in all_positions[i]])
            canvas.tag_raise(str_upper, str_lower)



    def display_cube(self):
        a_x, a_y = self.position_from_relative_points(*self.__position)
        big_diag = BIG_DIAG
        small_diag = SMALL_DIAG
        dis = small_diag
        b_x = a_x+big_diag/2
        b_y = a_y+small_diag/2
        c_x = a_x
        c_y = a_y+small_diag
        d_x = a_x-big_diag/2
        d_y = a_y+small_diag/2

        color = self.__color
        shaded_1 = self.__color.shade_color(0.25)
        shaded_2 = shaded_1.shade_color(0.25)
        str_pos = " ".join([str(x) for x in self.__position])
        id_1 = Rhombus(color, "sup", a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y,
                        tags=(str_pos, "cube"))
        id_2 = Rhombus(shaded_1, "left", d_x, d_y, c_x, c_y, c_x, c_y+dis, d_x, d_y+dis,
                        tags=(str_pos, "cube"))

        id_3 = Rhombus(shaded_2, "right", c_x, c_y, b_x, b_y, b_x, b_y+dis, c_x, c_y+dis,
                        tags=(str_pos, "cube"))
        self.all_cubes[tuple(self.__position)] = [id_1, id_2, id_3]
        self.painter_algorithm()
