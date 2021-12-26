import tkinter as tk
from rhombus import Rhombus
from cube import Cube
from plan import Plan
from color import Color

from time import sleep
from PIL import Image, ImageTk

def change_col(event, frame):
    frame.configure(bg="cyan")

button_= None
def display_color_window():
    print(button_)
    s_height = root.winfo_height()
    x_width = root.winfo_width()
    s_width = root.winfo_width()/3
    color_frame = tk.Frame(root, bg="red",height=s_height, width=s_width)

    color_frame.place(in_=main_frame, x=1920, y=0, anchor="ne")

    button_frame =  tk.Frame(color_frame)
    tk.Button(button_frame, bitmap="error" ).pack(side="right")
    button_frame.pack(side="top")
    image_x = Image.open("./img/blue.jpg")


    img = ImageTk.PhotoImage(image_x)

    tk.Button(color_frame, image=img,  width=160, height=160, highlightcolor="cyan", highlightthickness=30,
               relief="raised", overrelief="raised", padx=70, pady=70).pack(side="top")

    colors = ["yellow", "red", "pink", "black", "white", "blue", "brown",
              "cyan", "DarkBlue", "green", "orange"]
    btn = []

    rw = 0
    col = 0
    # for color in colors:
    #     if rw%3 == 0:
    #         container_frame = tk.Frame(color_frame)
    #         container_frame.pack(side="top", fill="x")

    #     curr_frame = tk.Frame(container_frame, relief="raised", highlightcolor="cyan", bd=4,
    #              padx=50, pady=50, bg=color, width=s_width/4,
    #              height=s_width/4)
    #     curr_frame.pack(side="left")
    #     curr_frame.bind(sequence="<ButtonPress-1>", func= lambda x : change_col(x, curr_frame))

    #     rw+=1


    # btn[0].grid(row=1, column=0)
    # btn[1].grid(row=1, column=1)
    # btn[2].grid(row=1, column=2)
    # btn[3].grid(row=2, column=0)




    # id_x = canvas.create_window(x_width, 0, window=color_frame, anchor="ne",
    #                      height=s_height, width=s_width)
    # button_.lift(color_frame)
    color_frame.lift(canvas)


def create_plan():
    global button_

    print(scale.get())
    root.attributes("-zoom", True)
    Plan.set_root(root)
    p = Plan(scale.get())
    initial_frame.place_forget()
    scale.pack_forget()
    button.pack_forget()
    canvas.pack(side="top", expand=True, fill="both")
    x_x = root.winfo_width()

    button_color = tk.Button(main_frame, bitmap="gray12", command=display_color_window)
    button_color.place(in_=main_frame, x=x_x, y=0, anchor="ne")
    # button_ = canvas.create_window(x, 0, window=button_color, anchor="ne", tags="button")
    # button_ = button_color
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
    initial_frame = tk.Frame(main_frame, bg="green")

    canvas = tk.Canvas(main_frame, bg="white")
    button = tk.Button(initial_frame, text="display plan",
                       command= create_plan, takefocus=True)
    scale = tk.Scale(initial_frame, from_=1, to=50, repeatinterval=5,
                     orient="horizontal", label="Taille", tickinterval=2,
                     length=800)


    Rhombus.set_canvas(canvas)
    Cube.set_canvas(canvas)

    # root.geometry("960x540")
    root.attributes("-zoom", True)
    root.resizable(False, False)

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

