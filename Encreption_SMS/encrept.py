import random

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'

with open('encreption_key.txt') as t:
    key = t.read()

def encode(code):
    final = ''
    key_index = 0
    alternate = 0

    for j, i in enumerate(code):

        if j != 0 and j%int(key[0]) == 0:
            final += key[key_index%len(key)] # IMPORTANT ALGORITHEM...(it's like looping some range of integer.)
            key_index += 1

        if i not in alpha:
            final += i
            continue

        if i == ' ':
            final += ' '
            continue
        
        index = alpha.index(i)

        if (index == len(alpha) - 1) and (alternate%2==0):
            change = 'A'
        else:
            if alternate%2==0:
                change = alpha[index + 1]
            else:
                change = alpha[index - 1]
            
        final += change

        alternate += 1

    return final

def decode(code):
    final = ''
    key_index = 0
    alternate = 0


    for j, i in enumerate(code):

        if j != 0 and j == int(key[0]) + key_index*int(key[0]) + key_index:
            key_index += 1
            continue

        if i not in alpha:
            final += i
            continue

        if i == ' ':
            final += ' '
            continue

        index = alpha.index(i)

        if (index == len(alpha) - 1) and (alternate%2==1):
            change = 'A'
        else:
            if alternate%2==1:
                change = alpha[index + 1]
            else:
                change = alpha[index - 1]
            
        final += change

        alternate += 1

    return final



if __name__ == "__main__":
    print(encode('ID00034'))
    print(decode('JC21z`12X5'))




# want = True

# while want:

#     choice = input('what you want to do DECODE(d)/ENCODE(e): ')

#     if choice[0].lower() == 'e':
#         final = ''
#         key_index = 0
#         alternate = 0
#         code = input('Enter Your Code To ENCODE: ')

#         for j, i in enumerate(code):

#             if j != 0 and j%int(key[0]) == 0:
#                 final += key[key_index%len(key)] # IMPORTANT ALGORITHEM...(it's like looping some range of integer.)
#                 key_index += 1

#             if i not in alpha:
#                 final += i
#                 continue

#             if i == ' ':
#                 final += ' '
#                 continue
            
#             index = alpha.index(i)

#             if (index == len(alpha) - 1) and (alternate%2==0):
#                 change = 'a'
#             else:
#                 if alternate%2==0:
#                     change = alpha[index + 1]
#                 else:
#                     change = alpha[index - 1]
                
#             final += change

#             alternate += 1
            
#         print(f'ENCODED CODE: {final}')

#     if choice[0].lower() == 'd':
#         final = ''
#         key_index = 0
#         alternate = 0
#         code = input('Enter Your Code To DECODE: ')


#         for j, i in enumerate(code):

#             if j != 0 and j == int(key[0]) + key_index*int(key[0]) + key_index:
#                 key_index += 1
#                 continue

#             if i not in alpha:
#                 final += i
#                 continue

#             if i == ' ':
#                 final += ' '
#                 continue

#             index = alpha.index(i)

#             if (index == len(alpha) - 1) and (alternate%2==1):
#                 change = 'a'
#             else:
#                 if alternate%2==1:
#                     change = alpha[index + 1]
#                 else:
#                     change = alpha[index - 1]
                
#             final += change

#             alternate += 1

#         print(f'DECODED CODE: {final}')
    

#     temp = input('Do you want to DECODE/ENCODE again?? YES(y)/NO(n): ')

#     if temp[0].lower() == 'n':
#         want = False
