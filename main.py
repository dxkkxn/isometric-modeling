import tkinter as tk
from tkinter import colorchooser
from tkinter import filedialog
from rhombus import Rhombus
from cube import Cube
from plan import Plan
from color import Color
import json

from time import sleep
from PIL import Image, ImageTk




btns= []
btns_colour = {0:[0,238, 238], 1:[0,255,127], 2:[105, 105, 105],
               3:[255, 62, 150], 4:[255, 0, 0], 5:[5, 5, 5], 6:None, 7:None}
def test(i):
    global colour
    if btns_colour[i] is not None:
        colour = Color(*btns_colour[i])
    else :
        colour = None
    for btn in btns:
        btn.configure(relief="flat", highlightbackground="#d9d9d9")
    if i == 7 :
        btns[i].configure( highlightbackground="cyan")
        result = colorchooser.askcolor(color="cyan",
                                       title="chossisez une couleur",
                                       parent = root)
        print(result)
        if result != (None, None) :
            colour = Color(*(result[0]))
        else :
            test(6)
    else :
        btns[i].configure(relief="sunken", highlightbackground="cyan")
color_frame = None
def display_color_window():
    global color_frame
    if color_frame is not None:
        color_frame.place(in_=main_frame, x=1920, y=0, anchor="ne")
        return

    s_height = root.winfo_height()
    x_width = root.winfo_width()
    s_width = root.winfo_width()/3
    color_frame = tk.Frame(root, height=s_height, width=s_width)

    color_frame.place(in_=main_frame, x=1920, y=0, anchor="ne")

    button_frame =  tk.Frame(color_frame)

    image_x = Image.open("./img/x.jpg")
    image_x = image_x.resize((50,50))
    img = ImageTk.PhotoImage(image_x)
    def hide_color_frame():
        color_frame.place_forget()
    x_btn = tk.Button(button_frame, image = img, width=50, height=50, command=hide_color_frame)
    button_frame.grid(row = 0, column=0, columnspan= 2, sticky=tk.E)
    x_btn.image = img
    x_btn.pack(side="right")

    taille = int(s_width/3)
    colors = ["cyan", "green", "grey", "rose", "red", "black", "random",
              "color_chooser"]

    i = 0
    j = 0
    for color in colors:
        image_x = Image.open("./img/"+color+".PNG")
        image_x = image_x.resize((taille, taille-40))
        img = ImageTk.PhotoImage(image_x)

        btn = tk.Button(color_frame, image=img, command= lambda idx=i: test(idx)
                        , padx=50, pady=50, highlightthickness=5)
        btn.image = img
        btns.append(btn)
        i+= 1

    btns[0].grid(row=1, column=0)
    btns[1].grid(row=1, column=1)
    btns[2].grid(row=2, column=0)
    btns[3].grid(row=2, column=1)
    btns[4].grid(row=3, column=0)
    btns[5].grid(row=3, column=1)
    btns[6].grid(row=4, column=0)
    btns[7].grid(row=4, column=1)
    test(6)
    color_frame.lift(canvas)


def create_plan(size):
    root.attributes("-zoom", True)
    Plan.set_root(root)
    p = Plan(size)
    initial_frame.place_forget()
    scale.pack_forget()
    button.pack_forget()
    canvas.pack(side="top", expand=True, fill="both")
    x_x = root.winfo_width()

    taille = 50
    image_x = Image.open("./img/tool.PNG")
    image_x = image_x.resize((taille, taille))
    img = ImageTk.PhotoImage(image_x)

    btn_tool= tk.Button(main_frame, image = img, command=display_color_window)
    btn_tool.image = img
    btn_tool.place(in_=main_frame, x=x_x, y=0, anchor="ne")
    # button_ = canvas.create_window(x, 0, window=button_color, anchor="ne", tags="button")
    # button_ = button_color
    file_menu_ops.entryconfigure(3, state="active")
    return


def create_cube(event=None, colour=None, relative_pos=None):

    if colour is None :
        colour = Color.random_col()
    color = colour
    if relative_pos is None:
        id_curr = canvas.find_withtag("current")[0]
        relative_pos = canvas.gettags(id_curr)[0]
        relative_pos = [int(x) for x in relative_pos.split(' ')]
        rhombus = Rhombus.all_rhombus[id_curr]
        orientation = (rhombus.all_rhombus[id_curr].orientation)
        if orientation == "sup":
            relative_pos[0] += 1
        elif orientation == "right":
            relative_pos[1] += 1
        elif orientation == "left":
            relative_pos[2] += 1

    cube = Cube(relative_pos, color, "xd")


def save_as_file(event=None):
    path = filedialog.asksaveasfilename(defaultextension=".cubes")
    res = {}
    res["size"] = Plan.size
    cubes = []
    all_cubes = Cube.all_cubes
    for pos, rhombus in all_cubes.items():
        a_cube = {}
        a_cube["pos"] = pos
        a_cube["color"] = rhombus[0].color.to_list()
        cubes.append(a_cube)
    res["cubes"]  = cubes
    with open(path, "w") as f :
        f.write(json.dumps(res, indent=2))
    print("Succeed")


def open_file(event=None):
    path = filedialog.askopenfilename(filetypes=[("cubes","*.cubes")])
    with open(path, "r") as f:
        res = json.loads(f.read())
        canvas.delete("all")
        create_plan(res["size"])
        for cube in res["cubes"]:
            create_cube(colour=Color(*cube["color"]), relative_pos=cube["pos"])
    print("Succeed")

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("plan")

    main_frame = tk.Frame(root, bg="yellow", width=960, height=540)
    initial_frame = tk.Frame(main_frame, bg="green")

    canvas = tk.Canvas(main_frame, bg="white")
    button = tk.Button(initial_frame, text="display plan",
                       command= lambda :create_plan(scale.get()), takefocus=True)
    scale = tk.Scale(initial_frame, from_=1, to=50, repeatinterval=5,
                     orient="horizontal", label="Taille", tickinterval=2,
                     length=800)

    menu_frame = tk.Frame()
    file_menu = tk.Menubutton(menu_frame, text="Fichier", relief="flat")
    file_menu_ops = tk.Menu(file_menu)
    file_menu_ops.add_command(label="Nouveau")
    file_menu_ops.add_command(label="Ouvrir", command=open_file)
    file_menu_ops.add_command(label="Enregistrer comme", state="disabled",
                              command=save_as_file)
    file_menu_ops.add_separator()
    file_menu_ops.add_command(label="Quitter")
    file_menu["menu"] = file_menu_ops
    help_btn = tk.Button(menu_frame, text="Aide", relief="flat")

    help_btn.pack(side="right")
    file_menu.pack(side="left")
    menu_frame.pack(side="top", fill="x")

    Rhombus.set_canvas(canvas)
    Cube.set_canvas(canvas)

    # root.geometry("960x540")
    root.attributes("-zoom", True)
    root.resizable(False, False)
    colour = None
    canvas.bind(sequence="<ButtonPress-1>", func= lambda x: create_cube(x, colour))

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

