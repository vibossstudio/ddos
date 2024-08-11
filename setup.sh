#!/bin/bash

# Cập nhật hệ thống
echo "Cập nhật hệ thống..."
sudo apt-get update

# Cài đặt Python3 và pip
echo "Cài đặt Python3 và pip..."
sudo apt-get install -y python3 python3-pip

# Cài đặt các thư viện Python cần thiết
echo "Cài đặt các thư viện Python cần thiết..."
pip3 install scapy pyuseragents requests rainbowtext pyfiglet colorama

# Kiểm tra xem tệp ddos.py có tồn tại không
if [ -f "ddos.py" ]; then
    echo "Tệp ddos.py đã được tìm thấy. Chạy tệp..."
    python3 ddos.py
else
    echo "Tệp ddos.py không tồn tại. Vui lòng kiểm tra lại."
fi