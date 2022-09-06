from dataclasses import dataclass
from logging import root
from multiprocessing.sharedctypes import Value
from tkinter import*
from tkinter import font
from tkinter import ttk
from turtle import width
from winreg import QueryInfoKey

from numpy import pad
from pyparsing import col

import pypyodbc as obdc
from tkinter import messagebox
import datetime
import tkinter

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-GOJTSQ5\SQLEXPRESS'
DATABASE_NAME = 'v_library'

connection_string = f"""
    DRIVER={DRIVER_NAME};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Library Management System')
        self.root.geometry('1550x800+0+0')


        # ===========================   VARIABLE =========================== #
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()


        lbltitle = Label(self.root, text='LIBRARY MANAGEMENT SYSTEM', bg='powder blue', fg='green', bd=20, relief=RIDGE, font=('arial', 50, 'bold'), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        frame.place(x=0, y=130, width=1530, height=400)


        # =========================== DATA FRAME LEFT =========================== #

        DataFrameLeft = LabelFrame(frame, text= 'Library Membership Information', bg='powder blue', fg='green', bd=12, relief=RIDGE, font=('arial', 12, 'bold'))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMember = Label(DataFrameLeft, bg='powder blue', textvariable=self.member_var, text='Member Type', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=('arial', 12, 'bold'), width=27, state='readonly')
        comMember['value'] = ('Admin Staff', 'Student', 'Lecturer')
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, bg='powder blue', text='PRN No', font=('arial', 12, 'bold'), padx=2, pady=4)
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtPRN_No.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='ID No:', padx=2, pady=4, bg='powder blue')
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='FirstName:', padx=2, pady=6, bg='powder blue')
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='LastName:', padx=2, pady=6, bg='powder blue')
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Address1:', padx=2, pady=6, bg='powder blue')
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtAddress1.grid(row=5, column=1)

        lblAddress2 = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Address2:', padx=2, pady=6, bg='powder blue')
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtAddress2.grid(row=6, column=1)

        lblPostCode = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Post Code:', padx=2, pady=4, bg='powder blue')
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtPostCode.grid(row=7, column=1)

        lblMobile = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Mobile:', padx=2, pady=6, bg='powder blue')
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtMobile.grid(row=8, column=1)

        lblBookId = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Book Id:', padx=2, pady=6, bg='powder blue')
        lblBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtBookId.grid(row=0, column=3)

        lblBookTitle = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Book Title:', padx=2, pady=6, bg='powder blue')
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=('arial', 13, 'bold'), width=29)
        txtBookTitle.grid(row=1, column=3)

        lblAuthor = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Author Name:', padx=2, pady=6, bg='powder blue')
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=29)
        txtAuthor.grid(row=2, column=3)

        lblDateBorrowed = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Date Borrowed:', padx=2, pady=6, bg='powder blue')
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=29)
        txtDateBorrowed.grid(row=3, column=3)

        lblDateDue = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Date Due:', padx=2, pady=6, bg='powder blue')
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=29)
        txtDateDue.grid(row=4, column=3)

        lblDaysOnBook = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Days On Book:', padx=2, pady=6, bg='powder blue')
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=29)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Late Return Fine:', padx=2, pady=6, bg='powder blue')
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=29)
        txtLateReturnFine.grid(row=6, column=3)


        # =========================== MISSPELL, OVERDATE SHOULD BE OVERDUE =========================== #
        lblDateOverdate = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Date Overdue:', padx=2, pady=6, bg='powder blue')
        lblDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=29)
        txtDateOverdate.grid(row=7, column=3)

        lblActualPrice = Label(DataFrameLeft, font=('arial', 12, 'bold'), text='Actual Price:', padx=2, pady=6, bg='powder blue')
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=('arial', 12, 'bold'), width=29)
        txtActualPrice.grid(row=8, column=3)

        # =========================== DATA FRAME RIGHT =========================== #

        DataFrameRight = LabelFrame(frame, text= 'Book Details', bg='powder blue', fg='green', bd=12, relief=RIDGE, font=('arial', 12, 'bold'))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.txtBox = Text(DataFrameRight, font=('arial', 12, 'bold'), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)
        
        
        # =========================== SELF INSERT LIST =========================== #

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky='ns')

        listBooks = []
        def SelectBook(event=''):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x=='Head First Book'):
                self.bookid_var.set('BKID5454')
                self.booktitle_var.set('Python Manual')
                self.author_var.set('Paul Berry')

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook.set(15)
                self.lateratefine_var.set('Rs.50')
                self.dateoverdue.set('NO')
                self.finalprice.set('Rs.788')

                # =========================== SPAM ELIF 1:10:57 =========================== #
            
                

        listBox = Listbox(DataFrameRight, font=('Arial', 12, 'bold'), width=20, height=16)
        listBox.bind('<<ListboxSelect>>', SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)


        # =========================== BUTTONS FRAME =========================== #

        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        FrameButton.place(x=0, y=530, width=1530, height=60)

        btnAddData = Button(FrameButton, command=self.adda_data, text='Add Data', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(FrameButton, command=self.showData, text='Show Data', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(FrameButton, command=self.update, text='Update', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(FrameButton, command=self.delete, text='Delete', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(FrameButton, command=self.reset, text='Reset', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(FrameButton, command=self.iExit, text='Exit', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=5)


        # =========================== INFO FRAME =========================== #

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg='powder blue')
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame, column=('membertype', 'prnno', 'title', 'firstname', 'lastname', 'address1', 'address2', 'postid', 'mobile', 'bookid',
                                            'booktitle', 'author', 'dateborrowed', 'datedue', 'days', 'latereturnfine', 'dateoverdue', 'finalprice'), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading('membertype', text='Member Type')
        self.library_table.heading('prnno', text='Reference No.')
        self.library_table.heading('title', text = 'Title')
        self.library_table.heading('firstname', text = 'First Name')
        self.library_table.heading('lastname', text='Last Name')
        self.library_table.heading('address1', text='Address1')
        self.library_table.heading('address2', text='Address2')
        self.library_table.heading('postid', text='Post ID')
        self.library_table.heading('mobile', text='Mobile Number')
        self.library_table.heading('bookid', text='Book ID')
        self.library_table.heading('booktitle', text='Book Title')
        self.library_table.heading('author', text='Author')
        self.library_table.heading('dateborrowed', text='Date Borrowed')
        self.library_table.heading('datedue', text='Date Due')
        self.library_table.heading('days', text='Days On Book')
        self.library_table.heading('latereturnfine', text='Late Return Fine')
        self.library_table.heading('dateoverdue', text='Date Overdue')
        self.library_table.heading('finalprice', text='Final Price')

        self.library_table['show'] = 'headings'
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column('membertype', width=100)
        self.library_table.column('prnno', width=100)
        self.library_table.column('title', width=100)
        self.library_table.column('lastname', width=100)
        self.library_table.column('address1', width=100)
        self.library_table.column('address2', width=100)
        self.library_table.column('postid', width=100)
        self.library_table.column('mobile', width=100)
        self.library_table.column('bookid', width=100)
        self.library_table.column('booktitle', width=100)
        self.library_table.column('author', width=100)
        self.library_table.column('dateborrowed', width=100)
        self.library_table.column('datedue', width=100)
        self.library_table.column('days', width=100)
        self.library_table.column('dateoverdue', width=100)
        self.library_table.column('finalprice', width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def adda_data(self):        
        conn = obdc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute('insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                                                                                                                self.member_var.get(),
                                                                                                                self.prn_var.get(),
                                                                                                                self.id_var.get(),
                                                                                                                self.firstname_var.get(),
                                                                                                                self.lastname_var.get(),
                                                                                                                self.address1_var.get(),
                                                                                                                self.address2_var.get(),
                                                                                                                self.postcode_var.get(),
                                                                                                                self.mobile_var.get(),
                                                                                                                self.bookid_var.get(),
                                                                                                                self.booktitle_var.get(),
                                                                                                                self.author_var.get(),
                                                                                                                self.dateborrowed_var.get(),
                                                                                                                self.datedue_var.get(),
                                                                                                                self.daysonbook_var.get(),
                                                                                                                self.lateratefine_var.get(),
                                                                                                                self.dateoverdue_var.get(),
                                                                                                                self.finalprice_var.get(),
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo('Success', 'Member has been successfully Updated')

    def update(self):
        conn = obdc.connect(connection_string)
        cursor = conn.cursor
        cursor.execute('update library set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address1=%s, Address2=%s, PostId=%s, Mobile=%s, Bookid=%s, Booktitle=%s, Author=%s, dateborrowed=%s, datedue=%s, daysonbook=%s, latereturnfine=%s, dateoverdue=%s, finalprice=%s where PRN_NO=%s')

    def fetch_data(self):
        conn = obdc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute('select top (1) * from mylibrary')
        rows = cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert('', END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4])
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17]),

    def showData(self):
        self.txtBox.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.prn_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.id_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.firstname_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.lastname_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.address1_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.address2_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.postcode_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.mobile_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.bookid_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.booktitle_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.author_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.dateborrowed.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.datedue_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.daysonbook_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.lateratefine_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.dateoverdue_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')
        self.finalprice_var.insert(END, 'Member Type\t\t' + self.member_var.get() + '\n')

    def reset(self):
        self.member_var.set(''),
        self.prn_var.set(''),
        self.id_var.set(''),
        self.firstname_var.set(''),
        self.lastname_var.set('')
        self.address1_var.set(''),
        self.address2_var.set(''),
        self.postcode_var.set(''),
        self.mobile_var.set(''),
        self.bookid_var.set(''),
        self.booktitle_var.set(''),
        self.author_var.set(''),
        self.dateborrowed_var.set(''),
        self.datedue_var.set(''),
        self.daysonbook_var.set(''),
        self.lateratefine_var.set(''),
        self.dateoverdue_var.set(''),
        self.finalprice_var.set(''),
        self.txtBox.delete('1.0', END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno('Library Management System', 'Do you want to exit')
        if iExit > 0:
            self.root.destroy()

    def delete(self):
        if self.prn_var.get() == '' or self.id_var.get() == '':
            messagebox.showerror('Error', 'First select the Member')
        else:
            conn = obdc.connector(connection_string)
            cursor = conn.cursor
            query = 'delete from library where PRN_No=%s'
            value = (self.prn_var.get())

            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo('Success', 'Member has been Deleted')



if __name__ == '__main__':
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
