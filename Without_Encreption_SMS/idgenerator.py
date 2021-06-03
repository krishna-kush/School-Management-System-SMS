# It generate ID example: "ID00001"
# num = "00000"

def get_id():
    with open('id_record.txt', 'r') as t:
        data = t.readlines()
    lastline = data[-1]

    lastline = lastline[2:]
    temp = int(lastline) + 1
    if len(str(temp)) < 6:
        lastline = lastline[:len(lastline)-len(str(temp))] + str(temp) 
    else:
        lastline = temp

    with open('id_record.txt', 'a') as t:
        t.write(f'\nID{lastline}')
    
    return f'ID{lastline}'
