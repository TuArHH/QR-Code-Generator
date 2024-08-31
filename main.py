from tkinter import *
from datetime import datetime
import qrcode
from PIL import ImageTk, Image
import os

root = Tk()

# current date for the footer
now = datetime.now()
current_year = now.year

# change the default tk logo to a custom icon
icon = Image.open("favicon/favicon.ico")  # Ensure this path is correct
icon = ImageTk.PhotoImage(icon)
root.iconphoto(False, icon)

root.title("QR Code Generator")


def generate_qrcode():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Ensure the directory exists
    if not os.path.exists("img"):
        os.makedirs("img")

    img_path = os.path.join("img", file_name)
    img.save(img_path)

    # Display the QR code image
    image = ImageTk.PhotoImage(Image.open(img_path))
    image_label = Label(root, image=image)
    image_label.image = image  # Keep a reference to avoid garbage collection
    canvas.create_window(200, 450, window=image_label)


canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg="green", font=("Arial", 30))
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

# Footer
footer_label = Label(
    root, text=f"Created by @Tugrul Arslan\t{current_year}", font=("Arial", 10)
)
footer_label.pack(side=BOTTOM, pady=10)

root.mainloop()
