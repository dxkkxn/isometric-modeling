import tkinter as tk
from rhombus import Rhombus
from colorframe import ColorFrame
from cube import Cube
from plan import Plan
from color import Color
from menubar import MenuBar
from PIL import Image, ImageTk

class InitialFrame(object):
    main_app = None

    def __init__(self, master):
        self.initial_frame = tk.Frame(master)
        self.container_frame = tk.Frame(self.initial_frame)
        self.confirm_button = tk.Button(self.container_frame,
                                        text="Creer nouveau projet",
        command=lambda:InitialFrame.main_app.create_plan(self.scale.get()))

        length = master.winfo_width() * 0.80
        print(length, master.winfo_width())
        length = int(length)
        self.scale = tk.Scale(self.container_frame, from_=1, to=50,
                              repeatinterval=5, orient="horizontal",
                              label="Indiquez la taille du nouveau projet",
                              tickinterval=2, length=length)

        self.initial_frame.pack(side="top", fill="both", expand=True)
        master.update_idletasks()
        self.container_frame.place(in_=self.initial_frame, anchor="center",
                                   relx=0.5, rely=.5)
        self.scale.pack(side="top", fill="both", expand=True)
        self.confirm_button.pack(side="right")
        self.shown = True


    @staticmethod
    def set_main_app(main_app):
        InitialFrame.main_app = main_app

    def toggle_visibility(self):
        if self.shown:
            self.initial_frame.pack_forget()
            self.shown = False
        else :
            self.initial_frame.pack(side="top", fill="both", expand=True)
            self.shown = True


class MainApplication(object):

    def __init__(self, master):
        self.root = master
        self.menu_bar = MenuBar(self.root)
        self.initial_frame = InitialFrame(self.root)
        InitialFrame.set_main_app(self)
        self.main_frame = tk.Frame(self.root)
        self.canvas = tk.Canvas(self.main_frame)
        MenuBar.set_canvas(self.canvas, self)

        ColorFrame.set_canvas(self.canvas)
        ColorFrame.set_root(self.root)
        ColorFrame.set_main_app(self)
        Rhombus.set_canvas(self.canvas)
        Cube.set_canvas(self.canvas)
        Plan.set_canvas(self.canvas)

        self.created = False

        self.canvas.bind(sequence="<ButtonPress-1>", func=self.create_cube)
        self.canvas.bind(sequence="<Button-4>", func=self.canvas_zoom)
        self.canvas.bind(sequence="<Button-5>", func=self.canvas_zoom_out)
        self.last_pos = (None, None)

    def canvas_zoom(self,event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.canvas.scale("rhombus", x, y, 1.01, 1.01)


    def canvas_zoom_out(self,event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.canvas.scale("rhombus", x, y, 0.99, 0.99)


    def clear_canvas(self):
        if self.created:
            self.rotate_left_btn.place_forget()
            self.rotate_right_btn.place_forget()
            self.canvas.delete("all")
            self.main_frame.pack_forget()
            Cube.clean_all_cubes()


    def create_tool_btn(self):
        size = 50
        img = Image.open("./img/tool.PNG")
        img = img.resize((size, size))
        img = ImageTk.PhotoImage(img)
        self.tool_btn= tk.Button(self.canvas, image = img,
                            command=ColorFrame.toggle_visibility)
        self.tool_btn.image = img
        sc_width = self.main_frame.winfo_width()
        self.tool_btn_visibility = False


    def tool_btn_toggle_visibility(self):
        if not self.tool_btn_visibility:
            self.tool_btn.pack(in_=self.canvas, side="right", anchor="ne")
            self.tool_btn_visibility = True
        else:
            self.tool_btn.pack_forget()
            self.tool_btn_visibility = False


    def display_color_frame(self):
        if ColorFrame.hidden == None:
            color_frame = ColorFrame()
        else :
            ColorFrame.show_hide_color_frame()


    def create_cube(self, event=None, relative_pos=None):
        rhombus = None
        if relative_pos is None:
            try:
                id_curr = self.canvas.find_withtag("current")[0]
            except IndexError:
                print("Position invalide")
                return
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
        print(color)
        cube = Cube(relative_pos, color, rhombus)


    def create_plan(self, size):
        if self.initial_frame.shown:
            self.initial_frame.toggle_visibility()
        self.canvas.pack(side="top", expand=True, fill="both")
        self.main_frame.pack(fill="both", expand=True)
        self.root.update_idletasks()
        self.menu_bar.file_menu_ops.entryconfig(3, state = "active")
        self.menu_bar.file_menu_ops.entryconfig(1, state = "active")

        if not self.created:
            # button and color frame creation
            # this is necessary to not recreate every time the items
            # the user opens a file or creates a new project
            self.create_tool_btn()
            self.create_right_and_left_btns()
            self.tool_btn_toggle_visibility()
            self.color_frame = ColorFrame()
            self.cf_created = True
            self.color_frame.frame.lift(self.tool_btn)
            self.created = True


        self.rotate_left_btn.place(in_=self.canvas, anchor="s",
                                   relx=0.4, rely=1)
        self.rotate_right_btn.place(in_=self.canvas, anchor="s",
                                   relx=0.6, rely=1)
        self.canvas.pack(side="top", expand=True, fill="both")
        self.plan = Plan(size)
        return


    def create_right_and_left_btns(self):
        size = 50
        img = Image.open("./img/arrow_l.png")
        img = img.resize((size, size-20))
        img = ImageTk.PhotoImage(img)
        self.rotate_left_btn= tk.Button(self.canvas, image=img,
                                        command=Cube.rotate_90_deg_left)

        #keep reference
        self.rotate_left_btn.image = img
        img = Image.open("./img/arrow_r.png")
        img = img.resize((size, size-20))
        img = ImageTk.PhotoImage(img)
        self.rotate_right_btn= tk.Button(self.canvas, image = img,
                                         command = Cube.rotate_90_deg_right)
        #keep reference
        self.rotate_right_btn.image = img




def main():
    root = tk.Tk()
    root.title("Modelisation Isometrique")
    root.attributes("-zoom", True)
    root.geometry("1920x1080")
    root.update_idletasks()

    app = MainApplication(root)

    root.mainloop()


if __name__ == "__main__" :
    main()
    exit(0)


