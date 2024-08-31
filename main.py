from tkinter import *
from datetime import datetime
from PIL import ImageTk, Image

root = Tk()

# current date for the footer
now = datetime.now()
current_year = now.year


# change the default tk logo to my own
icon = Image.open("favicon.ico")  # replace here your own image
icon = ImageTk.PhotoImage(icon)
root.iconphoto(False, icon)

root.title("QR Code Generator")


canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg="blue", font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link name")
link_label = Label(root, text="Link URL")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

button = Button(text="Generate QR code", command=generate_qrcode)
canvas.create_window(200, 230, window=button)
