from customtkinter import *

app = CTk()
app.geometry("300x400")

search = CTkEntry(app, font=("Helvetica", 18), 
                  placeholder_text='SEARCH', width=250, height=20)
search.pack(pady=10, anchor='w', padx=10)

app.mainloop()