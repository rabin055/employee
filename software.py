from tkinter import*
from tkinter import ttk,messagebox
import time
import os

class File_App:
    def __init__(self):
        self.root=Tk()
        self.root.title("Employee Registration System")
        self.root.geometry("1550x830+0+0")

        title=Label(self.root,text="Employee Management System",bd=10, bg="black",fg="white",pady=10,font=("times new roman",35,"bold")).pack(fill=X)
        employee_Frame=Frame(self.root,bd=10, bg="black")
        employee_Frame.place(x=20,y=100,height=480)


        #employee detail ko frame:

        stitle=Label(employee_Frame,text="Employee Details",font=("times new roman",30,"bold"),bg="black",fg="white").grid(row=0,columnspan=4,pady=20)

        #ALL VARS
        self.s_id=StringVar()
        self.contact = StringVar()
        self.name = StringVar()
        self.date = StringVar()
        self.course = StringVar()
        self.address = StringVar()
        self.city = StringVar()
        self.gender = StringVar()
        self.proof = StringVar()
        self.payment=StringVar()



        #EMPLOYEE ID

        lblsid=Label(employee_Frame,text="Employee ID",font=("arial",20,"bold"), bg="black",fg="white").grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txtsid=Entry(employee_Frame,bd=7,textvariable=self.s_id,relief=GROOVE,width=23,font="arial 15 bold").grid(row=1,column=1,padx=10,pady=10)


        #employee ko contact number

        lblcontact=Label(employee_Frame,text="Contact Number",font=("arial",20,"bold"), bg="black",fg="white").grid(row=1,column=2,pady=10,padx=20,sticky="w")
        txtcontact=Entry(employee_Frame,bd=7,textvariable=self.contact,relief=GROOVE,width=23,font="arial 15 bold").grid(row=1,column=3,padx=10,pady=10)


        #employee ko name

        lblname=Label(employee_Frame,text="Name",font=("arial",20,"bold"), bg="black",fg="white").grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txtname=Entry(employee_Frame,bd=7,textvariable=self.name,relief=GROOVE,width=23,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)


        #employee ko DOB

        lblDOB=Label(employee_Frame,text="Date(dd/mm/yyyy)", font=("arial", 20, "bold"), bg="black",fg="white").grid(row=2, column=2, pady=10, padx=20,sticky="w")
        txtDOB=Entry(employee_Frame,bd=7,textvariable=self.date,relief=GROOVE,width=23,font="arial 15 bold").grid(row=2,column=3,padx=10,pady=10)


        #Employee le liyeko course

        lblcourse=Label(employee_Frame,text="Course Taken",font=("arial",20,"bold"), bg="black",fg="white").grid(row=4,column=0,pady=10,padx=20,sticky="w")
        txtcourse=Entry(employee_Frame,bd=7,textvariable=self.course,relief=GROOVE,width=23,font="arial 15 bold").grid(row=4,column=1,padx=10,pady=10)


        #employee ko address

        lbladdress=Label(employee_Frame,text="Address",font=("arial",20,"bold"), bg="black",fg="white").grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txtaddress=Entry(employee_Frame,bd=7,textvariable=self.address,relief=GROOVE,width=23,font="arial 15 bold").grid(row=3,column=1,padx=10,pady=10)


        #employee basne city

        lblcity=Label(employee_Frame,text="City",font=("arial",20,"bold"), bg="black",fg="white").grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txtcity=Entry(employee_Frame,bd=7,textvariable=self.city,relief=GROOVE,width=23,font="arial 15 bold").grid(row=5,column=1,padx=10,pady=10)


        #aba combobox where data is selected and user inpput data saabai hudaina.

        lbldegree=Label(employee_Frame,text="Gender",font=("times new roman",20,"bold"),bg="black",fg="white").grid(row=4,column=2,pady=10,padx=20,sticky="w")
        lblproof=Label(employee_Frame,text="Department",font=("times new roman",20,"bold"),bg="black",fg="white").grid(row=3,column=2,pady=10,padx=20,sticky="w")
        lblpaymentmode=Label(employee_Frame,text="Payment Mode",font=("times new roman",20,"bold"),bg="black",fg="white").grid(row=5,column=2,pady=10,padx=20,sticky="w")

        gendercombo=ttk.Combobox(employee_Frame,textvariable=self.gender,width=30,state="readonly",font="arial 15 bold")
        gendercombo['values']=("Female","Male")
        gendercombo.grid(row=4,column=3,padx=10,pady=10)

        idcombo=ttk.Combobox(employee_Frame,textvariable=self.proof,width=30, state="readonly", font="arial 15 bold")
        idcombo['values'] = ("Account","Management","IT","Administration","Reception",)
        idcombo.grid(row=3, column=3, padx=10, pady=10)

        paymentcombo=ttk.Combobox(employee_Frame,textvariable=self.payment,width=30,state="readonly",font="arial 15 bold")
        paymentcombo['values']=("Cheque","Cash","Credit Card","Internet Banking")
        paymentcombo.grid(row=5,column=3,padx=10,pady=0)



        #========BUTTON KO FRAME===============

        btnFrame=Frame(self.root, bg="black")
        btnFrame.place(x=10,y=680)

        btnAdd=Button(btnFrame,text="Add",font="arial 15 bold",bd=7,width=15,command=self.save_data).grid(row=0,column=0,padx=12,pady=10)
        btndelete=Button(btnFrame,text="Delete",font="arial 15 bold",bd=7,width=15,command=self.delete).grid(row=0,column=1,padx=12,pady=10)
        btnclear=Button(btnFrame,text="Clear",font="arial 15 bold",bd=7,width=15,command=self.clear).grid(row=0,column=2,padx=12,pady=10)
        btnlog=Button(btnFrame,text="Logout",font="arial 15 bold",bd=7,width=15,command=self.logout).grid(row=0,column=3,padx=12,pady=10)
        btnexit=Button(btnFrame,text="Exit",font="arial 15 bold",bd=7,width=15,command=self.exit_fun).grid(row=0,column=4,padx=12,pady=10)


