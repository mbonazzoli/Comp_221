from Tkinter import *

# Global Variables
BACKGROUND = 'lavender'
rootWin = None
title_label = None
create_user_button = None
create_pass_button = None
main_frame = None
button_frame = None

signupWin = None
signup_label = None
new_username_label = None
new_username_Entry = None
new_password_label = None
new_password_button = None
new_user_label = None
new_user_submit_button = None

loginWin = None
login_label = None
username_label = None
username_Entry = None
password_label = None
password_button = None
correct_login_label = None
user_submit_button = None



def gui_main():
    global rootWin, title_label, create_pass_button, create_user_button, main_frame, button_frame

    # create the main GUI window
    rootWin = Tk()
    rootWin.title("Audio Password 2.0")
    rootWin.config(bg=BACKGROUND)

    title_label = Label(rootWin, font='Arial 24 bold', text='Audio Password', justify='center', bg=BACKGROUND)
    title_label.grid(row=0, column=0, columnspan=2)

    create_user_button = Button(rootWin, command=create_user, text='Create User', font='Arial 14')
    create_user_button.grid(row=1, column=0)

    create_pass_button = Button(rootWin, command=sign_in, text='Login', font='Arial 14')
    create_pass_button.grid(row=1, column=1)

    rootWin.mainloop()


def create_user():
    global signupWin, signup_label, new_username_Entry, new_password_button, new_user_label, new_username_label,\
        new_password_label, new_user_submit_button

    signupWin = Tk()
    signupWin.title("New User")
    signupWin.config(bg=BACKGROUND)

    # Title
    signup_label = Label(signupWin, font='Arial 24 bold', text='Sign-up Here', justify='center', bg=BACKGROUND)
    signup_label.grid(row=0, column=0, columnspan=3)

    # Username section
    new_username_label = Label(signupWin, font='Arial 12 bold', text='New Username:', bg=BACKGROUND)
    new_username_label.grid(row=1, column=0)
    new_username_Entry = Entry(signupWin, font='Arial 12', text='Username')
    new_username_Entry.grid(row=1, column=1)

    # Password Section
    new_password_label = Label(signupWin, font='Arial 12 bold', text='New Password:', bg=BACKGROUND)
    new_password_label.grid(row=2, column=0)
    new_password_button = Button(signupWin, command=record_password, text='Record', font='Arial 12')
    new_password_button.grid(row=2, column=1)

    # submit button
    new_user_submit_button = Button(signupWin, command=create_new_user, font='Arial 12', text='Submit')
    new_user_submit_button.grid(row=3, column=0, columnspan=2)

    # Message after submit
    new_user_label = Label(signupWin, font='Arial 12', foreground='red', text=None, background=BACKGROUND)
    new_user_label.grid(row=4, column=0, columnspan=2)


def sign_in():
    global loginWin, login_label, username_label, username_Entry, password_label, password_button, correct_login_label,\
        user_submit_button
    loginWin = Tk()
    loginWin.title("Account Log-in")
    loginWin.config(bg='lavender')

    # Title
    login_label = Label(loginWin, font='Arial 24 bold', text='Log-in Here', justify='center', bg='lavender')
    login_label.grid(row=0, column=0, columnspan=3)

    # username Section
    username_label = Label(loginWin, font='Arial 12 bold', text='Username:', bg='lavender')
    username_label.grid(row=1, column=0)
    username_Entry = Entry(loginWin, font='Arial 12', text='Username')
    username_Entry.grid(row=1, column=1)

    # Password Section
    password_label = Label(loginWin, font='Arial 12 bold', text='Password:', bg='lavender')
    password_label.grid(row=2, column=0)
    password_button = Button(loginWin, command=record_password, text='Record', font='Arial 12')
    password_button.grid(row=2, column=1)

    # submit button
    user_submit_button = Button(loginWin, command=create_new_user, font='Arial 12', text='Submit')
    user_submit_button.grid(row=3, column=0, columnspan=2)

    # Message after submit
    correct_login_label = Label(loginWin, font='Arial 12', foreground='red', text=None, background='lavender')
    correct_login_label.grid(row=4, column=0, columnspan=2)

    pass

def locate_user():
    pass

def create_new_user():
    pass

def record_password():
    pass

    signupWin.mainloop()
gui_main()

