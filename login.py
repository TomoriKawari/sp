from cgitb import text
from tkinter import*

class LogIn:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1550x800+0+0')
        self.root['bg'] = '#C6E2FF'

        LogInFrame = Frame(self.root, bd=12, bg='white')
        LogInFrame.place(width=750, height=450, anchor=CENTER, relx=.5, rely=.5)

        LogInLabel = Label(LogInFrame, text='ACCOUNT LOGIN', font=('arial', 18, 'bold'), bg='white', fg='#267FD7')
        LogInLabel.place(x=30, y=25)

        UsernameLabel = Label(LogInFrame, text='USERNAME', font=('arial', 10), bg='white', fg='#68696A')
        UsernameLabel.place(x=30, y=80)
        UsernameEntry = Entry(LogInFrame, font=('arial', 30), width=30, bg='#C5C5C6')
        UsernameEntry.place(x=30, y=110)

        PasswordLabel = Label(LogInFrame, text='PASSWORD', font=('arial', 10), bg='white', fg='#68696A')
        PasswordLabel.place(x=30, y=170)
        PasswordEntry = Entry(LogInFrame, font=('arial', 30), width=30, bg='#C5C5C6')
        PasswordEntry.place(x=30, y=200)

        LogInButton = Button(LogInFrame, text='LOG IN', font=('Arial', 11), bg='#2222DC', fg='white')
        LogInButton.place(x=160, y=300, width=400, height=50)

if __name__ == '__main__':
    root = Tk()
    obj = LogIn(root)
    root.mainloop()