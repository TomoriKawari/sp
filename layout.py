from dataclasses import dataclass
from logging import root
from tkinter import*
from tkinter import font
from tkinter import ttk
from turtle import width

from numpy import pad
from pyparsing import col



class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title('Library Management System')
        self.root.geometry('1550x800+0+0')

        lbltitle = Label(self.root, text='LIBRARY MANAGEMENT SYSTEM', bg='powder blue', fg='green', bd=20, relief=RIDGE, font=('arial', 50, 'bold'), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        frame.place(x=0, y=130, width=1530, height=400)


        # =========================== DATA FRAME LEFT =========================== #

        DataFrameLeft = LabelFrame(frame, text= 'Library Membership Information', bg='powder blue', fg='green', bd=12, relief=RIDGE, font=('arial', 12, 'bold'))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMembr = Label(DataFrameLeft, bg='powder blue', text='Member Type', font=('arial', 12, 'bold'), padx=2, pady=6)
        lblMembr.grid(row=0, column=0, sticky=W)

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
        listBox = Listbox(DataFrameRight, font=('Arial', 12, 'bold'), width=20, height=16)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)


        # =========================== BUTTONS FRAME =========================== #

        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        FrameButton.place(x=0, y=530, width=1530, height=60)

        btnAddData = Button(FrameButton, text='Add Data', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(FrameButton, text='Show Data', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(FrameButton, text='Update', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(FrameButton, text='Delete', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(FrameButton, text='Reset', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=4)

        btnAddData = Button(FrameButton, text='Exit', font=('Arial', 12, 'bold'), width=23, bg='blue', fg='white')
        btnAddData.grid(row=0, column=5)


        # =========================== INFO FRAME =========================== #

        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg='powder blue')
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_frame = Frame(FrameDetails, bd=6, relief=RIDGE, bg='powder blue')
        Table_frame.place(x=0, y=2, width=1460, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame, columns=('membertype', 'prnno', 'title', 'firstname', 'lastname', 'address1', 'address2', 'postid', 'mobile', 'bookid',
                                            'booktitle', 'author', 'dateborrowed', 'datedue', 'days', 'latereturnfine', 'dateoverdue', 'finalprice'), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading('membertype', text='Member Type')
        self.library_table.heading('prnno', text='Reference No.')
        self.library_table.heading('tile', text='Title')
        self.library_table.heading('firstname', text='First Name')
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



if __name__ == '__main__':
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()




# =========================== 43:58 =========================== #
