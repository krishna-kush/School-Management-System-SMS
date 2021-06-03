from tkinter import *
from matplotlib import pyplot as pl
import numpy as np, connect_mysql, idgenerator, encrept

# (Pending) Stop printing output in console...

def register():
    global root
    root.destroy()

    def back():
        global root
        root.destroy()
        start()

    def submit():
        if fee_status_val.get() == 0:
            fee_status = 'Not Pending'
        else:
            fee_status = 'Pending'
        if pending_fee_val.get() == '':
            pending_fee_val.set("Null")

        # Encrepting Values
        name = encrept.encode(f'{first_name_val.get()} {last_name_val.get()}').split()
        first_name = name[0]
        last_name = name[-1]
        clas = clas_val.get().upper()
        clas = encrept.encode(clas)
        id_stu = encrept.encode(idgenerator.get_id())
        # fee_status = encrept.encode(fee_status)
        # pending_fee = encrept.encode(pending_fee_val.get())

        connect_mysql.add_student(first_name, last_name, clas, id_stu, fee_status, pending_fee_val.get())

        Label(root, text = "SUBMITED").grid(row = 5) 

    root = Tk()
    root.title("Registration")

    # creatings labes and grid them
    Label(root, text="First Name").grid()
    Label(root, text="Last Name").grid(row = 1)
    Label(root, text="Class").grid(row = 2)
    Label(root, text = "Pending Fee(Leave If Not Pending)").grid(row = 4)

    # Creating tings to store data
    first_name_val = StringVar()
    last_name_val = StringVar()
    clas_val = StringVar()
    fee_status_val = IntVar()
    pending_fee_val = StringVar()

    # creating entries and grid them
    Entry(root, textvariable = first_name_val).grid(row = 0, column = 1)
    Entry(root, textvariable = last_name_val).grid(row = 1, column = 1)
    Entry(root, textvariable = clas_val).grid(row = 2, column = 1)
    Checkbutton(root, text = "Fee_Status(If Pending Check The Box)", variable = fee_status_val).grid(row = 3, column = 0)
    Entry(root, textvariable = pending_fee_val).grid(row = 4, column = 1)

    Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2, row=6)
    Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = back).grid(pady = 2, row=7)

    root.mainloop()

