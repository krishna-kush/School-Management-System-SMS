from tkinter import *

def submit():
    if name_val.get():
        with open('my_name', 'w') as t:
            t.write(name_val.get())
    if mysql_pass_val.get():
        with open('sql_pass', 'w') as t:
            t.write(mysql_pass_val.get())

    Label(root, text = "SUBMITED").grid(row = 3) 

root = Tk()
root.title("Settings")

# creatings labes and grid them
Label(root, text="Name").grid()
Label(root, text="MySQL Passwords").grid(row = 1)

# Creating tings to store data
name_val = StringVar()
mysql_pass_val = StringVar()

# creating entries and grid them
Entry(root, textvariable = name_val).grid(row = 0, column = 1)
Entry(root, textvariable = mysql_pass_val).grid(row = 1, column = 1)

Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2, row=6)

root.mainloop()  