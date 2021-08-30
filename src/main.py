import os
import sys
from getch import getch
import glob
def FuckDrive():
    f=open(os.path.join(path,'fuckdisk'+str(times)),'w')
    f.write(write_str * 1024 * 1024 * filesize)
    f.close()
    print(os.path.join(path,'fuckdisk'+str(times)),'is written!')

def Clean():
    ls = glob.glob(os.path.join(path,'fuckdisk*'))
    for x in ls:
        os.remove(x)
        print('Successfully removed',x)
print('Welcome to use FuckDrive!\n')
print('\033[1;31mThis program is harmful! This program will write a lot of rubbish files in your drive!\033[0m')
confirm=input('Please input "I have already known the harm of the program." to continue: \033[0;33m')
print('\033[0m',end='')
if confirm != 'I have already known the harm of the program.':
    print('You didn\'t type the correct words. The program will exit.')
    sys.exit(0)
path=input('Please type the path which will be fucked by the program: \033[0;33m')
print('\033[0m',end='')
if not os.path.exists(path):
    print('Oooops! This path does not exist!')
    sys.exit(255)
try:
    filesize=int(input('Please input the size of each rubbish file in MB: \033[0;33m'))
    print('\033[0m',end='')
except ValueError:
    print('This is not a correct file size.')
    sys.exit(255)
write_str='f'
print('\nPress Enter to fuck once, press "C" to clean the rubbish file, or press "Q" to quit.')
times = 0
while True:
    ch=getch()
    if ch=='\n':
        FuckDrive()
        times += 1
    elif ch in ['c','C']:
        Clean()
        times = 0
    elif ch in ['q','Q']:
        print('Enjoy!')
        sys.exit(0)

