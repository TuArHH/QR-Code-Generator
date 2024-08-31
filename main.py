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
