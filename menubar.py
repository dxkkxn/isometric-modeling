import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import json
from plan import Plan
from cube import Cube
from color import Color
from colorframe import ColorFrame

class MenuBar(object):
    main_frame = None
    canvas = None
    main_app = None

    @staticmethod
    def set_canvas(canvas, main):
        MenuBar.canvas = canvas
        MenuBar.main_app=main

    def ask_confirm(self):
        txt = "Si vous n'avez pas sauvegarde et vous continuez vous perderez votre projet actuel"
        res = messagebox.askokcancel(title="Attention", message= txt)
        return res

    def new_project(self):
        continue_ = True
        if MenuBar.main_app.created:
            continue_ = self.ask_confirm()

        if continue_:
            MenuBar.main_app.clear_canvas()
            MenuBar.main_app.initial_frame.toggle_visibility()


    def __init__(self, master):
        self.menu_frame = tk.Frame(master, bd=3, bg="#dbdbdb")
        self.file_menu = tk.Menubutton(self.menu_frame, text="Fichier",
                                       relief="raised")
        file_menu = self.file_menu
        menu_frame = self.menu_frame

        self.file_menu_ops = tk.Menu(file_menu)
        file_menu_ops = self.file_menu_ops
        file_menu_ops.add_command(label="Nouveau", state="disabled",
                                  command=self.new_project)
        file_menu_ops.add_command(label="Ouvrir", command=self.open_file)
        file_menu_ops.add_command(label="Enregistrer sous",
                                       state="disabled",
                                       command=self.save_as_file)
        self.file_menu_ops.add_separator()
        file_menu_ops.add_command(label="Quitter")
        file_menu["menu"] = file_menu_ops
        help_btn = tk.Button(menu_frame, text="Aide", relief="raised",
                            command=self.open_help_window)

        help_btn.pack(side="right")
        file_menu.pack(side="left")
        menu_frame.pack(side="top", fill="x")


    def save_as_file(self, event=None):
        path = filedialog.asksaveasfilename(defaultextension=".cubes")
        if path != "":
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


    def open_file(self, event=None):
        continue_ = True
        if MenuBar.main_app.created:
            continue_ = self.ask_confirm()

        if continue_:
            path = filedialog.askopenfilename(filetypes=[("cubes","*.cubes")])
            if path != "":
                with open(path, "r") as f:
                    res = json.loads(f.read())
                    MenuBar.main_app.clear_canvas()
                    MenuBar.main_app.create_plan(res["size"])
                    for cube in res["cubes"]:
                        ColorFrame.color = Color(*cube["color"])
                        MenuBar.main_app.create_cube(relative_pos=cube["pos"])
            print("Succeed")


    def open_help_window(self):
        placer_p = """ \

        """
        help_window = tk.Toplevel()
        help_window.title("Aide")
        help_text= tk.Text(help_window, cursor="hand2")
        help_text.insert("end", "Sommaire\n", ())
        help_text.insert("end", "Comment placer un cube?\n",
                         ("hyperlink", "p1"))
        help_text.insert("end", "Comment effacer un cube?\n",
                         ("hyperlink","p2"))
        help_text.insert("end", "Comment changer la couleur d'un cube?\n",
                        ("hyperlink", "p3"))
        help_text.insert("end", "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        help_text.tag_config("hyperlink", foreground="blue", underline=1)
        with open("aide/placer.txt", "r") as f:
            placer = (help_text.index("end"))
            help_text.insert("end", f.read())

        with open("aide/effacer.txt", "r") as f:
            effacer = (help_text.index("end"))
            help_text.insert("end", f.read())

        with open("aide/changer_coul.txt", "r") as f:
            changer_coul = (help_text.index("end"))
            help_text.insert("end", f.read())

        help_text.tag_bind(tagName="p1", sequence="<ButtonRelease-1>",
                        func= lambda x: help_text.see(placer))
        help_text.tag_bind(tagName="p2", sequence="<ButtonRelease-1>",
                        func= lambda x: help_text.see(effacer))
        help_text.tag_bind(tagName="p3", sequence="<ButtonRelease-1>",
                        func= lambda x: help_text.see(changer_coul))
        help_text.config(state="disabled")
        help_text.pack(side="top")

