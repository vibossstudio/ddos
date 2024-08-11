#!/bin/bash

# Hàm cài đặt thư viện Python
install_python_libraries() {
    echo "Cài đặt các thư viện Python cần thiết..."
    pip3 install scapy pyuseragents requests rainbowtext pyfiglet colorama
}

# Kiểm tra hệ điều hành và môi trường
if [ "$(uname)" == "Linux" ]; then
    if [ -n "$ANDROID_ROOT" ]; then
        # Termux
        echo "Phát hiện Termux. Cài đặt thư viện Python..."
        pkg update
        pkg install -y python
        install_python_libraries
    elif [ -x "$(command -v apt-get)" ]; then
        # Debian/Ubuntu
        echo "Phát hiện hệ điều hành Debian/Ubuntu. Cài đặt Python3 và pip..."
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip
        install_python_libraries
    elif [ -x "$(command -v yum)" ]; then
        # Red Hat/Fedora/CentOS
        echo "Phát hiện hệ điều hành Red Hat/Fedora/CentOS. Cài đặt Python3 và pip..."
        sudo yum update -y
        sudo yum install -y python3 python3-pip
        install_python_libraries
    elif [ -x "$(command -v dnf)" ]; then
        # Fedora mới hơn
        echo "Phát hiện hệ điều hành Fedora. Cài đặt Python3 và pip..."
        sudo dnf update -y
        sudo dnf install -y python3 python3-pip
        install_python_libraries
    elif [ -x "$(command -v pacman)" ]; then
        # Arch Linux
        echo "Phát hiện hệ điều hành Arch Linux. Cài đặt Python3 và pip..."
        sudo pacman -Syu --noconfirm
        sudo pacman -S --noconfirm python python-pip
        install_python_libraries
    else
        echo "Hệ điều hành không được hỗ trợ hoặc không thể nhận diện."
        exit 1
    fi
elif [ "$(uname)" == "Darwin" ]; then
    # macOS
    echo "Phát hiện macOS. Cài đặt Python3 và pip..."
    if [ -x "$(command -v brew)" ]; then
        brew update
        brew install python
        install_python_libraries
    else
        echo "Homebrew không được cài đặt. Vui lòng cài đặt Homebrew trước."
        exit 1
    fi
elif [ "$(uname)" == "MINGW"* ] || [ "$(uname)" == "MSYS"* ]; then
    # Windows với Git Bash
    echo "Phát hiện Windows. Cài đặt Python3 và pip..."
    echo "Vui lòng cài đặt Python và pip từ trang chính thức Python."
    echo "https://www.python.org/downloads/"
    echo "Sau khi cài đặt, hãy chạy 'pip install scapy pyuseragents requests rainbowtext pyfiglet colorama' để cài đặt các thư viện cần thiết."
    exit 1
else
    echo "Hệ điều hành không được hỗ trợ."
    exit 1
fi

# Kiểm tra xem tệp ddos.py có tồn tại không
if [ -f "ddos.py" ]; then
    echo "Tệp ddos.py đã được tìm thấy. Chạy tệp..."
    python3 ddos.py
else
    echo "Tệp ddos.py không tồn tại. Vui lòng kiểm tra lại."
fi