import tkinter as tk

def create_rhombus(x: int, y: int):
    canvas.create_polygon(x,y, x+300, y+100, x, y+200, x-300, y+100,x,y,
                          outline="red", joinstyle="round")

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("xd")

    canvas = tk.Canvas(root, width=2000, height=2000, bg="white")
    canvas.pack(side="top")
    for i in range(3):
        create_rhombus(1000+i*300,1000+i*100)
    for i in range(1,3):
        create_rhombus(1000+i*-300,1000+i*100)

    root.mainloop()
