from Tkinter import *
import record_data as rd
import convert
import compare

# Global Variables
# Main Window Variables
BACKGROUND = 'lavender'
rootWin = None
title_label = None
create_user_button = None
create_pass_button = None
action_label = None

# Signup Window Variables
signupWin = None
signup_label = None
new_username_label = None
new_username_Entry = None
new_password_label = None
new_password_button = None

new_user_submit_button = None

# Login Window Variables
loginWin = None
login_label = None
username_label = None
username_Entry = None
password_label = None
password_button = None

user_submit_button = None

# User Storage
users = {}
user_name = None
user_password = None
password_attempt = None

# Record Window
recordWin = None
record_Label = None
temp_sample_width = None
temp_data = None


def gui_main():
    global rootWin, title_label, create_pass_button, create_user_button, action_label

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

    # Message after submit
    action_label = Label(signupWin, font='Arial 12', foreground='red', text=None, background=BACKGROUND)
    action_label.grid(row=2, column=0, columnspan=2)

    rootWin.mainloop()


def create_user():
    global signupWin, signup_label, new_username_Entry, new_password_button, new_user_label, new_username_label,\
        new_password_label, new_user_submit_button, is_user_password

    is_user_password = True

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


def sign_in():
    global loginWin, login_label, username_label,username_Entry, password_label, password_button, correct_login_label,\
        user_submit_button
    loginWin = Tk()
    loginWin.title("Account Log-in")
    loginWin.config(bg=BACKGROUND)

    # Title
    login_label = Label(loginWin, font='Arial 24 bold', text='Log-in Here', justify='center', bg=BACKGROUND)
    login_label.grid(row=0, column=0, columnspan=3)

    # Username Section
    username_label = Label(loginWin, font='Arial 12 bold', text='Username:', bg=BACKGROUND)
    username_label.grid(row=1, column=0)
    username_Entry = Entry(loginWin, font='Arial 12', text='Username')
    username_Entry.grid(row=1, column=1)

    # Password Section
    password_label = Label(loginWin, font='Arial 12 bold', text='Password:', bg=BACKGROUND)
    password_label.grid(row=2, column=0)
    password_button = Button(loginWin, command=record_password, text='Record', font='Arial 12')
    password_button.grid(row=2, column=1)

    # Submit button
    user_submit_button = Button(loginWin, command=locate_user, font='Arial 12', text='Submit')
    user_submit_button.grid(row=3, column=0, columnspan=2)

    signupWin.mainloop()


def locate_user():
    global user_name, temp_sample_width, temp_data, loginWin, new_username_Entry, signupWin, action_label
    user_name = username_Entry.get()
    if user_name in users:
        password_data = users[user_name]

        path = 'attempt.wav'
        rd.record_to_file(temp_sample_width, temp_data, path)
        attempt_data = convert.process_audio(path)

        if compare.compare_data(password_data, attempt_data):
            action_label['text'] = 'You have been granted access to the profile of ' + user_name +\
                                   '\n correctness: '+compare.correctness
        else:
            action_label['text'] = 'The password had a correctness value of '+str(compare.correctness)+'\n password denied.'
    else:
        action_label['text'] = 'Incorrect username, try again.'

    # resets the recorded data
    temp_sample_width = None
    temp_data = None

    loginWin.destroy()


def create_new_user():
    global user_name, temp_sample_width, temp_data, loginWin, new_username_Entry, signupWin, action_label
    user_name = new_username_Entry.get()
    path = 'audio_file.wav'
    rd.record_to_file(temp_sample_width, temp_data, path)
    password_data = convert.process_audio(path)

    users[user_name] = password_data

    action_label['text'] = 'Profile has been create for '+user_name

    # resets the recorded data
    temp_sample_width = None
    temp_data = None

    signupWin.destroy()


def record_password():
    global recordWin, record_Label, temp_data, temp_sample_width
    recordWin = Tk()
    recordWin.title('Record')
    recordWin.config(height=200, width=150, bg=BACKGROUND)

    record_Label = Label(recordWin, text='Please speak a word into the microphone.', font='Arial 12', bg=BACKGROUND)
    record_Label.grid(row=0, column=0)
    temp_sample_width, temp_data = rd.record()
    record_Label['text'] = 'Recording Finished'

    recordWin.mainloop()


gui_main()

