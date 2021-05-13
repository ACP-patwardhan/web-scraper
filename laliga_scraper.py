from typing import Text
import requests 
from bs4 import BeautifulSoup
URL="https://en.wikipedia.org/wiki/2020%E2%80%9321_La_Liga" #URL we want to get
r=requests.get(URL) #getting URL
soup=BeautifulSoup(r.content,'html5lib') # creating beatutiful soup object
tables=soup.find_all('table',attrs={'class':'wikitable'})
pts_table=tables[3]
pos=[]
team_name=[]
games_pld=[]
pts=[]
rows = pts_table.find_all('tr')
for row in rows[1:]:
    name=row.find_all('th')
    n=name[0].text
    if(' (Q)' in n or ' (Y)' in n):
        n=n[:-4:]
    n=n[:-1:]
    team_name.append(n)
    cols=row.find_all('td')
    p=cols[0].text
    pos.append(p[:-1])
    p=cols[1].text
    games_pld.append(p[:-1])
    p=cols[8].text
    pts.append(p[:-1])
