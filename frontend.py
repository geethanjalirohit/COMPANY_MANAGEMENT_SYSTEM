import tkinter as tk
from tkinter import *
from tkinter import messagebox
import dbbackend

# Function to validate login
def validate_login():
    # Dummy username and password (replace with your authentication logic)
    username = "admin"
    password = "admin"

    # Get the entered username and password from entry widgets
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Check if username and password match
    if entered_username == username and entered_password == password:
        # If login successful, destroy the login window and open the main window
        login_window.destroy()
        open_main_window()
    else:
        # If login failed, show error message
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to open the main window
def open_main_window():
    class Student:
        def __init__(self,root):
            self.root =root
            self.root.title("Company Database Management System")
            self.root.geometry("1350x750+0+0")
            self.root.config(bg="purple")

            StdID = StringVar()
            Firstname = StringVar()
            Surname = StringVar()
            DoB = StringVar()
            Age = StringVar()
            Gender = StringVar()
            Address = StringVar()
            Mobile = StringVar()
# --------------------------------------FUNCTIONS-------------------------------------------------------------------
            def iExit():
                iExit = tkinter.messagebox.askyesno("Company Database Management Systems", "Confirm if you want to exit")
                if iExit > 0:
                    root.destroy()
                    return
            def clearData():
                self.txtStdID.delete(0, END)
                self.txtfna.delete(0, END)
                self.txtSna.delete(0, END)
                self.txtDoB.delete(0, END)
                self.txtAge.delete(0, END)
                self.txtGender.delete(0, END)
                self.txtAdr.delete(0, END)
                self.txtMobile.delete(0, END)
            def addData():
                if(len(StdID.get())!=0):
                    dbbackend.addStdRec(StdID.get(), Firstname.get(), Surname.get() , DoB.get() ,Age.get(), Gender.get(), Address.get(), Mobile.get())
                    studentlist.delete(0, END)
                    studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

            def DisplayData():
                studentlist.delete(0,END)
                for row in dbbackend.viewData():
                    studentlist.insert(END, row, str(""))

            def StudentRec(event):
                global sd
                searchStd= studentlist.curselection()[0]
                sd = studentlist.get(searchStd)

                self.txtStdID.delete(0, END)
                self.txtStdID.insert(END, sd[1])
                self.txtfna.delete(0, END)
                self.txtfna.insert(END, sd[2])
                self.txtSna.delete(0, END)
                self.txtSna.insert(END, sd[3])
                self.txtDoB.delete(0, END)
                self.txtDoB.insert(END, sd[4])
                self.txtAge.delete(0, END)
                self.txtAge.insert(END, sd[5])
                self.txtGender.delete(0, END)
                self.txtGender.insert(END, sd[6])
                self.txtAdr.delete(0, END)
                self.txtAdr.insert(END, sd[7])
                self.txtMobile.delete(0, END)
                self.txtMobile.insert(END, sd[8])

            def DeleteData():
                if(len(StdID.get())!=0):
                    dbbackend.deleteRec(sd[0])
                    clearData()
                    DisplayData()

            def searchDatabase():
                studentlist.delete(0,END)
                for row in dbbackend.searchData(StdID.get(), Firstname.get(), Surname.get() , DoB.get() ,Age.get(), Gender.get(), Address.get(), Mobile.get()):
                    studentlist.insert(END, row, str(""))

            def update():
                if (len(StdID.get()) != 0):
                    dbbackend.deleteRec(sd[0])
                if (len(StdID.get()) != 0):
                    dbbackend.addStdRec(StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(),Address.get(), Mobile.get())
                    studentlist.delete(0, END)
                    studentlist.insert(END, (StdID.get(), Firstname.get(), Surname.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))
#--------------------------------------Frames-----------------------------------------------------------------------__________________________________________________________
            MainFrame = Frame(self.root, bg="purple")
            MainFrame.grid()
            TitFrame = Frame(MainFrame, bd=2, padx=54,pady=8, bg="Ghost White", relief=RIDGE)
            TitFrame.pack(side=TOP)
            self.lblTit = Label(TitFrame ,font=('times new roman',48,'bold'),text="Company Database Management System",bg="Ghost White")
            self.lblTit.grid()
            ButtonFrame =Frame(MainFrame,bd=2,width=1350,height=70,padx=19,pady=10,bg="Ghost White",relief =RIDGE)
            ButtonFrame.pack(side=BOTTOM)
            DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,bg="purple")
            DataFrame.pack(side=BOTTOM)
            DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20,relief=RIDGE,bg="Ghost White", font=('times new roman',26,'bold'),text="Employee Info\n")
            DataFrameLEFT.pack(side=LEFT)
            DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg="Ghost White",font=('times new roman',20,'bold'),text="Employee Details\n")
            DataFrameRIGHT.pack(side=RIGHT)
