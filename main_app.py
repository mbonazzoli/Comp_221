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

    main_frame = Frame(rootWin)
    main_frame.grid(row = 0, column = 0)
    title_label = Label(main_frame, font = 'Arial 30 Bold', text = 'Welcome to the future.', justify = 'CENTER')




    rootWin.mainloop()

gui_main()

