#!/bin/bash

# Thông báo bắt đầu cài đặt
echo "Đang cài đặt các gói, vui lòng đợi..."

# Cài đặt các gói cần thiết
pip_install() {
    pip3 install --upgrade pip
    pip3 install colorama scapy
}

# Kiểm tra và cài đặt pip nếu chưa có
install_pip() {
    if ! command -v pip3 &> /dev/null; then
        echo "pip3 chưa được cài đặt. Đang cài đặt pip3..."
        if [[ "$OSTYPE" == "linux-android"* ]]; then
            pkg install python-pip -y
        elif [[ "$OSTYPE" == "linux"* ]]; then
            apt-get update
            apt-get install python3-pip -y
        elif [[ "$OSTYPE" == "darwin"* ]]; then
            brew install python
        elif [[ "$OSTYPE" == "cygwin" || "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
            echo "Vui lòng cài đặt Python và pip từ https://www.python.org/downloads/"
            exit 1
        else
            echo "Hệ điều hành không được hỗ trợ."
            exit 1
        fi
    fi
}

# Hỏi người dùng có muốn chạy công cụ từ bất kỳ đâu trên hệ thống hay không
echo "Bạn có muốn chạy DDoS từ bất kỳ đâu trên hệ thống của bạn không? [y/n]: "
read usr

# Hỏi người dùng đang sử dụng môi trường nào: Termux, iSH, hay Linux
echo "Bạn đang sử dụng Termux, iSH Shell, hay Linux? [termux/ish/linux]: "
read usr_env

# Cài đặt pip nếu cần và các thư viện Python
install_pip
pip_install

# Thiết lập môi trường dựa trên sự lựa chọn của người dùng
if [ "$usr_env" == "termux" ] && [ "$usr" == "y" ]; then
    python=$(command -v python3)
    sed -i "1i \#!$python" ddos.py
    mv ddos.py ddos
    mv ddos /data/data/com.termux/files/usr/bin
    echo "Cài đặt hoàn tất. Bây giờ bạn có thể chạy script bằng cách gõ 'ddos'."

elif [ "$usr_env" == "ish" ] && [ "$usr" == "y" ]; then
    python=$(command -v python3)
    sed -i "1i \#!$python" ddos.py
    mv ddos.py ddos
    mv ddos /usr/local/bin
    echo "Cài đặt hoàn tất. Bây giờ bạn có thể chạy script bằng cách gõ 'ddos'."

elif [ "$usr_env" == "linux" ] && [ "$usr" == "y" ]; then
    linux=$(command -v python3)
    sed -i "1i \#!$linux" ddos.py
    mv ddos.py ddos
    sudo mv ddos /usr/bin
    echo "Cài đặt hoàn tất. Bây giờ bạn có thể chạy script bằng cách gõ 'ddos'."

else
    ./ddos.py
fi