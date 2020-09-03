from tkinter import *
import string
from random import *

main_window = Tk()
main_window.title("Password Generator")
main_window.geometry("500x400")
main_window.configure(bg="magenta")

global b1
global b2
global b3


def getpass():

    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    punctuations = list(string.punctuation)

    password = choice(lowercase) + choice(uppercase) + choice(punctuations) + choice(lowercase) + choice(uppercase) + choice(punctuations) + choice(lowercase) + choice(uppercase) + choice(punctuations)

    Label(generate_window, text=password, bg="magenta", fg="yellow", font=("MS Sherif", 30, "bold")).grid(row=2, column=0, columnspan=2)

    File = open("password.txt", "a")
    File.write(Field_entry.get() + "    :     " + password + "\n")
    File.close()


def generate():

    global generate_window
    global Field_entry

    generate_window = Toplevel()
    generate_window.title("Password Generator")
    generate_window.geometry("500x400")
    generate_window.configure(bg="magenta")

    L = Label(generate_window, text="Field  :  ", bg="magenta", fg="yellow", font=("MS Sherif", 20, "bold"))
    L.grid(row=0, column=0, padx=(70, 20), pady=(150,20))
    Field_entry = Entry(generate_window)
    Field_entry.grid(row=0, column=1, padx=(0, 30), pady=(150, 20), ipadx=50)
    Button(generate_window, text="Get Password", command=getpass).grid(row=1, column=0, columnspan=2, padx=90, ipadx=100)


def forget():
    File = open("password.txt", "r")
    l = File.read().split("\n")

    forget_window = Toplevel()
    forget_window.title("Password Generator")
    forget_window.configure(bg="magenta")

    for i in range(len(l)):
        if i == 0:
            Label(forget_window, text=l[i], bg="magenta", fg="yellow", font=("MS Sherif", 20, "bold")).pack(pady=(50,0), padx=20)
        else:
            Label(forget_window, text=l[i], bg="magenta", fg="yellow", font=("MS Sherif", 20, "bold")).pack(padx=20)

    File.close()


Label(main_window, text="Password Generator", bg="magenta", fg="yellow", font=("MS Sherif", 20, "bold")).pack(pady=(120, 30))
b1 = Button(main_window, text="Generate", font=("MS Sherif", 10), command=generate).pack(pady=(30, 15), ipadx=150)
b3 = Button(main_window, text="Forget Password", font=("MS Sherif", 10), command=forget).pack(ipadx=128)

main_window.mainloop()