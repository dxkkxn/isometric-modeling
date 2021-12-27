import tkinter as tk
from PIL import Image, ImageTk

if __name__ == "__main__" :
    root = tk.Tk()
    root.title("plan")
    photo_imgs = tk.PhotoImage("../img/blue.gif")
    img = Image.open("../img/blue.jpg")
    tkimage = ImageTk.PhotoImage(img)
    button = tk.Button(root, image=tkimage, width=100, height=100).pack()
#    button.image = photo_imgs

    label= tk.Label(root, image=photo_imgs)
    label.image = photo_imgs
    label.pack(side="top")

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(side="top", expand=True, fill="both")
    root.mainloop()