def get_info():
    global root
    root.destroy()

    def back():
        global root
        root.destroy()
        start()

    def s_name():
        def submit():
            global root
            root.destroy()

            root = Tk()
            root.title("Result")
            extra = encrept.encode(search_name.get()).split()
            ls = connect_mysql.name_search_student(extra)

            for i in range(len(ls)//7):
                temp = i*7
                name = encrept.decode(f'{ls[temp]} {ls[temp+1]}').split()
                Label(root, text = f"NAME : {name[0]} {name[-1]}").pack()
                Label(root, text = f"Class : {encrept.decode(ls[temp+2])}").pack()
                Label(root, text = f"Roll_No : {ls[temp+3]}").pack()
                Label(root, text = f"ID : {encrept.decode(ls[temp+4])}").pack()
                Label(root, text = f"Fee Status : {ls[temp+5]}").pack()
                Label(root, text = f"Pending Fee : {ls[temp+6]}").pack()
                if i != (len(ls)//7)-1:
                    Label(root, text = f"------------------------------------------------").pack()


            Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = s_name).pack(pady = 2)
            Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).pack(pady = 2)

            root.mainloop()

        global root
        root.destroy()
        root = Tk()
        root.title("Search By Name")

        Label(root, text = "Enter Student\'s Full Name").grid()
        search_name = StringVar()
        Entry(root, textvariable = search_name).grid(row = 0, column = 1)

        Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2, row = 1)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = get_info).grid(pady = 2, row = 2)

        root.mainloop()

    def s_class():
        def submit():
            global root
            root.destroy()

            root = Tk()
            root.title("Result")
            extra = encrept.encode(search_class.get())
            ls = connect_mysql.class_search_student(extra)

            for i in range(len(ls)//7):
                temp = i*7
                name = encrept.decode(f'{ls[temp]} {ls[temp+1]}').split()
                Label(root, text = f"NAME : {name[0]} {name[-1]}").pack()
                Label(root, text = f"Class : {encrept.decode(ls[temp+2])}").pack()
                Label(root, text = f"Roll_No : {ls[temp+3]}").pack()
                Label(root, text = f"ID : {encrept.decode(ls[temp+4])}").pack()
                Label(root, text = f"Fee Status : {ls[temp+5]}").pack()
                Label(root, text = f"Pending Fee : {ls[temp+6]}").pack()
                if i != (len(ls)//7)-1:
                    Label(root, text = f"------------------------------------------------").pack()


            Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = s_name).pack(pady = 2)
            Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).pack(pady = 2)

            root.mainloop()

        global root
        root.destroy()
        root = Tk()
        root.title("Search By Class")

        Label(root, text = "Enter Student\'s Class").grid()
        search_class = StringVar()
        Entry(root, textvariable = search_class).grid(row = 0, column = 1)

        Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2, row = 1)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = get_info).grid(pady = 2, row = 2)

        root.mainloop()


    def s_name_class():
        def submit():
            global root
            root.destroy()

            root = Tk()
            root.title("Result")
            extra = []
            every = search_name_class.get().split()
            name = encrept.encode(f'{every[0]} {every[1]}').split()
            for i in name:
                extra.append(i)
            extra.append(encrept.encode(every[2]))
            ls = connect_mysql.name_class_search_student(extra)

            for i in range(len(ls)//7):
                temp = i*7
                name = encrept.decode(f'{ls[temp]} {ls[temp+1]}').split()
                Label(root, text = f"NAME : {name[0]} {name[-1]}").pack()
                Label(root, text = f"Class : {encrept.decode(ls[temp+2])}").pack()
                Label(root, text = f"Roll_No : {ls[temp+3]}").pack()
                Label(root, text = f"ID : {encrept.decode(ls[temp+4])}").pack()
                Label(root, text = f"Fee Status : {ls[temp+5]}").pack()
                Label(root, text = f"Pending Fee : {ls[temp+6]}").pack()
                if i != (len(ls)//7)-1:
                    Label(root, text = f"------------------------------------------------").pack()

            Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = s_name).pack(pady = 2)
            Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).pack(pady = 2)

            root.mainloop()

        global root
        root.destroy()
        root = Tk()
        root.title("Search By Name And Class")

        Label(root, text = "Enter Student\'s First Name, Second Name And Class(seperated by space)").grid()
        search_name_class = StringVar()
        Entry(root, textvariable = search_name_class).grid(row = 0, column = 1)

        Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2, row = 1)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = get_info).grid(pady = 2, row = 2)

        root.mainloop()
    def s_id():
        def submit():
            global root
            root.destroy()

            root = Tk()
            root.title("Result")
            extra = encrept.encode(search_id.get())
            ls = connect_mysql.id_search_student(extra)

            for i in range(len(ls)//7):
                temp = i*7
                name = encrept.decode(f'{ls[temp]} {ls[temp+1]}').split()
                Label(root, text = f"NAME : {name[0]} {name[-1]}").pack()
                Label(root, text = f"Class : {encrept.decode(ls[temp+2])}").pack()
                Label(root, text = f"Roll_No : {ls[temp+3]}").pack()
                Label(root, text = f"ID : {encrept.decode(ls[temp+4])}").pack()
                Label(root, text = f"Fee Status : {ls[temp+5]}").pack()
                Label(root, text = f"Pending Fee : {ls[temp+6]}").pack()
                if i != (len(ls)//7)-1:
                    Label(root, text = f"------------------------------------------------").pack()

            Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = s_name).pack(pady = 2)
            Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).pack(pady = 2)

            root.mainloop()

        global root
        root.destroy()
        root = Tk()
        root.title("Search By ID")

        Label(root, text = "Enter Student\'s ID").grid()
        search_id = StringVar()
        Entry(root, textvariable = search_id).grid(row = 0, column = 1)

        Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2, row = 1)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = get_info).grid(pady = 2, row = 2)

        root.mainloop()

    root = Tk()
    root.title("Fetch Information")

    Button(root, bg = "lightgreen", fg = "blue", text = "Search By Name", command = s_name).grid(pady = 2)
    Button(root, bg = "lightgreen", fg = "blue", text = "Search By Class", command = s_class).grid(pady = 2)
    Button(root, bg = "lightgreen", fg = "blue", text = "Search By Name and Class", command = s_name_class).grid(pady = 2)
    Button(root, bg = "lightgreen", fg = "blue", text = "Search By ID", command = s_id).grid(pady = 2)
    Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = back).grid(pady = 2)

    mainloop()

