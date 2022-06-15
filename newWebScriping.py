import requests
from bs4 import BeautifulSoup
# try:
#     from urllib.parse import urlparse
# except ImportError:
#      from urlparse import urlparse

url = "https://exrx.net/Lists/Directory"
url2="https://exrx.net/Lists/"
urlLink2="https://exrx.net/"

r = requests.get(url)
newr=requests.get("https://exrx.net/Lists/ExList/WaistWt")
soup = BeautifulSoup(r.content, 'html.parser')

List1=[]
List2=[]
for link in soup.find_all('article'):
    for link1 in link.find_all('a'):
        List1.append(url2+link1.get('href'))
with open("FirstPageLinkData.txt", "w",encoding="utf-8") as output:
    output.write(str(List1))
# print(List1)
# print(len(List1))
# myset=set(List1)
# print(len(myset))