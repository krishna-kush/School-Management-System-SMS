import mysql.connector

with open('sql_pass') as t:
    passwd = t.read()

db = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    passwd = passwd
    )
    
cr = db.cursor()

# Making Table in MySql if not exsist...
with open('sql_table_exsist.txt',) as t:
    temp = t.read()   
    if temp == "false":
        with open('sql_table_exsist.txt', 'w') as t:
            t.write("true")
        cr.execute("create database project_SMS")    # put if not exsist command here...    
        cr.execute("use project_SMS")       
        cr.execute("create table Students(First_Name char(20),Last_Name char(20),Class varchar(5),Roll_No int(5) default Null,ID varchar(15) primary key,FEE_Status char(15) not null, Pending_Fee int(10))")
    else:
        cr.execute("use project_SMS")       

def add_student(first_name, last_name, clas, id_stu, fee_status, pending_fee):
    cr.execute(f"insert into students values('{first_name}','{last_name}','{clas}',null,'{id_stu}','{fee_status}',{pending_fee})")
    db.commit()

def search_student(how, extra):
    if how == 1:
        cr.execute(f"select * from students where first_name = '{extra[0]}' and last_name = '{extra[1]}'")
        for row in cr:
            print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")
        
    if how == 2:
        cr.execute(f"select * from students where class = '{extra}'")
        for row in cr:
            print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")

    if how == 3:
        cr.execute(f"select * from students where first_name = '{extra[0]}' and last_name = '{extra[1]}' and class = '{extra[2]}'")
        for row in cr:
            print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")

    if how == 4:
        cr.execute(f"select * from students where id = '{extra}'")
        for row in cr:
            print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")

def name_search_student(extra):
    cr.execute(f"select * from students where first_name = '{extra[0]}' and last_name = '{extra[1]}'")
    ls = []
    for row in cr:
        # print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")
        ls.append(row[0])
        ls.append(row[1])
        ls.append(row[2])
        ls.append(row[3])
        ls.append(row[4])
        ls.append(row[5])
        ls.append(row[6])
    return ls

def class_search_student(extra):
    cr.execute(f"select * from students where class = '{extra}'")
    ls = []
    for row in cr:
        # print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")
        ls.append(row[0])
        ls.append(row[1])
        ls.append(row[2])
        ls.append(row[3])
        ls.append(row[4])
        ls.append(row[5])
        ls.append(row[6])
    return ls

def class_search_student_for_roll_no_generator(extra):
    cr.execute(f"select id from students where class='{extra}' order by first_name;")
    ls = []
    for row in cr:
        # print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")
        ls.append(row[0])
        # ls.append(row[1])
        # ls.append(row[2])
        # ls.append(row[3])
        # ls.append(row[4])
        # ls.append(row[5])
        # ls.append(row[6])
    return ls
    # print(ls)
    
def name_class_search_student(extra):
    cr.execute(f"select * from students where first_name = '{extra[0]}' and last_name = '{extra[1]}' and class = '{extra[2]}'")
    ls = []
    for row in cr:
        # print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")
        ls.append(row[0])
        ls.append(row[1])
        ls.append(row[2])
        ls.append(row[3])
        ls.append(row[4])
        ls.append(row[5])
        ls.append(row[6])
    return ls

def id_search_student(extra):
    cr.execute(f"select * from students where id = '{extra}'")
    ls = []
    for row in cr:
        # print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")
        ls.append(row[0])
        ls.append(row[1])
        ls.append(row[2])
        ls.append(row[3])
        ls.append(row[4])
        ls.append(row[5])
        ls.append(row[6])
    return ls

def see_all_stu():
    cr.execute("select*from students")
    for row in cr:
        print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")

def see_all_stu_tk():
    cr.execute("select*from students")
    ls = []
    for row in cr:
        # print(f"Name : {row[0]} {row[1]}\nClass : {row[2]}\nRoll_No : {row[3]}\nID : {row[4]}\nFee_Status : {row[5]}\nPending_Fee : {row[6]}\n")
        ls.append(row[0])
        ls.append(row[1])
        ls.append(row[2])
        ls.append(row[3])
        ls.append(row[4])
        ls.append(row[5])
        ls.append(row[6])
    return ls

def update_student(how, extra, stu_id):
    if how == 1:
        cr.execute(f"update students set first_name = '{extra[0]}', last_name = '{extra[1]}' where id = '{stu_id}'")
        db.commit()

    if how == 2:
        cr.execute(f"update students set class = '{extra}' where id = '{stu_id}'")
        db.commit()

    if how == 3:
        if extra[0] == 'Pending':
            cr.execute(f"update students set fee_status = '{extra[0]}', pending_fee = {extra[1]} where id = '{stu_id}'")
        else:
            cr.execute(f"update students set fee_status = '{extra[0]}', pending_fee = Null where id = '{stu_id}'")
        db.commit()

def update_name(extra, stu_id):
    cr.execute(f"update students set first_name = '{extra[0]}', last_name = '{extra[1]}' where id = '{stu_id}'")
    db.commit()

def update_class(extra, stu_id):
    cr.execute(f"update students set class = '{extra}' where id = '{stu_id}'")
    db.commit()

def update_roll_no(extra, stu_id):
    cr.execute(f"update students set roll_no = '{extra}' where id = '{stu_id}'")
    db.commit()

def update_id(how, extra, stu_id):
    if how == 1:
        cr.execute(f"update students set fee_status = 'Pending', pending_fee = {extra} where id = '{stu_id}'")
    else:
        cr.execute(f"update students set fee_status = 'Not Pending', pending_fee = Null where id = '{stu_id}'")
    db.commit()

def delete_student(stu_id):
    cr.execute(f"delete from students where id = '{stu_id}'")
    db.commit()

def statisics():
    cr.execute(f"select fee_status from students")
    ls = []
    for row in cr:
        ls.append(row)
    return ls
