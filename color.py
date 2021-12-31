from parserx import parser
import random

class Color(object):
    cols_dict = parser()
    cols  = list(cols_dict.keys())

    def __init__(self, red :int, green: int, blue: int):
        self.__red = red
        self.__green = green
        self.__blue = blue

    @classmethod
    def from_hex_str(cls, str_hex_col: str):
        color = str_hex_col
        rgb_list = []
        for x in range(1, len(color), 2):
            hex_x = color[x:x+2]
            rgb_list.append(int(hex_x, 16))
        res = cls(rgb_list[0],rgb_list[1], rgb_list[2])
        return res

    def __str__(self):
        color_s = f"(red = {self.__red}, green= {self.__green}, blue = {self.__blue})"
        return color_s


    def to_list(self):
        return [self.__red, self.__green, self.__blue]


    def shade_color(self, factor:int):
        """
        return a new instance class with a shaded color
        """
        color = self.to_list()
        shaded_color  = [(1-factor)*x for x in color]
        shaded_color  = [int(x) for x in shaded_color]
        return Color(*shaded_color)


    def to_hex_rgb(self):
        """
        Returns de color in 8bits hexadecimal form in str format
        """
        color = self.to_list();
        hex_rgb_list = []
        for x in color:
            hex_x = hex(x)[2:]
            if len(hex_x) == 1:
                hex_x = "0"+hex_x
            hex_rgb_list.append(hex_x)

        return "#"+ "".join(hex_rgb_list)


    @classmethod
    def random_col(cls):
        rgb = Color.cols_dict[random.choice(Color.cols)]
        return cls(*rgb)


if __name__ == "__main__" :
    col = Color.from_hex_str("#ff0000")
    col2 =  col.shade_color(0.25)
    print(col.to_hex_rgb(), col2.to_hex_rgb())
