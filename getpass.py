import sys, msvcrt

def getpass(prompt = 'Password: ', hideChar = ' '):

    password = ''
    for char in prompt: # so that we don't have to fiddle with print password, 
        msvcrt.putch(char)
    
    count = 0
    while True:
        char = msvcrt.getch()
        if char == '\r' or char == '\n': break
        if char == '\003': raise KeyboardInterrupt #ctrl + c

        if char == '\b':
            count -= 1
            password = password[:-1]

            if count >= 0:
                msvcrt.putch('\b')
                msvcrt.putch(' ')
                msvcrt.putch('\b')
            
        else:
            if count < 0: count = 0
            count += 1
            password += char
            msvcrt.putch(hideChar)
            
    msvcrt.putch('\r')
    msvcrt.putch('\n')
    return password if password != '' else "''"

password = getpass(hideChar = '?')
raw_input('pass = ' + password)
