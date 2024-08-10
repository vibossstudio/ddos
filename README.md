# Script DDoS

Kho lưu trữ này chứa một script DDoS (Distributed Denial of Service) được viết bằng Python. **Lưu ý: Công cụ này chỉ dành cho mục đích giáo dục. Nhà phát triển không chịu trách nhiệm cho bất kỳ hành động lạm dụng nào của công cụ này.**

## Tính năng

- Tấn công DDoS đa luồng.
- Tùy chỉnh URL và cổng mục tiêu.
- Tùy chọn sử dụng địa chỉ IP giả.
- Tương thích với nhiều môi trường: Termux, iSH, Linux.
- Script cài đặt (`setup.sh`) để dễ dàng cài đặt các thư viện cần thiết.

## Hướng dẫn cài đặt

### 1. Clone kho lưu trữ

Trước tiên, bạn cần tải về mã nguồn của dự án từ GitHub bằng lệnh sau:

```bash
git clone https://github.com/dhungx/ddos.git
cd ddos

2. Chạy script cài đặt

Chúng tôi đã chuẩn bị một script cài đặt (setup.sh) để tự động cài đặt tất cả các thư viện cần thiết và cấu hình công cụ để có thể chạy từ bất kỳ đâu trên hệ thống của bạn. Dưới đây là hướng dẫn chi tiết cho từng hệ điều hành:

Trên Linux

	1.	Mở terminal và điều hướng đến thư mục chứa mã nguồn:

cd ddos


	2.	Cấp quyền thực thi cho file setup.sh:

chmod +x setup.sh


	3.	Chạy script cài đặt:

sudo ./setup.sh



Trên Termux (Android)

	1.	Mở ứng dụng Termux và điều hướng đến thư mục chứa mã nguồn:

cd ddos


	2.	Cấp quyền thực thi cho file setup.sh:

chmod +x setup.sh


	3.	Chạy script cài đặt:

./setup.sh



Trên iSH (iOS)

	1.	Mở ứng dụng iSH và điều hướng đến thư mục chứa mã nguồn:

cd ddos


	2.	Cấp quyền thực thi cho file setup.sh:

chmod +x setup.sh


	3.	Chạy script cài đặt:

./setup.sh



Trên Windows (WSL)

	1.	Mở Windows Subsystem for Linux (WSL) và điều hướng đến thư mục chứa mã nguồn:

cd ddos


	2.	Cấp quyền thực thi cho file setup.sh:

chmod +x setup.sh


	3.	Chạy script cài đặt:

sudo ./setup.sh



3. Chạy script DDoS

Sau khi cài đặt xong, bạn có thể chạy script bằng cách gõ lệnh sau từ bất kỳ đâu trên hệ thống của bạn:

ddos

Hoặc nếu bạn chọn không di chuyển script vào thư mục hệ thống:

python3 ddos.py

Lưu ý

	•	Script này yêu cầu Python 3 và pip.
	•	Chỉ sử dụng script này cho mục đích giáo dục và kiểm thử. Không sử dụng nó để tấn công bất kỳ hệ thống nào mà bạn không có quyền.

Đóng góp

Nếu bạn muốn đóng góp cho dự án, bạn có thể fork kho lưu trữ này và tạo pull request với những thay đổi của bạn.