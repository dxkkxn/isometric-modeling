import tkinter as tk


SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def distance(x_0: int, y_0: int, x_1: int, y_1:int):
    print(x_0, y_0, x_1, y_1)
    return ((x_0-x_1)**2+(y_0-y_1)**2)**0.5

def create_rhombus(start_x:int, start_y:int, big_diag:int):
    """
    Create a rhombus based on the start point and the big diagonal [2:1] prop
    """
    small_diag = big_diag/2
    canvas.create_polygon(start_x, start_y, start_x+big_diag/2,
                          start_y+small_diag/2, start_x, start_y+small_diag,
                          start_x-big_diag/2, start_y+small_diag/2,
                          outline="red", tags="rhombus")

def change_color(event=None):
    id_curr = canvas.find_withtag("current")
    canvas.itemconfigure(id_curr, fill="cyan")

def reset_color(event=None):
    id_curr = canvas.find_withtag("current")
    canvas.itemconfigure(id_curr, fill="black")

def display_cube(event=None):
    print("ok")
    id_curr = canvas.find_withtag("current")
    print(canvas.itemconfigure(id_curr))
    print(canvas.coords(id_curr))
    a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y = canvas.coords(id_curr)
    # l = 50;
    # a_x = event.x
    # a_y = event.y
    big_diag = distance(d_x, d_y, b_x, b_y)
    small_diag = big_diag/2
    print(big_diag, small_diag)
    # assert(small_diag == distance(a_x, a_y, c_x, c_y))

    # b_x = a_x+big_diag/2
    # b_y = a_y+small_diag/2
    # c_x = a_x
    # c_y = a_y+small_diag
    # d_x = a_x-big_diag/2
    # d_y = a_y+small_diag/2
    cube_edge = distance(a_x, a_y, b_x, b_y)
    print(f"a = {event.x+2*event.y/(4*cube_edge)},b = {2*event.y-event.x/(4*cube_edge)}")
    a_y -= cube_edge
    b_y -= cube_edge
    c_y -= cube_edge
    d_y -= cube_edge

    canvas.create_polygon(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y,
                          outline="red", tags="rhombus")

    canvas.create_polygon(d_x, d_y, c_x, c_y, c_x, c_y+cube_edge, d_x, d_y+cube_edge,
                          outline="red", tags="rhombus")

    canvas.create_polygon(c_x, c_y, b_x, b_y, b_x, b_y+cube_edge, c_x, c_y+cube_edge,
                          outline="red", tags="rhombus")
    return

def create_plan():
    # canvas.create_polygon(x,y, x+300, y+100, x, y+200, x-3008. The Ca8. The Ca, y+100,x,y,
    #                       outline="red", joinstyle="round")

    # we create a plan with vertex called A,B,C,D
    #               A
    #               .
    #            D / \ B
    #              \ /
    #               C

    grid_size = 7

    global SCREEN_HEIGHT, SCREEN_WIDTH
    SCREEN_HEIGHT = root.winfo_height()
    SCREEN_WIDTH = root.winfo_width()
    print(SCREEN_HEIGHT, SCREEN_WIDTH)
    a_y = SCREEN_HEIGHT/2
    a_x = SCREEN_WIDTH/2
    # 10 pixels de marge
    SMALL_DIAG = SCREEN_HEIGHT-a_y-10
    BIG_DIAG = SMALL_DIAG*2
    b_x = a_x+BIG_DIAG/2
    b_y = a_y+SMALL_DIAG/2
    c_x = a_x
    c_y = a_y+SMALL_DIAG
    d_x = a_x-BIG_DIAG/2
    d_y = a_y+SMALL_DIAG/2
    cube_edge = distance(a_x, a_y, c_x, c_y)
    # side_rhombus = dis/3
    small_diag = cube_edge/grid_size
    big_diag = small_diag*2
    # canvas.create_polygon(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y)
    for i in range(grid_size):
        for j in range(grid_size):
            create_rhombus(a_x-i*(big_diag/2)+j*(big_diag/2),
                           a_y+i*(small_diag/2)+j*(small_diag/2), big_diag)

    button.pack_forget()
    canvas.tag_bind("rhombus", sequence="<Enter>", func=change_color)
    canvas.tag_bind("rhombus", sequence="<Leave>", func=reset_color)
    canvas.tag_bind("rhombus", sequence="<ButtonPress-1>", func=display_cube)
    print("created")

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
