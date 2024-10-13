from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strptime
from datetime import datetime


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        self.var_Contact=StringVar()
        self.var_check_in=StringVar()
        self.var_check_out=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()




        # ================================title==================================================================================
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)



        # =========================================logo==========================================================================
        img2 = Image.open("D:/images (2) (1).png")
        img2 = img2.resize((100, 42), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=42)
        # ==========================================lableframe===================================================================
        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details",font=("times new roman", 12, "bold"), padx=2)
        lblframeleft.place(x=5, y=50, width=425, height=490)

        # ====================================lables and entry==================================================================
        # custContact
        lbl_cust_contact = Label(lblframeleft, text="Customer Contact:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_cust_contact.grid(row=0, column=0, stick=W)
        enty_contact = ttk.Entry(lblframeleft,textvariable=self.var_Contact,font=("times new roman", 13, "bold"),width=20)
        enty_contact.grid(row=0, column=1, sticky=W)

        # =============================fecth data button=========================================================================

        btnFetchData = Button(lblframeleft,command=self.Fetch_contact,text="Fetch Data", font=("Arial", 11, "bold"),bg="black", fg="gold", width=9)
        btnFetchData.place(x=325, y=4)

        # Check_in_date
        check_in_date = Label(lblframeleft, font=("Arial", 12, "bold"), text="Check_in Date:", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, stick=W)
        txtcheck_in_date = ttk.Entry(lblframeleft,textvariable=self.var_check_in,font=("Arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check_out_date
        lblCheck_out = Label(lblframeleft, font=("Arial", 12, "bold"), text="Check_out Date:", padx=2, pady=6)
        lblCheck_out.grid(row=2, column=0, stick=W)
        txtCheck_out = ttk.Entry(lblframeleft,textvariable=self.var_check_out,font=("Arial", 13, "bold"), width=29)
        txtCheck_out.grid(row=2, column=1)

        # Room Type
        lbl_RoomType = Label(lblframeleft, font=("Arial", 12, "bold"), text="Room type:", padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0, stick=W)
        conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide= my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(lblframeleft,textvariable=self.var_roomtype,font=("Arial", 12, "bold"),width=27)
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblAvailable = Label(lblframeleft, font=("Arial", 12, "bold"), text="Available Room:", padx=2, pady=6)
        lblAvailable.grid(row=4, column=0, stick=W)
        #txtAvailable = ttk.Entry(lblframeleft,textvariable=self.var_roomavailable,font=("Arial", 13, "bold"),width=29)
        #txtAvailable.grid(row=4, column=1)
        conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(lblframeleft, textvariable=self.var_roomavailable, font=("Arial", 12, "bold"),width=27)
        combo_RoomType["value"] =rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=4, column=1)

        # Meal
        lblMeal = Label(lblframeleft, font=("Arial", 12, "bold"), text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, stick=W)
        txtMeal = ttk.Entry(lblframeleft,textvariable=self.var_meal,font=("Arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No of Days
        lblNoOfDays = Label(lblframeleft, font=("Arial", 12, "bold"), text="No Of Days:", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, stick=W)
        txtNoOfDays = ttk.Entry(lblframeleft,textvariable=self.var_noOfdays,font=("Arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblpaidTax = Label(lblframeleft, font=("Arial", 12, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblpaidTax.grid(row=7, column=0, stick=W)
        txtNoOfDays = ttk.Entry(lblframeleft,textvariable=self.var_paidtax,font=("Arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(lblframeleft, font=("Arial", 12, "bold"), text="Sub Total:", padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, stick=W)
        txtSubTotal = ttk.Entry(lblframeleft,textvariable=self.var_actualtotal,font=("Arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(lblframeleft, font=("Arial", 12, "bold"), text="Total Cost:", padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, stick=W)
        txtTotalCost = ttk.Entry(lblframeleft,textvariable=self.var_total,font=("times new roman", 13, "bold"),
                                 width=29)
        txtTotalCost.grid(row=9, column=1)

        btnBill = Button(lblframeleft, text="Bill",command=self.total,font=("Arial", 11, "bold"), bg="Black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # ==============================================Buttons=============================================
        btn_frame = Frame(lblframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data, font=("Arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpadate = Button(btn_frame, text="Update",command=self.update,font=("Arial", 11, "bold"), bg="black",
                            fg="gold", width=10)
        btnUpadate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete,font=("Arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("Arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # =======================RightSide Image==================================================================================

        img3 = Image.open("D:/images (2) (1).png")
        img3 = img2.resize((550, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=550, height=300)

        # =======================================Tableframe search====================================================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And search ",
                                 font=("Arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, font=("Arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, stick=W, padx=2)

        self.serch_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.serch_var, font=("Arial", 12, "bold"), width=24,
                                    state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("times new roman", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search",command=self.search, font=("Arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All",command=self.fetch_data, font=("Arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table= ttk.Treeview(details_table, column=(
        "Contact", "check_in", "check_out", "roomtype", "roomavailable", "meal", "noOfdays"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Contact", text="Contact")
        self.room_table.heading("check_in", text="check_in")
        self.room_table.heading("check_out", text="check_out")
        self.room_table.heading("roomtype", text="roomtype")
        self.room_table.heading("roomavailable", text="roomavailable")
        self.room_table.heading("meal", text="meal")
        self.room_table.heading("noOfdays", text="noOfdays")



        self.room_table["show"] = "headings"

        self.room_table.column("Contact", width=100)
        self.room_table.column("check_in", width=100)
        self.room_table.column("check_out", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if self.var_Contact.get()=="" or self.var_check_in.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                self.var_Contact.get(),
                                                                                                self.var_check_in.get(),
                                                                                                self.var_check_out.get(),
                                                                                                self.var_roomtype.get(),
                                                                                                self.var_roomavailable.get(),
                                                                                                self.var_meal.get(),
                                                                                                self.var_noOfdays.get(),

                                                                                             ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showinfo("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
            conn.close()


    def get_cuersor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_Contact.set(row[0])
        self.var_check_in.set(row[1])
        self.var_check_out.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noOfdays.set(row[6])


    def update(self):
        if self.var_Contact.get()=="":
            messagebox.showerror("Error","Please enter your mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
                                                                                                                                                                                self.var_check_in.get(),
                                                                                                                                                                                self.var_check_out.get(),
                                                                                                                                                                                self.var_roomtype.get(),
                                                                                                                                                                                self.var_roomavailable.get(),
                                                                                                                                                                                self.var_meal.get(),
                                                                                                                                                                                self.var_noOfdays.get(),
                                                                                                                                                                                self.var_Contact.get()

                                                                                                                                                                                 ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","room Details has been updated successfully",parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management Systum", "Do You Want delete this customer", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",
                                           database="management")
            my_cursor = conn.cursor()
            query = "delete from room where Contact=%s"
            value = (self.var_Contact.get(),)
            my_cursor.execute(query, value)

        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_Contact.set(""),
        self.var_check_in.set(""),
        self.var_check_out.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noOfdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set(""),





    def Fetch_contact(self):
        if self.var_Contact.get()=="":
            messagebox.showerror("Error","Please enter contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
            my_cursor = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_Contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)


                lblName=Label(showDataframe,text="Name:",font=("Arial 12 bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("Arial 12 bold"))
                lbl.place(x=90,y=0)

                conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:", font=("Arial 12 bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=("Arial 12 bold"))
                lbl2.place(x=90, y=30)

                conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Nationality:", font=("Arial 12 bold"))
                lblGender.place(x=0, y=60)

                lbl2 = Label(showDataframe, text=row, font=("Arial 12 bold"))
                lbl2.place(x=90, y=60)

                #============================

                conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
                my_cursor = conn.cursor()
                query = ("select Idnumber from customer where Mobile=%s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Idnumber:", font=("Arial 12 bold"))
                lblGender.place(x=0, y=90)

                lbl2 = Label(showDataframe, text=row, font=("Arial 12 bold"))
                lbl2.place(x=90, y=90)
                #==============

                conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_Contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Address:", font=("Arial 12 bold"))
                lblGender.place(x=0, y=120)

                lbl2 = Label(showDataframe, text=row, font=("Arial 12 bold"))
                lbl2.place(x=90, y=120)

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023", database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where "+str(self.serch_var.get())+"Like'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_check_in.get()
        outDate=self.var_check_out.get()
        inDate=datetime.strptime(inDate,"%d-%m-%Y")
        outDate = datetime.strptime(outDate,"%d-%m-%Y")
        self.var_noOfdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="laxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noOfdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()