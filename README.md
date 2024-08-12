# DDoS Attack Script

Đây là một tập lệnh Python đơn giản để thực hiện các cuộc tấn công DDoS (Từ chối dịch vụ phân tán). Tập lệnh này cung cấp hai loại tấn công:

1. **HTTP GET Flood**: Gửi các yêu cầu HTTP GET liên tục tới mục tiêu.
2. **SYN Flood**: Gửi các gói SYN để làm tắc nghẽn kết nối TCP tới mục tiêu.

## Cảnh báo

Sử dụng tập lệnh này chỉ trong môi trường kiểm tra và với sự cho phép rõ ràng từ các bên liên quan. Việc tấn công các trang web hoặc dịch vụ mà không có sự đồng ý là bất hợp pháp và có thể dẫn đến các hậu quả pháp lý nghiêm trọng. Đừng tấn công các trang web chính phủ hoặc các dịch vụ quan trọng.

## Yêu cầu

- Python 3
- pip (Python package installer)

## Cài đặt

### Bước 1: Clone hoặc tải mã nguồn

```bash
git clone https://github.com/dhungx/ddos.git
cd ddos
chmod +x setup.sh
bash setup.sh
```

Tập lệnh `setup.sh` sẽ kiểm tra hệ điều hành của bạn và cài đặt các thư viện Python cần thiết như `requests`, `colorama`, và `tqdm`.

## Sử dụng

Sau khi cài đặt xong, bạn có thể chạy tập lệnh `ddos.py` để thực hiện tấn công DDoS.

```bash
python3 ddos.py
```

## Hướng dẫn sử dụng `ddos.py`

1. Nhập URL mục tiêu.
2. Nhập số lượng gói tin cho HTTP GET Flood hoặc nhập `u` để tấn công không giới hạn.
3. Nhập IP giả mạo cho SYN Flood (hoặc để trống để tự động tạo một IP giả).
4. Nhập số lượng luồng cho HTTP GET Flood và SYN Flood.

## Góp ý và báo lỗi

Nếu bạn gặp phải lỗi hoặc có bất kỳ đề xuất nào, vui lòng mở một vấn đề mới trên [GitHub Issues](https://github.com/dhungx/ddos/issues).

## Giấy phép

Dự án này được phát hành dưới giấy phép [MIT](LICENSE)
