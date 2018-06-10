import requests
import urllib.request 
from bs4 import BeautifulSoup 


def CommonOrgs():
    CommonOrgsl = []
    for s in summerOrgs:
        for w in winterOrgs:
            if s == w:
                CommonOrgsl.append(s)
    print(CommonOrgsl)

##def SummerGSoCCommon():
 

##def WinterGsocCommon():


def CheckOrg():
    print("Enter organisation you wanna check")
    org = str(input())
    for s in range(len(summerOrgs)):
        if summerOrgs[s] == org:
            print(org +' participated in Summers\n')
    for w in range(len(winterOrgs)):
        if winterOrgs[w] == org:
            print(org +' participated in Winters\n')




url= 'https://www.outreachy.org/alums/'

r = requests.get(url)

html_content=r.text

soup= BeautifulSoup(html_content, "html.parser")

organisation = []
summerOrgs =[]
winterOrgs =[]
organisation = soup.findAll("div", {"class" :"card-header bg-light"}) #card-header bg-light
interns = [] #card-border before card-header
Winter = 0
## Seperation of Winter and Summer organisations
for i in range(len(organisation)):
    for j in range(0,i):
        if organisation[i].string == organisation[j].string:
            Winter = i
            break
        else:
            continue
    if Winter!=0:
        break
    else: 
        continue

##print('Summer organisations\n')
for s in range(0, i-1):
    summerOrgs.append((organisation[s].string).lower())
##print('Winter organisations\n')
for w in range(i, len(organisation)-1):
    winterOrgs.append((organisation[w].string).lower())





#Driver part

print("What do you wanna know?")
print("\n1.Organisations common in summer and winter of Outreachy")
print("\n2.Organisations common with GSoC and Summer edition of Outreachy")
print("\n3.Organisations common with GSoc and Winter edition of Outreachy")
print("\n4. Check whether your desired organisation took part past two times")
print("\n5. Organisations for summer and no. of interns they took")
print("\n6. Organisations for winter and no. of interns they took")


n = int(input())

#according to choices
if n == 1 :
    CommonOrgs()
elif n == 2:
    SummerGSoCCommon()
elif n == 3:
    WinterGsocCommon()
elif n == 4: 
    CheckOrg()
elif n == 5:
    SummerOrgsI()
elif n == 6:
    WinterOrgsI()



