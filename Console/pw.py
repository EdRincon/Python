#! python3
# pw.py -  An insecure password locker program.

Password = {'email' : 'fewhri2uiu3ke',
            'blog'  : 'd2jfjhro3ij32',
            'luggage' : '12345'}

import sys, pyperclip


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy accoun password')
    sys.exit()

account = sys.argv[1]   #first command line arg is the account name

if account in Password:
    pyperclip.copy(Password[account])
    print('Password for ' + account + ' coppied to the clipboard.')
else:
    print('There is no account named ' + account)
