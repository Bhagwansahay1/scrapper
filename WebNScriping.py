import requests
import re
import sys
import os
import csv
from json import dumps
from bs4 import BeautifulSoup
# try:
#     from urllib.parse import urlparse
# except ImportError:
#      from urlparse import urlparse

myfile = open('AllLinksData.txt', 'r')
line = myfile.readline().split(",")
myfile1 = open('FirstPageLinkData.txt', 'r')
lineFirst = myfile1.readline().split(",")

DataList = []
OtherLinks = []
# fields = ['Link', 'Classification', 'Utility', 'UtilityData','Mechanics','MechanicsData','Force','ForceData','Instructions','Preparation','PreparationData','Execution','ExecutionData','Comments','CommentsData','Muscles','Target','TargetData','Synergists','SynergistsData','Stabilizers','StabilizersData',]
i = 0
# for mainLink in lineFirst:
for data in line:
    List1 = []
    i = i+1
    if(i >= 2801):
        data1 = data.replace("'", "")
        r = requests.get(data1)
        soup = BeautifulSoup(r.content, 'html.parser')
        link = soup.find('article')
        try:
            header1 = link.find('h2')
            if(header1 == None):
                continue
            elif(header1.get_text() == "Classification"):
                # List1.append('\n')
                List1.append(data1)
                ExerciseName = soup.find('h1', class_='page-title')
                List1.append("Exercise Name:")
                List1.append(ExerciseName.get_text())
                List1.append(header1.get_text())
                # tableElement=header1.find('table')
                # for tableElement in soup.find('tbody'):
                #     Ex=tableElement.find('strong')
                #     List1.append(Ex.get_text())
                #     Ex1=tableElement.find('a')
                #     Ex2=Ex1.find_next('a')
                #     List1.append(Ex1.get_text()+" or "+Ex2.get_text())
                #     # Ex1=tableElement.find('td')
                #     # Ex2=Ex1.find_next('a')
                #     # Ex6=Ex2.find_next('a')
                #     # print(Ex1)

                #     # List1.append(Ex2.get_text())
                #     Ex3=Ex.find_next('strong')
                #     List1.append(Ex3.get_text())
                #     Ex4=Ex2.find_next('a')
                #     List1.append(Ex4.get_text())
                #     Ex5=Ex3.find_next('strong')
                #     List1.append(Ex5.get_text())
                #     Ex6=Ex4.find_next('a')
                #     List1.append(Ex6.get_text())

                List1.append("Utility:")
                List1.append("Basic or Auxiliary")
                List1.append("Mechanics:")
                List1.append("Isolated")
                List1.append("Force:")
                List1.append("Pull")

                header2 = header1.find_next('h2')
                List1.append(header2.get_text())
                subheading = header2.find_next('strong')
                List1.append(subheading.get_text())
                paragraph1 = subheading.find_next('p')
                mysortdata1 = str(paragraph1).split('<p>')
                # print(mysortdata)
                List1.append(mysortdata1[1])
                subheading1 = subheading.find_next('strong')
                List1.append(subheading1.get_text())
                # print(List1)
                try:
                    mysortdata2 = mysortdata1[3].split('</p>')
                    List1.append(mysortdata2[0])
                    header3 = header2.find_next('h2')
                    List1.append(header3.get_text())
                    paragraph2 = header3.find_next('p')
                    mysortdata3 = str(paragraph2)
                    # print(mysortdata3)
                    mysortdata3 = re.split('<p>|<h2>', mysortdata3)
                    # print(mysortdata3)
                    mysortdata3 = re.split('<a|>|</a|>', mysortdata3[1])
                    # print(len(mysortdata3))
                    commentsDataString = ""
                    for commentsData in mysortdata3:
                        if(commentsData[:5] == "href="):
                            continue
                        commentsDataString = commentsDataString+commentsData

                    List1.append(commentsDataString)
                    header4 = header3.find_next('h2')
                    List1.append(header4.get_text())
                    subheading2 = header4.find_next('strong')
                    List1.append(subheading2.get_text())
                    Item1 = subheading2.find_next('li')
                    List1.append(Item1.get_text())
                    subheading3 = subheading2.find_next('strong')
                    List1.append(subheading3.get_text())
                    Item2 = subheading3.find_next('li')
                    List1.append(Item2.get_text())
                    subheading4 = subheading3.find_next('strong')
                    if(subheading4 == None):
                        List1.append(" ")
                    else:
                        List1.append(subheading4.get_text())
                    try:
                        Item3 = subheading4.find_next('li')
                        List1.append(Item3.get_text())
                    except:
                        List1.append(" ")
                    # if(Item3==None):
                    #     List1.append(" ")
                    # else:
                    #     List1.append(Item3.get_text())
                    DataList.append(List1)
                except:
                    OtherLinks.append(data1)
            elif(header1.get_text() == "Instructions"):
                List1.append(data1)
                ExerciseName = soup.find('h1', class_='page-title')
                List1.append("Exercise Name:")
                List1.append(ExerciseName.get_text())
                List1.append(" ")
                # tableElement=header1.find('table')
                # for tableElement in soup.find('tbody'):
                #     Ex=tableElement.find('strong')
                #     List1.append(Ex.get_text())
                #     Ex1=tableElement.find('a')
                #     Ex2=Ex1.find_next('a')
                #     List1.append(Ex1.get_text()+" or "+Ex2.get_text())
                #     Ex3=Ex.find_next('strong')
                #     List1.append(Ex3.get_text())
                #     Ex4=Ex2.find_next('a')
                #     List1.append(Ex4.get_text())
                #     Ex5=Ex3.find_next('strong')
                #     List1.append(Ex5.get_text())
                #     Ex6=Ex4.find_next('a')
                #     List1.append(Ex6.get_text())
                List1.append(" ")
                List1.append(" ")
                List1.append(" ")
                List1.append(" ")
                List1.append(" ")
                List1.append(" ")
                header2 = header1
                List1.append(header2.get_text())
                subheading = header2.find_next('strong')
                List1.append(subheading.get_text())
                paragraph1 = subheading.find_next('p')
                mysortdata1 = str(paragraph1).split('<p>')
                # print(mysortdata)
                List1.append(mysortdata1[1])
                subheading1 = subheading.find_next('strong')
                List1.append(subheading1.get_text())
                mysortdata2 = mysortdata1[3].split('</p>')
                List1.append(mysortdata2[0])
                header3 = header2.find_next('h2')
                List1.append(header3.get_text())
                paragraph2 = header3.find_next('p')
                mysortdata3 = str(paragraph2)
                # print(mysortdata3)
                mysortdata3 = re.split('<p>|<h2>', mysortdata3)
                # print(mysortdata3)
                mysortdata3 = re.split('<a|>|</a|>', mysortdata3[1])
                # print(len(mysortdata3))
                commentsDataString = ""
                for commentsData in mysortdata3:
                    if(commentsData[:5] == "href="):
                        continue
                    commentsDataString = commentsDataString+commentsData

                List1.append(commentsDataString)
                header4 = header3.find_next('h2')
                List1.append(header4.get_text())
                subheading2 = header4.find_next('p')
                if(subheading2 == None):
                    List1.append(" ")
                else:
                    subheading3 = str(subheading2)
                    mysortdata4 = re.split('<p>|<ul>', subheading3)
                    List1.append(mysortdata4[1])
                Item1 = subheading2.find_next('li')
                if(Item1 == None):
                    List1.append(" ")
                else:
                    List1.append(Item1.get_text())
                # try:
                #     subheading3=subheading2.find_next('strong')
                #     print(List1)
                #     if(subheading2==None):
                #         List1.append(" ")
                #     else:
                #         List1.append(subheading3.get_text())
                #     Item2=subheading3.find_next('li')
                #     if(subheading2==None):
                #         List1.append(" ")
                #     else:
                #         List1.append(Item2.get_text())
                #     subheading4=subheading3.find_next('strong')
                #     if(subheading2==None):
                #         List1.append(" ")
                #     else:
                #         List1.append(subheading4.get_text())
                #     Item3=subheading4.find_next('li')
                #     if(subheading2==None):
                #         List1.append(" ")
                #     else:
                #         List1.append(Item3.get_text())
                # except:
                #     continue
                # print(List1)
                DataList.append(List1)

            # for values1 in tableElement.find_next('td'):
            #     List1.append(values1.get_text())
            # elements=tableElement.find('td')
            # value1=soup.find_all('td')
            # for myval in tableElement.find_all('td'):
            # List1.append(elements)
            # List1.append(soup.find('td').get_text())
        except:
            continue

        # for link1 in link.find_all(['h2','a','strong','p']):
        #     List1.append(link1.get_text())
        # for link in soup.find('article'):
        #     for link1 in link.find_all(['h2','a','strong','p']):
        #         List1.append(link1.get_text())
    if(i == 3095):
        break
