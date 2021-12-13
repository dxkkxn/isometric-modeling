from color import Color
from rhombus import Rhombus
from cube import Cube

def create_rhombus(color, orientation, *args, **kwargs):
    start_x, start_y = args
    points = [start_x, start_y, start_x+BIG_DIAG/2,
              start_y+SMALL_DIAG/2, start_x, start_y+SMALL_DIAG,
              start_x-BIG_DIAG/2, start_y+SMALL_DIAG/2]
    rhombus = Rhombus(color, orientation, *points, **kwargs)

def distance(x_0 :int, y_0: int, x_1: int, y_1:int):
    return ((x_0-x_1)**2+(y_0-y_1)**2)**0.5

class Plan():
    root = None
    @staticmethod
    def set_root(root):
        Plan.root = root
    def __init__(self, size, *args, **kwargs):
        # we create a plan with vertex called A,B,C,D
        #               A
        #               .
        #            D / \ B
        #              \ /
        #               C

        global A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y, PLAN_SIZE, SMALL_DIAG, BIG_DIAG
        PLAN_SIZE = size

        global SCREEN_HEIGHT, SCREEN_WIDTH
        SCREEN_HEIGHT = Plan.root.winfo_height()
        SCREEN_WIDTH = Plan.root.winfo_width()
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
                create_rhombus(Color.from_hex_str("#ffffff"), "sup",
                               A_x-i*(BIG_DIAG/2)+j*(BIG_DIAG/2),
                               A_y+i*(SMALL_DIAG/2)+j*(SMALL_DIAG/2),
                               tags=(pos_str,))
        Cube.set_global_vars(SMALL_DIAG, BIG_DIAG, A_x, A_y)