def see_all_stu():
    global root
    root.destroy()

    def back():
        global root
        root.destroy()
        start()

    root = Tk()
    root.geometry("250x500")
    root.title("Get All Students Information")

    ls = connect_mysql.see_all_stu_tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root, yscrollcommand = scrollbar.set)

    for i in range(len(ls)//7):
        temp = i*7

        # BEFORE
        # Label(root, text = f"NAME : {ls[temp]} {ls[temp+1]}").pack()
        # Label(root, text = f"Class : {ls[temp+2]}").pack()
        # Label(root, text = f"Roll_No : {ls[temp+3]}").pack()
        # Label(root, text = f"ID : {ls[temp+4]}").pack()
        # Label(root, text = f"Fee Status : {ls[temp+5]}").pack()
        # Label(root, text = f"Pending Fee : {ls[temp+6]}").pack()

        # AFTER
        name = encrept.decode(f'{ls[temp]} {ls[temp+1]}').split()
        listbox.insert(END, f"NAME : {name[0]} {name[-1]}")
        listbox.insert(END, f"Class : {encrept.decode(ls[temp+2])}")
        listbox.insert(END, f"Roll_No : {ls[temp+3]}")
        listbox.insert(END, f"ID : {encrept.decode(ls[temp+4])}")
        listbox.insert(END, f"Fee Status : {ls[temp+5]}")
        listbox.insert(END, f"Pending Fee : {ls[temp+6]}")

        if i != (len(ls)//7)-1:
            # Label(root, text = f"------------------------------------------------").pack()
            listbox.insert(END, f"------------------------------------------------")

    listbox.pack(fill=BOTH, expand=1)
    scrollbar.config(command=listbox.yview)


    Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = back).pack(pady = 2)

    mainloop()

def update_stu_info():
    global root
    root.destroy()

    def back():
        global root
        root.destroy()
        start()

    def up_name():
        global root
        root.destroy()

        def submit():
            extra = encrept.encode(new_name.get()).split()
            connect_mysql.update_name(extra, encrept.encode(stu_id.get()))

        root = Tk()

        Label(root, text = "Enter New First Name And Last Name Of Student Seperated By Space").grid()

        new_name = StringVar()
        Entry(root, textvariable = new_name).grid(row = 0, column = 1)

        Label(root, text = "Enter Student\'s ID").grid()

        stu_id = StringVar()
        Entry(root, textvariable = stu_id).grid(row = 1, column = 1)

        Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = update_stu_info).grid(pady = 2)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).grid(pady = 2)

        root.mainloop()
    
    def up_class():
        global root
        root.destroy()

        def submit():
            # root.destroy()
            connect_mysql.update_class(encrept.encode(new_class.get()), encrept.encode(stu_id.get()))

        root = Tk()

        Label(root, text = "Enter New Class Of Student").grid()

        new_class = StringVar()
        Entry(root, textvariable = new_class).grid(row = 0, column = 1)

        Label(root, text = "Enter Student\'s ID").grid()

        stu_id = StringVar()
        Entry(root, textvariable = stu_id).grid(row = 1, column = 1)

        Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = update_stu_info).grid(pady = 2)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).grid(pady = 2)

        root.mainloop()

    def up_fee_status():
        global root
        root.destroy()

        def submit():
            global root
            root.destroy()
            root = Tk()

            if pending_fee.get() == "":
                pending_fee.set("Null")
            connect_mysql.update_id(fee_status.get(), pending_fee.get(), encrept.encode(stu_id.get()))

            Label(root, text = "DONE").grid()
            Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = up_fee_status).grid(pady = 2)
            Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).grid(pady = 2)

            root.mainloop()


        root = Tk()

        fee_status = IntVar()
        pending_fee = StringVar()

        Checkbutton(root, text = "Fee Pending(select if fee is pending)", variable = fee_status).grid()

        Label(root, text = "Pending Fee(leave if not pending)").grid()
        Entry(root, textvariable = pending_fee).grid()

        Label(root, text = "Enter Student\'s ID").grid()

        stu_id = StringVar()
        Entry(root, textvariable = stu_id).grid()

        Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = update_stu_info).grid(pady = 2)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).grid(pady = 2)

        root.mainloop()


    root = Tk()
    root.title("Update Student Information")

    Button(root, bg = "lightgreen", fg = "blue", text = "Update Student\'s Name", command = up_name).grid(pady = 2)
    Button(root, bg = "lightgreen", fg = "blue", text = "Update Student\'s Class", command = up_class).grid(pady = 2)
    Button(root, bg = "lightgreen", fg = "blue", text = "Update Student\'s Fee Status", command = up_fee_status).grid(pady = 2)
    Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = back).grid(pady = 2)

    mainloop()

