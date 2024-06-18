import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


class Registration:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="black")

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
            root.destroy()
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


if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
