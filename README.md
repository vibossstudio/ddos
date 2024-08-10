Dưới đây là tệp `README.md` bằng tiếng Việt cho dự án DDoS của bạn:

```markdown
# Script DDoS

Kho lưu trữ này chứa một script DDoS (Distributed Denial of Service) được viết bằng Python. **Lưu ý: Công cụ này chỉ dành cho mục đích giáo dục. Nhà phát triển không chịu trách nhiệm cho bất kỳ hành động lạm dụng nào của công cụ này.**

## Tính năng

- Tấn công DDoS đa luồng.
- Tùy chỉnh URL và cổng mục tiêu.
- Tùy chọn sử dụng địa chỉ IP giả.
- Tương thích với nhiều môi trường: Termux, iSH, Linux.
- Script cài đặt (`setup.sh`) để dễ dàng cài đặt các thư viện cần thiết.

## Hướng dẫn cài đặt

1. **Clone kho lưu trữ**

   ```bash
   git clone https://github.com/dhungx/ddos.git
   cd ddos
   ```

2. **Chạy script cài đặt**

   Chạy `setup.sh` để cài đặt tất cả các thư viện cần thiết và cấu hình script để có thể chạy từ bất kỳ đâu trên hệ thống.

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. **Chạy script DDoS**

   Sau khi cài đặt xong, bạn có thể chạy script bằng cách gõ lệnh:

   ```bash
   ddos
   ```

   Hoặc nếu bạn chọn không di chuyển script vào thư mục hệ thống:

   ```bash
   python3 ddos.py
   ```

## Lưu ý

- Script này yêu cầu Python 3 và pip.
- **Chỉ sử dụng script này cho mục đích giáo dục và kiểm thử.** Không sử dụng nó để tấn công bất kỳ hệ thống nào mà bạn không có quyền.
- Hãy cẩn trọng khi sử dụng vì có thể PHẠM PHÁP