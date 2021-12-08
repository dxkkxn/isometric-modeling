import tkinter as tk
import random
from parser_x import parser

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def distance(x_0: int, y_0: int, x_1: int, y_1:int):
    # print(x_0, y_0, x_1, y_1)
    return ((x_0-x_1)**2+(y_0-y_1)**2)**0.5

def create_rhombus(start_x:int, start_y:int, big_diag:int, height:int, pos_x:int, pos_y:int):
    """
    Create a rhombus based on the start point and the big diagonal [2:1] prop
    """
    small_diag = big_diag/2
    canvas.create_polygon(start_x, start_y, start_x+big_diag/2,
                          start_y+small_diag/2, start_x, start_y+small_diag,
                          start_x-big_diag/2, start_y+small_diag/2,
                          outline="black", width=2, fill="white", tags=("rhombus", (height, pos_x, pos_y), "sup"))


def get_grid_pos(event=None):
    # grid_size = 3
    # big_d = distance(B_x, B_y, D_x, D_y) / grid_size
    # small_d = distance(A_x, A_y, C_x, C_y) / grid_size
    # coords = [None, None]
    # print("entered")
    # a_x = A_x
    # a_y = A_y
    id_curr = canvas.find_withtag("current")
    height, pos_x, pos_y = [int(x) for x in canvas.gettags(id_curr)[1].split(' ')]
    # print(f"here >> height = {height}, pos_x = {pos_x}, pos_y = {pos_y}")
    return [height, pos_x, pos_y]

    # a, b = (A_x+event.x)+A_y+
    # for i in range(grid_size):
    #     a_x = A_x-i*(big_d/2)
    #     a_y = A_y+i*(small_d/2)
    #     for j in range(grid_size):
    #         # a_x, a_y = A_x-i*(big_d/2)+j*(big_d/2), A_y+i*(small_d/2)+j*(small_d/2)
    #         if (a_x-(big_d/2)) < event.x < a_x+(big_d/2) and a_y < event.y < a_y+small_d:
    #             canvas.create_line(a_x, a_y, a_x, a_y+small_d, fill="red")
    #             print("here",j,i)
    #         a_x += big_d/2
    #         a_y += small_d/2

old_color = None
def change_color(event=None):
    global old_color
    id_curr = canvas.find_withtag("current")
    old_color = canvas.itemcget(id_curr, "fill")
    # print(old_color)
    canvas.itemconfigure(id_curr, fill="#2bfafa")


def reset_color(event=None):
    id_curr = canvas.find_withtag("current")
    canvas.itemconfigure(id_curr, fill=old_color)

def erase_cube(event=None):
    id_curr = canvas.find_withtag("current")
    pos = canvas.gettags(id_curr)[1]
    all_cubes_pos.remove([int (x) for x in pos.split(' ')])
    for id_curr in canvas.find_withtag(pos):
        canvas.delete(id_curr)

A_x = None
A_y = None
B_x = None
B_y = None
C_x = None
C_y = None
D_x = None
D_y = None
grid_size = None
def create_plan():
    # canvas.create_polygon(x,y, x+300, y+100, x, y+200, x-3008. The Ca8. The Ca, y+100,x,y,
    #                       outline="red", joinstyle="round")

    # we create a plan with vertex called A,B,C,D
    #               A
    #               .
    #            D / \ B
    #              \ /
    #               C

    global A_x, A_y, B_x, B_y, C_x, C_y, D_x, D_y, grid_size
    grid_size = 7

    global SCREEN_HEIGHT, SCREEN_WIDTH
    SCREEN_HEIGHT = root.winfo_height()
    SCREEN_WIDTH = root.winfo_width()
    print(SCREEN_HEIGHT, SCREEN_WIDTH)
    A_y = SCREEN_HEIGHT/2
    A_x = SCREEN_WIDTH/2
    # 10 pixels de marge
    small_diag = SCREEN_HEIGHT-A_y-10
    BIG_DIAG = small_diag*2
    B_x = A_x+BIG_DIAG/2
    B_y = A_y+small_diag/2
    C_x = A_x
    C_y = A_y+small_diag
    D_x = A_x-BIG_DIAG/2
    D_y = A_y+small_diag/2
    cube_edge = distance(A_x, A_y, C_x, C_y)
    # side_rhombus = dis/3
    small_diag = cube_edge/grid_size
    big_diag = small_diag*2
    # canvas.create_polygon(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y)
    for i in range(grid_size):
        for j in range(grid_size):
            create_rhombus(A_x-i*(big_diag/2)+j*(big_diag/2),
                           A_y+i*(small_diag/2)+j*(small_diag/2), big_diag, -1, j, i)
            print(i,j)

    button.pack_forget()
    canvas.tag_bind("rhombus", sequence="<Enter>", func=change_color)
    canvas.tag_bind("rhombus", sequence="<Leave>", func=reset_color)
    canvas.tag_bind("rhombus", sequence="<ButtonPress-1>", func=display_cube)
    canvas.tag_bind("rhombus", sequence="<ButtonPress-3>", func=erase_cube)
    print("created")

    return


