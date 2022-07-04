from importlib.metadata import PathDistribution
from tkinter import *
from turtle import width

# Imp 
root = Tk()
frame = Frame(root,width=700, height=700, bg="powder blue").place(x=5,y=8)
root.geometry("1550x800+0+0")
root.config(bg="powder blue")
#

# Frame Box
secondFrame = Frame(root, bd=10, relief=RIDGE, padx=20, bg="powder blue")
secondFrame.place(x=0, y=65, width=1535.5, height=400)
#

# Headline
headlineLabel = Label(frame, text="LIBRARY MANAGEMENT SYSTEM",font=('Arial',20,"bold"), bg="powder blue", bd=10, relief=RIDGE, fg="green", padx=2, pady=6)
headlineLabel.pack(side=TOP, fill=X)
#
# Label
libraryMembershipInfoLabel = Label(secondFrame, text="Library Membership Information", bg="powder blue", font=('Arial',10))
libraryMembershipInfoLabel.place(x=10, y=8)
#
# MemberType
memberTypeLabel = Label(secondFrame, text="Member Type", bg="powder blue", font=("Arial",10))
memberTypeLabel.place(x=25, y=40)
#
# PRN No
prnNoLabel = Label(secondFrame, text="PRN No:", bg="powder blue", font=('Arial',10))
prnNoLabel.place(x=25, y=72)
prnNoEntry = Entry(secondFrame)
prnNoEntry.place(x=130, y=72, width=220)
#
# ID No
idNoLabel = Label(secondFrame, text="ID No:", bg="powder blue", font=('Arial',10))
idNoLabel.place(x=25, y=104)
idNoEntry = Entry(secondFrame)
idNoEntry.place(x=130, y=104, width=220)
#
# First Name
firstNameLabel = Label(secondFrame, text="First Name:", bg="powder blue", font=('Arial',10))
firstNameLabel.place(x=25, y=136)
firstNameEntry = Entry(secondFrame)
firstNameEntry.place(x=130, y=136, width=220)
#
# Surname
surNameLabel = Label(secondFrame, text="Sur Name:", bg="powder blue", font=('Arial',10))
surNameLabel.place(x=25, y=168)
surNameEntry = Entry(secondFrame)
surNameEntry.place(x=130, y=168, width=220)
#
# Address 1
address1Label = Label(secondFrame, text="Adress 1:", bg="powder blue", font=('Arial',10))
address1Label.place(x=25, y=200)
address1Entry = Entry(secondFrame)
address1Entry.place(x=130, y=200, width=220)
#
# Address 2
address2Label = Label(secondFrame, text="Adress 2:", bg="powder blue", font=('Arial',10))
address2Label.place(x=25, y=232)
address2Entry = Entry(secondFrame)
address2Entry.place(x=130, y=232, width=220)
#
# Post Code
postCodeLabel = Label(secondFrame, text="Post Code:", bg="powder blue", font=('Arial',10))
postCodeLabel.place(x=25, y=264)
postCodeEntry = Entry(secondFrame)
postCodeEntry.place(x=130, y=264, width=220)
#
# Mobile Number
mobileNumberLabel = Label(secondFrame, text="Mobile Number:", bg="powder blue", font=('Arial',10))
mobileNumberLabel.place(x=25, y=296)
mobileNumberEntry = Entry(secondFrame)
mobileNumberEntry.place(x=130, y=296, width=220)
#
# Book ID
bookIDLabel = Label(secondFrame, text="Book ID:", bg="powder blue", font=('Arial', 10))
bookIDLabel.place(x=380, y=40)
bookIDEntry = Entry(secondFrame)
bookIDEntry.place(x=485, y=40, width=220)
#
# Book Title
bookTitleLabel = Label(secondFrame, text="Book Title:", bg="powder blue", font=('Arial', 10))
bookTitleLabel.place(x=380, y=72)
bookTitleEntry = Entry(secondFrame)
bookTitleEntry.place(x=485, y=72, width=220)
#
# Author Name
authorNameLabel = Label(secondFrame, text="Author Name:", bg="powder blue", font=('Arial', 10),)
authorNameLabel.place(x=380, y=104)
authorNameEntry = Entry(secondFrame)
authorNameEntry.place(x=485, y=104, width=220)
#
# Date Borrowed
dateBorrowedLabel = Label(secondFrame, text="Date Borrowed:", bg="powder blue", font=('Arial', 10))
dateBorrowedLabel.place(x=380, y=136)
dateBorrowedEntry = Entry(secondFrame)
dateBorrowedEntry.place(x=485, y=136, width=220)
#
# Date Due
dateDueLabel = Label(secondFrame, text="Date Due:", bg="powder blue", font=('Arial', 10))
dateDueLabel.place(x=380, y=168)
dateDueEntry = Entry(secondFrame)
dateDueEntry.place(x=485, y=168, width=220)
#
# Days Borrowed
daysBorrowedLabel = Label(secondFrame, text="Date Borrowed:", bg="powder blue", font=('Arial', 10))
daysBorrowedLabel.place(x=380, y=200)
daysBorrowedEntry = Entry(secondFrame)
daysBorrowedEntry.place(x=485, y=200, width=220)
#
# Late Return Fee
LateReturnFeeLabel = Label(secondFrame, text="Date Due:", bg="powder blue", font=('Arial', 10))
LateReturnFeeLabel.place(x=380, y=232)
LateReturnFeeEntry = Entry(secondFrame)
LateReturnFeeEntry.place(x=485, y=232, width=220)
#
# Date Overdue
dateOverdueLabel = Label(secondFrame, text="Date Overdue:", bg="powder blue", font=('Arial', 10))
dateOverdueLabel.place(x=380, y=264)
dateOverdueEntry = Entry(secondFrame)
dateOverdueEntry.place(x=485, y=264, width=220)
#
# Total Price
totalPriceLabel = Label(secondFrame, text="Total Price:", bg="powder blue", font=('Arial', 10))
totalPriceLabel.place(x=380, y=296)
totalPriceEntry = Entry(secondFrame)
totalPriceEntry.place(x=485, y=296, width=220)
#

