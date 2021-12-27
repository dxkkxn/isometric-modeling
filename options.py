#!/usr/bin/env python3

class Options(object):
    def __init__():
btns= []

def test(i):
    btns[i].configure(relief="sunken", highlightbackground="cyan"
                        )
def display_color_window():
    s_height = root.winfo_height()
    x_width = root.winfo_width()
    s_width = root.winfo_width()/3
    color_frame = tk.Frame(root, height=s_height, width=s_width)

    color_frame.place(in_=main_frame, x=1920, y=0, anchor="ne")

    button_frame =  tk.Frame(color_frame)

    image_x = Image.open("./img/x.jpg")
    image_x = image_x.resize((50,50))
    img = ImageTk.PhotoImage(image_x)
    x_btn = tk.Button(button_frame, image = img, width=50, height=50)
    button_frame.grid(row = 0, column=0, columnspan= 2, sticky=tk.E)
    x_btn.image = img
    x_btn.pack(side="right")

    taille = int(s_width/3)
    colors = ["cyan", "green", "grey", "rose", "red", "black", "random", "color_chooser"]

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
    color_frame.lift(canvas)
