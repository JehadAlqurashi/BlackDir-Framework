from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urlsplit,parse_qs
from termcolor import colored
import requests
import argparse
import googlesearch
import os
import time
def logo():
	print("""
\x1b[30m
 ____  _            _    ____  _      
| __ )| | __ _  ___| | _|  _ \(_)_ __ 
|  _ \| |/ _` |/ __| |/ / | | | | '__|
| |_) | | (_| | (__|   <| |_| | | |   
|____/|_|\__,_|\___|_|\_\____/|_|_| version:0.7
  
help: python3 BlackDir.py -h
==================================================
C0ded By RedVirus[@redvirus0]
Group:BlackPearl[@bp.team]
Site:blackpearl.team                                                                                                    
""")
def fast_crawl(url):
    global list_direct, url_access
    list_direct = []
    url_trim = url.replace("https", "http")
    url_access = url_trim.strip("")
    url_www = url_access.strip("www")
    if "https" in url:
        url_trim = url.replace("https","http")
        url_access = url_trim.strip("http://")
        list_direct.append(url_trim)
    else:
        list_direct.append(url)
    Purl  = request.urlopen(url).read()
    soup = BeautifulSoup(Purl,"html.parser")
    for link in soup.find_all('a'):
        links = link.get('href')
        links = str(links)
        if links == "#" or links == " ":
            pass
        else:
            if "https" in links or "http" in links:
                if "https" in links:
                    if url_access in links:
                        if url_www in links:
                            url_replace = links.replace("https","http")
                            list_direct.append(url_replace)
                    else:
                        pass
                else:
                    if url_www in links:
                        list_direct.append(links)
                    else:
                        pass

def scan(url): #Function FOr Find xss vulnerability
        fast_crawl(url)
        global payload
        print(colored("Please Wait We Scanning . .", "red"))
        time.sleep(2)
        for url_direct in list_direct:
            print(colored("We Scanning This Url: ","grey"),colored(url_direct,"green"))
            time.sleep(2)
            payloads = open("xss_payloads.txt","r")
            query = urlsplit(url).query
            params = parse_qs(query)
            kyes = list(params.keys())
            single_cotation = "'"
            slash = "//"
            double_cotation = '"'
            symbol = ">"
            post_data_get = {}
            post_data_post = {}
            for payload in payloads:
                payload = payload.strip()
                for index,item in enumerate(kyes):
                    if payload == "; alert(1);":
                        payload = single_cotation+payload
                        post_data_get[kyes[index]] = payload
                        response = requests.get(url_direct,params=post_data_get)
                        if payload in response.text:
                            print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                            print("Url Vulnerable", response.url)
                            print(colored("Method:","red")+colored("GET","grey"))
                            print("--------------------------------------------------------")
                        else:
                            print(colored("This Payload Not in Source: Payload >> {}","red").format(payload))
                            print(colored("[!] Method:", "red") + colored("GET", "grey"))
                            print("--------------------------------------------------------")
                    elif payload == ")alert(1);":
                        payload = single_cotation+payload+slash
                        post_data_get[kyes[index]] = payload
                        response = requests.get(url_direct,params=post_data_get)
                        if payload in response.text:
                            print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                            print("Url Vulnerable", response.url)
                            print(colored("Method:","red")+colored("GET","grey"))
                            print("--------------------------------------------------------")
                        else:
                            pass
                    elif payload == '<IMG SRC=”javascript:alert(123);':
                        payload =  payload+double_cotation+symbol
                        post_data_get[kyes[index]] = payload
                        response = requests.get(url_direct,params=post_data_get)
                        if payload in response.text:
                            print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                            print("Url Vulnerable", response.url)
                            print(colored("Method:","red")+colored("GET","grey"))
                            print("--------------------------------------------------------")
                        else:
                            pass

                    else:
                        post_data_get[kyes[index]] = payload
                        response = requests.get(url_direct,params=post_data_get)
                        if payload in response.text:
                            print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                            print("Url Vulnerable", response.url)
                            print(colored("Method:","red")+colored("GET","grey"))
                            print("--------------------------------------------------------")
                        else:
                            pass
                url_content = request.urlopen(url_direct).read()
                inputs = BeautifulSoup(url_content, "html.parser")
                for inputs_form in inputs.find_all("input"):
                    if inputs_form in inputs.find_all("input"):
                        if inputs_form.get('type') == "submit":
                            input_submit = inputs_form.get('name')
                            post_data_post[input_submit] = inputs_form.get("value")
                        if inputs_form.get('type') == 'text':
                            input_name = inputs_form.get('name')
                            post_data_post[input_name] = payload
                response = requests.post(url, post_data_post)  # POST
                if payload in response.text:
                    print(colored("Information:", "grey"))
                    print("")
                    print(colored("[!] Url Vulnerable {}", "green").format(url))
                    print("--------------------------------------------------------")
                    print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                    print("--------------------------------------------------------")
                    print(colored("[!] Method:", "red") + colored("POST", "grey"))
                    print("--------------------------------------------------------")
                    print(colored("Source:", "green"))
                    print("")
                    print(response.text)
                    print("--------------------------------------------------------")
                else:
                    pass

