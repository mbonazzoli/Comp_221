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

    title_label = Label(rootWin, font = 'Arial 30 bold', text = 'Welcome to the future.', justify = 'center')
    # todo

    button_frame = Frame(rootWin)
    button_frame.grid(row=1, column=0)
    create_user_button = Button(button_frame, text='Create User', font='Arial 24')



    rootWin.mainloop()

gui_main()

