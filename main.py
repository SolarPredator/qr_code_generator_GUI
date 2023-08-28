import customtkinter
import tkinter
from PIL import Image, ImageTk
import qrcode
import os
from pathlib import Path
import random
import requests
import shutil

url = r"https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" #url for downloading githyb logo
github_logo ="git_img.png"

res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(github_logo,'wb') as f:
        shutil.copyfileobj(res.raw, f)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")

canvas = customtkinter.CTkCanvas(root, width=250, height=250)
canvas.pack()



image_path = r"git_img"
img = Image.open(image_path)
img = img.resize((250, 250))  # Resize the image to fit the canvas
png = ImageTk.PhotoImage(img)

canvas.create_image(0, 0, image=png, anchor="nw")





def rand_number_gen():
  rand_number = random.randrange(1000,9999)
  return rand_number

def qr_code_generate():

  download_path = str(Path.home()/ "Downloads")
  os.chdir(download_path)
  qr_code = qrcode.make(entry1.get())
  number = rand_number_gen()
  files = os.listdir()
  number = str(number)


  for item in files:        #check if theres dupe numbers

      if item.endswith(number):
          qr_code_generate()
  name = f"qr_code_{number}.png"
  qr_code.save(name)
  abselute_path = os.getcwd()
  to_send = os.path.join(abselute_path,name)
  update_photo(to_send)


def update_photo(new_photo):
    image_path = new_photo
    img = Image.open(image_path)
    img = img.resize((250, 250))  # Resize the image to fit the canvas
    png = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, image=png, anchor="nw")
    canvas.pack()
    root.mainloop()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=50, padx=10, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="QR Code Generator")
label.pack(pady=10, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="content of QR")
entry1.pack(pady=10, padx=10)

button1 = customtkinter.CTkButton(master=frame, text="generate", command=qr_code_generate)
button1.pack(side="bottom",pady=10, padx=10)

root.mainloop()