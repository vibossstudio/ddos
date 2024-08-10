# DDoS Attack Simulation Tool

Đây là công cụ mô phỏng tấn công DDoS (Distributed Denial of Service) được tạo ra cho mục đích giáo dục. Công cụ này giúp người dùng hiểu rõ hơn về cách thức hoạt động của một cuộc tấn công DDoS cơ bản. **Không được sử dụng công cụ này cho bất kỳ hoạt động phi pháp nào.**

## Tính năng

- Tấn công DDoS một URL hoặc địa chỉ IP cụ thể.
- Cấu hình số luồng tấn công và cổng.
- Tô màu văn bản trên terminal sử dụng thư viện `colorama`.

## Yêu cầu

- Python 3.x
- Thư viện `colorama`

## Hướng dẫn cài đặt

Bạn có thể dễ dàng cài đặt và thiết lập công cụ này bằng cách sử dụng tệp `setup.sh` đi kèm:

### 1. Clone Repository

Đầu tiên, bạn cần clone repository này về máy của mình:

```bash
git clone https://github.com/dhungx/ddos.git
cd ddos
bash setup.sh
```


Script này sẽ tự động cài đặt tất cả các gói cần thiết để chạy công cụ.

2. Chạy Công Cụ

Sau khi cài đặt xong, bạn có thể chạy công cụ bằng lệnh:
```bash
python3 ddos.py hoặc python ddos.py
```

Hướng dẫn sử dụng

	1.	Khởi động công cụ: Sau khi chạy, bạn sẽ thấy một menu hiển thị các tùy chọn. Chọn 1 để bắt đầu mô phỏng một cuộc tấn công DDoS.
	2.	Nhập thông tin mục tiêu: Nhập URL hoặc địa chỉ IP của mục tiêu, số luồng và cổng muốn tấn công.
	3.	Bắt đầu tấn công: Công cụ sẽ bắt đầu gửi các gói tin đến mục tiêu và hiển thị số lượng gói tin đã được gửi.

Cảnh báo pháp lý

Cảnh báo: Công cụ này chỉ được sử dụng cho mục đích giáo dục và học tập. Tác giả không chịu trách nhiệm đối với bất kỳ thiệt hại nào phát sinh từ việc sử dụng công cụ này cho các mục đích phi pháp. Tấn công DDoS vào các hệ thống mà không có sự cho phép là hành vi vi phạm pháp luật và có thể dẫn đến các hình phạt nghiêm khắc.

- Hãy suy nghĩ thật cẩn thận trước khi sử dụng, vì nó có thể là PHẠM PHÁP