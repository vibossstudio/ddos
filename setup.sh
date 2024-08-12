#!/bin/bash

# Kiểm tra hệ điều hành
OS=$(uname -s)

echo "Bạn đang dùng: $OS"

# Cài đặt thư viện cần thiết cho từng hệ điều hành

if [ "$OS" = "Linux" ]; then
    echo "Đang cài đặt thư viện cho Linux..."

    # Cài đặt pip nếu chưa có
    if ! command -v pip3 &> /dev/null; then
        echo "pip3 không tìm thấy. Đang cài đặt pip3..."
        sudo apt update
        sudo apt install -y python3-pip
    fi

    # Cài đặt các thư viện Python cần thiết
    pip3 install requests colorama tqdm

elif [ "$OS" = "Darwin" ]; then
    echo "Đang cài đặt thư viện cho macOS..."

    # Cài đặt pip nếu chưa có
    if ! command -v pip3 &> /dev/null; then
        echo "pip3 không tìm thấy. Đang cài đặt pip3..."
        sudo easy_install pip
    fi

    # Cài đặt các thư viện Python cần thiết
    pip3 install requests colorama tqdm

elif [ "$OS" = "Termux" ]; then
    echo "Đang cài đặt thư viện cho Termux..."

    # Cài đặt pip nếu chưa có
    if ! command -v pip &> /dev/null; then
        echo "pip không tìm thấy. Đang cài đặt pip..."
        pkg install python
    fi

    # Cài đặt các thư viện Python cần thiết
    pip install requests colorama tqdm

elif [ "$OS" = "iOS" ] || [ "$OS" = "iSH" ]; then
    echo "Đang cài đặt thư viện cho iSH Shell..."

    # Cài đặt pip nếu chưa có
    if ! command -v pip3 &> /dev/null; then
        echo "pip3 không tìm thấy. Đang cài đặt pip3..."
        apk update
        apk add py3-pip
    fi

    # Cài đặt các thư viện Python cần thiết
    pip3 install requests colorama tqdm

else
    echo "Hệ điều hành không được hỗ trợ!"
    exit 1
fi

# Chạy file ddos.py bằng Python 3
echo "Đang chạy ddos.py bằng Python 3..."
python3 ddos.py