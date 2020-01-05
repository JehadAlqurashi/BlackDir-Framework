import requests
import argparse
import threading
import googlesearch
import os
def logo():
	print("""
\x1b[30m
 ____  _            _    ____  _      
| __ )| | __ _  ___| | _|  _ \(_)_ __ 
|  _ \| |/ _` |/ __| |/ / | | | | '__|
| |_) | | (_| | (__|   <| |_| | | |   
|____/|_|\__,_|\___|_|\_\____/|_|_| version:0.4
  
help: python3 BlackDir.py -h
==================================================
C0ded By RedVirus[@redvirus0]
Group:BlackPearl[@bp.team]
Site:blackpearl.team                                                                                                    
""")
#function for find Directory
def Dir(url,list): #function for find Directory
    for i in list:
        i = i.strip()
        Purl = url+"/"+i
        response = requests.get(Purl,data=None)
        if response.status_code == 200:
            print("\x1b[32mFound[+]")
            print(Purl)
        else:
            pass
def dorks(dork,country,level): # function for Get Dork
    print("Please Wait ...")
    searching = dork+" "+country
    search = googlesearch.search(searching,stop=level)
    for se in search:
        with open("Dorks.txt","a+") as file:
            file.write("\n"+se)
    print("Directory of file: ", os.getcwd() + "/" + "Droks.txt")
parser = argparse.ArgumentParser("""
--url : Url to find Directory
--list : If you have list
--dork  : Dump all sites by dork
--level : If you chose level for Dork [Default=20]
--country : find Dork By Country
ex:
BlackDir.py --list /root/Desktop/list.txt --url http://google.com
BlackDir.py --dork inurl:admin/login.php --country site:uk --level 100
""")
parser.add_argument("-url","--url")
parser.add_argument("-list","--list")
parser.add_argument("-dork","--dork")
parser.add_argument("-country","--country")
parser.add_argument("-level","--level")
args = parser.parse_args()
listuser = args.list
dork = args.dork
country = args.country
level = int(args.level)
url = args.url
if level != None:
    level = level
else:
    level= 20
if country != None:
    site=country
else:
    site = " "
if listuser != None:
    lists = open(listuser,"r")
else:
    lists = open("list.txt","r")

thred = threading.Thread(target=Dir, args=(url, lists))
if dork != None and url == None:
    dorks(dork,site,level)
elif url != None and dork == None:
    print("Please Wait ... ")
    thred.start()
else:
    logo()
