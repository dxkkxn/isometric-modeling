from color import Color

class Rhombus():
    BIG_DIAG = None
    SMALL_DIAG = None
    all_rhombus = {}
    canvas = None
    
    @staticmethod
    def set_canvas(canvas):
        Rhombus.canvas = canvas

    def change_color(self, event=None):
        Rhombus.canvas.itemconfigure(self.__id, fill="#2bfafa")

    def reset_color(self, event=None):
        Rhombus.canvas.itemconfigure(self.__id, fill=self.__color.to_hex_rgb())

    @property
    def orientation(self):
        return self.__orientation

    def __init__(self, color, orientation, *args, **kwargs):
        """
        Create a rhombus based on the start point and the big diagonal [2:1] prop
        """
        canvas = Rhombus.canvas
        self.__color = color
        self.__orientation = orientation
        print(self.__orientation)
        self.__id = canvas.create_polygon(*args, **kwargs, outline="black",
                                           fill=self.__color.to_hex_rgb(),
                                           width=2)
        self.all_rhombus[self.__id] = self
        if "rhombus" not in canvas.gettags(self.__id):
            canvas.addtag_withtag( "rhombus", self.__id)
        canvas.tag_bind(self.__id, sequence="<Enter>", func=lambda event :self.change_color(event))
        canvas.tag_bind(self.__id, sequence="<Leave>", func=lambda event :self.reset_color(event))

