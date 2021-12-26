import tkinter as tk
from rhombus import Rhombus
from cube import Cube
from plan import Plan
from color import Color

from time import sleep

button_= None
def display_color_window():
    print(button_)
    color_frame = tk.Frame(root, bg="red")
    s_height = root.winfo_height()
    x_width = root.winfo_width()
    s_width = root.winfo_width()/3
    id_x = canvas.create_window(x_width, 0, window=color_frame, anchor="ne",
                         height=s_height, width=s_width)
    button_.lift(color_frame)

    sleep(10)
    color_frame.pack_forget()

    print("raised OK")
def create_plan():
    global button_

    print(scale.get())
    root.title("xd")
    root.attributes("-fullscreen", True)
    print("zoomed")
    return
    Plan.set_root(root)
    p = Plan(scale.get())
    initial_frame.place_forget()
    scale.pack_forget()
    button.pack_forget()

    return

    canvas.pack(side="top", expand=True, fill="both")
    x = root.winfo_width()

    button_color = tk.Button(root, bitmap="gray12", command=display_color_window)
    button_ = canvas.create_window(x, 0, window=button_color, anchor="ne", tags="button")
    button_ = button_color
    print(button_)
    return

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


if __name__ == "__main__" :
    root = tk.Tk()
    root.title("plan")

    main_frame = tk.Frame(root, bg="yellow", width=960, height=540)
    initial_frame = tk.Frame(main_frame, bg="green", width=1920/2, height=1080/2)

    canvas = tk.Canvas(main_frame, bg="white")
    button = tk.Button(initial_frame, text="display plan",
                       command= create_plan, takefocus=True)
    scale = tk.Scale(initial_frame, from_=1, to=50, repeatinterval=5,
                     orient="horizontal", label="Taille", tickinterval=2,
                     length=800)


    Rhombus.set_canvas(canvas)
    Cube.set_canvas(canvas)

    # root.geometry("960x540")
    # root.attributes("-zoom", True)

    canvas.bind(sequence="<ButtonPress-1>", func= create_cube)

    main_frame.pack(fill="both", expand=True)
    initial_frame.place(in_=main_frame, anchor="center", relx=0.5, rely=.5)
    scale.pack(side="top", fill="both", expand=True )
    button.pack(side="right")

    # s_height = root.winfo_height()
    # x_width = root.winfo_width()
    # print(s_height, x_width)
    #
    # f1 = tk.Frame(width=200, height=200, background="red")
    # f2 = tk.Frame(width=100, height=100, background="blue")

    # f1.pack(fill="both", expand=True, padx=20, pady=20)
    # f2.place(in_=f1, anchor="c", relx=.5, rely=.5)

    root.mainloop()
    # scale.grid(row = 0)
    # button.grid(row=1 )

