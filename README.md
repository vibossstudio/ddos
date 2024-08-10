# DDoS Tool

**DDoS Tool** là một công cụ đơn giản cho phép thực hiện các cuộc tấn công từ chối dịch vụ phân tán (DDoS) với các phương pháp UDP Flood, SYN Flood, và HTTP Flood.

## **Cảnh báo**
- **Mục đích giáo dục**: Công cụ này được phát triển với mục đích giáo dục và thử nghiệm bảo mật. Người dùng phải tuân thủ luật pháp và chỉ sử dụng công cụ này trên các hệ thống mà họ có quyền kiểm soát hợp pháp.
- **Không chịu trách nhiệm**: Tác giả không chịu trách nhiệm về bất kỳ thiệt hại nào gây ra bởi việc sử dụng công cụ này.

## **Tính năng**
- **UDP Flood**: Gửi một lượng lớn gói tin UDP đến cổng ngẫu nhiên của máy chủ mục tiêu để làm quá tải hệ thống.
- **SYN Flood**: Tấn công cơ chế bắt tay của giao thức TCP bằng cách gửi nhiều gói SYN mà không hoàn tất quá trình bắt tay.
- **HTTP Flood**: Gửi yêu cầu HTTP hợp lệ nhưng quá mức để làm máy chủ web quá tải.

## **Cài đặt**

1. **Clone repository**
   ```bash
   git clone https://github.com/dhungx/ddos.git
   cd ddos
