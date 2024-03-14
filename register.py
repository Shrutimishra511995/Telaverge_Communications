from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1500x800+0+0")

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
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Telaverage Project\images\reg_bg.jpeg")
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

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()