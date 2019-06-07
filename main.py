import tkinter as tk
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Sign in"
        self.hi_there["command"] = self.sign_in
        self.hi_there.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        image = Image.open("image.jpg")
        photo = ImageTk.PhotoImage(image,size='750')

        label = tk.Label(image=photo,width=750)
        label.image = photo # keep a reference!
        label.pack()

    def sign_in(self):
        print("Initiating sign-in")

root = tk.Tk()
root.geometry('800x480')
app = Application(master=root)
app.mainloop()
