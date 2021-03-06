#!/usr/bin/env python3
import tkinter as tk
import display_plan as dp
import random
from parser_x import parser
from PIL import Image, ImageTk

def shade_color(color: list, factor:int):
    shaded_color  = [(1-factor)*x for x in color]
    shaded_color  = [int(x) for x in shaded_color]
    return shaded_color


def rgb_to_hex_rgb(self):
    """
    Returns de color in 8bits hexadecimal form in str format
    """
    color = self
    hex_rgb_list = []
    for x in color:
        hex_x = hex(x)[2:]
        if len(hex_x) == 1:
            hex_x = "0"+hex_x
        hex_rgb_list.append(hex_x)

    return "#"+ "".join(hex_rgb_list)


colors = list(parser().keys())
def display_cube(event=None):
    print("ok")
    l = 50;
    a_x = event.x
    a_y = event.y
    big_diag = 100
    small_diag = 50
    b_x = a_x+big_diag/2
    b_y = a_y+small_diag/2
    c_x = a_x
    c_y = a_y+small_diag
    d_x = a_x-big_diag/2
    d_y = a_y+small_diag/2
    dis = dp.distance(a_x, a_y, b_x, b_y)

    color_choice = random.choice(colors)
    print(color_choice)
    print(parser()[color_choice])
    rgb_list = (parser()[color_choice])
    s1 = shade_color(rgb_list, 0.5)
    s2 = shade_color(s1, 0.5)
    s1 = rgb_to_hex_rgb(s1)
    s2 = rgb_to_hex_rgb(s2)

    canvas.create_polygon(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y,
                          fill=color_choice, outline="black", width=2, tags="rhombus")

    canvas.create_polygon(d_x, d_y, c_x, c_y, c_x, c_y+dis, d_x, d_y+dis,
                          fill=s2, outline="black", width=2, tags="rhombus")

    canvas.create_polygon(c_x, c_y, b_x, b_y, b_x, b_y+dis, c_x, c_y+dis,
                          fill=s1, width=2,outline="black", tags="rhombus")

    canvas.create_image(a_x, a_y+small_diag, image =img, anchor="center")

    return

if __name__ == "__main__" :
   root = tk.Tk()
   root.title("plan")

   img = Image.open("./img/minecraft.png")
   img = ImageTk.PhotoImage(img)
   canvas = tk.Canvas(root, bg="white")
   canvas.pack(side="top", expand=True, fill="both")
   canvas.bind(sequence="<ButtonPress-1>", func=display_cube)
   root.attributes("-zoomed", True)
   frm  = tk.Frame(canvas, bg="green", width=400, height=200 )
   frm.pack(side="left")
   root.mainloop()
