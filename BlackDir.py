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
import datetime


def logo():
    print("""
\x1b[30m
  ____  _            _    _____  _        ______                                           _    
 |  _ \| |          | |  |  __ \(_)      |  ____|                                         | |   
 | |_) | | __ _  ___| | _| |  | |_ _ __  | |__ _ __ __ _ _ __ ___   _____      _____  _ __| | __
 |  _ <| |/ _` |/ __| |/ / |  | | | '__| |  __| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
 | |_) | | (_| | (__|   <| |__| | | |    | |  | | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
 |____/|_|\__,_|\___|_|\_\_____/|_|_|    |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
                                                                                                
                                                                                                                                                                   
help: python3 BlackDir.py -h
==================================================
C0ded By RedVirus[@redvirus0]                                                                                           
""")


def fast_crawl(url):
    global list_direct, url_access, url_pure, url_source
    list_direct_pure = []
    list_direct = []
    url_pure = url.strip("https://www.")
    url_pure = "http://" + url_pure
    list_direct.append(url_pure)
    url_request = request.urlopen(url_pure)
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
                    url_generate = url_pure + "/" + link_pure
                    if url_generate in list_direct:
                        pass
                    else:
                        list_direct.append(url_pure + "/" + link_pure)
    for sec_url in list_direct:
        try:
            url_request = request.urlopen(sec_url).read()
            url_source = BeautifulSoup(url_request, "html.parser")
        except error.URLError:
            pass
        for urls in url_source.findAll("a"):
            urls_find = urls.get("href")
            if urls_find == None:
                urls_find = "#"
            if "#" in urls_find or " " in urls_find or "http" in urls_find or "https" in urls_find or "www" in urls_find or "@" in urls_find or urls_find == "#":
                pass
            else:
                urls_avi = url + "/" + urls_find
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
                            if url in urls_find:
                                pass
                            else:
                                list_direct_pure.append(url_pure + "/" + urls_find)
    for urls_error in list_direct_pure:
        if urls_error in list_direct:
            pass
        else:
            list_direct.append(urls_error)
    for urls_final in list_direct:
        if urls_final == url_pure:
            pass
        else:
            print(colored("Found[+]\n" + urls_final, "green"))
    print(colored("Fast spider Done ..", "red"))


def sql(url):  # Function F0r find Sql_Injection
    global equal_parameter, keys, equal_par, response
    fast_crawl(url)
    for urls in list_direct:
        query = urlsplit(urls).query
        parameter = parse_qs(query)
        url_request = request.urlopen(urls).read().decode(encoding="iso-8859-1")
        url_source = BeautifulSoup(url_request, "html.parser")
        values = list(parameter.values())
        for index, item in enumerate(values):
            equal_par = values[index]
            for i in equal_par:
                equal_parameter = str(i + "'")
                keys = list(parameter.keys())
            for index, item in enumerate(keys):
                parmeter_name = keys[index]
                parmeter_name = str(parmeter_name)
                post_sql = {}
                post_sql[parmeter_name] = equal_parameter
                response = requests.get(urls, post_sql)
            if "Warning" in response.text:
                print("Information: ")
                print(colored("SQL Injection", "red"), colored("Type:Union Based", "grey"))
                print("Url Vulnerable:", urls)
            else:
                pass


def sql_dorks(url):
    global equal_parameter, response, keys
    try:
        query = urlsplit(url).query
        parameter = parse_qs(query)
        url_request = request.urlopen(url).read().decode(encoding="iso-8859-1")
        url_source = BeautifulSoup(url_request, "html.parser")
        values = list(parameter.values())
        for index, item in enumerate(values):
            equal_par = values[index]
            for i in equal_par:
                equal_parameter = str(i + "'")
                keys = list(parameter.keys())
            for index, item in enumerate(keys):
                parmeter_name = keys[index]
                parmeter_name = str(parmeter_name)
                post_sql = {}
                post_sql[parmeter_name] = equal_parameter
                response = requests.get(url, post_sql)
            if "Warning" in response.text:
                print(colored("Please Wait .. ", "red"))
                print("Information: ")
                print(colored("SQL Injection", "red"), colored("Type:Union Based", "grey"))
                print("Url Vulnerable:", url)
            else:
                pass
    except error.HTTPError:
        pass