def spider(url,lists):
    if "https" in url:
        url_trim = url.replace("https","http")
        url_access = url_trim.strip("http://")
    Purl  = request.urlopen(url).read()
    soup = BeautifulSoup(Purl,"html.parser")
    for link in soup.find_all('a'):
        links = link.get('href')
        if links == "#" or links == " ":
            pass
        else:
            if "https" in links or "http" in links:
                if "https" in links:
                    if url_access in links:
                        links_replace = links.replace("https","http")
                        print(colored("Found[+]","green"))
                        print("\x1b[32m"+links_replace)
            else:
                print("Found[+]")
                url_fast = url_trim+"/"+links
                print("\x1b[32m"+url_fast)
    for i in lists:
        i = i.strip()
        Purl = url+"/"+i
        response = requests.get(Purl)
        if response.status_code == 200:
            print("\x1b[32mFound[+]")
            print(Purl)
        else:
            pass
    lists = open("list.txt","r")
    if list_dir != None:
        print('Please Wait We Crawling This Directory ',colored(Purl,"red"))
        for direct in  list_dir:
            for i in lists:
                Purl_New = direct+"/"+i
                new_response = requests.get(Purl_New)
                if new_response.status_code == 200:
                    list_dir.append(Purl_New)
                    print("\x1b[32mFound[+]")
                    print(Purl_New)
                else:
                    pass
def dorks(dork,country,level,text): # function for Get Dork
    print("Please Wait ...")
    searching = dork+" "+country+" "+text
    search = googlesearch.search(searching,stop=level)
    for se in search:
        with open("Dorks.txt","a+") as file:
            file.write("\n"+se)
    print("Directory of file: ", os.getcwd() + "/" + "Droks.txt")
def sub(url,subs): #function for gussing subdomain
    for i in subs:
        i = i.strip()
        Purl = i+"."+url
        try:
            response = requests.get("http://"+Purl)
            if response.status_code == 200:
                print("http://"+Purl)
        except requests.exceptions.ConnectionError:
            pass
parser = argparse.ArgumentParser("""
--spider            : Url to find Directory
--list              : If you have list
--dork              : Dump all sites by dork
--level             : If you chose level for Dork [Default=20]
--country           : find Dork By Country
--text              : Dump site text if in site
--subdomain         : find SubDomain of site
--scan              : Scan Site if vulnerable [xss]
ex:
BlackDir.py --list /root/Desktop/list.txt --url http://google.com
BlackDir.py --dork inurl:admin/login.php --country site:uk --level 100
BlackDir.py --subdomain google.com
""")
parser.add_argument("-spider","--spider")
parser.add_argument("-list","--list")
parser.add_argument("-dork","--dork")
parser.add_argument("-country","--country")
parser.add_argument("-level","--level")
parser.add_argument("-subdomain","--subdomain")
parser.add_argument("-scan","--scan")
parser.add_argument("-text","--text")
args = parser.parse_args()
unknown = parser.parse_known_args()
listuser = args.list
dork = args.dork
country = args.country
level = args.level
url = args.spider
subdomains = args.subdomain
scanner = args.scan
text = args.text
sublist = open("sub.txt","r")
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

if dork != None and url == None and subdomains ==None and scanner == None:
    dorks(dork,site,int(level),text)
elif url != None and dork == None and subdomains == None and scanner ==  None:
    spider(url,lists)

elif subdomains!= None and url == None and dork ==None and scanner == None :
    sub(subdomains,sublist)
elif scanner != None and url == None and dork ==None and subdomains == None:
    scan(scanner)
else:
    logo()
