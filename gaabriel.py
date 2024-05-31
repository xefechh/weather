from customtkinter import *
from PIL import Image
import requests

api = '58ece528195235057712455ac755125d'
app = CTk()
app.geometry("300x400")

def search_click():
  city = search.get()
  

frame = CTkFrame(app)
frame.pack(pady=10, anchor='w', padx=10)

search = CTkEntry(frame, font=("Helvetica", 18), placeholder_text='SEARCH', width=250, height=30)
search.grid(row=0, column=0)

search_icon = CTkImage(light_image=Image.open("search_icon.png"), dark_image=Image.open("search_icon.png"))

search_button = CTkButton(frame, text='', image=search_icon, width=30, height=30, command=search_click, corner_radius=0)
search_button.grid(row=0, column=1)

app.mainloop()
