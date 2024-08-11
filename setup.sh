#!/bin/sh

# Hàm cài đặt thư viện Python
install_python_libraries() {
    echo "Cài đặt các thư viện Python cần thiết..."
    pip3 install scapy rainbowtext requests colorama pyfiglet pyuseragents
}

# Hàm cài đặt cho Linux
install_linux() {
    echo "Cài đặt Python3 và pip trên Linux..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
    install_python_libraries
}

# Hàm cài đặt cho Windows (WSL)
install_windows() {
    echo "Cài đặt Python3 và pip trên Windows (WSL)..."
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip
    install_python_libraries
}

# Hàm cài đặt cho iSH shell
install_ish() {
    echo "Cài đặt Python3 và pip trên iSH shell..."
    apk update
    apk add python3 py3-pip
    install_python_libraries
}

# Hàm cài đặt cho Termux
install_termux() {
    echo "Cài đặt Python3 và pip trên Termux..."
    pkg update
    pkg install -y python
    pip install --upgrade pip
    install_python_libraries
}

# Xác định hệ điều hành và cài đặt tương ứng
case "$(uname -s)" in
    Linux)
        if [ -x "$(command -v apk)" ]; then
            # iSH shell (Alpine Linux)
            install_ish
        else
            # Linux
            install_linux
        fi
        ;;
    MINGW* | MSYS* | MSL*)
        # Windows (WSL)
        install_windows
        ;;
    *)
        if [ -x "$(command -v apk)" ]; then
            # iSH shell (Alpine Linux)
            install_ish
        elif [ -x "$(command -v pkg)" ]; then
            # Termux
            install_termux
        else
            echo "Hệ điều hành không được hỗ trợ."
            exit 1
        fi
        ;;
esac

# Kiểm tra xem tệp ddos.py có tồn tại không
if [ -f "ddos.py" ]; then
    echo "Tệp ddos.py đã được tìm thấy. Chạy tệp..."
    python3 ddos.py
else
    echo "Tệp ddos.py không tồn tại. Vui lòng kiểm tra lại."
fi