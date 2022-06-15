import requests
import re
import sys 
import os
import csv
from json import dumps
from bs4 import BeautifulSoup

myfile = open('sortedLinks.txt', 'r')
Links=myfile.readline().split(",")
DataList=[]
OtherLinks=[]
i=0
# url = "https://exrx.net/WeightExercises/Sternocleidomastoid/CBNeckFlxBelt"
# url1="https://exrx.net/Stretches/ChestGeneral/BehindHead"
# url2='https://exrx.net/WeightExercises/Supinators/LVSeatedSupination'
# url3='https://exrx.net/WeightExercises/ErectorSpinae/BBStraightLegDeadlift'
# url4='https://exrx.net/Stretches/ErectorSpinae/Cat'


for data in Links:
    List1=[]
    i=i+1
    if(i>=1501):
        data1=data.replace("'", "")
        r = requests.get(data1)
        soup = BeautifulSoup(r.content, 'html.parser')
        mainHeading=soup.find('h1',class_='page-title')
        try:
            subHeading=mainHeading.find_next('h2')
            if(subHeading==None):
                continue
            elif(subHeading.get_text()=="Classification"):
                List1.append(data1)
                List1.append("Exercise Name:")
                List1.append(mainHeading.get_text())
                List1.append(subHeading.get_text())
                tableHeading1=subHeading.find_next('strong')
                List1.append(tableHeading1.get_text())
                
                # print(mydata)
                tableData1=tableHeading1.find_next('td')
                tableDataLink1=tableData1.find_all('a')
                if(len(tableDataLink1)==3):
                    List1.append(tableDataLink1[0].get_text())
                    tableHeading2=tableHeading1.find_next('strong')
                    List1.append(tableHeading2.get_text())
                    List1.append(tableDataLink1[1].get_text())
                    tableHeading3=tableHeading2.find_next('strong')
                    List1.append(tableHeading3.get_text())
                    List1.append(tableDataLink1[2].get_text())
                elif(len(tableDataLink1)==4):
                    data1=tableDataLink1[0].get_text()+" or "+tableDataLink1[1].get_text()
                    List1.append(data1)
                    tableHeading2=tableHeading1.find_next('strong')
                    List1.append(tableHeading2.get_text())
                    List1.append(tableDataLink1[2].get_text())
                    tableHeading3=tableHeading2.find_next('strong')
                    List1.append(tableHeading3.get_text())
                    List1.append(tableDataLink1[3].get_text())
                else:
                    tableData1=tableHeading1.find_next('td')
                    mydata=str(tableHeading1.find_next('td'))
                    mydata=re.split('<p>|<strong>|</strong>|<h2>|</h2>|</p>|<a|>|</a>|<tr|<tr>|</tr>|<td>|<td|</td>',mydata)
                    for datainloop in mydata:
                        if(datainloop==''):
                            continue
                        elif(datainloop[:7]==' width='):
                            continue
                        elif(datainloop[:8]==' height='):
                            continue
                        elif(datainloop[:6]==" href="):
                            continue
                        else:
                            List1.append(datainloop)
                subHeading=tableData1.find_next('h2')
                List1.append(subHeading.get_text())
                Heading1=subHeading.find_next('strong')
                List1.append(Heading1.get_text())
                paragraph1=str(Heading1.find_next('p'))
                paragraph1=re.split('<p>|<strong>|</strong>|<h2>|</h2>|</p>|<a|>|</a>',paragraph1)
                ListData1=""
                for check in paragraph1:
                    if(check=='Execution'):
                        break
                    elif(check[:6]==" href="):
                        continue
                    else:
                        ListData1=ListData1+check
                        
                List1.append(" ".join(ListData1.split( )))
                Heading2=Heading1.find_next('strong')
                List1.append(Heading2.get_text())
                paragraph2=str(Heading2.find_next('p'))
                paragraph2=re.split('<p>|<strong>|</strong>|<h2>|</h2>|</p>|<a|>|</a>',paragraph2)
                ListData2=""
                for check1 in paragraph2:
                    if(check1=='Comments'):
                        break
                    elif(check1[:6]==" href="):
                        continue
                    else:
                        ListData2=ListData2+check1
                        
                List1.append(" ".join(ListData2.split( )))
                subHeading1=subHeading.find_next('h2')
                List1.append(subHeading1.get_text())
                paragraph3=str(subHeading1.find_next('p'))
                paragraphstring=subHeading1.find_next('p')
                paragraph4=str(paragraphstring.find_next('div'))
                # print(paragraph4)
                paragraph5=paragraph3+paragraph4
                paragraph5=re.split('<p>|<strong>|</strong>|<h2>|</h2>|</p>|<a|>|</a>|<ul>|<li>|</ul>|</li>|<div|<span|</span>',paragraph5)
                ListData3=""
                for check2 in paragraph5:
                    if(check2=='Muscles'):
                        break
                    elif(check2=='Force (Articulation)'):
                        OtherLinks.append(data1)
                        break
                    elif(check2[:6]==" href="):
                        continue
                    elif(check2[:5]==" data"):
                        continue
                    # elif(check2[:7]==" class="):
                    #     continue
                    else:
                        ListData3=ListData3+" "+check2
                List1.append(" ".join(ListData3.split( )))
                try:
                    subHeading2=subHeading1.find_next('h2')
                    List1.append(subHeading2.get_text())
                    Heading3=subHeading2.find_next('strong')
                    List1.append(Heading3.get_text())
                    ListItem1=Heading3.find_next('ul')
                    ListItemString=str(Heading3.find_next('ul'))
                    ListItemString=re.split('<p>|</p>|<ul>|<ul|</ul>|</ul|<li>|<li|</li>|</li|<a|>|</a>',ListItemString)
                    ListData4=""
                    for check5 in ListItemString:
                        if(check5[:6]==" href="):
                            continue
                        else:
                            ListData4=ListData4+" "+check5
                    List1.append(" ".join(ListData4.split( )))
                    Heading4=Heading3.find_next('strong')
                    # print(Heading4)
                    List1.append(Heading4.get_text())
                    ListItem2=Heading4.find_next('ul')
                    # print(ListItem2)
                    ListItemString1=str(Heading4.find_next('ul'))
                    ListItemString1=re.split('<p>|</p>|<ul>|<ul|</ul>|</ul|<li>|<li|</li>|</li|<a|>|</a>',ListItemString1)
                    ListData5=""
                    for check4 in ListItemString1:
                        if(check4[:6]==" href="):
                            continue
                        else:
                            ListData5=ListData5+" "+check4
                    List1.append(" ".join(ListData5.split( )))
                    try:
                        Heading5=Heading4.find_next('strong')
                        List1.append(Heading5.get_text())
                        UnorderedListData1=Heading5.find_next('ul')
                        ListItem3=str(Heading5.find_next('ul'))
                        ListItem3=re.split('<p>|</p>|<ul>|<ul|</ul>|</ul|<li>|<li|</li>|</li|<a|>|</a>',ListItem3)
                        ListData6=""
                        for check3 in ListItem3:
                            if(check3[:6]==" href="):
                                continue
                            else:
                                ListData6=ListData6+" "+check3
                        List1.append(" ".join(ListData6.split( )))
                        
                        Heading6=Heading5.find_next('strong')
                        List1.append(Heading6.get_text())
                        UnorderedListData2=Heading6.find_next('ul')
                        ListItem4=str(Heading6.find_next('ul'))
                        ListItem4=re.split('<p>|</p>|<ul>|<ul|</ul>|</ul|<li>|<li|</li>|</li|<a|>|</a>',ListItem4)
                        ListData7=""
                        for check4 in ListItem4:
                            if(check4[:6]==" href="):
                                continue
                            else:
                                ListData7=ListData7+" "+check4
                        List1.append(" ".join(ListData7.split( )))

                        Heading7=Heading6.find_next('strong')
                        List1.append(Heading7.get_text())
                        ListItem5=str(Heading7.find_next('ul'))
                        ListItem5=re.split('<p>|</p>|<ul>|<ul|</ul>|</ul|<li>|<li|</li>|</li|<a|>|</a>',ListItem5)
                        ListData8=""
                        for check5 in ListItem5:
                            if(check5[:6]==" href="):
                                continue
                            else:
                                ListData8=ListData8+" "+check5
                        List1.append(" ".join(ListData8.split( )))
                        
                        # List1.append(ListItem3.get_text())
                    except:
                        pass
                    DataList.append(List1)
                    # print(List1)
                except:
                    OtherLinks.append(data1)
            elif(subHeading.get_text()=="Instructions"):
                List1.append(data1)
                List1.append("Exercise Name:")
                List1.append(mainHeading.get_text())
                List1.append(" ")
                List1.append(" ")
                List1.append(" ")
                List1.append(" ")
                List1.append(" ")
                List1.append(" ")
                List1.append(" ")
                List1.append(subHeading.get_text())
                Heading1=subHeading.find_next('strong')
                List1.append(Heading1.get_text())
                paragraph1=str(Heading1.find_next('p'))
                paragraph1=re.split('<p>|<strong>|</strong>|<h2>|</h2></p>|<a|>|</a>',paragraph1)
                ListData1=""
                for check in paragraph1:
                    if(check=='Execution'):
                        break
                    elif(check[:6]==" href="):
                        continue
                    else:
                        ListData1=ListData1+check
                        
                List1.append(" ".join(ListData1.split( )))
                Heading2=Heading1.find_next('strong')
                List1.append(Heading2.get_text())
                paragraph2=str(Heading2.find_next('p'))
                paragraph2=re.split('<p>|<strong>|</strong>|<h2>|</h2>|</p>|<a|>|</a>',paragraph2)
                ListData2=""
                for check1 in paragraph2:
                    if(check1=='Comments'):
                        break
                    elif(check1[:6]==" href="):
                        continue
                    else:
                        ListData2=ListData2+check1
                        
                List1.append(" ".join(ListData2.split( )))
                subHeading1=subHeading.find_next('h2')
                List1.append(subHeading1.get_text())
                paragraph3=str(subHeading1.find_next('p'))
                paragraphstring=subHeading1.find_next('p')
                paragraph4=str(paragraphstring.find_next('p'))
                paragraph5=paragraph3+paragraph4
                paragraph5=re.split('<p>|<strong>|</strong>|<h2>|</h2>|</p>|<a|>|</a>|<ul>|<li>|</ul>|</li>',paragraph5)
                ListData3=""
                for check2 in paragraph5:
                    if(check2=='Muscles'):
                        break
                    elif(check2[:6]==" href="):
                        continue
                    elif(check2[:5]==" data"):
                        continue
                    else:
                        ListData3=ListData3+check2
                List1.append(" ".join(ListData3.split( )))
                subHeading2=subHeading1.find_next('h2')
                List1.append(subHeading2.get_text())
                
                try:
                    ItemListHeading=subHeading2.find_next('p')
                    ListItemString2=str(subHeading2.find_next('p'))
                    ListItemString2=re.split('<p>|</p>|<ul>|<ul|</ul>|</ul|<li>|<li|</li>|</li|<a|>|</a>',ListItemString2)
                    List1.append(ListItemString2[1])
                    unorderListData=ItemListHeading.find_next('ul')
                    unorderListData1=str(ItemListHeading.find_next('ul'))
                    unorderListData1=re.split('<p>|</p>|<ul>|<ul|</ul>|</ul|<li>|<li|</li>|</li|<a|>|</a>',unorderListData1)
                    ListData4=""
                    for check3 in unorderListData1:
                        if(check3[:6]==" href="):
                            continue
                        else:
                            ListData4=ListData4+" "+check3
                    List1.append(" ".join(ListData4.split( )))
                    ItemListHeading1=unorderListData.find_next('p')
                    ListItemString3=str(unorderListData.find_next('p'))
                    ListItemString3=re.split('<p>|</p>|<ul>|<ul|</ul>|</ul|<li>|<li|</li>|</li|<a|>|</a>',ListItemString3)
                    List1.append(ListItemString3[1])
                    unorderListData2=ItemListHeading1.find_next('ul')
                    unorderListData3=str(ItemListHeading1.find_next('ul'))
                    unorderListData3=re.split('<p>|</p>|<ul>|<ul|</ul>|</ul|<li>|<li|</li>|</li|<a|>|</a>',unorderListData3)
                    ListData5=""
                    for check4 in unorderListData3:
                        if(check4[:6]==" href="):
                            continue
                        else:
                            ListData5=ListData5+" "+check4
                    List1.append(" ".join(ListData5.split( )))
                except:
                    pass
                DataList.append(List1)
                # print(List1)
        except:
            pass
    if(i==2006):
        break
# print(DataList)
with open("testing.csv", 'w',encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(fields)
    csvwriter.writerows(DataList)
with open("finaldata1.txt", "w",encoding="utf-8") as output:
    output.write(str(OtherLinks))