def position_form_relative_points(height, x_pos, y_pos):
    cube_edge = distance(A_x, A_y, C_x, C_y)
    small_diag = cube_edge/grid_size
    big_diag = small_diag*2
    res_x = A_x
    res_y = A_y
    for _ in range(x_pos):
        res_x += big_diag/2
        res_y += small_diag/2
    for _ in range(y_pos):
        res_x -= big_diag/2
        res_y += small_diag/2
    for _ in range(height):
        res_y -= small_diag
    return res_x, res_y


def shade_color(color: list, factor:int):
    shaded_color  = [(1-factor)*x for x in color]
    shaded_color  = [int(x) for x in shaded_color]
    return shaded_color 

def rgb_list_to_hex_rgb(color: list):
    print(color)
    hex_rgb_list = []
    for x in color:
        hex_x = hex(x)[2:]
        if len(hex_x) == 1: 
            hex_x = "0"+hex_x
        hex_rgb_list.append(hex_x)
        
    return "#"+ "".join(hex_rgb_list)

def hex_rgb_to_rgb_list(color: str):
    print(color)
    rgb_list = []
    for x in range(1, len(color), 2):
        hex_x = color[x:x+2]
        print("here", hex_x)
        rgb_list.append(int(hex_x, 16))
    return rgb_list

