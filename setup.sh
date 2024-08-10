#!/bin/sh

# Thông báo bắt đầu cài đặt
echo "Đang cài đặt các gói, vui lòng đợi..."

# Kiểm tra và cài đặt pip3
install_pip() {
    if ! command -v pip3 > /dev/null; then
        echo "pip3 chưa được cài đặt. Đang cài đặt pip3..."
        case "$(uname -s)" in
            Linux*)
                if [ -x "$(command -v apt-get)" ]; then
                    sudo apt-get update
                    sudo apt-get install -y python3-pip
                elif [ -x "$(command -v apk)" ]; then
                    apk add --no-cache py3-pip
                else
                    echo "Không thể xác định công cụ quản lý gói."
                    exit 1
                fi
                ;;
            Darwin*)
                echo "MacOS không hỗ trợ tự động cài đặt pip3 trong script này."
                exit 1
                ;;
            *)
                echo "Hệ điều hành không được hỗ trợ."
                exit 1
                ;;
        esac
    fi
}

install_pip

# Cài đặt thư viện colorama và scapy
pip3 install colorama scapy

# Hỏi người dùng có muốn chạy DDoS từ bất kỳ đâu trên hệ thống hay không
echo "Bạn có muốn chạy DDoS từ bất kỳ đâu trên hệ thống của bạn không? [y/n]: "
read usr

# Hỏi người dùng đang sử dụng môi trường nào: Termux, iSH Shell, hay Linux
echo "Bạn đang sử dụng Termux, iSH Shell, hay Linux? [termux/ish/linux]: "
read usr_env

if [ "$usr_env" = "termux" ] && [ "$usr" = "y" ]; then
    python=$(command -v python3)
    sed -i "1i \#!$python" ddos.py
    chmod +x ddos.py
    mv ddos.py ddos
    mv ddos /data/data/com.termux/files/usr/bin
    echo "Cài đặt thành công. Bạn có thể chạy script bằng lệnh 'ddos'."

elif [ "$usr_env" = "ish" ] && [ "$usr" = "y" ]; then
    python=$(command -v python3)
    sed -i "1i \#!$python" ddos.py
    chmod +x ddos.py
    mv ddos.py ddos
    mv ddos /usr/local/bin
    echo "Cài đặt thành công. Bạn có thể chạy script bằng lệnh 'ddos'."

elif [ "$usr_env" = "linux" ] && [ "$usr" = "y" ]; then
    python=$(command -v python3)
    sed -i "1i \#!$python" ddos.py
    chmod +x ddos.py
    mv ddos.py ddos
    sudo mv ddos /usr/bin
    echo "Cài đặt thành công. Bạn có thể chạy script bằng lệnh 'ddos'."

else
    chmod +x ddos.py
    ./ddos.py
fi