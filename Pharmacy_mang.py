import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class HomePage:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        # x-axis, y-axis,0,0, are the loaction from the left most
        self.master.geometry('1700x900+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.labelTitle = Label(self.frame, text="Pharmacy Management System", font=(
            "arial", 40, "bold"), bd=10, relief="sunken")
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.Loginframe1 = Frame(
            self.frame, width=1000, height=300, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(
            self.frame, width=1000, height=100, bd=10, relief="groove")
        self.Loginframe2.grid(row=2, column=0, pady=15)

        self.Loginframe3 = Frame(
            self.frame, width=1000, height=200, bd=10, relief="groove")
        self.Loginframe3.grid(row=6, column=0, pady=5)

        self.button_Reg = Button(self.Loginframe3, text="Patient registration Window", state=DISABLED, font=(
            "arial", 15, "bold"), command=self.Registration_window)
        self.button_Reg.grid(row=0, column=0, padx=10, pady=10)

        self.button_Hosp = Button(self.Loginframe3, text="Hospital Management Window", state=DISABLED, font=(
            "arial", 15, "bold"), command=self.Hospital_window)
        self.button_Hosp.grid(row=0, column=1, padx=10, pady=10)

        self.button_Dr_appt = Button(self.Loginframe3, text="Doctor Management Window", state=DISABLED, font=(
            "arial", 15, "bold"), command=self.Dr_Appoint_window)
        self.button_Dr_appt.grid(row=1, column=0, columnspan=2,
                                 padx=10, pady=10, sticky="we")

        # Now we will make username and password frame
        self.LabelUsername = Label(
            self.Loginframe1, text="User Name", font=("arial", 20, "bold"), bd=3)
        self.LabelUsername.grid(row=0, column=0)

        self.textUsername = Entry(self.Loginframe1, font=(
            "arial", 20, "bold"), bd=3, textvariable=self.Username)
        self.textUsername.grid(row=0, column=1, padx=40, pady=15)

        self.LabelPassword = Label(
            self.Loginframe1, text="Password", font=("arial", 20, "bold"), bd=3)
        self.LabelPassword.grid(row=1, column=0)

        self.textPassword = Entry(self.Loginframe1, font=(
            "arial", 20, "bold"), show="*", bd=3, textvariable=self.Password)
        self.textPassword.grid(row=1, column=1, padx=40, pady=15)

        self.button_Login = Button(
            self.Loginframe2, text="Login", width=20, font=("arial", 18, "bold"), command=self.Login_system)
        self.button_Login.grid(row=0, column=0, padx=10, pady=10)

        self.button_Reset = Button(
            self.Loginframe2, text="Reset", width=20, font=("arial", 18, "bold"), command=self.reset_btn)
        self.button_Reset.grid(row=0, column=3, padx=10, pady=10)

        self.button_Exit = Button(
            self.Loginframe2, text="Exit", width=20, font=("arial", 18, "bold"), command=self.Exit_btn)
        self.button_Exit.grid(row=0, column=6, padx=10, pady=10)

    def Login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()

        if (user == str("admin")) and (pswd == str("admin")):
            self.button_Reg.config(state=NORMAL)
            self.button_Hosp.config(state=NORMAL)
            self.button_Dr_appt.config(state=NORMAL)
            self.button_Med_stock.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno(
                "Pharmacy Management System", "You have entered an invalid user name or password")
            self.button_Reg.config(state=DISABLED)
            self.button_Hosp.config(state=DISABLED)
            self.button_Dr_appt.config(state=DISABLED)
            self.button_Med_stock.config(state=DISABLED)

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus()

    def reset_btn(self):
        self.button_Reg.config(state=DISABLED)
        self.button_Hosp.config(state=DISABLED)
        self.button_Dr_appt.config(state=DISABLED)
        self.button_Med_stock.config(state=DISABLED)
        # Because when we reset still we will haven't given correct user name and password

        self.Username.set("")
        self.Password.set("")
        self.textUsername.focus()

    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno(
            "Pharmacy Management System", "Are you sure you want to exit?")
        if self.Exit_btn > 0:
            # we will close the master screen
            self.master.destroy()
            return

# First we will define all our windows

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)

    def Dr_Appoint_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Doctor(self.newWindow)


