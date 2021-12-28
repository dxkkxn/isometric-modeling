import tkinter as tk
from rhombus import Rhombus
from colorframe import ColorFrame
from cube import Cube
from plan import Plan
from color import Color
from menubar import MenuBar
from PIL import Image, ImageTk
import json

class MainApplication(object):

    def display_color_frame(self):
        if ColorFrame.hidden == None:
            color_frame = ColorFrame()
        else :
            ColorFrame.show_hide_color_frame()


    def create_cube(self, event=None, relative_pos=None):
        if relative_pos is None:
            id_curr = self.canvas.find_withtag("current")[0]
            relative_pos = self.canvas.gettags(id_curr)[0]
            relative_pos = [int(x) for x in relative_pos.split(' ')]
            rhombus = Rhombus.all_rhombus[id_curr]
            orientation = (rhombus.all_rhombus[id_curr].orientation)
            if orientation == "sup":
                relative_pos[0] += 1
            elif orientation == "right":
                relative_pos[1] += 1
            elif orientation == "left":
                relative_pos[2] += 1

        color = ColorFrame.color
        cube = Cube(relative_pos, color, "xd")


    def create_plan(self, size):
        self.root.attributes("-zoom", True)
        self.root.update_idletasks()

        Plan.set_canvas(self.canvas)
        p = Plan(size)

        self.initial_frame.place_forget()
        self.scale.pack_forget()
        self.confirm_button.pack_forget()


        size = 50
        img = Image.open("./img/tool.PNG")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        btn_tool= tk.Button(self.main_frame, image = img,
                            command=self.display_color_frame)
        btn_tool.image = img
        sc_width = self.root.winfo_width()
        btn_tool.place(in_=self.main_frame, x=sc_width, y=0, anchor="ne")
        return


    def __init__(self, master):
        self.root = master
        self.main_frame = tk.Frame(master)
        self.initial_frame = tk.Frame()
        self.canvas = tk.Canvas(self.main_frame)
        self.confirm_button = tk.Button(self.initial_frame,
                                        text="Creer nouveau projet",
                            command=lambda :self.create_plan(self.scale.get()))
        menu_bar = MenuBar(self.main_frame)
        length = master.winfo_width() * 0.80
        length = int(length)
        self.scale = tk.Scale(self.initial_frame, from_=1, to=50, repeatinterval=5,
                              orient="horizontal",
                              label="Indiquez la taille du nouveau projet",
                              tickinterval=2, length=length)

        ColorFrame.set_canvas(self.canvas)
        ColorFrame.set_root(master)

        Rhombus.set_canvas(self.canvas)
        Cube.set_canvas(self.canvas)

        self.canvas.bind(sequence="<ButtonRelease-1>", func=self.create_cube)

        self.canvas.pack(side="top", expand=True, fill="both")
        self.initial_frame.lift(self.canvas)


        self.main_frame.pack(fill="both", expand=True)
        self.initial_frame.place(in_=master, anchor="center", relx=0.5, rely=.5)
        self.scale.pack(side="top", fill="both", expand=True )
        self.confirm_button.pack(side="right")




def main():
    root = tk.Tk()
    root.title("Modelisation Isometrique")
    sc_width = root.winfo_screenwidth()
    sc_height = root.winfo_screenheight()
    root.geometry("{}x{}".format(sc_width//2, sc_height//2,))
    root.resizable(False, False)
    root.update_idletasks()

    app = MainApplication(root)

    root.mainloop()


if __name__ == "__main__" :
    main()
    exit(0)


