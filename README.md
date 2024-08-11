# DDoS Attack Script

## Mô tả

Đây là một script Python để thực hiện các cuộc tấn công từ chối dịch vụ (DDoS) bao gồm hai loại tấn công: HTTP Flood và SYN Flood. Script này hỗ trợ nhiều hệ điều hành khác nhau và bao gồm một tập lệnh shell để tự động cài đặt các thư viện cần thiết.

## Yêu Cầu

- Python 3
- pip (Python package installer)

## Cài Đặt

1. **Clone Repository**

   Nếu bạn chưa clone repository, hãy sử dụng lệnh sau:

   ```bash
   git clone https://github.com/dhungx/ddos.git
   cd ddos
   ```

2. **Chạy Script Cài Đặt**

   Tạo và chạy tập lệnh cài đặt `setup.sh` để cài đặt các thư viện cần thiết và chạy script chính:

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

## Sử Dụng

1. **Chạy Script Python**

   Sau khi cài đặt xong, bạn có thể chạy script `ddos.py` trực tiếp từ dòng lệnh:

   ```bash
   python3 ddos.py
   ```

2. **Nhập Thông Tin Tấn Công**

   - **HTTP Flood**: Nhập URL mục tiêu và kích thước gói tin (hoặc để trống để tấn công không giới hạn).
   - **SYN Flood**: Script sẽ tự động chạy tấn công SYN Flood.

## Cảnh Báo

Sử dụng script này chỉ cho mục đích học thuật và kiểm tra bảo mật trên hệ thống của bạn hoặc hệ thống mà bạn có sự cho phép. Việc sử dụng script này để tấn công các hệ thống mà bạn không có quyền kiểm soát là bất hợp pháp và có thể dẫn đến hậu quả pháp lý nghiêm trọng.

## Giấy Phép

Script này được phát hành dưới giấy phép MIT. Xem [LICENSE](LICENSE) để biết thêm chi tiết.