import tkinter as tk
from color import Color

def create_rhombus(color, *args, **kwargs):
    # start_x = event.x
    # start_y = event.y
    start_x, start_y = args
    points = [start_x, start_y, start_x+BIG_DIAG/2,
              start_y+SMALL_DIAG/2, start_x, start_y+SMALL_DIAG,
              start_x-BIG_DIAG/2, start_y+SMALL_DIAG/2]
    print(args, kwargs)
    print(points)
    rhombus = Rhombus(color, *points, **kwargs)

class Rhombus():
    BIG_DIAG = None
    SMALL_DIAG = None
    def change_color(self, event=None):
        id_curr = canvas.find_withtag("current")
        print(canvas.gettags(id_curr))
        canvas.itemconfigure(id_curr, fill="#2bfafa")

    def reset_color(self, event=None):
        id_curr = canvas.find_withtag("current")
        print(id_curr, self, type(self))
        canvas.itemconfigure(id_curr, fill=self.__color.to_hex_rgb())
    def __init__(self, color, *args, **kwargs):
        """
        Create a rhombus based on the start point and the big diagonal [2:1] prop
        """
        BIG_DIAG = self.BIG_DIAG
        SMALL_DIAG = self.SMALL_DIAG
        self.__canvas = canvas
        self.__color = color
        self.__id = canvas.create_polygon(*args, **kwargs, outline="black",
                                           fill=self.__color.to_hex_rgb(),
                                          width=2)
        if "rhombus" not in canvas.gettags(self.__id):
            canvas.addtag_withtag( "rhombus", self.__id)
        canvas.tag_bind(self.__id, sequence="<Enter>", func=lambda event :self.change_color(event))
        canvas.tag_bind(self.__id, sequence="<Leave>", func=lambda event :self.reset_color(event))


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



def create_plan(size):
    p = Plan(size)

def distance(x_0: int, y_0: int, x_1: int, y_1:int):
    return ((x_0-x_1)**2+(y_0-y_1)**2)**0.5

SCREEN_WIDTH = None
SCREEN_HEIGHT = None
A_x = None
A_y = None
B_x = None
B_y = None
C_x = None
C_y = None
D_x = None
D_y = None
PLAN_SIZE = None
BIG_DIAG = None
SMALL_DIAG = None
class Plan():
    def __init__(self, size, *args, **kwargs):
        # we create a plan with vertex called A,B,C,D
        #               A
        #               .
        #            D / \ B
        #              \ /
        #               C

        global A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y, PLAN_SIZE, SMALL_DIAG, BIG_DIAG
        PLAN_SIZE = 7

        global SCREEN_HEIGHT, SCREEN_WIDTH
        SCREEN_HEIGHT = root.winfo_height()
        SCREEN_WIDTH = root.winfo_width()
        print(SCREEN_HEIGHT, SCREEN_WIDTH)
        A_y = SCREEN_HEIGHT/2
        A_x = SCREEN_WIDTH/2
        # 10 pixels de marge
        SMALL_DIAG = SCREEN_HEIGHT-A_y-10
        BIG_DIAG = SMALL_DIAG*2
        B_x = A_x+BIG_DIAG/2
        B_y = A_y+SMALL_DIAG/2
        C_x = A_x
        C_y = A_y+SMALL_DIAG
        D_x = A_x-BIG_DIAG/2
        D_y = A_y+SMALL_DIAG/2
        SMALL_DIAG = distance(A_x, A_y, C_x, C_y)/PLAN_SIZE
        BIG_DIAG = SMALL_DIAG*2
        for i in range(PLAN_SIZE):
            for j in range(PLAN_SIZE):
                pos_str = " ".join(str(x) for x in [-1, j, i])
                print(pos_str)
                create_rhombus(Color.from_hex_str("#ffffff"),
                               A_x-i*(BIG_DIAG/2)+j*(BIG_DIAG/2),
                               A_y+i*(SMALL_DIAG/2)+j*(SMALL_DIAG/2),
                               tags=(pos_str,))
                print(i,j)


if __name__ == "__main__" :
    root = tk.Tk()
    root.title("plan")
    canvas = tk.Canvas(root, bg="white")
    canvas.bind(sequence="<ButtonPress-1>", func= create_rhombus)
    canvas.pack(side="top", expand=True, fill="both")
    button = tk.Button(root, text="display plan", command=lambda: create_plan(7), takefocus=True)
    button.pack(side="top")
    root.attributes("-zoomed", True)
    root.mainloop()
