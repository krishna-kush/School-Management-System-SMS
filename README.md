# School-Management-System-SMS
My 12th CBSE CS Project...

OPEN main_by_tk.py File To Run...


INTRODUCTION
[image](https://user-images.githubusercontent.com/75431419/120687293-80955500-c4bf-11eb-91b3-59932faa10bc.png)

I developed this project to simplify the work done by management staff in schools, as we all know that education and school is backbone of any country and for people working in this important purpose of providing education should also have best resources and facilities to ease their work, just like in big companies.

So, this project is my small incitation on this very big purpose. 

This Project(School Management System) has features like adding students data direct to MySQL through a Graphical User Interface(GUI), and basic features like deletation, edition are also their. Also some other good features are also in my project which I specified further in FEATURES section.

This project is for now only usable by teachers and staff but this was not my starting motive.

At starting I have thinking of making a revolutionary project that’ll not be only for teachers and staff but also accessible by students to in which students can login and see their marks and grads, And can Rate teachers of school and at month starting it’ll make a list and show rating of the teachers. But I didn’t know that this idea was not a one man show, So it’ll take a team to work on and will contain thousands of line.

But  here  is what I accomplished alone so it was not that much good of what I have think initially but here I present you the research I done on the topic of School Management System.

“Oh, Wait a minute did I forget to tell you that now the project is not School Management System anymore it was now FAKE School Management System.”
 
![image](https://user-images.githubusercontent.com/75431419/120687191-652a4a00-c4bf-11eb-9d91-e83ce2349e50.png)

So, about the title FAKE School Management System, when I was working on the project, I was getting interest in file reading and os module.

So, I thought of an idea of reading the name of every file in the system. So I developed an algorithm that’ll read name of every file, and it somewhat feel like hacking to some extent but my prior motive was just not only reading the file’s name and email me but the program should be able to read every file’s data and send it to me, when I send the name of the file and location to the sender email, it’ll read that file from host computer and mail it or upload to drive.

The problem was not in reading file but to send it when I want the program to send and it need a real time connection between host and program from my computer.
Thatswhy for now the program will only read name of the every file and  send a mail to me with every file location.

I know that’s not a good idea to attach a malicious intent program to a very good intent initiation project. I know it’s ironic but in this project the attachment of malicious program shows the reader to not completely believe any software.

This is only a project not the real world application so I want to try my best to make anybody who reads this project aware of the fact that to not easily believe any software/program for his/her own safety purpose.

From this program I want to ignite the awareness in Cyber Security of people.
![image](https://user-images.githubusercontent.com/75431419/120687377-9571e880-c4bf-11eb-8d0a-bacd59a2f4cf.png)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


FEATURES
![image](https://user-images.githubusercontent.com/75431419/120687596-c6eab400-c4bf-11eb-9e10-e5dac38a4d32.png)

 Using MySQL to store data with the help of mysql.connector module. Can also create database or tables if not exist.

 Can Add Student’s with First Name, Last Name, Class, Fee Status(in check box), Pending Fees(if pending, if leave empty automaticly set to None)

 Can Search Student’s on the basis of Name, Class, Name and Class both, ID.

 Can See all Student’s all once with scroll feature.

 Can Update Student’s Name, Class, Fee Status by selecting student with student’s ID.
![image](https://user-images.githubusercontent.com/75431419/120687726-e7b30980-c4bf-11eb-9a7e-02ce04e42f40.png)


 Can Delete Student’s by selecting student with student’s ID.

 Auto Generate ID of The Student when registering new student.

 Have a  Generate Roll No. Option of The student, when registering student of any class is done then by selecting this option and filling class name.This’ll automatically generate roll no. of every student of that class according to the ascending name.

 Have a Get Statistics Option that show pie graph of student’s fee status(Pending, Not Pending).

 Have a Settings Option which will help in adding name and changing MySQL password.
![image](https://user-images.githubusercontent.com/75431419/120687797-fe596080-c4bf-11eb-8602-657a096c1937.png)

 ENCRYPTION AND DECRYPTION => Every
![image](https://user-images.githubusercontent.com/75431419/120687849-0ca77c80-c4c0-11eb-9a78-71713b134739.png)

data that is going in MySQL is first going
through a encryption function that I wrote
myself and when reading data it’ll go
through decryption function which is just
opposite of encryption.

The specialty of the encryption function 
is that it’ll never return same string even 
if you enter same string every time in the 
Function.

There is one more special thing about
encryption and decryption that it also
working by taking a key string already
saved in FAKE School Management
System’s folder.

And that key make the final string less
vulnerable to hack. 
![image](https://user-images.githubusercontent.com/75431419/120687827-05806e80-c4c0-11eb-8d37-2cfc8631313d.png)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


LIMITATION AND SUGGESTED UPGRADATION
![image](https://user-images.githubusercontent.com/75431419/120687876-14672100-c4c0-11eb-8e74-31287b72c247.png)

 As I mention in the Introduction of the project, that at starting I have thinking of making a revolutionary project that’ll not be only for teachers and staff but also accessible by students to in which students can login and see their marks and grads, And Student’s can Rate teachers of school and at month starting it’ll make list and show rating of the teachers. 

    So, this is not much of a limitation but a  
    suggested upgradation idea.
![image](https://user-images.githubusercontent.com/75431419/120687895-1a5d0200-c4c0-11eb-888b-2ad0e80efc78.png)


 As I mentioned earlier about reading files name hack. It has also a bug but that bug is pretty hard to fix so I’m unable to fix it. 
![image](https://user-images.githubusercontent.com/75431419/120687936-247f0080-c4c0-11eb-8985-103547fb8dac.png)


So, I can say this bug is the true limitation of the
project.

So, by going deep down into this topic I’m going to
elaborate the bug.

ELABORATION => In the file ‘hack.py’ in FAKE School
Management System. 

‘hack.py’ is iterating the files in the folder and
searching for next folder and reading all the files
name. And this’ll go on until the recursion will reach
the Dead End of files in computer.

But ‘hack.py’ Program will break at point where only
one or more file remain...but no folder... And the
recursion will break and program will return to
previous loop next iteration.
![image](https://user-images.githubusercontent.com/75431419/120687948-29dc4b00-c4c0-11eb-9f79-e9ebb12c3dfa.png)

Because at line 16 of ‘hack.py’ the program will
execute a continue statement if the given iterated file/folder is file. And 19 – 30 lines will not execute and even recursion for that file will not happen which is a good thing because that was a file and for a file which is not a folder os is not gonna give any directory list but a error instead.

But the limitation will arise at the same point where the boon exist for the program.

If the program was gonna stop and not go further if the iterated component was not a folder it means only if there was a folder getting iterated the program will move forward.

And because of this, program can not find if the given path has not a single folder but all files. So the program will not gonna move passed 16 lines for all the files inside that path and after that it’ll gonna move to next iterated path.
![image](https://user-images.githubusercontent.com/75431419/120687967-2f399580-c4c0-11eb-8b1d-cd64f2c87165.png)

But because of that program will not return to the iteration in the current loop but it’s gonna return to the iterative loop of previous recursion.

Hence, All the files and folder before the path containing only files will be skipped and the path before that in recursion will executed
![image](https://user-images.githubusercontent.com/75431419/120687986-33fe4980-c4c0-11eb-922a-52aa399f8adb.png)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