#file frame:
        File_Frame=Frame(self.root, bg="black")
        File_Frame.place(x=1250,y=100,width=270,height=670)

#ALL files lekheko banako:

        ftitle=Label(File_Frame,text="All Files",font="arial 20 bold", bg="black",fg="white").pack(side=TOP,fill=X)

        scroll_y=Scrollbar(File_Frame,orient=VERTICAL)
        self.file_list=Listbox(File_Frame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()
        self.root.mainloop()


#saving data:
    def save_data(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error!","Employee ID is must!")
        else:
            f=os.listdir("file/")
            if len(f) > 0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present = "yes"
                if present == "yes":
                    ask = messagebox.askyesno("Update", "File already present still \nDo you want to update?")
                    if ask > 0:
                        self.save_file()
                        messagebox.showinfo("Update","Record has been updated successfully")
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo("Saved", "Record has been saved successfully")
                    self.show_files()

            else:
                self.save_file()
                messagebox.showinfo("Saved", "Record has been saved successfully")
                self.show_files()

#file save gane in text:
    def save_file(self):
        f = open("file/" + str(self.s_id.get()), "w")
        f.write(
            str(self.s_id.get()) + "," +
            str(self.name.get()) + "," +
            str(self.course.get()) + "," +
            str(self.city.get()) + "," +
            str(self.date.get()) + "," +
            str(self.address.get()) + "," +
            str(self.contact.get()) + "," +
            str(self.gender.get()) + "," +
            str(self.proof.get()) + "," +
            str(self.payment.get()) + ","
            )
        f.close()


#save vayeko data dekhaune and tyo saved data lai pull garne along with edit garne::
    def show_files(self):
        files=os.listdir("file/")
        self.file_list.delete(0, END)
        if len(files)>0:
            for i in files:
                 self.file_list.insert(END,i)
    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        # print(self.file_list.get(get_cursor))
        f1=open("file/"+self.file_list.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(",")

        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.city.set(value[3])
        self.date.set(value[4])
        self.address.set(value[5])
        self.contact.set(value[6])
        self.gender.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])

    def clear(self):
        self.s_id.set("")
        self.contact.set("")
        self.name.set("")
        self.date.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.gender.set("")
        self.proof.set("")
        self.payment.set("")

    def delete(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error!","Student ID is required!")
        else:
            f=os.listdir("file/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]== self.s_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Delete","Do you really want to delete?")
                    if ask>0:
                        os.remove("file/"+self.s_id.get())
                        messagebox.showinfo("Sucess","Deleted Successfully")
                        self.show_files()
                else:
                    messagebox.showerror("Error","File not found")

    def exit_fun(self):
        ask = messagebox.askyesno("Exit", "Are you sure?")
        if ask > 0:
            self.root.destroy()

    def logout(self):
        ask=messagebox.askyesno("Logout", "Do you want to logout?")
        if ask>0:
            self.root.destroy()
            import login1