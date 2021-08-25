# Imports
import os
import sys


# Console message: File Open --> Success
def open_success():
    print(f_name, 'opened successfully.')


# Console message: File Open --> Fail
def open_fail():
    sys.stderr.write(f'The file {f_name} could not be opened. \nError: {os.strerror(e.errno)} \nProcessing '
                     f'aborted.')


# User input: file name
def get_f_name(file_type='text'):
    global f_name
    f_name = input(f"{file_type.capitalize()} file name: ")
    print("Opening file", f_name + '...')


# Lines 25-30: Try to open image file;
# Lines 33-39: Try to open message file;
# Lines 41-46: Append message to image
try:
    get_f_name('image')
    img = open(f_name, mode="a")
    open_success()
except IOError as e:
    open_fail()
else:
    try:
        get_f_name()
        txt = open(f_name, mode="r")
        open_success()
    except IOError as e:
        open_fail()
    else:
        print("Processing commencing...")
        msg = '\n\n' + txt.read()
        char = img.write(msg)
        print(f"Processing complete! {char} bytes written.")
        img.close()
        txt.close()
