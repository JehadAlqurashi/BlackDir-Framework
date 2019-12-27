import requests
import argparse
import threading
def logo():
	print("""
\x1b[32m
 ____  _            _    ____  _      
| __ )| | __ _  ___| | _|  _ \(_)_ __ 
|  _ \| |/ _` |/ __| |/ / | | | | '__|
| |_) | | (_| | (__|   <| |_| | | |   
|____/|_|\__,_|\___|_|\_\____/|_|_| version:0.2  

==================================================
C0ded By RedVirus[@redvirus0]
Group:BlackPearl[@bp.team]
Site:blackpearl.team
==================================================
BlackDir.py --url : url to find Directory
BlackDir.py --list : if you have list
ex:
BlackDir.py --list /root/Desktop/list.txt --url http://google.com                                                                                                     
""")
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
parser = argparse.ArgumentParser("find Directory and File")
parser.add_argument("-url","--url")
parser.add_argument("-list","--list")
args = parser.parse_args()
listuser = args.list
if listuser != None:
    lists = open(listuser,"r")
else:
    lists = open("list.txt","r")
url = args.url
thred = threading.Thread(target=Dir,args=(url,lists))
if args.url == None:
	logo()
else:
	print("\x1b[32mPlease wait we find Directory .. ")
	thred.start()