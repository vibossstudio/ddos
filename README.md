# Script DDoS

Kho lưu trữ này chứa một script DDoS (Distributed Denial of Service) viết bằng Python. **Lưu ý: Công cụ này chỉ dành cho mục đích giáo dục. Nhà phát triển không chịu trách nhiệm cho bất kỳ hành động lạm dụng nào của công cụ này.**

## Tính năng

- Tấn công DDoS đa luồng.
- Tùy chỉnh URL và cổng mục tiêu.
- Tùy chọn sử dụng địa chỉ IP giả.
- Tương thích với các môi trường: Termux, iSH, Windows (WSL).

## Hướng dẫn cài đặt

1. **Clone kho lưu trữ**

   Tải về mã nguồn của dự án từ GitHub:

   ```bash
   git clone https://github.com/dhungx/ddos.git
   cd ddos
   ```

2. **Chạy script cài đặt**

   Chạy script cài đặt để tự động cài đặt tất cả các thư viện cần thiết và cấu hình công cụ:
Linux, Android, IOS
   ```bash
   bash setup.sh
   ```
windows
   ```bash
    setup.bat 
   ```
   

3. **Chạy script DDoS**

   Sau khi cài đặt xong, bạn có thể chạy script bằng cách gõ lệnh sau từ bất kỳ đâu trên hệ thống của bạn:

   ```bash
   ddos
   ```

   Hoặc nếu bạn chọn không di chuyển script vào thư mục hệ thống:

   ```bash
   python3 ddos.py
   ```

## Lưu ý

- **Script này yêu cầu Python 3 và pip.** Nếu bạn chưa cài đặt chúng, hãy cài đặt Python 3 và pip trước khi chạy script.
- **Chỉ sử dụng script này cho mục đích giáo dục và kiểm thử.** Không sử dụng nó để tấn công bất kỳ hệ thống nào mà bạn không có quyền.

## Đóng góp

Nếu bạn muốn đóng góp cho dự án, bạn có thể fork kho lưu trữ này và gửi pull request với những thay đổi của bạn.

## Liên hệ

Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ qua email hoặc tạo issue trên GitHub.
```

### Hướng dẫn sử dụng:

- **Clone repo:** Tải về mã nguồn từ GitHub và điều hướng đến thư mục chứa mã nguồn.
- **Cài đặt:** Chạy `bash setup.sh` để cài đặt các phụ thuộc và cấu hình.
- **Chạy:** Sử dụng lệnh `ddos` từ bất kỳ đâu trên hệ thống hoặc chạy trực tiếp bằng Python nếu không di chuyển script.