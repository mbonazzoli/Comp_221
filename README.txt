Audio Password Program created by Matthew Bonazzoli, Brett Graham, and Garret Eichhorn

This program is written in Python 2.7 and relies on the built in python libraries and two imported libraries, pyaudio
and NumPy. Use of the fft and subsequent conversion into a comparable data types were made possible with the help from Bret
Jackson. The audio recorder code was implemented from an open source code supplied by a response from user 'cryo' at
http://stackoverflow.com/questions/892199/detect-record-audio-in-python.

This code runs through the audio_password_app.py, which is the interface for the program. We tested specific recorded
data to see the accuracy of our program. These files are saved within the Test_Files folder and can be run using the
commented out code at the end of the compare.py file.

The root window of the interface is structured with a label and two buttons. The user is given two options denoted by
the buttons, 'Create User' and 'Login'. If the button 'Create User' is selected the user is taken to a separate window
where they enter a username and record a password, which is done by pressing the record button and then immediately
saying the password. The user can then submit the password by pressing the submit button. The username and password is
then stored in a users dictionary. If the user selects the 'Login' button they are taken to a new window where they
enter in their username and record their password in the same steps as was done in the 'Create User' window. If the
password is deemed a match through our compare method a label on the main screen will say that the password is a match.
If the password is not a match the main screen will have a message saying the percent match and that the password was
incorrect.