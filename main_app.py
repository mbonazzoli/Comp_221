import record_data
import convert
import compare
from Tkinter import *

# Global Variables

rootWin = None
title_label = None
create_user_button = None
create_pass_button = None
main_frame = None
button_frame = None


def gui_main():
    global rootWin, title_label, create_pass_button, create_user_button, main_frame, button_frame

    # create the main GUI window
    rootWin = Tk()
    rootWin.title("Audio Password 2.0")
    rootWin.config(bg = 'lavender')

    title_label = Label(rootWin, font='Arial 30 bold', text='Welcome to the future', justify='center')
    title_label.grid(row=0, column=0, columnspan=2)

    create_user_button = Button(rootWin, text='Create User', font='Arial 24', justify='left')
    create_user_button.grid(row=1, column=0)

    create_pass_button = Button(rootWin, text='Create User', font='Arial 24', justify='right')
    create_pass_button.grid(row=1, column=1)

    rootWin.mainloop()

gui_main()

