@echo off
setlocal

echo Đang cài đặt các gói, vui lòng đợi...

:: Kiểm tra và cài đặt pip
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python chưa được cài đặt. Vui lòng cài đặt Python trước khi tiếp tục.
    exit /b 1
)

python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo pip chưa được cài đặt. Đang cài đặt pip...
    python -m ensurepip
)

:: Cài đặt các thư viện cần thiết
pip install colorama scapy requests

:: Tạo tệp thực thi cho Windows
echo Đang tạo tệp thực thi cho ddos.py...
echo @echo off > ddos.bat
echo python ddos.py %%* >> ddos.bat

echo Cài đặt hoàn tất. Bạn có thể chạy script bằng cách sử dụng file 'ddos.bat'.

:: Chạy ddos.py
python ddos.py

endlocal