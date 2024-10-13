from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strptime
from datetime import datetime


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")




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
        lblframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add",
                                  font=("times new roman", 12, "bold"), padx=2)
        lblframeleft.place(x=5, y=50, width=520, height=350)

        # Floor
        lbl_floor = Label(lblframeleft, text="Floor:", font=("times new roman", 12, "bold"), padx=2,pady=6)
        lbl_floor.grid(row=0, column=0, stick=W)
        self.var_Floor=StringVar()
        enty_floor=ttk.Entry(lblframeleft,textvariable=self.var_Floor,font=("times new roman", 13, "bold"),width=20)
        enty_floor.grid(row=0, column=1, sticky=W)

        # Room No
        lbl_RoomNo = Label(lblframeleft, text="Room No:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, stick=W)
        self.var_RoomNo=StringVar()
        enty_RoomNo = ttk.Entry(lblframeleft,textvariable=self.var_RoomNo,font=("times new roman", 13, "bold"), width=20)
        enty_RoomNo.grid(row=1, column=1, sticky=W)

        # Room Type
        lbl_RoomType = Label(lblframeleft, text="Room Type:", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, stick=W)
        self.var_RoomType=StringVar()
        enty_RoomType = ttk.Entry(lblframeleft,textvariable=self.var_RoomType,font=("times new roman", 13, "bold"), width=20)
        enty_RoomType.grid(row=2,column=1, sticky=W)

        # ==============================================Buttons=============================================
        btn_frame = Frame(lblframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add",command=self.add_data,font=("Arial", 11, "bold"), bg="black", fg="gold",width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpadate = Button(btn_frame, text="Update",command=self.update,font=("Arial", 11, "bold"), bg="black",fg="gold", width=10)
        btnUpadate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete,font=("Arial", 11, "bold"), bg="black",fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("Arial", 11, "bold"), bg="black",fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
#=================================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details",font=("Arial", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame, column=("Floor", "RoomNo", "RoomType"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("RoomNo", text="RoomNo")
        self.room_table.heading("RoomType", text="RoomType")


        self.room_table["show"] = "headings"

        self.room_table.column("Floor", width=100)
        self.room_table.column("RoomNo", width=100)
        self.room_table.column("RoomType", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if self.var_Floor.get()=="" or self.var_RoomType.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                                                                                                self.var_Floor.get(),
                                                                                                self.var_RoomNo.get(),
                                                                                                self.var_RoomType.get()

                                                                                             ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showinfo("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)



    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_Floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])

    def update(self):
        if self.var_Floor.get()=="":
            messagebox.showerror("Error","Please enter your mobile number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor=%s, RoomType=%s where RoomNo=%s",(
                                                                                                        self.var_Floor.get(),
                                                                                                        self.var_RoomType.get(),
                                                                                                        self.var_RoomNo.get(),

                                                                                                      ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room Details has been updated successfully",parent=self.root)


    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management Systum","Do You Want delete this Room Details",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="ducat@2023",database="management")
            my_cursor = conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_Floor.set(""),
        self.var_RoomNo.set(""),
        self.var_RoomType.set(""),






if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()