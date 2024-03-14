from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import pyshorteners
import pyperclip

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\background.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\Img1.jpg")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="darkblue",bg="white")
        get_str.place(x=95,y=100)

        # Label for username
        username_lbl=Label(frame,text="UserName",font=("times new roman",15,"bold"),fg="darkblue",bg="white")
        username_lbl.place(x=130,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        # Label for password
        password_lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="darkblue",bg="white")
        password_lbl.place(x=130,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=260,width=270)

        # Icon Image
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\Img2.jpg")
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=700,y=328,width=25,height=25)

        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\Img3.png")
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=700,y=397,width=25,height=25)

        # Login Button

        loginbtn=Button(frame,command=self.login,text="LOGIN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=40)

        # Register Button

        registerbtn=Button(frame,text="New User Register",command=self.register_win,font=("times new roman",10,"bold"),borderwidth=0,fg="red",bg="white",activeforeground="white",activebackground="pink",cursor="hand2")
        registerbtn.place(x=90,y=350,width=160)

       
    
    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All the fields are required")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1206",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register1 where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password")
            else:
                open_main=messagebox.askyesno("YES/NO","Admin only")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app=Url_Shortner(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    #================================Reset Password Function======================
    



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")

        #=================Variables=================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_secQ=StringVar()
        self.var_secA=StringVar()
        self.var_pass=StringVar()
        self.var_Cpass=StringVar()
        self.var_check=IntVar()


        #==================background image================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\reg_bg.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)

        #==================right image================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\reg_form.jpeg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=550,y=150,height=450,width=750)

        #==================Main Frame=================
        frame=Frame(self.root,bg="lightblue")
        frame.place(x=250,y=150,width=750,height=450)

        reg_lbl=Label(frame,text=" NEW USER REGISTERATION",font=("times new roman",25,"bold"),fg="darkblue",bg="lightblue")
        reg_lbl.place(x=150,y=10)


        #=================Labels and Entry===============
        fname=Label(frame,text="First Name:",font=("times new roman",15,"bold"),bg="lightblue")
        fname.place(x=50,y=80)
        #======First Name Entry-Field========
        fname_en=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_en.place(x=170,y=80,width=150)

        lname=Label(frame,text="Last Name:",font=("times new roman",15,"bold"),bg="lightblue")
        lname.place(x=400,y=80)
        #======Last Name Entry-Field========
        lname_en=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_lname)
        lname_en.place(x=520,y=80,width=150)

        contact=Label(frame,text="Contact No:",font=("times new roman",15,"bold"),bg="lightblue")
        contact.place(x=50,y=150)
        #======Contact No Entry-Field========
        contact_en=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_contact)
        contact_en.place(x=170,y=150,width=150)

        email=Label(frame,text="Email ID :",font=("times new roman",15,"bold"),bg="lightblue")
        email.place(x=400,y=150)
        #======Email Entry-Field========
        email_en=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_email)
        email_en.place(x=520,y=150,width=200)

        secQ=Label(frame,text="Security Q:",font=("times new roman",15,"bold"),bg="lightblue")
        secQ.place(x=50,y=220)
        #======Security Ques Choosing Field========
        self.combo_secQ=ttk.Combobox(frame,text="Select Security Question",textvariable=self.var_secQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_secQ["values"]=("Select","Your Birth Place?","Your Mother's Name?","Your Father's Name?")
        self.combo_secQ.place(x=170,y=220,width=150)
        self.combo_secQ.current(0)

        secA=Label(frame,text="Security A:",font=("times new roman",15,"bold"),bg="lightblue")
        secA.place(x=400,y=220)
        #======Security Ans Entry-Field========
        secA_en=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_secA)
        secA_en.place(x=520,y=220,width=150)

        password=Label(frame,text="Password :",font=("times new roman",15,"bold"),bg="lightblue")
        password.place(x=50,y=290)
        #======Entry-Field========
        password_en=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_pass)
        password_en.place(x=170,y=290,width=150)

        c_pass=Label(frame,text="C-Password :",font=("times new roman",15,"bold"),bg="lightblue")
        c_pass.place(x=400,y=290)
        #======Entry-Field========
        c_pass_en=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.var_Cpass)
        c_pass_en.place(x=520,y=290,width=150)


        #==============Check Button================
        checkbtn=Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.var_check,font=("times new roman",12,"bold"),bg="lightblue",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=330)

        #===============Registeration Button=============
        img=Image.open(r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\register_btn.jpeg")
        img=img.resize((200,60),Image.LANCZOS)
        self.reg_btn=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.reg_btn,command=self.reg_data,borderwidth=0,cursor="hand2")
        b1.place(x=150,y=370,width=200)

        #================Login Button==================
        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\login.jpeg")
        img1=img1.resize((200,60),Image.LANCZOS)
        self.log_btn=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.log_btn,borderwidth=0,cursor="hand2")
        b1.place(x=450,y=365,width=200)

    #===================Register Data Function=================
    def reg_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_secQ.get()=="Select":
                messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_Cpass.get():
            messagebox.showerror("Error","Password & Confirm Password doesn't Match.")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree the Terms and Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1206",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register1 where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exist, Please try another email.")
            else:
                my_cursor.execute("insert into register1 values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_secQ.get(),
                                                                                        self.var_secA.get(),
                                                                                        self.var_pass.get()    
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","User Successfully Registered")




class Url_Shortner:
    def __init__(self,root):
        self.root=root
        self.root.title("URL-SHORTErNER")
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
        b1=Button(frame,text="GENERATE & COPY",font=("times new roman",12,"bold"),command=lambda:(urlshortner(),copyurl()),cursor="hand2",bg="darkblue",fg="red")
        b1.place(x=80,y=170,width=200)

        url_sh=Label(frame,text="Short URL LINK :",font=("times new roman",15,"bold"),bg="darkblue",fg="lightblue")
        url_sh.place(x=35,y=230)
        #======Short URL Entry-Field========
        sh_en=ttk.Entry(frame,font=("times new roman",15,"bold"),textvariable=self.url_add)
        sh_en.place(x=35,y=270,width=280)






if __name__ == "__main__":
    main()