all_cubes_pos = []
colors_dict = parser()
colors = list(colors_dict.keys())
def display_cube(event=None):
    new_pos = get_grid_pos(event)
    orientation = canvas.gettags(canvas.find_withtag("current"))[2]
    if orientation == "right":
        new_pos[1] += 1
    elif orientation == "sup" :
        new_pos[0] += 1
    elif orientation == "left":
        new_pos[2] += 1
    all_cubes_pos.append(new_pos)
    # print(all_cubes_pos)
    all_cubes_pos.sort()
    print(all_cubes_pos)
    # print("here",all_cubes_pos)
    got_color  = False
    for cube_pos in all_cubes_pos:
        A = set((canvas.find_withtag(" ".join([str(x) for x in cube_pos]))))
        B = set((canvas.find_withtag("sup")))
        C = set((canvas.find_withtag("left")))
        D = set((canvas.find_withtag("right")))
        try:
            old_color = canvas.itemcget(list(A.intersection(B))[0], "fill")
            s2 = canvas.itemcget(list(A.intersection(C))[0], "fill")
            s1 = canvas.itemcget(list(A.intersection(D))[0], "fill")
            print("here", old_color, s1, s2)
            print("here", A.intersection(B), A.intersection(C), A.intersection(D))
            got_color = True
        except: 
            got_color = False

        for id_curr in canvas.find_withtag(" ".join([str(x) for x in cube_pos])):
            canvas.delete(id_curr)

        if got_color is False:
            old_color = colors_dict[random.choice(colors)]
            s1 = shade_color(old_color, 0.5)
            s2 = shade_color(s1, 0.5)
            s1 = rgb_list_to_hex_rgb(s1)
            s2 = rgb_list_to_hex_rgb(s2)
            old_color = rgb_list_to_hex_rgb(old_color)
            print(old_color, s1, s2)
        got_color  = False

        
        # print("orientation", canvas.gettags(id_curr))
        # print( canvas.find_withtag(cube_pos))
        # id_curr = canvas.find_withtag(cube_pos)[0]
        # print("id_curr", id_curr)
        cube_edge = distance(A_x, A_y, C_x, C_y)
        small_diag = cube_edge/grid_size
        big_diag = small_diag*2
        a_x, a_y = position_form_relative_points((cube_pos[0]), (cube_pos[1]),
                                                 (cube_pos[2]))
        b_x, b_y= a_x+big_diag/2, a_y+small_diag/2
        c_x, c_y, d_x, d_y = a_x, a_y+small_diag, a_x-big_diag/2, a_y+small_diag/2
        # print("here", a_x, a_y, position_form_relative_points(int(cube_pos[0]),
        #                                               int(cube_pos[1]),
        #                                               int(cube_pos[2])))
        cube_edge = small_diag
        # print(f"a = {event.x+2*event.y/(4*cube_edge)},b = {2*event.y-event.x/(4*cube_edge)}")
        a_y -= cube_edge
        b_y -= cube_edge
        c_y -= cube_edge
        d_y -= cube_edge

        # print("cube_pos=", cube_pos)
        # cube_pos_str = str(int(cube_pos_str[0])+1)+cube_pos_str[1:]
        # cube_pos[0] = str(int(cube_pos[0]) + 1)
        cube_pos = " ".join([str(x) for x in cube_pos])
        # print("cube_pos=", cube_pos)
        canvas.create_polygon(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y,
                              outline="black", width=2, fill=old_color,
                              tags=("rhombus", cube_pos, "sup"))

        canvas.create_polygon(d_x, d_y, c_x, c_y, c_x, c_y+cube_edge, d_x, d_y+cube_edge,
                              outline="black", width=2, fill=s2,
                              tags=("rhombus", cube_pos, "left"))

        canvas.create_polygon(c_x, c_y, b_x, b_y, b_x, b_y+cube_edge, c_x,
                              c_y+cube_edge, outline="black", width=2,
                              fill=s1,
                              tags=("rhombus", cube_pos, "right",))
    # print(canvas.itemconfigure(id_curr))
    # print(canvas.coords(id_curr))
    # l = 50;
    # a_x = event.x
    # a_y = event.y
    # print(big_diag, small_diag)
    # assert(small_diag == distance(a_x, a_y, c_x, c_y))

    # b_x = a_x+big_diag/2
    # b_y = a_y+small_diag/2
    # c_x = a_x
    # c_y = a_y+small_diag
    # d_x = a_x-big_diag/2
    # d_y = a_y+small_diag/2
    return


def get_window_size(event=None):
    #print("OOOOOOOOk")
    #print(event)
    SCREEN_HEIGTH = root.winfo_height()
    SCREEN_WIDTH = root.winfo_width()
#    print(canvas.cget("height"))
    """
    if CANVAS_WIDTH - 2 != event.width :
        CANVAS_WIDTH = event_width-2
        canvas.configure(width=event.width-2, height=event.height)
        canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANV0AS_HEIGHT,
    if CANVAS_HEIGHT- 2 != event.height:
        CANVAS_HEIGHT = event_width-2
        canvas.configure(width=event.width, height=event.height)
    """
    return

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("plan")
    # top_level = tk.Toplevel()
    button = tk.Button(root, text="display plan", command=create_plan, takefocus=True)
    button.pack(side="top")
    # SCREEN_HEIGHT = 1080
    # SCREEN_WIDTH = 1920
    # geometry_str = str(SCREEN_WIDTH)+str(SCREEN_HEIGHT)
    # root.geometry()
    # print(root.winfo_screenheight())

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(side="top", expand=True, fill="both")
    # print("-----------")
    # print(canvas.winfo_height(), canvas.winfo_width())
    # print(SCREEN_WIDTH, SCREEN_HEIGHT)
    #for i in range(3):
    #    create_plan(500-600+i*300, 200+200+i*100)
    #root.bind(sequence="<Configure>", func=resize)
    #root.attributes('-fullscreen', True)
    root.attributes("-zoomed", True)
    #print("here->",root.winfo_height())
    #root.resizable(False, False)
    root.mainloop()
