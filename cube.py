from color import Color
from parserx import parser
import random
from rhombus import Rhombus

def create_cube(event=None):
    id_curr = canvas.find_withtag("current")[0]

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
    small_diag = None
    big_diag = None
    A_x = None 
    A_y = None
    canvas = None
    grid_rhombus = None
    grid_size = None

    @staticmethod
    def set_global_vars(small_diag, big_diag, A_x, A_y, gr, grid_size):
        Cube.small_diag = small_diag
        Cube.big_diag = big_diag
        Cube.A_x = A_x
        Cube.A_y = A_y
        Cube.grid_rhombus = gr
        Cube.grid_size = grid_size


    @staticmethod
    def distance(x_0 :int, y_0: int, x_1: int, y_1:int):
        return ((x_0-x_1)**2+(y_0-y_1)**2)**0.5

    @staticmethod
    def calculate_diags():
        id_ = Cube.canvas.find_withtag("cont")
        x0, y0, x1, y1, x2, y2, x3, y3= Cube.canvas.coords(id_)
        Cube.small_diag = Cube.distance(x0, y0, x2, y2)/Cube.grid_size
        Cube.big_diag = Cube.small_diag*2
        Cube.A_x = x0
        Cube.A_y = y0


    @staticmethod
    def set_canvas(canvas):
        Cube.canvas = canvas


    @staticmethod
    def position_from_relative_points(height, x_pos, y_pos):
        # cube_edge = distance(A_x, A_y, C_x, C_y)
        Cube.calculate_diags()
        small_diag = Cube.small_diag
        big_diag = Cube.big_diag 
        res_x = Cube.A_x
        res_y = Cube.A_y
        for _ in range(x_pos):
            res_x += big_diag/2
            res_y += small_diag/2
        for _ in range(y_pos):
            res_x -= big_diag/2
            res_y += small_diag/2
        for _ in range(height+1):
            res_y -= small_diag
        return res_x, res_y

    def position_from_clicked_rhombus(self):
        orientation = self.__rhombus.orientation
        small_diag = Cube.small_diag
        big_diag = Cube.big_diag
        x, y =  Cube.canvas.coords(self.__rhombus.id)[0],Cube.canvas.coords(self.__rhombus.id)[1]
        if orientation == "sup":
            a_x, a_y = x, y-small_diag
        elif orientation == "right":
            a_x, a_y =  Cube.canvas.coords(self.__rhombus.id)[2],Cube.canvas.coords(self.__rhombus.id)[3]
        elif orientation == "left":
            a_x, a_y = x, y
        return a_x, a_y


    def __init__(self, position: list, color: Color, rhombus):
        self.__position = position
        self.__color = color
        self.__rhombus= rhombus
        if rhombus:
            self.display_cube()
        else:
            Cube.display_cube_from_rel_points(position, self.__color)
        if self.nmemb == 0:
            Cube.bind()
        Cube.nmemb += 1


    @staticmethod
    def bind():
        Cube.canvas.tag_bind("cube", sequence="<ButtonPress-3>",
                        func=Cube.erase_cube)

    @staticmethod

    def erase_cube(event=None):
        id_curr = Cube.canvas.find_withtag("current")
        pos = Cube.canvas.gettags(id_curr)[0]
        ids = Cube.all_cubes.pop(tuple((int(x)) for x in pos.split(' ')))
        for id_curr in Cube.canvas.find_withtag(pos):
            Cube.canvas.delete(id_curr)


    @staticmethod
    def number_of_cubes():
        return nmemb;


    @staticmethod
    def clean_all_cubes():
        Cube.all_cubes = {}


    @staticmethod
    def painter_algorithm():
        all_positions = list(Cube.all_cubes.keys())
        all_positions.sort()
        for i in range(1,len(all_positions)):
            str_lower = " ".join([str(x) for x in all_positions[i-1]])
            str_upper = " ".join([str(x) for x in all_positions[i]])
            Cube.canvas.tag_raise(str_upper, str_lower)


    @staticmethod
    def rotate_90_deg_left():
        new_pos = {}
        for pos, ids in Cube.all_cubes.items():
            color = ids[0].color
            for id_ in ids:
                Cube.canvas.delete(id_)
            z, x, y = pos
            new_pos[(z,(Cube.grid_size-1)-y, x)] = color
            Cube.canvas.delete("cube")
        Cube.all_cubes = {}
        for pos, color in new_pos.items():
            Cube.display_cube_from_rel_points(pos, (color))


    @staticmethod
    def rotate_90_deg_right():
        new_pos = {}
        for pos, ids in Cube.all_cubes.items():
            color = ids[0].color
            for id_ in ids:
                Cube.canvas.delete(id_)
            z, x, y = pos
            new_pos[(z, y, Cube.grid_size-1-x)] = color
            Cube.canvas.delete("cube")
        Cube.all_cubes = {}
        for pos, color in new_pos.items():
            Cube.display_cube_from_rel_points(pos, (color))


    @staticmethod
    def display_cube_from_rel_points(rel_pos, color):
        a_x, a_y = Cube.position_from_relative_points(*rel_pos)
        big_diag = Cube.big_diag
        small_diag = Cube.small_diag
        dis = small_diag
        b_x = a_x+big_diag/2
        b_y = a_y+small_diag/2
        c_x = a_x
        c_y = a_y+small_diag
        d_x = a_x-big_diag/2
        d_y = a_y+small_diag/2

        shaded_1 = color.shade_color(0.25)
        shaded_2 = shaded_1.shade_color(0.25)
        str_pos = " ".join([str(x) for x in rel_pos])

        id_1 = Rhombus(color, "sup", a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y,
                        tags=(str_pos, "cube"))
        id_2 = Rhombus(shaded_2, "left", d_x, d_y, c_x, c_y, c_x, c_y+dis, d_x,
                       d_y+dis, tags=(str_pos, "cube"))

        id_3 = Rhombus(shaded_1, "right", c_x, c_y, b_x, b_y, b_x, b_y+dis,
                       c_x, c_y+dis, tags=(str_pos, "cube"))
        Cube.all_cubes[tuple(rel_pos)] = [id_1, id_2, id_3]
        Cube.painter_algorithm()


    def display_cube(self):
        self.calculate_diags()
        a_x, a_y = self.position_from_clicked_rhombus()
        big_diag = Cube.big_diag
        small_diag = Cube.small_diag
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
        id_2 = Rhombus(shaded_2, "left", d_x, d_y, c_x, c_y, c_x, c_y+dis, d_x,
                       d_y+dis, tags=(str_pos, "cube"))

        id_3 = Rhombus(shaded_1, "right", c_x, c_y, b_x, b_y, b_x, b_y+dis,
                       c_x, c_y+dis, tags=(str_pos, "cube"))
        self.all_cubes[tuple(self.__position)] = [id_1, id_2, id_3]
        self.painter_algorithm()
