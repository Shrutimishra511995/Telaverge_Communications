from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import pyshorteners
import pyperclip

class Url_Shortner:
    def __init__(self,root):
        self.root=root
        self.root.title("URL SHORTNER")
        self.root.geometry("1550x800+0+0")

        #==================Variables==================
        self.url=StringVar()
        self.url_add=StringVar()

        def urlshortner():
            url_input = self.url.get()
            url_short= pyshorteners.Shortener().tinyurl.short(url_input)
            self.url_add.set(url_short)
        
        def copyurl():
            url_short = self.url_add.get()
            pyperclip.copy(url_short)
        
        #==================background image================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\url_bg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)

                #==================right image================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\url_link.jpeg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=530,y=160,height=470,width=450)

        #==================Main Frame=================
        frame=Frame(self.root,bg="darkblue")
        frame.place(x=580,y=200,width=350,height=400)

        url_lbl=Label(frame,text="URL SHORTNER",font=("times new roman",25,"bold"),fg="lightblue",bg="darkblue")
        url_lbl.place(x=45,y=10)

        #=================Labels and Entry===============
        url_data=Label(frame,text="Enter your URL LINK :",font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        url_data.place(x=35,y=80)
        #======URL Entry-Field========
        url_en=ttk.Entry(frame,textvariable=self.url,font=("times new roman",15,"bold"))
        url_en.place(x=35,y=120,width=280)
        
        #===============Generate Button=============
        b1=Button(frame,text="GENERATE",font=("times new roman",15,"bold"),command=urlshortner,cursor="hand2",bg="darkblue",fg="red")
        b1.place(x=80,y=170,width=200)

        url_sh=Label(frame,text="Short URL LINK :",font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        url_sh.place(x=35,y=230)
        #======Short URL Entry-Field========
        sh_en=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.url_add)
        sh_en.place(x=35,y=270,width=280)






if __name__ == "__main__":
    root=Tk()
    app=Url_Shortner(root)
    root.mainloop()
