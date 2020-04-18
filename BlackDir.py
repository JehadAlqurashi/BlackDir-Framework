import time
from urllib import request
from urllib.parse import urlsplit, parse_qs
import os
import subprocess

try:
    from bs4 import BeautifulSoup
except:
    os.system("clear")
    print(colored("\nPlease Install bs4 library command install:\npip3 install bs4", "red"))
    exit()

# ----------------------------------
try:
    from termcolor import colored
except:
    os.system("clear")
    print(colored("\nPlease Install termcolor library command install:\npip3 install termcolor", "red"))
    exit()

# --------------------------------

try:
    import requests
except:
    os.system("clear")
    print(colored("\nPlease Install requests library command install:\npip3 install requests", "red"))
    exit()

# --------------------------------

try:
    import argparse
except:
    os.system("clear")
    print(colored("\nPlease Install argparse library command install:\npip3 install argparse", "red"))
    exit()

# --------------------------------

try:
    import googlesearch
except:
    os.system("clear")
    print(colored("\nPlease Install google library command install:\npip3 install google", "red"))
    exit()


def logo():
    print("""
\x1b[32m
  ____  _            _    _____  _        ______                                           _    
 |  _ \| |          | |  |  __ \(_)      |  ____|                                         | |   
 | |_) | | __ _  ___| | _| |  | |_ _ __  | |__ _ __ __ _ _ __ ___   _____      _____  _ __| | __
 |  _ <| |/ _` |/ __| |/ / |  | | | '__| |  __| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
 | |_) | | (_| | (__|   <| |__| | | |    | |  | | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
 |____/|_|\__,_|\___|_|\_\_____/|_|_|    |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\ version:1.9


help: python3 BlackDir.py -h
==================================================
C0ded By RedVirus[@redvirus0]                                                                                           
""")


def fast_crawl(url):
    global list_direct, url_access, url_source
    list_direct_pure = []
    list_direct = []
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
                                list_direct_pure.append(url + "/" + urls_find)
    for urls_error in list_direct_pure:
        if urls_error in list_direct:
            pass
        else:
            list_direct.append(urls_error)
    for urls_final in list_direct:
        if urls_final == None:
            pass
        else:
            req = requests.get(urls_final)
            try:
                if req.status_code == 200:
                    print(colored("Status Code:", "red"), colored(req.status_code, "green"))
                else:
                    print(colored("Status Code:", "red"), colored(req.status_code, "green"))
            except requests.exceptions.ConnectionError:
                pass
            print(colored("Url:", "red"), colored(urls_final, "green"))
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
    global equal_parameter, response, keys, request_status
    try:
        time.sleep(1.0)
        try:
            request_status = requests.get(url)
            if request_status.status_code == 200:
                print(colored("Request Status:", "red"), colored(request_status.status_code, "green"))
                print("Url:", colored(url, "green"))
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
                        print(colored("SQL Injection", "red"), colored("Type:Union Based", "grey"))
                        print(colored("Url Vulnerable:", "green"), colored(url, "red"))
                    else:
                        print(colored("Url Not Vulnerable: ", "red"), colored(response.url, "green"))
            else:
                print(colored("Request Status:" + request_status.status_code, "red"))
                print("Url:", request_status.url)
        except requests.exceptions.ConnectionError:
            pass
    except:
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
                print(colored("[!] Url Vulnerable {}", "green").format(url))
                print("--------------------------------------------------------")
                print(colored("[!] Is Vulnerable [xss] Payload >> {}", "green").format(payload))
                print("--------------------------------------------------------")
                print(colored("[!] Method:", "red") + colored("POST", "grey"))
                print("--------------------------------------------------------")
                print(colored("Source:", "green"))
                print(response.text)
                print("--------------------------------------------------------")
            else:
                pass


def httplive(url):
    global live
    live = None
    bool(live)
    try:
        request_live = requests.get(url)
        if request_live.status_code == 200:
            print(colored("Http Live : ", "green"), url)
            live = 1
    except requests.exceptions.ConnectionError:
        print(colored("Http Down : ", "red"), url)
        live = 0


def spider(url, lists, secure):
    print(colored("Please Wait We Check if URL Live or Down . . ", "green"))
    time.sleep(3)
    httplive(url)
    if live == 1:
        if secure == "list.txt":
            print(colored("Please Wait We Spider all Directories . .", "red"))
            time.sleep(3)
            fast_crawl(url)
            print(colored("We Crawling By This File >>" + os.getcwd() + "/" + "list.txt", "green"))
            for i in lists:
                i = i.strip()
                Purl = url + "/" + i
                response = requests.get(Purl)
                if response.status_code == 200:
                    print("\x1b[32mFound[+]")
                    print(response.url)
                else:
                    pass
        else:
            fast_crawl(url)
            print(colored("We Crawling By This File >>" + listuser, "green"))
            for i in lists:
                i = i.strip()
                Purl = url + "/" + i
                response = requests.get(Purl)
                if response.status_code == 200:
                    print("\x1b[32mFound[+]")
                    print(response.url)
                else:
                    pass
    else:
        pass


def dorks(dork, country, text):  # function for Get Dork
    global soup
    list_of_url = []
    results = []
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {'user-agent': user_agent}
    link = "https://google.com/search?q=inurl:" + dork
    rep = requests.get(link, headers=headers)
    if rep.status_code == 200:
        soup = BeautifulSoup(rep.content, "html.parser")
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
    for dic in results:
        list_of_link = list(dic.values())
        print("\n")
        print(colored("Title Of Link:", "green"), list_of_link[0], "\n")
        print(colored("Link:", "green"), list_of_link[1], "\n")
        list_of_url.append(list_of_link[1])
    line = input(colored("You Want Scan All URLs [Y/N]: ", "grey"))
    if line == "Y" or line == "y" or line == None:
        for urls in list_of_url:
            sql_dorks(urls)
    else:
        pass


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


def ip_reverse(ip):
    try:
        url = ("https://api.hackertarget.com/reverseiplookup/?q=")
        url_ip = url + ip
        req = requests.get(url_ip)
        response = req.text
        print(colored(response, "blue"))
    except requests.exceptions.ConnectionError:
        print(colored("Connection Fail", "blue"))


def update():
    os.system("cd .. && rm -rf BlackDir-Framework-New && mkdir BlackDir-Framework-New && cd BlackDir-Framework-New && git clone https://github.com/RedVirus0/BlackDir-Framework.git && echo 'New Directory >> ' && pwd")


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
--RevIP             : Dump all site by ip
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
parser.add_argument("-RevIP", "--RevIP")
args = parser.parse_args()
secure = None
listuser = args.list
if listuser != None:
    listuser = args.list
    secure = None
elif listuser == None:
    listuser = open("list.txt", "r")
    secure = "list.txt"
ip = args.RevIP
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
site = args.country
if dork != None and url == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None and updates == None and ip == None:
    dorks(dork, site, text)
elif url != None and dork == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None and updates == None and ip == None:
    spider(url, listuser, secure)
elif subdomains != None and url == None and dork == None and scanner == None and sql_inection == None and list_dork == None and updates == None and ip == None:
    sub(subdomains, sublist)
elif scanner != None and url == None and dork == None and subdomains == None and sql_inection == None and list_dork == None and updates == None and ip == None:
    xss(scanner)
elif sql_inection != None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip == None:
    sql(sql_inection)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork != None and updates == None and ip == None:
    list_dorks(list_dork, int(level))
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates != None and ip == None:
    if updates == "check" or updates == "Check":
        update()
    else:
        print(colored("Error ! Please Enter --update check", "red"))
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip != None:
    ip_reverse(ip)
else:
    logo()
