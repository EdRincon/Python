#! python3
# maplt.py - Launches a map in the browser using an address from the
# command line or clipboard

import sys, webbrowser, pyperclip, sys

print(sys.version)

if len(sys.argv) > 1:
    # Get the address from command line.
    address = ' '.join(sysargv[1:])
else:
    #Get address from paperclip.
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com.mx/maps/place/' + address)
