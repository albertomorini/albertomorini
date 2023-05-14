
# DO THE MD5 OF A WEBPAGE AND CHECK WITH A PREVIOUS ONE TO SEE IF SOMETHING HAS CHANGED
import requests
from bs4 import *
import hashlib

# store the webpage into the filesystem
def storeWebPage2FS(url):
    urllib.request.urlretrieve(url, doMD5(url)+".html") # saving with the hash of the url

#get the content (text) of the webpage
def getHTML(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser').get_text() # get the content (text/info/data) of the page
    return (soup)

#return the hash of MD5 function
def doMD5(val):
    return hashlib.md5(val.encode()).hexdigest()

#TODO: compare a previous value with the new one
def compareRegister():
    #open json
    pass

def main():
    print("Welcome!\nMenu:")
    print("\t 1) Compare existing website")
    print("\t 2) Add a new website")
    choice = int(input("Insert your choice: "))

    if(choice==1):
        compareRegister()
    elif(choice==2): #add a new entry
        url=input("Put the url of the website you want to monitor: ")
        dwnIfChange = input("Download the new webpage if will change? (Yes or No)")
        
    else:
        print("I dunno, bye!")

    #x = getHTML("http://www.github.com/albertomorini")
    x = getHTML("https://time.is/")
    y = getHTML("https://beautiful-soup-4.readthedocs.io/en/latest/")
    print(x==y)

    '''
        IDEA OF STORAGE:
        [
            {
                url: ...
                last_hash: ...
                date_last: ...
                dwnIfChanged: true/false #download the page if different from last time
            }
        ]
    '''



main()