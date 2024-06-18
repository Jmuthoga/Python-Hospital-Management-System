import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Hospital():
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        # We will define full screen(maximum-screen)
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

        # ------------valiable decription------------#
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmdTabletNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tables = StringVar()
        lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientId = StringVar()
        PatientNHNumber = StringVar()
        Patientname = StringVar()
        Dateofbirth = StringVar()
        patientAddress = StringVar()
        Prescription = StringVar()
        NHIFnumber = StringVar()
        DailyDose = StringVar()
        Medication = StringVar()

        # ----------------Functions------------------#
        def Exitbtn():
            Exitbtn = tkinter.messagebox.askyesno(
                "Hospital Management System", "Are you sure you want to exit ?")
            if Exitbtn > 0:
                root.destroy()
                return

        def Deletefunc():
            Ref.set("")
            cmdTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tables.set("")
            lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            PatientId.set("")
            PatientNHNumber.set("")
            Patientname.set("")
            Dateofbirth.set("")
            patientAddress.set("")
            Prescription.set("")
            NHIFnumber.set("")
            DailyDose.set("")
            Medication.set("")
            TextPrescription.delete("1.0", END)
            TextPrescriptionData.delete("1.0", END)
            return

        def Resetfunc():
            Ref.set("")
            cmdTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tables.set("")
            lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            PatientId.set("")
            PatientNHNumber.set("")
            Patientname.set("")
            Dateofbirth.set("")
            patientAddress.set("")
            Prescription.set("")
            NHIFnumber.set("")
            DailyDose.set("")
            Medication.set("")
            TextPrescription.delete("1.0", END)
            return

        def Reference_numfunc():
            ranumber = random.randint(1000, 99999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def Prescriptiondata():
            Reference_numfunc()
            TextPrescriptionData.insert(END, Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"+PatientId.get()
                                        + "\t\t"+Dateofbirth.get()+"\t\t"+NHIFnumber.get()+"\t\t"+cmdTabletNames.get()+"\t"+Number_of_Tables.get()+"\t\t" +
                                        IssuedDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get() +
                                        "\t\t"+StorageAdvice.get()+"\t\t"+PatientId.get()+"\n")

        def Prescriptionfunc():
            Reference_numfunc()
            TextPrescription.insert(
                END, "Patient ID:  \t\t"+PatientId.get()+"\n")
            TextPrescription.insert(
                END, "Patient Name:  \t\t"+Patientname.get()+"\n")
            TextPrescription.insert(
                END, "Tablet:  \t\t"+cmdTabletNames.get()+"\n")
            TextPrescription.insert(
                END, "Number of Tablets:  \t\t"+Number_of_Tables.get()+"\n")
            TextPrescription.insert(
                END, "Daily Dose:  \t\t"+DailyDose.get()+"\n")
            TextPrescription.insert(
                END, "Issued Date:  \t\t"+IssuedDate.get()+"\n")
            TextPrescription.insert(
                END, "Expiry Date:  \t\t"+ExpiryDate.get()+"\n")
            TextPrescription.insert(
                END, "Storage:  \t\t"+StorageAdvice.get()+"\n")
            TextPrescription.insert(
                END, "More Information:  \t\t"+MoreInformation.get()+"\n")

        # ----------------Title----------------------#
        title = Label(self.root, text="Hospital Management System", font=(
            "monotype corsiva", 30, "bold"), bd=5, relief="groove", bg="#2ab8b8", fg="#000000")
        title.pack(side=TOP, fill=X)

        # ----------------FRAME-----------------------#
        Management_Frame = Frame(
            self.root, width=1600, height=400, bd=5, relief="ridge", bg="#0099cc")
        Management_Frame.place(x=10, y=80)

        Buttom_Frame = Frame(
            self.root, width=1600, height=55, bd=5, relief="ridge", bg="#328695")
        Buttom_Frame.place(x=10, y=460)

        Data_Frame = Frame(
            self.root, width=1600, height=270, bd=5, relief="ridge", bg="#266e73")
        Data_Frame.place(x=10, y=510)

        # ----------------Inner Frames------------------#
        Data_FrameLeft = LabelFrame(
            Management_Frame, width=1050, text="General Information", font=("arial", 20, "italic bold"), height=390, bd=7, relief="ridge", bg="#0099cc")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight = LabelFrame(
            Management_Frame, width=1050, text="Prescription", font=("arial", 15, "italic bold"), height=390, bd=7, relief="ridge", bg="#0099cc")
        Data_FrameRight.pack(side=RIGHT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Prescription Data", font=(
            "arial", 12, "italic bold"), height=390, bd=4, relief="ridge", bg="#3eb7bb")
        Data_Framedata.pack(side=LEFT)

        # ----------------LAbels------------------------#
        Datelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                        width=20, text="Date", padx=2, bg="#0099cc")
        Datelbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                        width=27, textvariable=Date_of_Registration)
        Datetxt.grid(row=0, column=1, padx=10, pady=5, sticky=E)

        Reflbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                       width=20, text="Reference", padx=2, bg="#0099cc")
        Reflbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        Reftxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), state=DISABLED,
                       width=27, textvariable=Ref)
        Reftxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        PatientIdlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                             width=20, text="Patient Id", padx=2, bg="#0099cc")
        PatientIdlbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        PatientIdtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                             width=27, textvariable=PatientId)
        PatientIdtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        PatientNamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                               width=20, text="Patient Name", padx=2, bg="#0099cc")
        PatientNamelbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        PatientNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                               width=27, textvariable=Patientname)
        PatientNametxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        Dateofbirthlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                               width=20, text="Date of birth", padx=2, bg="#0099cc")
        Dateofbirthlbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        Dateofbirthtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                               width=27, textvariable=Dateofbirth)
        Dateofbirthtxt.grid(row=4, column=1, padx=10, pady=5, sticky=E)

        Addresslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                           width=20, text="Address", padx=2, bg="#0099cc")
        Addresslbl.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Addresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                           width=27, textvariable=patientAddress)
        Addresstxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        NHIFnumberlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                              width=20, text="NHIF Unique Number", padx=2, bg="#0099cc")
        NHIFnumberlbl.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        NHIFnumbertxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                              width=27, textvariable=NHIFnumber)
        NHIFnumbertxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        Tabletlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                          width=20, text="Tablet", padx=2, bg="#0099cc")
        Tabletlbl.grid(row=7, column=0, padx=10, pady=5, sticky=W)

        Tabletcmd = ttk.Combobox(
            Data_FrameLeft, textvariable=cmdTabletNames,
            width=25, state="readonly", font=("arial", 12, "bold"))
        Tabletcmd['values'] = ("", "Paracetemol", "Don-p", "Dio-1 one", "Calpol", "Amlodipine Besylate",
                               "Nexium", "Singulair", "Plavix", "Amoxicillian", "Azithromycin", "Limcin-900")
        # When nothing it will be set as empty which we  have given as index 0
        Tabletcmd.current(0)
        Tabletcmd.grid(row=7, column=1, pady=5, padx=10)

        Number_of_Tableslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                                    width=20, text="Number of Tablets", padx=2, bg="#0099cc")
        Number_of_Tableslbl.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        Number_of_Tablestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                                    width=27, textvariable=Number_of_Tables)
        Number_of_Tablestxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)

        # Now we will make 2nd column of other details in the same frame

        HospitalCodelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                                width=20, text="Hospital Code", padx=2, bg="#0099cc")
        HospitalCodelbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        HospitalCodetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                                width=25, textvariable=HospitalCode)
        HospitalCodetxt.grid(row=0, column=3, padx=10, pady=5, sticky=E)

        StorageAdvicelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                                 width=20, text="Storage Advice", padx=2, bg="#0099cc")
        StorageAdvicelbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        StorageAdvicecmd = ttk.Combobox(
            Data_FrameLeft, textvariable=StorageAdvice,
            width=23, state="readonly", font=("arial", 12, "bold"))
        StorageAdvicecmd['values'] = (
            "", "Under Room Temp", "Below 5*C", "Below 0*C", "Refrigration")
        # When nothing it will be set as empty which we  have given as index 0
        StorageAdvicecmd.current(0)
        StorageAdvicecmd.grid(row=1, column=3, pady=5, padx=10)

        Lot_nolbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                          width=20, text="Lot Number", padx=2, bg="#0099cc")
        Lot_nolbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        Lot_notxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                          width=25, textvariable=lot)
        Lot_notxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)

        IssuedDatelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                              width=20, text="Date of Issue", padx=2, bg="#0099cc")
        IssuedDatelbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        IssuedDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                              width=25, textvariable=IssuedDate)
        IssuedDatetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)

        ExpiryDatelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                              width=20, text="Date of Expiry", padx=2, bg="#0099cc")
        ExpiryDatelbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        ExpiryDatetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                              width=25, textvariable=ExpiryDate)
        ExpiryDatetxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)

        Dailydoselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                             width=20, text="Daily Dosage", padx=2, bg="#0099cc")
        Dailydoselbl.grid(row=5, column=2, padx=10, pady=5, sticky=W)
        Dailydosetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                             width=25, textvariable=DailyDose)
        Dailydosetxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)

        SideEffectslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                               width=20, text="Side Effects", padx=2, bg="#0099cc")
        SideEffectslbl.grid(row=6, column=2, padx=10, pady=5, sticky=W)
        SideEffectstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                               width=25, textvariable=SideEffects)
        SideEffectstxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        MoreInformationlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                                   width=20, text="More Information", padx=2, bg="#0099cc")
        MoreInformationlbl.grid(row=7, column=2, padx=10, pady=5, sticky=W)
        MoreInformationtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                                   width=25, textvariable=MoreInformation)
        MoreInformationtxt.grid(row=7, column=3, padx=10, pady=5, sticky=E)

        Medicationlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                              width=20, text="Medication", padx=2, bg="#0099cc")
        Medicationlbl.grid(row=8, column=2, padx=10, pady=5, sticky=W)
        Medicationcmd = ttk.Combobox(
            Data_FrameLeft, textvariable=Medication,
            width=23, state="readonly", font=("arial", 12, "bold"))
        Medicationcmd['values'] = (
            "", "Yes", "No")
        # When nothing it will be set as empty which we  have given as index 0
        Medicationcmd.current(0)
        Medicationcmd.grid(row=8, column=3, pady=5, padx=10)

        # ---------Text field for prescription-----------#
        TextPrescription = Text(Data_FrameRight, font=(
            "arial", 12, "bold"), width=62, height=17, padx=3, pady=5)
        TextPrescription.grid(row=0, column=0)

        # ---------Text for prescription data-----------#
        TextPrescriptionData = Text(Data_Framedata, font=(
            "arial", 12, "bold"), width=203, height=12, padx=3, pady=5)
        TextPrescriptionData.grid(row=1, column=0)

        # Now we will add button to our middle frame
        Prescriptionbtn = Button(Buttom_Frame, text="Prescription", bg="#ffaab0",
                                 activebackground="#fcceb2", font=("arial", 15, "bold"), width=23, command=Prescriptionfunc)
        Prescriptionbtn.grid(row=0, column=0, padx=15)

        Receiptbtn = Button(Buttom_Frame, text="Prescriton Data", bg="#ffaab0",
                            activebackground="#fcceb2", font=("arial", 15, "bold"), width=23, command=Prescriptiondata)
        Receiptbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Buttom_Frame, text="Reset", bg="#ffaab0",
                          activebackground="#fcceb2", font=("arial", 15, "bold"), width=23, command=Resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Buttom_Frame, text="Delete", bg="#ffaab0",
                           activebackground="#fcceb2", font=("arial", 15, "bold"), width=23, command=Deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Buttom_Frame, text="Exit", bg="#ffaab0",
                         activebackground="#fcceb2", font=("arial", 15, "bold"), width=23, command=Exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)

        Prescriptiondatarow = Label(Data_Framedata, bg="white", font=("arial", 12, "bold"),
                                    text="Date\tReference Id\tPatient Name\tDate of Birth\tNHIF Number\tTablet\tNo of Tablet\tIssued Date\tExpiry Date\tDaily Dose\tStorage Advice\tPatient ID               ")
        Prescriptiondatarow.grid(row=0, column=0, sticky=W)


if __name__ == "__main__":

    root = Tk()
    app = Hospital(root)
    root.mainloop()
