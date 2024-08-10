# DDoS

**Author:** __ViBoss__  
**GitHub:** [ViBoss](https://github.com/dhungx)

## Giới thiệu

Dự án này cung cấp một công cụ để thực hiện các cuộc tấn công từ chối dịch vụ (DoS) bằng cách gửi yêu cầu HTTP đến một máy chủ mục tiêu với các thông số ngẫu nhiên, bao gồm các tiêu đề HTTP giả. Công cụ này cho phép bạn kiểm tra tính ổn định của máy chủ khi phải xử lý một lượng lớn yêu cầu.

**Lưu ý:** Công cụ này chỉ nên được sử dụng cho mục đích học tập và kiểm tra. Việc sử dụng công cụ này để tấn công các máy chủ không có sự cho phép là bất hợp pháp và có thể dẫn đến hậu quả pháp lý nghiêm trọng.

## Cài đặt

Để sử dụng công cụ này, bạn cần có Python 3.6 hoặc cao hơn được cài đặt trên hệ thống của mình. Bạn có thể tải Python từ [trang chính thức](https://www.python.org/).

## Cách sử dụng

1. **Clone Repository:**

   ```bash
   git clone https://github.com/dhungx/ddos.git
   cd ddos
   ```

2. **Chạy Công Cụ:**

   ```bash
   python ddos.py or python3 ddos.py
   ```

3. **Nhập thông tin yêu cầu:**

   Sau khi chạy công cụ, bạn sẽ được yêu cầu nhập các thông số sau:
   
   - **Target URL:** URL của máy chủ mục tiêu.
   - **Port:** Cổng mà máy chủ mục tiêu đang lắng nghe.
   - **Packet/s:** Số lượng gói tin muốn gửi mỗi giây.
   - **Threads:** Số lượng luồng (threads) để chạy đồng thời.

## Ví dụ

Khi được yêu cầu nhập thông tin, bạn có thể nhập như sau:

```
[+] Target URL: http://example.com
[+] Port: 80
[+] Packet/s: 100
[+] Threads: 10
```

## Các tùy chọn

- **fake_ip()**: Hàm này tạo một địa chỉ IP giả ngẫu nhiên. Tuy nhiên, trong mã hiện tại, các kết nối vẫn được thực hiện với IP thật của máy chủ mục tiêu.

## Phát triển

Nếu bạn muốn đóng góp vào dự án hoặc báo cáo lỗi, vui lòng gửi yêu cầu kéo (pull request) hoặc mở vấn đề (issue) trên GitHub.

## Cảnh báo

- Việc sử dụng công cụ này để tấn công các máy chủ hoặc dịch vụ mà bạn không có quyền kiểm tra là vi phạm pháp luật. Hãy đảm bảo bạn có sự cho phép của người sở hữu máy chủ trước khi thực hiện bất kỳ hoạt động nào.

- Tôi không chịu trách nhiệm cho bất cứ thứ gì bạn gây ra 

