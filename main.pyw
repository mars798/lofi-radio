import tkinter as tk
from PIL import Image, ImageTk
import vlc
import os

import sys

# For py2exe
# script_path = os.path.abspath(sys.executable)

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

media = vlc.Media("https://free.rcast.net/2628")

player = vlc.MediaPlayer()
player.set_media(media)


root = tk.Tk()
root.iconbitmap(os.path.join(script_dir, "assets", "favicon.ico"))
root.title("Lofi Radio")
root.geometry("332x498")
root.resizable(False, False)

gif_path = os.path.join(script_dir, "assets", "giphy.gif")
gif_image = Image.open(gif_path)
gif_frames = []
for frame in range(gif_image.n_frames):
    gif_image.seek(frame)
    gif_frames.append(ImageTk.PhotoImage(gif_image.copy()))

image_path = os.path.join(script_dir, "assets", "button.png")
image = Image.open(image_path)
cropped_image = image.crop((17, 1, 30 + 1, 14 + 1))
zoomed_image = cropped_image.resize((80, 80), resample=Image.NEAREST)
photo = ImageTk.PhotoImage(zoomed_image)

cropped_image2 = image.crop((33, 81, 46 + 1, 94 + 1))
zoomed_image2 = cropped_image2.resize((80, 80), resample=Image.NEAREST)
photo2 = ImageTk.PhotoImage(zoomed_image2)

canvas = tk.Canvas(root, width=332, height=498)
canvas.pack()

canvas.create_image(0, 0, anchor="nw", image=gif_frames[0])

button = tk.Button(canvas, text="", bd=0, highlightthickness=0)

button.config(image=photo)
button.place(x=130, y=390, anchor="nw")


def on_button_click(event):
    print("Изображение было нажато!")
    change_image()


currentImg = 1


def change_image():
    global currentImg
    if currentImg == 1:
        button.configure(image=photo2)
        currentImg = 2
        player.play()
    else:
        button.configure(image=photo)
        currentImg = 1
        player.stop()


button.bind("<Button-1>", on_button_click)


def update_gif(frame=0):
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=gif_frames[frame])
    frame = (frame + 1) % len(gif_frames)
    root.after(80, update_gif, frame)


update_gif()

root.mainloop()