class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1700x900+0+0")
        # We will define full screen(maximum-screen)
        self.root.configure(background="#2ab8b8")

        # We will date live date by using time module
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        mobile_no = StringVar()
        pincode = StringVar()
        Address = StringVar()
        FirstName = StringVar()
        LastName = StringVar()

        # this var1,2,3,4,5 are for combobox
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar()  # we will keep as int because we will keep numeric value

        Membership = StringVar()
        # when a member checkbox is unclicked or reset has been done it will automatically set as 0
        Membership.set("0")

        # ------------Functions-----------------------#
        def exitbtt():
            exitbtt = tkinter.messagebox.askyesno(
                "Member Registration Form", "Are you sure you want to exit ?")
            if exitbtt > 0:
                root.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Registration
            return

        def resetbtt():
            Ref.set("")
            mobile_no.set("")
            pincode.set("")
            Address.set("")
            FirstName.set("")
            LastName.set("")
            Membership.set("")
            member_gendercmb.current(0)
            member_id_proofcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt(state=DISABLED)

        def reeset():
            setbtt = tkinter.messagebox.askokcancel(
                "Member Registration Form", "You want to add as new record")
            if reeset > 0:
                resetbtt()
            elif resetbtt <= 0:
                resetbtt()
                detail_labeltxt("1.0", END)
                return

        def Reference_number():
            ranumber = random.randint(1000, 9999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def Membership_fees():
            if (var5.get() == 1):
                item = float(1500)  # Random price of member ship
                Membership.set("Ksh" + str(item))
            elif (var5.get() == 0):
                # When unchecked
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0")

        def Receipt():
            Reference_number()
            detail_labeltxt.insert(END, "\t" + Date_of_Registration.get() + "         \t" + Ref.get() + "\t\t" +
                                   FirstName.get() + "            \t" + LastName.get() + "        \t" + mobile_no.get() +
                                   "        \t\t" + Address.get() + "\t\t" + pincode.get() + "          \t" + member_gendercmb.get() +
                                   "\t\t" + Membership.get() + "\n")

        # ------------------Title----------------------#
        title = Label(self.root, text="Members Registration Form", font=(
            "monotype carvisa", 30, "bold"), bd=5, relief="groove", bg="#E6005c", fg="#000000")
        title.pack(side=TOP, fill=X)

        # ------------------Member Frame---------------#
        manage_Frame = Frame(self.root, relief="ridge", bg="#001066")
        manage_Frame.place(x=20, y=100, width=450, height=630)

        # --------------text, label, comboboxes in manage frame-------------------#
        cus_title = Label(manage_Frame, text="Customer Details", font=(
            "arial", 20, "bold"), bg="#001066", fg="white")
        cus_title.grid(row=0, columnspan=2, pady=5)

        member_datelbl = Label(manage_Frame, text="Date:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_datelbl.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        member_datetxt = Entry(manage_Frame, font=(
            "arial", 15, "bold"), textvariable=Date_of_Registration)
        member_datetxt.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        member_reflbl = Label(manage_Frame, text="Reference Id:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_reflbl.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        member_reftxt = Entry(manage_Frame, font=(
            "arial", 15, "bold"), state=DISABLED, textvariable=Ref)
        member_reftxt.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        member_fnamelbl = Label(manage_Frame, text="First Name:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_fnamelbl.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        member_fnametxt = Entry(manage_Frame, font=(
            "arial", 15, "bold"), textvariable=FirstName)
        member_fnametxt.grid(row=3, column=1, pady=5, padx=10, sticky="w")

        member_lnamelbl = Label(manage_Frame, text="Last Name:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_lnamelbl.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        member_lnametxt = Entry(manage_Frame, font=(
            "arial", 15, "bold"), textvariable=LastName)
        member_lnametxt.grid(row=4, column=1, pady=5, padx=10, sticky="w")

        member_mobilelbl = Label(manage_Frame, text="Mobile No:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_mobilelbl.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        member_mobiletxt = Entry(manage_Frame, font=(
            "arial", 15, "bold"), textvariable=mobile_no)
        member_mobiletxt.grid(row=5, column=1, pady=5, padx=10, sticky="w")

        member_addresslbl = Label(manage_Frame, text="Address:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_addresslbl.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        member_addresstxt = Entry(manage_Frame, font=(
            "arial", 15, "bold"), textvariable=Address)
        member_addresstxt.grid(row=6, column=1, pady=5, padx=10, sticky="w")

        member_pincodelbl = Label(manage_Frame, text="Pin code:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_pincodelbl.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        member_pincodetxt = Entry(manage_Frame, font=(
            "arial", 15, "bold"), textvariable=pincode)
        member_pincodetxt.grid(row=7, column=1, pady=5, padx=10, sticky="w")

        member_genderlbl = Label(manage_Frame, text="Gender:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_genderlbl.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        member_gendercmb = ttk.Combobox(
            manage_Frame, text=var4, state="readonly", font=("arial", 15, "bold"), width=19)
        member_gendercmb['values'] = ("", "Male", "Female", "Other")
        # When nothing it will be set as empty which we  have given as index 0
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8, column=1, pady=5, padx=10, sticky="w")

        member_id_prooflbl = Label(manage_Frame, text="Verify Id:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_id_prooflbl.grid(row=9, column=0, padx=10, pady=5, sticky="w")

        member_id_proofcmb = ttk.Combobox(
            manage_Frame, text=var3, state="readonly", font=("arial", 15, "bold"), width=19)
        member_id_proofcmb['values'] = ("", "National ID Card", "Huduma Namba",
                                        "Passport", "Driving Lincence", "Student Card", "NHIF Card")
        # When nothing it will be set as empty which we  have given as index 0
        member_id_proofcmb.current(0)
        member_id_proofcmb.grid(row=9, column=1, pady=5, padx=10, sticky="w")

        member_memtypelbl = Label(manage_Frame, text="Member Type:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_memtypelbl.grid(row=10, column=0, padx=10, pady=5, sticky="w")

        member_memtypecmb = ttk.Combobox(
            manage_Frame, text=var2, state="readonly", font=("arial", 15, "bold"), width=19)
        member_memtypecmb['values'] = ("", "National Health Insurance Fund", "Private Health Insurance",
                                       "Britam Health Insurance", "Pay When Leaving")
        # When nothing it will be set as empty which we  have given as index 0
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10, column=1, pady=5, padx=10, sticky="w")

        member_paymentwithlbl = Label(manage_Frame, text="Payment With:", font=(
            "arial", 15, "bold"), bg="#001066", fg="white")
        member_paymentwithlbl.grid(
            row=11, column=0, padx=10, pady=5, sticky="w")

        member_paymentwithcmb = ttk.Combobox(
            manage_Frame, text=var1, state="readonly", font=("arial", 15, "bold"), width=19)
        member_paymentwithcmb['values'] = ("", "Cash", "M-Pesa", "Bank Deposit",
                                           "Debit Card -KCB/I&M", "Credit Card - KCB/I&M", "Credit - Mastercard")
        # When nothing it will be set as empty which we  have given as index 0
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(
            row=11, column=1, pady=5, padx=10, sticky="w")

        member_membership = Checkbutton(manage_Frame, text="Membership Fees", variable=var5, onvalue=1, offvalue=0, font=(
            "arial", 15, "bold"), bg="#001066", fg="white", command=Membership_fees)
        member_membership.grid(row=12, column=0, sticky="w")

        member_membershiptxt = Entry(manage_Frame, font=(
            "arial", 15, "bold"), state=DISABLED, justify=RIGHT, textvariable=Membership)
        member_membershiptxt.grid(
            row=12, column=1, pady=5, padx=10, sticky="w")

        # ------------------Detail Frame---------------#
        detail_Frame = Frame(self.root, relief="ridge", bg="#001066")
        detail_Frame.place(x=500, y=100, width=820, height=630)

        detail_label = Label(detail_Frame, font=("arial", 11, "bold"), pady=10, padx=2, width=95,
                             text="Date\t     Ref Id\t     Firstname     Lastname     MobileNo     Address     Pincode     Gender     Membership")
        detail_label.grid(row=0, column=0, columnspan=4, sticky="w")

        detail_labeltxt = Text(detail_Frame, width=123,
                               height=34, font=("arial", 10))
        detail_labeltxt.grid(row=1, column=0, columnspan=4)

        # -------------We will add button in detail frame-----------#
        receiptbtn = Button(detail_Frame, padx=15, bd=5, font=(
            "arial", 12, "bold"), bg="#ff9966", width=20, text="Receipt", command=Receipt)
        receiptbtn.grid(row=2, column=0)

        resetbtn = Button(detail_Frame, padx=15, bd=5, font=(
            "arial", 12, "bold"), bg="#ff9966", width=20, text="Reset", command=reeset)
        resetbtn.grid(row=2, column=1)

        exitbtn = Button(detail_Frame, padx=15, bd=5, font=(
            "arial", 12, "bold"), bg="#ff9966", width=20, text="Exit", command=exitbtt)
        exitbtn.grid(row=2, column=2)


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


def main():
    root = Tk()
    app = HomePage(root)
    root.mainloop()


if __name__ == "__main__":
    main()
