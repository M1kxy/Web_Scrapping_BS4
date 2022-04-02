#importing requests to acess webpages and beautiful soup from the bs4 module
import requests
from bs4 import BeautifulSoup
#requesting google.com
result=requests.get("https://www.google.co.in/")
print(result.status_code)
#my part including if statement
if(result.status_code==200):
    print("page is accesable")
else:
    print("Acess denied")
#printing the header of the google homepage
#print(result.headers)
#printing the source code of the google homepage
src = result.content;
#lxml is a extra perimetre but is put into to avoid errors
#in my case lxml didnt work so i passed features="html.parser" as instructed by python
soup = BeautifulSoup(src,features="html.parser")
links = soup.find_all("a")
#print(links)
#print("\n")
#if we want a link on all abouts on this page we use the 
#printing the links and attributes of the links
for link in links:
    if "Images" in link.text:
        print(link)
        print(link.attrs['href'])