from color import Color
from rhombus import Rhombus
from cube import Cube


class Plan():
    canvas = None
    size = None
    @staticmethod
    def set_canvas(canvas):
        Plan.canvas= canvas

    def create_rhombus(self, color, orientation, *args, **kwargs):
        SMALL_DIAG = self.small_diag
        BIG_DIAG = self.big_diag
        start_x, start_y = args
        points = [start_x, start_y, start_x+BIG_DIAG/2,
                start_y+SMALL_DIAG/2, start_x, start_y+SMALL_DIAG,
                start_x-BIG_DIAG/2, start_y+SMALL_DIAG/2]
        rhombus = Rhombus(color, orientation, *points, **kwargs)
        return rhombus

    def distance(self, x_0 :int, y_0: int, x_1: int, y_1:int):
        return ((x_0-x_1)**2+(y_0-y_1)**2)**0.5

    def __init__(self, size, *args, **kwargs):
        # creation of a plan with vertex called A,B,C,D
        #               A
        #               .
        #            D / \ B
        #              \ /
        #               C
        Plan.size = size

        self.size = size
        self.all_cubes = {}

        PLAN_SIZE = size
        SCREEN_HEIGHT = Plan.canvas.winfo_height()
        SCREEN_WIDTH = Plan.canvas.winfo_width()
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
        SMALL_DIAG = self.distance(A_x, A_y, C_x, C_y)/PLAN_SIZE
        BIG_DIAG = SMALL_DIAG*2
        self.small_diag = SMALL_DIAG
        self.big_diag = BIG_DIAG
        points = [A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y]

        # the big rhombus where all the others rhombus are displayed
        self.cont_rhombus = Rhombus(Color.from_hex_str("#ff0000"), "sup",
                                    *points, tags=("rhombus", "cont"))
        for i in range(PLAN_SIZE):
            for j in range(PLAN_SIZE):
                pos_str = " ".join(str(x) for x in [-1, j, i])
                idr = self.create_rhombus(Color.from_hex_str("#ffffff"), "sup",
                               A_x-i*(BIG_DIAG/2)+j*(BIG_DIAG/2),
                               A_y+i*(SMALL_DIAG/2)+j*(SMALL_DIAG/2),
                               tags=(pos_str,))
        Cube.set_global_vars(SMALL_DIAG, BIG_DIAG, A_x, A_y, idr.id, PLAN_SIZE)