# Book Details Label
bookDetailsLabel = Label(secondFrame, text="Book Details", bg="powder blue", font=('Arial', 10))
bookDetailsLabel.place(x=850, y=8)
#
# Book Details Scrollbar
bookDetailsScrollbar = Scrollbar(secondFrame)
bookDetailsScrollbar.place(x=865, y=40, width=500, height=278)
#

# Third Frame
thirdFrame = Frame(root, bd=10, relief=RIDGE, padx=20, bg="powder blue")
thirdFrame.place(x=0, y=465, width=1535.5, height=80)
#

# Add Data Button
addDataButton = Button(thirdFrame, text="ADD DATA", activebackground="red", font=('Arial', 12))
addDataButton.place(x=0, y=0, width=250, height=59)
#
# Show Data Button
showDataButton = Button(thirdFrame, text="ADD DATA", activebackground="red", font=('Arial', 12))
showDataButton.place(x=250, y=0, width=250, height=59)
#
# Update Button
updateButton = Button(thirdFrame, text="UPDATE", activebackground="red", font=('Arial', 12))
updateButton.place(x=500, y=0, width=250, height=59)
#
# Delete Butotn
deleteButton = Button(thirdFrame, text="DELETE", activebackground="red", font=('Arial', 12))
deleteButton.place(x=750, y=0, width=250, height=59)
#
# Reset Button
resetButton = Button(thirdFrame, text="RESET", activebackground="red", font=('Arial', 12))
resetButton.place(x=1000, y=0, width=250, height=59)
#
# Exit Button
exitButton = Button(thirdFrame, text="EXIT", activebackground="red", font=('Arial', 12))
exitButton.place(x=1250, y=0, width=240, height=59)
#

# Fourth Frame
fourthFrame = Frame(root, bd=10, relief=RIDGE, padx=20, bg="powder blue")
fourthFrame.place(x=0, y=545, width=1535.5, height=295)
#

# Customer Details Scrollbar
customerScrollbar = Scrollbar(fourthFrame)
customerScrollbar.place(x=0, y=10, width=1480, height=250)
#
root.mainloop()