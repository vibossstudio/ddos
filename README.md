# Fox DDOSER

Fox DDOSER là một công cụ tấn công từ chối dịch vụ (DDoS) đa năng. Công cụ này hỗ trợ nhiều phương pháp tấn công khác nhau, bao gồm cả các cuộc tấn công Layer 4 và Layer 7.

## Cài đặt

### Bước 1: Sao chép mã nguồn

Sao chép mã nguồn từ GitHub về máy của bạn:

```bash
git clone https://github.com/dhungx/ddos.git
cd ddos
```

Bước 2: Cài đặt phụ thuộc

Chạy tệp setup.sh để tự động cài đặt tất cả các phụ thuộc cần thiết cho dự án:

bash setup.sh

Bước 3: Chạy ứng dụng

Sau khi cài đặt xong, bạn có thể chạy ứng dụng bằng cách:
```bash
python ddos.py

hoặc

python3 ddos.py
```

Các phương pháp tấn công

Layer 4

	•	Ping of Death
	•	SYN Flood
	•	Malformed Packet
	•	Land Attack
	•	ARP Spoofing
	•	Nestea
	•	UDP Flood
	•	Teardrop Attack
	•	TCP Flood

Layer 7

	•	GET Request Flood
	•	POST Request Flood
	•	HEAD Request Flood
	•	PUT Request Flood
	•	OPTIONS Request Flood

Yêu cầu

	•	Python 3.x
	•	pip (Trình quản lý gói Python)

# Lưu ý
- DDoS (Distributed Denial of Service) là một cuộc tấn công phạm pháp. Việc sử dụng công cụ này có thể vi phạm pháp luật hoặc các chính sách của mạng. Đảm bảo rằng bạn chỉ sử dụng công cụ này trong môi trường kiểm tra và với sự cho phép từ các bên liên quan.
- Đừng sử dụng công cụ này để tấn công các hệ thống mà bạn không có quyền kiểm soát. 
- Tác giả sẽ không chịu trách nhiệm cho bất kì thứ gì mã bạn gây ra.