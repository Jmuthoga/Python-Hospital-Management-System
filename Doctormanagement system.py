import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Doctor():
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor Management System")
        # We will define full screen(maximum-screen)
        self.root.geometry("1700x900+0+0")
        self.root.configure(background="black")

        # ------------valiable decription------------#
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        DrId = StringVar()
        DrName = StringVar()
        Dateofbirth = StringVar()
        Spes = StringVar()
        GorvPri = StringVar()
        Surgeries = StringVar()
        Experience = StringVar()
        Nurses = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        PatientAddress = StringVar()
        PtMobile = StringVar()
        Disease = StringVar()
        Case = StringVar()
        BenefitCard = StringVar()
        AppTime = StringVar()
        PtAge = StringVar()

        # ----------------Functions------------------#
        def Exitbtn():
            Exitbtn = tkinter.messagebox.askyesno(
                "Hospital Management System", "Are you sure you want to exit ?")
            if Exitbtn > 0:
                root.destroy()
                return

        def Deletefunc():
            DrId.set("")
            DrName.set("")
            Dateofbirth.set("")
            Spes.set("")
            GorvPri.set("")
            Surgeries.set("")
            Experience.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            AppTime.set("")
            PtAge.set("")
            TextPrescription.delete("1.0", END)
            TextPrescriptionData.delete("1.0", END)
            return

        def Resetfunc():
            DrId.set("")
            DrName.set("")
            Dateofbirth.set("")
            Spes.set("")
            GorvPri.set("")
            Surgeries.set("")
            Experience.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            AppTime.set("")
            PtAge.set("")
            TextPrescription.delete("1.0", END)
            return

        def Reference_numfunc():
            ranumber = random.randint(1000, 99999)
            randomnumber = str(ranumber)
            DrId.set(randomnumber)

        def Doctordata():
            Reference_numfunc()
            TextPrescriptionData.insert(END, Date_of_Registration.get()+"\t"+DrId.get()+"\t\t"+DrName.get()
                                        + "\t\t"+Dateofbirth.get()+"\t\t"+Spes.get()+"\t\t"+GorvPri.get()+"\t\t"+Surgeries.get()+"\t\t" +
                                        Experience.get()+"\t\t"+Nurses.get()+"\t"+DrMobile.get() +
                                        "\t\t"+PtName.get()+"\t\t"+Case.get() + "\t" + PtAge.get()+"\n")

        def Patientfunc():
            Reference_numfunc()
            TextPrescription.insert(
                END, "Date:  \t\t"+Date_of_Registration.get()+"\n")
            TextPrescription.insert(
                END, "Patient Name:  \t\t"+PtName.get()+"\n")
            TextPrescription.insert(
                END, "Appointment Time:  \t\t"+AppTime.get()+"\n")
            TextPrescription.insert(
                END, "Age:  \t\t"+PtAge.get()+"\n")
            TextPrescription.insert(
                END, "Address:  \t\t"+PatientAddress.get()+"\n")
            TextPrescription.insert(
                END, "Type of Disease:  \t\t"+Disease.get()+"\n")
            TextPrescription.insert(
                END, "Case:  \t\t"+Case.get()+"\n")
            TextPrescription.insert(
                END, "Benefit Card:  \t\t"+BenefitCard.get()+"\n")
            TextPrescription.insert(
                END, "To meet Dr:  \t\t"+DrName.get()+"\n")
            TextPrescription.insert(
                END, "Dr. Mobile No:  \t\t"+DrMobile.get()+"\n")

        # ----------------Title----------------------#
        title = Label(self.root, text="Doctor Management System", font=(
            "monotype corsiva", 42, "bold"), bd=5, relief="groove", bg="#b7d8d6", fg="black")
        title.pack(side=TOP, fill=X)

        # ----------------FRAME-----------------------#
        Management_Frame = Frame(
            self.root, width=1600, height=400, bd=5, relief="ridge", bg="#789898")
        Management_Frame.place(x=10, y=80)

        Buttom_Frame = Frame(
            self.root, width=1600, height=55, bd=5, relief="ridge", bg="#eef3db")
        Buttom_Frame.place(x=10, y=460)

        Data_Frame = Frame(
            self.root, width=1600, height=270, bd=5, relief="ridge", bg="#eef3db")
        Data_Frame.place(x=10, y=510)

        # ----------------Inner Frames------------------#
        Data_FrameLeft = LabelFrame(
            Management_Frame, width=1050, text="General Information", font=("arial", 20, "italic bold"), height=390, bd=7, relief="ridge", bg="#789e9e")
        Data_FrameLeft.pack(side=LEFT)

        Data_FrameRight = LabelFrame(
            Management_Frame, width=1050, text="Patient's Information", font=("arial", 15, "italic bold"), height=390, bd=7, relief="ridge", bg="#789e9e")
        Data_FrameRight.pack(side=RIGHT)

        Data_Framedata = LabelFrame(Data_Frame, width=1050, text="Doctor's Details", font=(
            "arial", 12, "italic bold"), height=390, bd=4, relief="ridge", bg="#789e9e")
        Data_Framedata.pack(side=LEFT)

        # ----------------LAbels------------------------#
        DrIdlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                        width=20, text="Doctor Id", padx=2, bg="#789e9e")
        DrIdlbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        DrIdtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"), state=DISABLED,
                        width=27, textvariable=DrId)
        DrIdtxt.grid(row=0, column=1, padx=10, pady=5, sticky=E)

        DrNamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                          width=20, text="Doctor Name", padx=2, bg="#789e9e")
        DrNamelbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        DrNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                          width=27, textvariable=DrName)
        DrNametxt.grid(row=1, column=1, padx=10, pady=5, sticky=E)

        Dateofbirthlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                               width=20, text="Date of Birth", padx=2, bg="#789e9e")
        Dateofbirthlbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        Dateofbirthtxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                               width=27, textvariable=Dateofbirth)
        Dateofbirthtxt.grid(row=2, column=1, padx=10, pady=5, sticky=E)

        Speslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                        width=20, text="Specialisation", padx=2, bg="#789e9e")
        Speslbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        Spestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                        width=27, textvariable=Spes)
        Spestxt.grid(row=3, column=1, padx=10, pady=5, sticky=E)

        GorvPrilbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                           width=20, text="Gort/Private", padx=2, bg="#789e9e")
        GorvPrilbl.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        GorvPricmd = ttk.Combobox(
            Data_FrameLeft, textvariable=GorvPri,
            width=25, state="readonly", font=("arial", 12, "bold"))
        GorvPricmd['values'] = ("", "Goverment", "Private")
        # When nothing it will be set as empty which we  have given as index 0
        GorvPricmd.current(0)
        GorvPricmd.grid(row=4, column=1, pady=5, padx=10)

        Surgerieslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                             width=20, text="Surgeries", padx=2, bg="#789e9e")
        Surgerieslbl.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        Surgeriestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                             width=27, textvariable=Surgeries)
        Surgeriestxt.grid(row=5, column=1, padx=10, pady=5, sticky=E)

        Experiencelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                              width=20, text="Experience", padx=2, bg="#789e9e")
        Experiencelbl.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        Experiencetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                              width=27, textvariable=Experience)
        Experiencetxt.grid(row=6, column=1, padx=10, pady=5, sticky=E)

        Nurseslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                          width=20, text="Nurses Under Dr", padx=2, bg="#789e9e")
        Nurseslbl.grid(row=7, column=0, padx=10, pady=5, sticky=W)
        Nursestxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                          width=27, textvariable=Nurses)
        Nursestxt.grid(row=7, column=1, padx=10, pady=5, sticky=E)

        DrMobilelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                            width=20, text="Doctor Mobile No", padx=2, bg="#789e9e")
        DrMobilelbl.grid(row=8, column=0, padx=10, pady=5, sticky=W)
        DrMobiletxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                            width=27, textvariable=DrMobile)
        DrMobiletxt.grid(row=8, column=1, padx=10, pady=5, sticky=E)

        # Now we will make 2nd column of other details in the same frame
        Datelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                        width=20, text="Date", padx=2, bg="#789e9e")
        Datelbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        Datetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                        width=25, textvariable=Date_of_Registration)
        Datetxt.grid(row=0, column=3, padx=10, pady=5, sticky=E)

        PtNamelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                          width=20, text="Patient Name", padx=2, bg="#789e9e")
        PtNamelbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        PtNametxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                          width=25, textvariable=PtName)
        PtNametxt.grid(row=1, column=3, padx=10, pady=5, sticky=E)

        AppTimelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                           width=20, text="Appointment Time", padx=2, bg="#789e9e")
        AppTimelbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        AppTimetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                           width=25, textvariable=AppTime)
        AppTimetxt.grid(row=2, column=3, padx=10, pady=5, sticky=E)

        PtAgelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                         width=20, text="Patient Age", padx=2, bg="#789e9e")
        PtAgelbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        PtAgetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                         width=25, textvariable=PtAge)
        PtAgetxt.grid(row=3, column=3, padx=10, pady=5, sticky=E)

        PatientAddresslbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                                  width=20, text="Patient Address", padx=2, bg="#789e9e")
        PatientAddresslbl.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        PatientAddresstxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                                  width=25, textvariable=PatientAddress)
        PatientAddresstxt.grid(row=4, column=3, padx=10, pady=5, sticky=E)

        PtMobilelbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                            width=20, text="Patient Mobile No", padx=2, bg="#789e9e")
        PtMobilelbl.grid(row=5, column=2, padx=10, pady=5, sticky=W)
        PtMobiletxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                            width=25, textvariable=PtMobile)
        PtMobiletxt.grid(row=5, column=3, padx=10, pady=5, sticky=E)

        Diseaselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                           width=20, text="Patient Disease", padx=2, bg="#789e9e")
        Diseaselbl.grid(row=6, column=2, padx=10, pady=5, sticky=W)
        Diseasetxt = Entry(Data_FrameLeft, font=("arial", 12, "bold"),
                           width=25, textvariable=Disease)
        Diseasetxt.grid(row=6, column=3, padx=10, pady=5, sticky=E)

        Caselbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                        width=20, text="Case", padx=2, bg="#789e9e")
        Caselbl.grid(row=7, column=2, padx=10, pady=5, sticky=W)
        Casecmd = ttk.Combobox(
            Data_FrameLeft, textvariable=Case,
            width=23, state="readonly", font=("arial", 12, "bold"))
        Casecmd['values'] = ("", "New", "Old")
        # When nothing it will be set as empty which we  have given as index 0
        Casecmd.current(0)
        Casecmd.grid(row=7, column=3, pady=5, padx=10)

        BenefitCardlbl = Label(Data_FrameLeft, font=("arial", 12, "bold"),
                               width=20, text="Benefit Card", padx=2, bg="#789e9e")
        BenefitCardlbl.grid(row=8, column=2, padx=10, pady=5, sticky=W)
        BenefitCardcmd = ttk.Combobox(
            Data_FrameLeft, textvariable=BenefitCard,
            width=23, state="readonly", font=("arial", 12, "bold"))
        BenefitCardcmd['values'] = (
            "", "Natural Health Insurance Fund", "Britam Health Insurance", "Private Health Insurance")
        # When nothing it will be set as empty which we  have given as index 0
        BenefitCardcmd.current(0)
        BenefitCardcmd.grid(row=8, column=3, pady=5, padx=10)

        # ---------Text field for prescription-----------#
        TextPrescription = Text(Data_FrameRight, font=(
            "arial", 12, "bold"), width=62, height=17, padx=3, pady=5)
        TextPrescription.grid(row=0, column=0)

        # ---------Text for prescription data-----------#
        TextPrescriptionData = Text(Data_Framedata, font=(
            "arial", 12, "bold"), width=203, height=12, padx=3, pady=5)
        TextPrescriptionData.grid(row=1, column=0)

        # Now we will add button to our middle frame
        Patientbtn = Button(Buttom_Frame, text="Patient's Information", bg="#fe6159",
                            activebackground="#cc6686", font=("arial", 15, "bold"), width=23, command=Patientfunc)
        Patientbtn.grid(row=0, column=0, padx=15)

        Receiptbtn = Button(Buttom_Frame, text="Doctor's Details", bg="#fe6159",
                            activebackground="#cc6686", font=("arial", 15, "bold"), width=23, command=Doctordata)
        Receiptbtn.grid(row=0, column=1, padx=15)

        Resetbtn = Button(Buttom_Frame, text="Reset", bg="#fe6159",
                          activebackground="#cc6686", font=("arial", 15, "bold"), width=23, command=Resetfunc)
        Resetbtn.grid(row=0, column=2, padx=15)

        Deletebtn = Button(Buttom_Frame, text="Delete", bg="#fe6159",
                           activebackground="#cc6686", font=("arial", 15, "bold"), width=23, command=Deletefunc)
        Deletebtn.grid(row=0, column=3, padx=15)

        Exitbtn = Button(Buttom_Frame, text="Exit", bg="#fe6159",
                         activebackground="#cc6686", font=("arial", 15, "bold"), width=23, command=Exitbtn)
        Exitbtn.grid(row=0, column=4, padx=15)

        Doctordatarow = Label(Data_Framedata, bg="white", font=("arial", 12, "bold"),
                              text="Date\tDoctor Id \tDoctor Name\tDate of Birth\tSpecialization\tGovt/Private\tSurgeries\tExperience\tNurses\tDr Mobile No\tPatient Name\tCase\tPT. Age             ")
        Doctordatarow.grid(row=0, column=0, sticky=W)


if __name__ == "__main__":

    root = Tk()
    app = Doctor(root)
    root.mainloop()
