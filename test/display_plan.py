import tkinter as tk

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

def create_rhombus():
    # canvas.create_polygon(x,y, x+300, y+100, x, y+200, x-300, y+100,x,y,
    #                       outline="red", joinstyle="round")
    global SCREEN_HEIGHT, SCREEN_WIDTH
    SCREEN_HEIGHT = canvas.winfo_height()
    SCREEN_WIDTH = canvas.winfo_width()
    print(SCREEN_HEIGHT, SCREEN_WIDTH)
    START_Y = SCREEN_HEIGHT/3
    START_X = SCREEN_WIDTH/2
    # 10 pixels de marge
    DIAG_P = SCREEN_HEIGHT-START_Y-10
    DIAG_G = DIAG_P*2
    canvas.create_polygon(START_X, START_Y, START_X+DIAG_G/2, START_Y+DIAG_P/2,
                   START_X, START_Y+DIAG_P, START_X-DIAG_G/2, START_Y+DIAG_P/2)
    print("created")

    return
def get_window_size(event=None):
    #print("OOOOOOOOk")
    #print(event)
    SCREEN_HEIGTH = root.winfo_height()
    SCREEN_WIDTH = root.winfo_width()
#    print(canvas.cget("height"))
    """
    if CANVAS_WIDTH - 2 != event.width :
        CANVAS_WIDTH = event_width-2
        canvas.configure(width=event.width-2, height=event.height)
        canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANV0AS_HEIGHT,
    if CANVAS_HEIGHT- 2 != event.height:
        CANVAS_HEIGHT = event_width-2
        canvas.configure(width=event.width, height=event.height)
    """
    return
if __name__ == "__main__" :
    root = tk.Tk()
    root.title("plan")
    top_level = tk.Toplevel()
    button = tk.Button(top_level, text="display plan", command=create_rhombus, takefocus=True)
    button.pack(side="top")
    # SCREEN_HEIGHT = 1080
    # SCREEN_WIDTH = 1920
    # geometry_str = str(SCREEN_WIDTH)+str(SCREEN_HEIGHT)
    # root.geometry()
    # print(root.winfo_screenheight())

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(side="top", expand=True, fill="both")
    # print("-----------")
    # print(canvas.winfo_height(), canvas.winfo_width())
    # print(SCREEN_WIDTH, SCREEN_HEIGHT)
    #for i in range(3):
    #    create_rhombus(500-600+i*300, 200+200+i*100)
    #root.bind(sequence="<Configure>", func=resize)
    #root.attributes('-fullscreen', True)
    root.attributes("-zoomed", True)
    #print("here->",root.winfo_height())
    #root.resizable(False, False)
    root.mainloop()
