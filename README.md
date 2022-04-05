# AlarmClock                         HOSPITAL MANAGEMENT SYSTEM
 from tkinter import *
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1450x820+0+0")
        self.root.configure(background='powderblue')

        cmbNameTablet = StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssueDate = StringVar()
        ExpDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        FurtherInformation = StringVar()
        Storage = StringVar()
        DrivingUsingMachine = StringVar()
        UseMedication = StringVar()
        PatientId = StringVar()
        PatientNHSNo = StringVar()
        PatientName = StringVar()
        DateOfBirth = StringVar()
        Address = StringVar()
        Prescription = StringVar()

        # *************************function declaration*************************
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hospital Management System", "Confrim if you want to exit")
            if iExit > 0:
                root.destroy()

            return

        def iPrescription():
            return

        def iPrescriptionData():
            self.txtFrameDetails.insert(END,
                                        "\t" + cmbNameTablet.get() + "\t" + Ref.get() + "\t" + Dose.get() + "\t" + NumberTablets.get() + "\t" + Lot.get() + "\t" + IssueDate.get() + "\t" + ExpDate.get() + "\t" + DailyDose.get() + "\t" + Storage.get() + "\t" + PatientNHSNo.get() + "\t" + PatientName.get() + "\t" + PatientId.get() + "\t" + DateOfBirth.get() + "\t" + Address.get() + "\n")

            return

        def iDelete():
            cmbNameTablet.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            FurtherInformation.set("")
            Storage.set("")
            DrivingUsingMachine.set("")
            UseMedication.set("")
            PatientId.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateOfBirth.set("")
            Address.set("")
            self.txtPrescription.delete("1.0", END)
            self.txtFrameDetails.delete("1.0", END)
            return

        def iReset():
            cmbNameTablet.set("")
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            FurtherInformation.set("")
            Storage.set("")
            DrivingUsingMachine.set("")
            UseMedication.set("")
            PatientId.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateOfBirth.set("")
            Address.set("")
            self.txtPrescription.delete("1.0", END)
            self.txtFrameDetails.delete("1.0", END)

            return

        # **************************************************

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=18, width=1260, padx=18, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 35, 'bold'), text="\tHospital Management System\t", padx=4)
        self.lblTitle.grid()
        #    [ Height ]

        FrameDetails = Frame(MainFrame, bd=20, width=1300, height=100, padx=18, relief=RIDGE)
        FrameDetails.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=20, width=1310, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1310, height=300, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = Frame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE, )

        DataFrameLEFT.pack(side=LEFT)
        ######
        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=438, height=280, padx=20, relief=RIDGE,
                                    font=('arial', 12, 'bold'), text="  Prescription")

        DataFrameRIGHT.pack(side=RIGHT)
        # ********************************DataFrameLEFT**************************************************

        self.lblNameTablet = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text=" Name of Tablets:", padx=2, pady=2)
        self.lblNameTablet.grid(row=0, column=0, sticky=W)

        self.cboNameTablet = ttk.Combobox(DataFrameLEFT, textvariable=cmbNameTablet, state='readonly',
                                          font=('arial', 12, 'bold'), width=20)
        self.cboNameTablet['value'] = ('', 'Ibuprofen', 'co-codamol', 'Paracetamol', 'Fulcaxol')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)

        self.lblFurtherInfo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Further Information:", padx=2,
                                    pady=2)
        self.lblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFurtherInfo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=FurtherInformation,
                                    width=20)
        self.txtFurtherInfo.grid(row=0, column=3)

        self.lblRefNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Refrence No:", padx=2, pady=2)
        self.lblRefNo.grid(row=1, column=0, sticky=W)
        self.txtRefNo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ref, width=20)
        self.txtRefNo.grid(row=1, column=1)

        self.lblStorage = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Storage:", padx=2, pady=2)
        self.lblStorage.grid(row=1, column=2, sticky=W)
        self.txtStorage = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Storage, width=20)
        self.txtStorage.grid(row=1, column=3)

        self.lblDose = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Dose:", padx=2, pady=2)
        self.lblDose.grid(row=2, column=0, sticky=W)
        self.txtDose = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Dose, width=20)
        self.txtDose.grid(row=2, column=1)

        self.lblDrivingUsingMachine = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="DrivingUsingMachine:",
                                            padx=2, pady=4)
        self.lblDrivingUsingMachine.grid(row=2, column=2, sticky=W)
        self.txtDrivingUsingMachine = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DrivingUsingMachine,
                                            width=20)
        self.txtDrivingUsingMachine.grid(row=2, column=3)

        self.lblNumberTablets = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="NumberTablets:", padx=2, pady=2)
        self.lblNumberTablets.grid(row=3, column=0, sticky=W)
        self.txtNumberTablets = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=NumberTablets, width=20)
        self.txtNumberTablets.grid(row=3, column=1)

        self.lblUseMedication = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="UseMedication:", padx=2, pady=2)
        self.lblUseMedication.grid(row=3, column=2, sticky=W)
        self.txtUseMedication = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=UseMedication, width=20)
        self.txtUseMedication.grid(row=3, column=3)

        self.lblLot = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Lot:", padx=2, pady=2)
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Lot, width=20)
        self.txtLot.grid(row=4, column=1)

        self.lblPatientId = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Patient Id ", padx=2, pady=2)
        self.lblPatientId.grid(row=4, column=2, sticky=W)
        self.txtPatientId = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PatientId, width=20)
        self.txtPatientId.grid(row=4, column=3)

        self.lblPatientName = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="PatientName ", padx=2, pady=2)
        self.lblPatientName.grid(row=5, column=0, sticky=W)
        self.txtPatientName = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PatientName, width=20)
        self.txtPatientName.grid(row=5, column=1)

        self.lblAddress = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Address  ", padx=2, pady=4)
        self.lblAddress.grid(row=6, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Address, width=20)
        self.txtAddress.grid(row=6, column=1)

        self.lblPatientNHSNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="PatientNHSNo", padx=2, pady=4)
        self.lblPatientNHSNo.grid(row=5, column=2, sticky=W)
        self.txtPatientNHSNo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=PatientNHSNo, width=20)
        self.txtPatientNHSNo.grid(row=5, column=3)

        self.lblDateOfBirth = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="DateOfBirth", padx=2, pady=2)
        self.lblDateOfBirth.grid(row=6, column=2, sticky=W)
        self.txtDateOfBirth = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DateOfBirth, width=20)
        self.txtDateOfBirth.grid(row=6, column=3)

        self.lblIssueDate = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="IssueDate", padx=2, pady=2)
        self.lblIssueDate.grid(row=7, column=0, sticky=W)
        self.txtIssueDate = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=IssueDate, width=20)
        self.txtIssueDate.grid(row=7, column=1)

        self.lblExpDate = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="ExpDate", padx=2, pady=4)
        self.lblExpDate.grid(row=7, column=2, sticky=W)
        self.txtExpDate = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=ExpDate, width=20)
        self.txtExpDate.grid(row=7, column=3)

        self.lblSideEffects = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="SideEffects", padx=2, pady=2)
        self.lblSideEffects.grid(row=8, column=0, sticky=W)
        self.txtSideEffects = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=SideEffects, width=20)
        self.txtSideEffects.grid(row=8, column=1)

        # ********************************DataFrameLEFT**************************************

        self.txtPrescription = Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width=41, height=12, padx=3, pady=10)
        self.txtPrescription.grid(row=0, column=0)
        # *******************************************[Button]*******
        self.btnPrescription = Button(ButtonFrame, text='Prescription', font=('arial', 13, 'bold'), width=23, bd=4,
                                      command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)
        self.btnPrescriptionData = Button(ButtonFrame, text='prescription Data', font=('arial', 13, 'bold'), width=22,
                                          bd=4,
                                          command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=1)
        self.btnDelete = Button(ButtonFrame, text='Delete', font=('arial', 13, 'bold'), width=22, bd=4,
                                command=iDelete)
        self.btnDelete.grid(row=0, column=2)
        self.btnReset = Button(ButtonFrame, text='Reset', font=('arial', 13, 'bold'), width=23, bd=4,
                               command=iReset)
        self.btnReset.grid(row=0, column=3)
        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 13, 'bold'), width=22, bd=4,
                              command=iExit)
        self.btnExit.grid(row=0, column=4)

        # **************************************************

        self.lblLabel = Label(FrameDetails, font=('arial', 9, 'bold'),
                              text="Name of Tablets\tRef No.\t Dose\t No.of Tablets\t Lot\t Issued Date\t Exp.Date\tDaily Dose\tStorage Adv.\tNHS Number\t Patient Name\t DOB\t Address", )
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetails = Text(FrameDetails, font=('arial', 12, 'bold'), width=132, height=3, padx=1, pady=1)
        self.txtFrameDetails.grid(row=1, column=0)


if __name__ == '__main__':
    root = Tk()
    application = Hospital(root)
    root.mainloop()





