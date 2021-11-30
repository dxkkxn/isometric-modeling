import tkinter as tk

def create_rhombus(x:int, y:int):
    canvas.create_polygon(x,y, x+300, y+100, x, y+200, x-300, y+100,x,y,
                          outline="red", joinstyle="round")

    return
def resize(event=None):
    #print("OOOOOOOOk")
    #print(event)
    #print(canvas.cget("width")) 
    #print(canvas.cget("height")) 
    """
    if CANVAS_WIDTH - 2 != event.width :
        CANVAS_WIDTH = event_width-2
        canvas.configure(width=event.width-2, height=event.height)
        canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANV0AS_HEIGHT,
    if CANVAS_HEIGHT- 2 != event.height:
        CANVAS_HEIGHT = event_width-2
        canvas.configure(width=event.width, height=event.height)
    """
if __name__ == "__main__" :
    root = tk.Tk()
    root.title("plan")
    SCREEN_HEIGHT = root.winfo_screenheight()
    SCREEN_WIDTH = root.winfo_screenwidth()
    geometry_str = str(SCREEN_WIDTH)+str(SCREEN_HEIGHT)
    root.geometry(
    print(root.winfo_screenheight())
    
    canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,
                       bg="white")
    canvas.pack(side="top", expand=True, fill="both")
    print(SCREEN_WIDTH, SCREEN_HEIGHT)
    START_X = SCREEN_WIDTH/2
    START_Y = SCREEN_HEIGHT/2
    DIAG_P = START_Y
    DIAG_G = START_Y*2
    print(DIAG_P, DIAG_G)
    canvas.create_polygon(START_X, START_Y, START_X+DIAG_G/2, START_Y+DIAG_P/2,
                   START_X, START_Y+DIAG_P, START_X-DIAG_G/2, START_Y+DIAG_P/2)
    #for i in range(3):
    #    create_rhombus(500-600+i*300, 200+200+i*100)
    root.bind(sequence="<Configure>", func=resize)
#    root.attributes('-fullscreen', True)
    root.resizable(False, False)
    root.mainloop()
