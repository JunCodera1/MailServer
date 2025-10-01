# 📋 HƯỚNG DẪN SỬ DỤNG MENU CLIENT

## 🚀 Cách chạy

### Bước 1: Khởi động Server
```bash
python3 mail_server.py
```
*Để server chạy ở terminal đầu tiên*

### Bước 2: Chạy Menu Client
```bash
python3 menu_client.py
```
### Bước 3: Chạy GUI
```bash
python3 mail_gui_advanced.py
```
*Chạy ở terminal thứ hai*

## 📋 Danh mục thao tác

### 1. 📧 Tạo tài khoản mới
- **Mục đích**: Tạo tài khoản email mới
- **Thao tác**: Nhập tên tài khoản
- **Kết quả**: Tạo thư mục và file chào mừng

**Ví dụ:**
```
Tên tài khoản: nguyen_van_a
✅ Account 'nguyen_van_a' created successfully
```

### 2. 📤 Gửi email
- **Mục đích**: Gửi email cho người khác
- **Thao tác**: 
  - Nhập người gửi
  - Nhập người nhận
  - Nhập tiêu đề
  - Nhập nội dung (Enter 2 lần để kết thúc)
- **Kết quả**: Tạo file email trong thư mục người nhận

**Ví dụ:**
```
Người gửi: alice
Người nhận: bob
Tiêu đề: Họp nhóm
Nội dung: Chúng ta họp lúc 2h chiều nhé!
```

### 3. 📥 Đăng nhập và xem email
- **Mục đích**: Xem danh sách email của một tài khoản
- **Thao tác**: Nhập tên tài khoản
- **Kết quả**: Hiển thị danh sách file email

**Ví dụ:**
```
Tên tài khoản: alice
📁 Danh sách email của alice:
   1. new_email.txt
   2. email_20250930_095130_bob.txt
   3. email_20250930_094750_charlie.txt
```

### 4. 📖 Đọc nội dung email
- **Mục đích**: Xem nội dung chi tiết của một email
- **Thao tác**: 
  - Nhập tên tài khoản
  - Nhập tên file email
- **Kết quả**: Hiển thị nội dung email đầy đủ

**Ví dụ:**
```
Tên tài khoản: alice
Tên file email: email_20250930_095130_bob.txt
📄 Nội dung email:
============================================================
From: bob
To: alice
Subject: Trả lời email
Date: 2025-09-30 09:51:30

Cảm ơn bạn đã gửi email!
============================================================
```

### 5. 👥 Xem danh sách tài khoản
- **Mục đích**: Xem tất cả tài khoản đã tạo
- **Thao tác**: Chọn option 5
- **Kết quả**: Hiển thị danh sách tài khoản và số email

**Ví dụ:**
```
📊 Tìm thấy 3 tài khoản:
   1. alice (5 emails)
   2. bob (3 emails)
   3. charlie (2 emails)
```

### 6. 📊 Thống kê hệ thống
- **Mục đích**: Xem thống kê tổng quan
- **Thao tác**: Chọn option 6
- **Kết quả**: Hiển thị số liệu thống kê

**Ví dụ:**
```
👥 Tổng số tài khoản: 3
📧 Tổng số email: 10
📁 Thư mục lưu trữ: /home/jun/Documents/Mailserver/accounts
```

### 7. 🧪 Demo nhanh
- **Mục đích**: Chạy demo tự động
- **Thao tác**: Chọn option 7
- **Kết quả**: Tự động tạo tài khoản và gửi email demo

### 0. ❌ Thoát
- **Mục đích**: Thoát khỏi chương trình
- **Thao tác**: Chọn option 0

## 💡 Lưu ý quan trọng

1. **Server phải chạy trước**: Luôn đảm bảo server đang chạy trước khi sử dụng client
2. **Tên tài khoản**: Không được để trống, nên dùng chữ thường và gạch dưới
3. **Người nhận**: Phải là tài khoản đã tồn tại
4. **File email**: Tên file phải chính xác (có thể copy từ danh sách email)

## 🔧 Xử lý lỗi thường gặp

### Lỗi "Request timeout"
- **Nguyên nhân**: Server không chạy
- **Giải pháp**: Khởi động server trước

### Lỗi "Recipient does not exist"
- **Nguyên nhân**: Người nhận chưa có tài khoản
- **Giải pháp**: Tạo tài khoản cho người nhận trước

### Lỗi "Account does not exist"
- **Nguyên nhân**: Tài khoản chưa được tạo
- **Giải pháp**: Tạo tài khoản trước khi đăng nhập

## 🎯 Quy trình sử dụng mẫu

1. **Khởi động hệ thống**:
   ```bash
   # Terminal 1
   python3 mail_server.py
   
   # Terminal 2
   python3 menu_client.py
   ```

2. **Tạo tài khoản**:
   - Chọn option 1
   - Tạo tài khoản cho alice, bob, charlie

3. **Gửi email**:
   - Chọn option 2
   - Alice gửi email cho Bob
   - Bob gửi email cho Alice

4. **Xem email**:
   - Chọn option 3
   - Đăng nhập vào tài khoản để xem email

5. **Đọc email**:
   - Chọn option 4
   - Đọc nội dung email cụ thể
