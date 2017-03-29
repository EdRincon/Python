#! python3
# lucky.py - opens several Google search results.

import bs4, sys, webbrowser, requests

print ('Googling...') #Display text while downloading the google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#Retrive top search results links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

#Opens a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
