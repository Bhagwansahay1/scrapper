import requests
from bs4 import BeautifulSoup
# try:
#     from urllib.parse import urlparse
# except ImportError:
#      from urlparse import urlparse

myfile = open('FirstPageLinkData.txt', 'r')
line=myfile.readline().split(",")

# print(line)
List1=[]
i=1
for data in line:
    i=i+1
    data1=data.replace("'", "")
    # List1.append('/n ParentLink')
    List1.append(data1)
    r = requests.get(data1)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('article'):
        for link1 in link.find_all('a'):
            elementData=link1.get('href')
            elementString=str(elementData)
            replaceData=elementString.replace("../../","https://exrx.net/").replace("../","https://exrx.net/")
            if(elementString=="None"):
                continue
            elif(replaceData[:8]!="https://"):
                continue
            List1.append(replaceData)
with open("rendom.txt", "w",encoding="utf-8") as output:
    output.write(str(List1))

print(len(List1))
# print(len(List1))
