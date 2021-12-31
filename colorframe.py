import tkinter as tk
from color import Color
from PIL import Image, ImageTk
from tkinter import colorchooser

class ColorFrame():
    btns= []
    btns_colour = {0:[0,238, 238], 1:[0,255,127], 2:[105, 105, 105],
                   3:[255, 62, 150], 4:[255, 0, 0], 5:[5, 5, 5], 6:"random",
                   7:"color_chooser", 8:"move"}
    main_frame = None
    canvas = None
    root = None
    hidden = None
    color_frame = None
    color = None
    main_app = None

    @staticmethod
    def set_main_app(ma):
        ColorFrame.main_app = ma

    @staticmethod
    def toggle_visibility():
        if ColorFrame.hidden:
            cvs_width = ColorFrame.canvas.winfo_width()
            ColorFrame.color_frame.place(in_=ColorFrame.canvas, x=cvs_width,
                                         y=0, anchor="ne")
            ColorFrame.hidden = False
        else:
            ColorFrame.color_frame.place_forget()
            ColorFrame.hidden = True


    def press(self, i):
        btns = ColorFrame.btns
        btns[self.pressed].configure(relief="flat",
                                     highlightbackground="#d9d9d9")
        btns[i].configure(relief="sunken", highlightbackground="cyan")
        if self.pressed == 8:
            self.canvas.unbind(sequence="<B1-Motion>")
            self.canvas.bind(sequence="<ButtonPress-1>")
            self.canvas.bind(sequence="<ButtonPress-1>",
                             func=ColorFrame.main_app.create_cube)
        self.pressed = i
        if ColorFrame.btns_colour[i] == "random" :
            colour = Color.random_col()
            #relief flat to show the user he can press multiple times
            btns[i].configure(relief="flat")
            ColorFrame.color = colour

        elif ColorFrame.btns_colour[i] == "color_chooser":
            btns[i].configure(highlightbackground="cyan")
            result = colorchooser.askcolor(color="cyan",
                                        title="chossisez une couleur",
                                        parent = ColorFrame.root)
            if result != (None, None) :
                colour = Color(*(result[0]))
            else :
                self.press(6)
            ColorFrame.color = colour
        elif ColorFrame.btns_colour[i] == "move":
            self.canvas.unbind("<ButtonPress-1>")
            self.canvas.bind(sequence="<B1-Motion>", func=self.move_canvas)
            self.canvas.bind(sequence="<ButtonPress-1>", func=self.set_last_pos)
        else:
            colour = Color(*self.btns_colour[i])
            ColorFrame.color = colour

    def set_last_pos(self, event):
        self.last_pos = event.x, event.y

    def move_canvas(self, event=None):
        x, y = self.last_pos
        print(event.x, event.y)
        self.canvas.move("rhombus",event.x - x , event.y - y)
        self.last_pos = event.x, event.y



    def __init__(self):
        cvs_width = ColorFrame.canvas.winfo_width()

        color_frame = tk.Frame(ColorFrame.canvas)
        self.frame = color_frame
        ColorFrame.color_frame = color_frame

        # x button creation
        button_x_frame =  tk.Frame(color_frame)

        image_x = Image.open("./img/x.jpg")
        image_x = image_x.resize((50,50))
        img = ImageTk.PhotoImage(image_x)

        x_btn = tk.Button(button_x_frame, image = img, width=50, height=50,
                          command=self.toggle_visibility)

        x_btn.image = img

        # placement of x_btn and his frame
        x_btn.pack(side="right")
        button_x_frame.grid(row = 0, column=0, columnspan= 2, sticky=tk.E)

        size = int(cvs_width/9)
        buttons_images = ["cyan", "green", "grey", "rose", "red", "black",
                          "random", "color_chooser", "move"]
        i = 0
        for image in buttons_images:
            img = Image.open("./img/{}.PNG".format(image))
            img = img.resize((size, size-40))
            img = ImageTk.PhotoImage(img)
            btn = tk.Button(color_frame, image=img,
                            command= lambda idx=i: self.press(idx), padx=50,
                            pady=50, highlightthickness=3)
            # ref to prevent the loose by the garbage collector
            btn.image = img
            ColorFrame.btns.append(btn)
            i += 1

        ColorFrame.btns[8].grid(row=1, column=0, columnspan=2)

        ColorFrame.btns[0].grid(row=2, column=0)
        ColorFrame.btns[1].grid(row=2, column=1)
        ColorFrame.btns[2].grid(row=3, column=0)
        ColorFrame.btns[3].grid(row=3, column=1)
        ColorFrame.btns[4].grid(row=4, column=0)
        ColorFrame.btns[5].grid(row=4, column=1)
        ColorFrame.btns[6].grid(row=5, column=0)
        ColorFrame.btns[7].grid(row=5, column=1)
        self.pressed = 6
        self.press(6)
        # color_frame.lift(canvas)
        ColorFrame.hidden = True
        return


    @staticmethod
    def set_main_frame(main_frame):
        ColorFrame.main_frame = main_frame


    @staticmethod
    def set_canvas(canvas):
        ColorFrame.canvas = canvas


    @staticmethod
    def set_root(root):
        ColorFrame.root = root
