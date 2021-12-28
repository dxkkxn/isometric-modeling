import tkinter as tk
from tkinter import filedialog

class MenuBar(object):
    main_frame = None

    def __init__ (self, master):

        self.menu_frame = tk.Frame(master, bd=3, bg="#dbdbdb")
        self.file_menu = tk.Menubutton(self.menu_frame, text="Fichier",
                                       relief="raised")
        file_menu = self.file_menu
        menu_frame = self.menu_frame

        self.file_menu_ops = tk.Menu(file_menu)
        file_menu_ops = self.file_menu_ops
        file_menu_ops.add_command(label="Nouveau")
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


    def open_help_window():
        # summary = """Sommaire
        # Comment placer un cube?
        # Comment effacer un cube?
        # Comment changer de couleur?
        # """
        placer_p = """ \

        """
        help_window = tk.Toplevel()
        help_window.title("Aide")
        help_text= tk.Text(help_window, cursor="hand2")
        help_text.insert("end", "Sommaire\n", ())
        help_text.insert("end", "Comment placer un cube?\n", ("hyperlink", "p1"))
        help_text.insert("end", "Comment effacer un cube?\n", ("hyperlink","p2"))
        help_text.insert("end", "Comment changer la couleur d'un cube?\n",
                        ("hyperlink", "p3"))
        help_text.insert("end", "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        help_text.tag_config("hyperlink", foreground="blue", underline=1)
        with open("placer.txt", "r") as f:
            placer = (help_text.index("end"))
            help_text.insert("end", f.read())

        with open("effacer.txt", "r") as f:
            effacer = (help_text.index("end"))
            help_text.insert("end", f.read())

        with open("changer_coul.txt", "r") as f:
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