# with open("finaldata1.txt", "w",encoding="utf-8") as output:
#     output.write(str(List1))
# print(DataList)


# import requests
# from bs4 import BeautifulSoup
# try:
#     from urllib.parse import urlparse
# except ImportError:
#     from urlparse import urlparse

# myfile = open('FirstPageLinkData.txt', 'r')
# line=myfile.readline().split(",")

# print(line)
# List1=[]
# for data in line:
#     data1=data.replace("'", "")
#     List1.append('/n ParentLink')
#     List1.append(data1)
#     r = requests.get(data1)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     for link in soup.find_all('article'):
#         for link1 in link.find_all('a'):
#             elementData=link1.get('href')
#             elementString=str(elementData)
#             replaceData=elementString.replace("../../","https://exrx.net/").replace("../","https://exrx.net/")
#             if(elementString=="None"):
#                 continue
#             List1.append(replaceData)
#             checkUrl=urlparse(replaceData)
#             if(all([checkUrl.scheme, checkUrl.netloc])==True):
#                 r1 = requests.get(replaceData)
#                 soup1 = BeautifulSoup(r1.content, 'html.parser')
#                 for link2 in soup1.find_all('article'):
#                     for link3 in link2.find_all(['h2','a','strong','p']):
#                         List1.append(link3.get_text())

# def write_to_csv(list_of_data):
#    with open('testing.csv', 'w') as csvfile:
#        writer = csv.writer(csvfile, delimiter = ",")
#        writer.writerows(list_of_data)

with open("testing.csv", 'w', encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(fields)
    csvwriter.writerows(DataList)
with open("finaldata1.txt", "w", encoding="utf-8") as output:
    output.write(str(OtherLinks))