def xss(url):  # Function FOr Find xss vulnerability
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
    print(colored("Please Wait We Spider all Directories . .", "red"))
    fast_crawl(url)
    print(colored("We Crawling By This File >>" + os.getcwd() + "/" + "list.txt", "grey"))
    for i in lists:
        i = i.strip()
        Purl = url_pure + "/" + i
        response = requests.get(Purl)
        if response.status_code == 200:
            print("\x1b[32mFound[+]")
            print(response.url)
        else:
            pass


def dorks(dork, country, level, text):  # function for Get Dork
    global searching, list_url, dork_search
    if country == None and text != None:
        dork_search = dork + "intext:" + text
    if text == None and country != None:
        dork_search = dork + "site:" + country
    if text == None and country == None:
        dork_search = dork
    print(colored("Please Wait .. ", "red"))
    time.sleep(40)
    searching = googlesearch.search(dork_search, stop=level)
    print(colored("-------------------------------------------", "red"))
    print(colored("Dork:" + dork, "red"))
    print(colored("-------------------------------------------", "red"))
    print(colored("level: {}", "red").format(level))
    for search in searching:
        print(search)
    print(colored("Finished Dork Search", "grey"))


def list_dorks(dork, level):
    global list_sql, dorks, search
    list_dork = []
    list_sql = []
    file = open(dork, "r+")
    for dorks in file:
        list_dork.append(dorks)
    file.close()
    for userAgent in googlesearch.get_random_user_agent():
        for URL in list_dork:
            print(colored("-------------------------------------------", "red"))
            print(colored("Dork:" + URL, "red"))
            print(colored("level: {}", "red").format(level))
            print(colored("-------------------------------------------", "red"))
            try:
                searching = googlesearch.search(URL, stop=level, user_agent=userAgent, num=15)
                time.sleep(40)
                for search in searching:
                    print(search)
                Req = requests.get(search)
                if Req.status_code == 200:
                    list_sql.append(search)
                else:
                    pass
            except requests.exceptions.ConnectionError:
                pass
    for urls in list_sql:
        sql_dorks(urls)


def sub(url, subs):  # function for gussing subdomain
    if "https" in url:
        url = url.strip("https://")
    elif "http" in url:
        url = url.strip("http://")
    for i in subs:
        i = i.strip()
        Purl = i + "." + url
        try:
            response = requests.get("http://" + Purl)
            if response.status_code == 200:
                print(colored("Status_Code:200"))
                print(colored("Url:http://{0}", "green").format(Purl))
            else:
                pass
        except:
            pass


def update():
    global year, month, day
    print(colored("Please wait we find update ..","green"))
    date_source = datetime.date(2020, 3, 20)
    request_date = request.urlopen(
        "https://raw.githubusercontent.com/RedVirus0/BlackDir-Framework/master/update.txt").read()
    request_source_date = BeautifulSoup(request_date, "html.parser")
    for date in request_source_date.find_all("p"):
        year = date.text
    for date in request_source_date.find_all("span"):
        month = date.text
    for date in request_source_date.find_all("i"):
        day = date.text
    date_github = datetime.date(int(year), int(month), int(day))
    if date_source < date_github:
        request_update = request.urlopen("https://raw.githubusercontent.com/RedVirus0/BlackDir-Framework/master/BlackDir.py")
        request_read = request_update.read()
        text_source = request_read.decode("utf-8")
        print(text_source)
        os.remove("BlackDir.py")
        file_replace = open("BlackDir.py", "w+")
        file_replace.write(text_source)
        print("Finish download last update ..")
    else:
        print(colored("Sorry .. No Update There !","red"))


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
--update            : Update Tool ex: --update check
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
parser.add_argument("-listDork", "--listDork")
parser.add_argument("-update", "--update")
args = parser.parse_args()
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
updates = args.update
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

if dork != None and url == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None and updates == None:
    dorks(dork, site, int(level), text)
elif url != None and dork == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None and updates == None:
    spider(url, lists)
elif subdomains != None and url == None and dork == None and scanner == None and sql_inection == None and list_dork == None and updates == None:
    sub(subdomains, sublist)
elif scanner != None and url == None and dork == None and subdomains == None and sql_inection == None and list_dork == None and updates == None:
    xss(scanner)
elif sql_inection != None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None:
    sql(sql_inection)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork != None and updates == None:
    list_dorks(list_dork, int(level))
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates != None:
    if updates=="check" or updates == "Check":
        update()
    else:
        print(colored("Error ! Please Ener --update check","red"))
else:
    logo()
