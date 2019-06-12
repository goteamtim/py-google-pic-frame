import tkinter as tk
from PIL import Image, ImageTk
import google_photos as google
import credentials as creds
import webbrowser
import google_auth

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        self.c = creds.credentials()
        api_key = str(self.c.client_id)
        self.gp = google.google_photos(api_key=api_key)

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Sign in"
        self.hi_there["command"] = self.sign_in
        self.hi_there.pack(side="left")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        new_window_button = tk.Button(self,text="New Window",command=self.sign_in)
        new_window_button.pack()

        image = Image.open("image.jpg")
        photo = ImageTk.PhotoImage(image,size='750')

        label = tk.Label(image=photo,width=750)
        label.image = photo # keep a reference!
        label.pack()

    def sign_in(self):
        auth = google_auth.google_auth()
        auth.login()
        webbrowser.open_new('https://www.google.com')
        print("Initiating sign-in")

    def create_window(self):
        window = tk.Toplevel(self)

        #json_credential = self.gp.get_token()
        #json_credential = google.google_photos.get_token(self)
        json_credential = 'testing'
        
        label = tk.Label(window, text=json_credential,fg="red")
        label.pack()

root = tk.Tk()
root.geometry('800x480')
app = Application(master=root)
app.mainloop()
