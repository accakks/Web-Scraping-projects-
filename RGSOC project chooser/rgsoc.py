import requests
import urllib.request 
from bs4 import BeautifulSoup 

url= 'https://teams.railsgirlssummerofcode.org/projects?filter=2018'

r = requests.get(url)

html_content=r.text

soup= BeautifulSoup(html_content, "html.parser")

name=[]
tags=[]


choice=[]
ch=[]
choice1_draft=[]
choice1_sent=[]
choice2_draft=[]
choice2_sent=[]

com=[]
project=[]
projects=[]




for  i in range(200):
    com.append(str(i))

for tr in soup.find_all('tr'):
    proj=[]
    for td in tr.find_all('td'):
        
        for a in td.find_all('a'):


            if a.string in com:
                 pass
            elif a.string=='LibreHealth':
                pass
            elif a.string=='Exercism':
                pass
          

            else:
                proj.append(a.string)
        
        for span in td.find_all('span'):
            if span.string in com:
                choice.append(span.string)
            elif span.string=='accepted' or span.string=='pending':
                pass

            else:
                proj.append(span.string)

    project.append(proj)  

projects=project[0:34]  
   

    
l=[]
for i in range(0,len(choice),4):
    choice1_draft.append(choice[i])
    choice1_sent.append(choice[i+1])

for i in range(2,len(choice),4):
    choice2_draft.append(choice[i])
    choice2_sent.append(choice[i+1])


#Working

skill=input("Enter your skill\n")

filter_skill=[]
skill_index=[]

for i in range(len(projects)):
    if skill in projects[i]:
        filter_skill.append(projects[i][0])
        skill_index.append(i)
    else: 
        pass

filter_skill_choice1_sent=[]
filter_skill_choice1_draft=[]
filter_skill_choice2_sent=[]
filter_skill_choice2_draft=[]

for i in skill_index:
    filter_skill_choice1_sent.append(choice1_sent[i])
    filter_skill_choice1_draft.append(choice1_draft[i])
    filter_skill_choice2_sent.append(choice2_sent[i])
    filter_skill_choice2_draft.append(choice1_draft[i])

if len(filter_skill)>1:

    c1_min=100
    c2_min=100
    filter_c1=[]
    
    filter_c1_index=[]
    
    for i in range(len(filter_skill_choice1_draft)):
        if int(filter_skill_choice1_draft[i])<c1_min:
            c1_min=int(filter_skill_choice1_draft[i])

    for i in range(len(filter_skill_choice1_draft)):
        if int(filter_skill_choice1_draft[i])==c1_min:
            filter_c1_index.append(i)
            filter_c1.append(filter_skill[i])

   
    print("You should choose ")
    print(filter_c1[0])   



else:
    print("You should choose ")
    print(filter_skill[0])



















        






   

