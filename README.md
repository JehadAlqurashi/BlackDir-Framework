# BlackDir
Tool for find directory and dump sites by dork version 3
# Installation
pip3 install -r requirements.txt
# Usage:
--url : Url to find Directory
--list : If you have list
--dork  : Dump all sites by dork
--level : If you chose level for Dork [Default=20]
--country : find Dork By Country
ex:
BlackDir.py --list /root/Desktop/list.txt --url http://google.com
BlackDir.py --dork inurl:admin/login.php --country site:uk --level 100

![Screenshot_2020-01-05_07-48-43](https://user-images.githubusercontent.com/46041727/71780373-f37b6300-2f8f-11ea-8fbc-d6b7b935654b.png)
