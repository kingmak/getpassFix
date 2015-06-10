import sys, msvcrt

def getpass(prompt = 'Password: '):

    password = ''
    hideChar = '?'
    
    for char in prompt:
        msvcrt.putch(char)
    
    while True:
        char = msvcrt.getch()
        if char == '\r' or char == '\n':
            break

        if char == '\003':     #ctrl + c
            raise KeyboardInterrupt

        if char == '\b':
            password = password[:-1]
            msvcrt.putch('\b')
            msvcrt.putch(' ')
            msvcrt.putch('\b')
            
        else:
            password += char
            msvcrt.putch(hideChar)
            
    msvcrt.putch('\r')
    msvcrt.putch('\n')
    return password

password = getpass()
raw_input('pass = ' + password)
