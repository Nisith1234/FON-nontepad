import time
from tkinter import *
from tkinter import font
from tkinter import filedialog
import getpass
import pyautogui
from tkinter.messagebox import showerror, showwarning, showinfo
import win32api
import os
import subprocess

r = Tk()
r.title('Fon Notepad')
r.iconbitmap("fon.ico")
r.resizable(False, False)

def change_color():
    app4 = Tk()
    def color_change_thing():
        text.config(fg=e101.get())
    label38432 = Label(app4, text="Type the color you want?(example: lightblue)")
    e101 = Entry(app4, width=40)
    label38432.pack()
    e101.pack()
    enter1023 = Button(app4, text="Enter", command=color_change_thing)
    enter1023.pack()


def change_color_highlight():
    app4 = Tk()
    def color_change_thing_highlight():
        text.config(bg=e101.get())
    label38432 = Label(app4, text="Type the highlight color you want?(example: lightblue)")
    e101 = Entry(app4, width=40)
    label38432.pack()
    e101.pack()
    enter1023 = Button(app4, text="Enter", command=color_change_thing_highlight)
    enter1023.pack()

def format_box():
    app1 = Tk()
    def font_size():

        try:
            text.config(font=(e.get(), 16))
            app1.destroy()

        except ValueError:
            print("Should be a number")

    app1.resizable(False, False)
    app1.iconbitmap('document.ico')
    app1.title("Font")
    thibieru = Label(app1, text="what font do you want?(Please type correctly)")
    e = Entry(app1, width=40)
    enter_button = Button(app1, text='Enter', command=font_size)
    thibieru.grid(row=0, column=0)
    e.grid(row=1, column=0)
    enter_button.grid(row=2, column=0, columnspan=2)
    app1.mainloop()



def print_thing():
    file_name_thing = filedialog.askopenfilename()

    if file_name_thing:
        win32api.ShellExecute(0, "print", file_name_thing, None, '.', 0)

frame = Frame(r)
frame.grid(column=0, row=0)



def redo_thing():
    pyautogui.hotkey("ctrl", 'y')


def cut_thing():
    pyautogui.hotkey("ctrl", 'x')


def coppy_coppy():
    pyautogui.hotkey("ctrl", "c")


def paste_thing():
    pyautogui.hotkey("ctrl", "v")


def undo_thing():
    pyautogui.hotkey("ctrl", "z")


def save_new():
    global path_name
    path_name = filedialog.asksaveasfilename(initialdir=f'C:/Users/{getpass.getuser()}/Desktop', title='save')
    if path_name == '':
        pass

    else:
        ajfosj = f"{path_name}"
        open(ajfosj, 'w').write(text.get(1.0, END))
        button101.config(state=NORMAL)


def new_thing():
    def on_leave1(e):
        pass

    def on_enter1(e):
        button1.config(fg="black", bg="white")

    def on_leave1(e):
        button1.config(bg="black", fg="white")

    def on_enter2(e):
        button2.config(fg="black", bg="white")

    def on_leave2(e):
        button2.config(bg="black", fg="white")

    def on_enter3(e):
        button3.config(fg="black", bg="white")

    def on_leave3(e):
        button3.config(bg="black", fg="white")

    app = Tk()
    app.attributes('-alpha', 0.8)
    app.configure(background='black')

    def yes_save():
        app.destroy()
        save_new()

    def no_need():
        text.delete(1.0, END)
        app.destroy()

    app.overrideredirect(1)
    label1011221 = Label(app, text="Have you saved the file?", bg="black", fg="white")
    label1011221.pack()
    button1 = Button(app, text="No need to save it!", command=no_need, bg="black", fg="white")
    button1.bind("<Enter>", on_enter1)
    button1.bind("<Leave>", on_leave1)
    button1.pack()
    button2 = Button(app, text="Yes return and save!", command=yes_save, bg="black", fg="white")
    button2.bind("<Enter>", on_enter2)
    button2.bind("<Leave>", on_leave2)
    button2.pack()
    button3 = Button(app, text="I have already saved it!", command=no_need, bg="black", fg="white")
    button3.bind("<Enter>", on_enter3)
    button3.bind("<Leave>", on_leave3)
    button3.pack()

    app.mainloop()


def run_this():
    if path_name[-1] == 'y':
        print("THE WINDOW WILL STOP RESPONDING RIGHT NOW, TO MAKE IT RESPOND CROSS OUT THE NEW CONSLE")
        commandsf = f'python {path_name}'
        subprocess.call(commandsf, creationflags=subprocess.CREATE_NEW_CONSOLE)
        # os.system(commandsf)

    elif path_name[-1] == 'l':
        pyautogui.hotkey('win', 'r')
        pyautogui.write(path_name)
        pyautogui.press('enter')

def open_thing():
    path = filedialog.askopenfilename()
    if path == '':
        pass
    else:
        print(path)
        text.delete(1.0, END)
        file_input = open(path, 'r').read()
        text.insert(END, file_input)
        button101.config(state=DISABLED)


text_scroll = Scrollbar(frame)
text_scroll.pack(side=RIGHT, fill=Y)
text = Text(frame, width=97, height=25, font=('Helvetica', 16), selectbackground='lightblue', selectforeground='black',
            undo=True, yscrollcommand=text_scroll.set)
text.pack(pady=5)
text_scroll.config(command=text.yview)


my_menu = Menu(r)
r.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='New', command=new_thing)
file_menu.add_command(label='Open', command=open_thing)
file_menu.add_command(label='Save', command=save_new)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=r.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Redo', command=redo_thing)
edit_menu.add_command(label='Undo', command=undo_thing)
edit_menu.add_separator()
edit_menu.add_command(label='Copy', command=coppy_coppy)
edit_menu.add_command(label='Cut', command=cut_thing)
edit_menu.add_command(label='Paste', command=paste_thing)
button101 = Button(r, text="RUN NOW!", state=DISABLED, command=run_this)
button101.grid(row=10, column=0)

print_menu = Menu(my_menu)
my_menu.add_cascade(label='Print', menu=print_menu)
print_menu.add_command(label="print", command=print_thing)

format_menu = Menu(my_menu)
my_menu.add_cascade(label='Format', menu=format_menu)
format_menu.add_command(label="Font", command=format_box)
format_menu.add_command(label="Font Color", command=change_color)
format_menu.add_command(label="Background Color", command=change_color_highlight)

r.mainloop()
