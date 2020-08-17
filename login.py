from tkinter import*
from tkinter import messagebox


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Registration System")
        self.root.geometry("1540x750+0+0")



        F1=Frame(self.root,bg="black")
        F1.place(x=550,y=150,height=360)

        self.user=StringVar()
        self.password=StringVar()

        title=Label(F1,text="Login System",font=("times new roman",31,"bold"),bg="black",fg="white").grid(row=0,columnspan=2,pady=20)
        lblusername=Label(F1,text="Username",font=("times new roman",26,"bold"),bg="black",fg="white").grid(row=1,column=0,pady=10,padx=10)

        txtuer=Entry(F1,textvariable=self.user,width=25,font=("arial", 15," bold")).grid(row=1,column=1,padx=10,pady=10)

        lblpass=Label(F1,text="Password",font=("times new roman",26,"bold"),bg="black",fg="white").grid(row=2,column=0,pady=10,padx=10)

        txtpass=Entry(F1,show="*",textvariable=self.password,width=25,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)

        btnlogin=Button(F1,text="Login",font="arial 15 bold",bd=7,width=10,command=self.log_fun).place(x=10,y=270)
        btnreser=Button(F1,text="Reset",font="arial 15 bold",bd=7,width=10,command=self.reset).place(x=169,y=270)
        btnexit=Button(F1,text="Exit",font="arial 15 bold",bd=7,width=10,command=self.exit_fun).place(x=329,y=270)
    def log_fun(self):
        if self.user.get()=="abcd" and self.password.get()=="1234":
            self.root.destroy()
            import software
            software.File_App()
        else:
            messagebox.showerror("Error","invalid username or password")
    def reset(self):
        self.user.set("")
        self.password.set("")

    def exit_fun(self):
        option=messagebox.askyesno("Exit","Do you really want to exit?")
        if option:
            self.root.destroy()
        else:
            return



root=Tk()
ob=Login(root)
root.mainloop()