import connect_mysql
import idgenerator
import sys

if __name__ == "__main__":
    while True:
        print('Welcome To SCHOOL MANAGEMENT SYSTEM By Krishna Kushwaha')
        print('1. Add Student...')
        print('2. Get Student Info...')
        print('3. See All Students Info')
        print('4. Update Student Info...')
        print('5. Delete Student Info...')
        print('6. Exit...')
        print()
        a = int(input('Select Option:'))
        print()

        if a == 6:
            sys.exit()

        if a == 1:
            first_name = input('Student\'s First Name:')
            last_name = input('Student\'s Last Name:')
            clas = input('Student\'s Class:')
            fee_status = input('Pending...(y/n):')
            pending_fee = 'Null'
            if fee_status[0] == 'y' or fee_status[0] == 'Y':
                fee_status = 'Pending'
            else:
                fee_status = 'Not Pending'
            if fee_status == 'Pending':
                pending_fee = int(input('How much?(Use Only Numbers):'))
                

            id_stu = idgenerator.get_id()

            connect_mysql.add_student(first_name, last_name, clas, id_stu, fee_status, pending_fee)

        if a == 2:
            print('1. Search By Name')
            print('2. Search By Class')
            print('3. Search By Name and Class')
            print('4. Search By ID')
            b = int(input('Select Option:'))
            if b == 1:
                extra = input('Enter Student\'s Full Name:').split()
            if b == 2:
                extra = input('Enter Student\'s Class:')
            if b == 3:
                extra = input('Enter Student\'s Full_Name and Class(by space seperated):').split()
            if b == 4:
                extra = input('Enter Student\'s ID:')

            connect_mysql.search_student(b, extra)

        if a == 3:
            connect_mysql.see_all_stu()

        if a == 4:
            print('1. Update Name')
            print('2. Update Class')
            print('3. Update Fee Status')
            b = int(input('Select Option:'))
            if b == 1:
                extra = input('Enter New First Name And Last Name Of Student Seperated By Space:').split()
                stu_id = input('Enter Student ID:')
            if b == 2:
                extra = input('Enter New Class Of Student:')
                stu_id = input('Enter Student ID:')
            if b == 3:
                extra = []
                fee_status = input('Enter Fee Status Of Student, Pending...(y/n):')
                pending_fee = 'Null'
                if fee_status[0] == 'y' or fee_status[0] == 'Y':
                    fee_status = 'Pending'
                else:
                    fee_status = 'Not Pending'
                if fee_status == 'Pending':
                    pending_fee = int(input('How much?(Use Only Numbers):'))
                extra.append(fee_status)
                extra.append(pending_fee)
                stu_id = input('Enter Student ID:')

            connect_mysql.update_student(b, extra, stu_id)

        if a == 5:
            stu_id = input('Enter Student ID:')
            connect_mysql.delete_student(stu_id)
