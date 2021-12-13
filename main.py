import tkinter as tk
from rhombus import Rhombus
from cube import Cube
from plan import Plan
from color import Color

def display_color_window():
    color_frame = tk.Frame(root)
    s_height = root.winfo_height()
    x_width = root.winfo_width()
    s_width = root.winfo_width()/3
    id_x = canvas.create_window(x_width, 0, window=color_frame, anchor="ne",
                         height=s_height, width=s_width)
    canvas.tag_raise("button", id_x)

def create_plan():
    print(scale.get())
    Plan.set_root(root)
    p = Plan(scale.get())
    scale.pack_forget()
    button.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    canvas.pack(side="top", expand=True, fill="both")
    x = root.winfo_width()
    button_color = tk.Button(root, bitmap="gray12", command=display_color_window)
    canvas.create_window(x, 0, window=button_color, anchor="ne", tags="button")
    button_color.bind()
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
    canvas = tk.Canvas(root, bg="white")
    button = tk.Button(root, text="display plan", 
                       command= create_plan, takefocus=True)
    scale = tk.Scale(root, from_=1, to=30, repeatinterval=1, 
                     orient="horizontal", label="Taille", tickinterval=1)
    Rhombus.set_canvas(canvas)
    Cube.set_canvas(canvas)

    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    canvas.bind(sequence="<ButtonPress-1>", func= create_cube)
    frame1.pack(fill="y", expand=True)
    scale.pack(side="top", anchor="center", fill="both")
    button.pack(anchor="center")
    frame2.pack(fill="y", expand=True)
    root.attributes("-zoomed", True)
    root.mainloop()
