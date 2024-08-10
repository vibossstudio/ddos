@echo off
echo Đang cài đặt các gói, vui lòng đợi...

:: Kiểm tra và cài đặt pip
python -m pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo pip chưa được cài đặt. Đang cài đặt pip...
    python -m ensurepip
)

:: Cài đặt các thư viện colorama, scapy, và requests
pip install colorama scapy requests

:: Hỏi người dùng có muốn chạy DDoS từ bất kỳ đâu trên hệ thống hay không
set /p usr="Bạn có muốn chạy DDoS từ bất kỳ đâu trên hệ thống của bạn không? [y/n]: "

:: Nếu người dùng chọn 'y'
if "%usr%"=="y" (
    :: Kiểm tra đường dẫn của Python và tạo liên kết
    set "python_path=%PYTHON_HOME%"
    if "%python_path%"=="" (
        set "python_path=%~dp0"
    )
    echo @echo off > ddos.bat
    echo "%python_path%\python.exe" "%~dp0\ddos.py" %%* >> ddos.bat
    echo Cài đặt thành công. Bạn có thể chạy script bằng lệnh 'ddos.bat'.
) else (
    echo Không tạo liên kết. Bạn có thể chạy script bằng cách sử dụng 'python ddos.py'.
)