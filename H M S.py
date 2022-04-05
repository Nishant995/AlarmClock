from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime


def main():
    root = Tk()
    app = Window1(root)


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management system")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        #
        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text='Pharmacy Management system', font=('arial', 50, 'bold'), bd=25,
                                )
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=15)

        self.Loginframe1 = Frame(self.frame, width=1010, height=300, bd=20, relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=20, relief='ridge')
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3 = Frame(self.frame, width=1010, height=200, bd=20, relief='ridge')
        self.Loginframe3.grid(row=3, column=0, pady=2)

        # **************************************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*****************************************
        # Username
        self.lblUsername = Label(self.Loginframe1, text='Username', font=('arial', 15, 'bold'), bd=18, )
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.Loginframe1, font=('arial', 15, 'bold'), bd=20, textvariable=self.Username, )
        self.txtUsername.grid(row=0, column=1)
        #  Password

        self.lblPassword = Label(self.Loginframe1, text='Password', font=('arial', 15, 'bold'), bd=18, )

        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.Loginframe1, font=('arial', 15, 'bold'), bd=20, textvariable=self.Password, )

        self.txtPassword.grid(row=1, column=1, padx=85)

        # **************************************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*****************************************

        self.btnLogin = Button(self.Loginframe2, text="Login", width=14, font=('arial', 16, 'bold'),
                               command=self.Loginsystem)
        self.btnLogin.grid(row=0, column=0)

        self.btnReset = Button(self.Loginframe2, text="Reset", width=14, font=('arial', 16, 'bold'),
                               command=self.Hospital_Window)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.Loginframe2, text="Exit", width=14, font=('arial', 16, 'bold'),
                              command=self.Registration_Window)
        self.btnExit.grid(row=0, column=2)
        # **************************************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*****************************************

        self.btnRegistration = Button(self.Loginframe3, text="Registration Systems", state=DISABLED,
                                      font=('arial', 18, 'bold'), command=self.Registration_Window)
        self.btnRegistration.grid(row=0, column=0, pady=10, padx=25)

        self.btnHospital = Button(self.Loginframe3, text="Hospital Management Systems", state=DISABLED,
                                  font=('arial', 18, 'bold'), command=self.Hospital_Window)
        self.btnHospital.grid(row=0, column=1, pady=10, padx=24)

        # **************************************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*****************************************

    def Loginsystem(self):
        user = (self.Username.get())
        Pas = (self.Password.get())

        if (user == str(1234)) and (Pas == str(2345)):
            self.btnRegistration.config(state=NORMAL)
            self.btnHospital.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System", "you have entered an invalid login details")
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

        # **************************************************$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*****************************************

    def Registration_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Hospital_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Registration Systems")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management system")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == '__main__':
    main()
