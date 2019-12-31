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
|____/|_|\__,_|\___|_|\_\____/|_|_| version:0.3  

==================================================
C0ded By RedVirus[@redvirus0]
Group:BlackPearl[@bp.team]
Site:blackpearl.team
==================================================
BlackDir.py --url : Url to find Directory
BlackDir.py --list : If you have list
BlackDir.py --dork : Dump all sites by dork
ex:
BlackDir.py --list /root/Desktop/list.txt --url http://google.com
BlackDir.py --dork inurl:admin/login.php                                                                                                     
""")
#function for find Directory
def Dir(url,list):
    for i in list:
        i = i.strip()
        Purl = url+"/"+i
        response = requests.get(Purl,data=None)
        if response.status_code == 200:
            print("\x1b[32mFound[+]")
            print(Purl)
        else:
            pass
def dorks(dork): # function for Get Dork
    print("Please Wait ...")
    search = googlesearch.search(dork,stop=10)
    for se in search:
        with open("Dorks.txt","a+") as file:
            file.write("\n"+se)
    print("Directory of file: ", os.getcwd() + "/" + "Droks.txt")
parser = argparse.ArgumentParser()
parser.add_argument("-url","--url")
parser.add_argument("-list","--list")
parser.add_argument("-dork","--dork")
args = parser.parse_args()
listuser = args.list
dork = args.dork
if listuser != None:
    lists = open(listuser,"r")
else:
    lists = open("list.txt","r")
url = args.url
thred = threading.Thread(target=Dir, args=(url, lists))
if dork != None and url == None:
    dorks(dork)
elif url != None and dork == None:
    print("Please Wait ... ")
    thred.start()
else:
    logo()