def delete_stu_info():
    global root
    root.destroy()

    def back():
        global root
        root.destroy()
        start()

    def submit():
        global root
        root.destroy()
        root = Tk()

        connect_mysql.delete_student(encrept.encode(stu_id.get()))

        Label(root, text = "DONE").grid()
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = delete_stu_info).grid(pady = 2)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).grid(pady = 2)

        root.mainloop()

    root = Tk()
    root.title("Delete Student Information")

    Label(root, text = "Enter Student\'s ID").grid()
    stu_id = StringVar()
    Entry(root, textvariable = stu_id).grid(row = 0, column = 1)

    Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2)
    Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = back).grid(pady = 2)

    mainloop()

def roll_no_generator():
    global root
    root.destroy()

    def back():
        global root
        root.destroy()
        start()

    def submit():
        global root
        root.destroy()
        root = Tk()

        id_s = connect_mysql.class_search_student_for_roll_no_generator(encrept.encode(clas.get().upper()))
        for i, j in enumerate(id_s):
            connect_mysql.update_roll_no(i+1, j)

        Label(root, text = "GENERATED").grid()
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = delete_stu_info).grid(pady = 2)
        Button(root, bg = "lightgreen", fg = "blue", text = "BACK To MAIN MENU", command = back).grid(pady = 2)

        root.mainloop()

    root = Tk()
    root.title("Generate Roll No.")

    Label(root, text = "Enter Class").grid()
    clas = StringVar()
    Entry(root, textvariable = clas).grid(row = 0, column = 1)

    Button(root, bg = "lightgreen", fg = "blue", text = "SUBMIT", command = submit).grid(pady = 2)
    Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = back).grid(pady = 2)

    mainloop()



def settings():
    global root
    root.destroy()

    def back():
        global root
        root.destroy()
        start()

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
    Button(root, bg = "lightgreen", fg = "blue", text = "BACK", command = back).grid(pady = 2, row=7)

    root.mainloop()    

def statatics():

    # pl.subplot(x, y, z)
    fee_status = connect_mysql.statisics()
    print(type(fee_status))
    Not_Pending = 0
    Pending = 0

    for i in range(len(fee_status)):
        if fee_status[i][0] == "Not Pending":
            Not_Pending += 1
        if fee_status[i][0] == "Pending":
            Pending += 1
            
    pl.pie([Not_Pending, Pending], labels=["Not_Pending", "Pending"], explode=[0.03, 0])
    pl.title("FEE Status")
    pl.show()



def start():
    global root
    root = Tk()

    widthmin = 900
    heightmin = 600

    root.minsize(widthmin, heightmin)

    root.geometry(f"{widthmin+100}x{heightmin}")

    root.title("School Management System")

    Label(text = "WELCOME To SCHOOL MANAGEMENT SYSTEM\nby- KRISHNA KUSHWAHA", pady = 10, font = "BatmanForeverAlternate 20", bg = "green", fg = "blue").pack(fill = X)


    frame = Frame(root, bg = "white", borderwidth = 4, relief = SUNKEN)
    frame.pack(anchor = "n", pady = 200)

    # frame1 = Frame(root, bg = "white", borderwidth = 4, relief = SUNKEN)
    # frame1.pack(anchor = "nw")

    Button(frame, bg = "lightgreen", fg = "blue", text = "Register New Student", command = register).pack(side = LEFT, padx = 3, pady = 10)

    Button(frame, bg = "lightgreen", fg = "blue", text = "Get Student Info", command = get_info).pack(side = LEFT, padx = 3, pady = 10)

    Button(frame, bg = "lightgreen", fg = "blue", text = "See All Students Info", command = see_all_stu).pack(side = LEFT, padx = 3, pady = 10)

    Button(frame, bg = "lightgreen", fg = "blue", text = "Update Student Info...", command = update_stu_info).pack(side = LEFT, padx = 3, pady = 10)

    Button(frame, bg = "lightgreen", fg = "blue", text = "Delete Student Info...", command = delete_stu_info).pack(side = LEFT, padx = 3, pady = 10)
    
    Button(frame, bg = "lightgreen", fg = "blue", text = "Generate Roll No.", command = roll_no_generator).pack(side = LEFT, padx = 3, pady = 10)

    Button(frame, bg = "lightgreen", fg = "blue", text = "Get Statatics", command = statatics).pack(side = LEFT, padx = 3, pady = 10)

    Button(frame, bg = "green", fg = "blue", text = "Settings", command = settings).pack(side = LEFT, padx = 3, pady = 10)

    root.mainloop()


if __name__ == "__main__":
    start()
