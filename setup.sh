#!/bin/bash

# Thông báo bắt đầu cài đặt
echo "PACKAGES ARE BEING INSTALLED, PLEASE WAIT..."

# Cài đặt thư viện colorama
pip3 install colorama

# Hỏi người dùng có muốn chạy công cụ từ bất kỳ đâu trên hệ thống hay không
echo "Do you want to execute DDoS from anywhere on your system? [y/n]: "
read usr

# Hỏi người dùng đang sử dụng môi trường nào: Termux, iSH, hay Linux
echo "Are you using Termux, iSH Shell, or Linux? [termux/ish/linux]: "
read usr_env

if [ "$usr_env" == "termux" ] && [ "$usr" == "y" ]; then
    python=$(command -v python3)
    sed -i "1i \#!$python" ddos.py
    mv ddos.py ddos
    mv ddos /data/data/com.termux/files/usr/bin
    echo "Setup successfully done. Now you can execute the script by typing 'ddos'."

elif [ "$usr_env" == "ish" ] && [ "$usr" == "y" ]; then
    python=$(command -v python3)
    sed -i "1i \#!$python" ddos.py
    mv ddos.py ddos
    mv ddos /usr/local/bin
    echo "Setup successfully done. Now you can execute the script by typing 'ddos'."

elif [ "$usr_env" == "linux" ] && [ "$usr" == "y" ]; then
    linux=$(command -v python3)
    sed -i "1i \#!$linux" ddos.py
    mv ddos.py ddos
    sudo mv ddos /usr/bin
    echo "Setup successfully done. Now you can execute the script by typing 'ddos'."

else
    ./ddos.py
fi