#--------------------------------entries-------------------------------------------------------------------------------------------------
            self.lblStdID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Employee ID:",padx=2,pady=2,bg="Ghost White")
            self.lblStdID.grid(row=0,column=0,sticky=W)
            self.txtStdID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=StdID, width=39)
            self.txtStdID.grid(row=0, column=1)

            self.lblfna = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Firstname:", padx=2, pady=2,bg="Ghost White")
            self.lblfna.grid(row=1, column=0, sticky=W)
            self.txtfna = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Firstname, width=39)
            self.txtfna.grid(row=1, column=1)

            self.lblSna = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="LastName:", padx=2, pady=2,bg="Ghost White")
            self.lblSna.grid(row=2, column=0, sticky=W)
            self.txtSna = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Surname, width=39)
            self.txtSna.grid(row=2, column=1)

            self.lblDoB = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Date of Birth:", padx=2, pady=2,bg="Ghost White")
            self.lblDoB.grid(row=3, column=0, sticky=W)
            self.txtDoB = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=DoB, width=39)
            self.txtDoB.grid(row=3, column=1)

            self.lblAge = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Age:", padx=2, pady=2,bg="Ghost White")
            self.lblAge.grid(row=4, column=0, sticky=W)
            self.txtAge = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Age, width=39)
            self.txtAge.grid(row=4, column=1)

            self.lblGender = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Gender:", padx=2, pady=2,bg="Ghost White")
            self.lblGender.grid(row=5, column=0, sticky=W)
            self.txtGender = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Gender, width=39)
            self.txtGender.grid(row=5, column=1)

            self.lblAdr = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Address:", padx=2, pady=2,bg="Ghost White")
            self.lblAdr.grid(row=6, column=0, sticky=W)
            self.txtAdr = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Address, width=39)
            self.txtAdr.grid(row=6, column=1)

            self.lblMobile = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Mobile:", padx=2, pady=2,bg="Ghost White")
            self.lblMobile.grid(row=7, column=0, sticky=W)
            self.txtMobile = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Mobile, width=39)
            self.txtMobile.grid(row=7, column=1)
#--------------------------------------scroll bar and list box----------------------------------------------------------------------------
            scrollbar= Scrollbar(DataFrameRIGHT)
            scrollbar.grid(row=0,column=1,sticky='ns')

            studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'),yscrollcommand=scrollbar.set)
            studentlist.bind('<<ListboxSelect>>',StudentRec)
            studentlist.grid(row=0, column=0, padx=8)
            scrollbar.config(command=studentlist.yview)
#--------------------------------------buttons-----------------------------------------------------------------------------------------------------------
            self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=addData)
            self.btnAddData.grid(row=0, column =0)

            self.btnDisplayData = Button(ButtonFrame, text="Display", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
            self.btnDisplayData.grid(row=0, column=1)

            self.btnClearData = Button(ButtonFrame, text="Clear", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=clearData)
            self.btnClearData.grid(row=0, column=2)

            self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=DeleteData)
            self.btnDeleteData.grid(row=0, column=3)

            self.btnSearchData = Button(ButtonFrame, text="Search", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
            self.btnSearchData.grid(row=0, column=4)

            self.btnUpdateData = Button(ButtonFrame, text="Update", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=update)
            self.btnUpdateData.grid(row=0, column=5)

            self.btnExit = Button(ButtonFrame, text="Exit", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
            self.btnExit.grid(row=0, column=6)

    if __name__=='__main__':
        root = Tk()
        application = Student(root)
        root.mainloop()

# Create the login window
login_window = tk.Tk()
login_window.title("Login")

# Set login window size and background color
login_window.geometry("1350x750+0+0")
login_window.configure(bg="purple")

# Username label and entry
username_label = tk.Label(login_window, text="Username:", font=("Arial", 20))
username_label.pack(pady=10)
username_entry = tk.Entry(login_window, font=("Arial", 20), width=30)
username_entry.pack(pady=10)

# Password label and entry
password_label = tk.Label(login_window, text="Password:", font=("Arial", 20))
password_label.pack(pady=10)
password_entry = tk.Entry(login_window, show="*", font=("Arial", 20), width=30)
password_entry.pack(pady=10)

# Login button
login_button = tk.Button(login_window, text="Login", font=("Arial", 20), padx=20, pady=10, command=validate_login)
login_button.pack(pady=10)

login_window.mainloop()
