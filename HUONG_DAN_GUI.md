# 🎨 HƯỚNG DẪN SỬ DỤNG GIAO DIỆN GUI

## 🚀 Khởi động nhanh

### Cách 1: Khởi động tự động
```bash
./start_gui.sh
```
*Script này sẽ tự động khởi động server và mở GUI nâng cao*

### Cách 2: Khởi động thủ công
```bash
# Terminal 1: Khởi động server
python3 mail_server.py

# Terminal 2: Chạy GUI
python3 mail_gui_advanced.py
```

## 🎨 Các phiên bản GUI

### 1. GUI Cơ bản (`mail_gui.py`)
- Giao diện đơn giản, dễ sử dụng
- Phù hợp cho người mới bắt đầu
- Các tính năng cơ bản: tạo tài khoản, gửi email, xem email

### 2. GUI Nâng cao (`mail_gui_advanced.py`) ⭐ **KHUYẾN NGHỊ**
- Giao diện đẹp mắt với nhiều màu sắc
- Nhiều tính năng nâng cao
- Xử lý đa luồng, không bị lag
- Thống kê chi tiết, xuất email

## 📋 Hướng dẫn sử dụng GUI Nâng cao

### 🖥️ Giao diện chính

#### **Header (Phần đầu)**
- **Tiêu đề**: "🚀 UDP Mail Server"
- **Trạng thái kết nối**: 
  - 🔴 Đỏ = Không kết nối được server
  - 🟢 Xanh = Kết nối thành công
- **Thời gian hiện tại**: Cập nhật mỗi giây

#### **Sidebar bên trái**
1. **👤 Thông tin người dùng**
   - Nhập tên tài khoản
   - Nút "🔑 Đăng nhập"

2. **⚡ Thao tác nhanh**
   - ➕ Tạo tài khoản
   - 📤 Gửi email
   - 🔄 Làm mới

3. **📧 Quản lý email**
   - 📋 Xem danh sách
   - 📖 Đọc email
   - 💾 Xuất email

4. **🔧 Công cụ hệ thống**
   - 👥 Tất cả tài khoản
   - 📊 Thống kê
   - 🧪 Demo
   - ⚙️ Cài đặt

#### **Vùng nội dung chính (3 tabs)**
1. **📧 Danh sách email**: Hiển thị danh sách email của tài khoản đã đăng nhập
2. **📄 Nội dung email**: Xem nội dung chi tiết của email được chọn
3. **📊 Thống kê**: Thống kê tổng quan hệ thống

### 🔧 Các tính năng chi tiết

#### **1. Tạo tài khoản mới**
- Nhấn nút "➕ Tạo tài khoản"
- Nhập tên tài khoản (chỉ chữ cái, số, gạch dưới)
- Nhấn "Tạo tài khoản" hoặc Enter
- ✅ Thành công: Tài khoản được tạo + file chào mừng

#### **2. Đăng nhập**
- Nhập tên tài khoản vào ô "Tài khoản hiện tại"
- Nhấn "🔑 Đăng nhập"
- ✅ Thành công: Danh sách email hiển thị ở tab "📧 Danh sách email"

#### **3. Gửi email**
- Phải đăng nhập trước
- Nhấn "📤 Gửi email"
- Điền thông tin:
  - Người nhận (bắt buộc)
  - Tiêu đề
  - Nội dung (có thể nhiều dòng)
- Nhấn "Gửi email"
- ✅ Thành công: Email được tạo trong thư mục người nhận

#### **4. Xem danh sách email**
- Đăng nhập trước
- Tab "📧 Danh sách email" sẽ hiển thị:
  - 📧 new_email.txt (email chào mừng)
  - ✉️ email_YYYYMMDD_HHMMSS_sender.txt (email từ người khác)

#### **5. Đọc email**
- **Cách 1**: Double-click vào email trong danh sách
- **Cách 2**: Chọn email rồi nhấn "📖 Đọc email"
- Nội dung hiển thị ở tab "📄 Nội dung email"

#### **6. Xuất email**
- Đăng nhập trước
- Nhấn "�� Xuất email"
- Chọn nơi lưu file
- ✅ Tất cả email sẽ được xuất ra file text

#### **7. Xem tất cả tài khoản**
- Nhấn "👥 Tất cả tài khoản"
- Hiển thị cửa sổ mới với:
  - Danh sách tất cả tài khoản
  - Số lượng email của mỗi tài khoản

#### **8. Thống kê hệ thống**
- Nhấn "📊 Thống kê"
- Chuyển sang tab "📊 Thống kê" với thông tin:
  - Tổng số tài khoản
  - Tổng số email
  - Thư mục lưu trữ
  - Chi tiết từng tài khoản

#### **9. Demo nhanh**
- Nhấn "🧪 Demo"
- Tự động tạo tài khoản "demo_gui_advanced"
- Gửi email demo
- Hiển thị kết quả

#### **10. Cài đặt**
- Nhấn "⚙️ Cài đặt"
- Xem thông tin:
  - Cài đặt server (host, port)
  - Thông tin phiên bản
  - Thông tin tác giả

### 🎯 Quy trình sử dụng mẫu

#### **Bước 1: Khởi động**
```bash
./start_gui.sh
```

#### **Bước 2: Tạo tài khoản**
1. Nhấn "➕ Tạo tài khoản"
2. Nhập tên: "alice"
3. Nhấn "Tạo tài khoản"
4. Làm tương tự cho "bob", "charlie"

#### **Bước 3: Đăng nhập**
1. Nhập "alice" vào ô tài khoản
2. Nhấn "🔑 Đăng nhập"
3. Xem danh sách email ở tab "📧 Danh sách email"

#### **Bước 4: Gửi email**
1. Nhấn "📤 Gửi email"
2. Điền:
   - Người nhận: "bob"
   - Tiêu đề: "Họp nhóm"
   - Nội dung: "Chúng ta họp lúc 2h chiều nhé!"
3. Nhấn "Gửi email"

#### **Bước 5: Đọc email**
1. Đăng nhập "bob"
2. Double-click vào email từ alice
3. Xem nội dung ở tab "📄 Nội dung email"

#### **Bước 6: Xem thống kê**
1. Nhấn "📊 Thống kê"
2. Xem tab "📊 Thống kê" để biết tổng quan hệ thống

### 🔧 Xử lý lỗi thường gặp

#### **Lỗi "Không thể kết nối server"**
- **Nguyên nhân**: Server chưa chạy
- **Giải pháp**: Chạy `python3 mail_server.py` trước

#### **Lỗi "Vui lòng đăng nhập trước"**
- **Nguyên nhân**: Chưa đăng nhập tài khoản
- **Giải pháp**: Nhập tên tài khoản và nhấn "🔑 Đăng nhập"

#### **Lỗi "Người nhận không tồn tại"**
- **Nguyên nhân**: Người nhận chưa có tài khoản
- **Giải pháp**: Tạo tài khoản cho người nhận trước

#### **Giao diện bị lag**
- **Nguyên nhân**: Xử lý nhiều tác vụ cùng lúc
- **Giải pháp**: Đợi tác vụ hiện tại hoàn thành

### 💡 Mẹo sử dụng

1. **Luôn đăng nhập trước** khi gửi email hoặc xem danh sách
2. **Double-click** để đọc email nhanh
3. **Sử dụng tab** để chuyển đổi giữa các chức năng
4. **Kiểm tra trạng thái kết nối** ở header
5. **Sử dụng nút "🔄 Làm mới"** để cập nhật danh sách email
6. **Xuất email** để backup dữ liệu quan trọng

### 🎨 Tùy chỉnh giao diện

- **Màu sắc**: Có thể thay đổi trong file `mail_gui_advanced.py`
- **Font chữ**: Có thể điều chỉnh kích thước và kiểu chữ
- **Kích thước cửa sổ**: Có thể thay đổi trong `root.geometry()`

### 📱 Responsive Design

- Giao diện tự động điều chỉnh theo kích thước cửa sổ
- Có thể kéo thả để thay đổi kích thước
- Scrollbar tự động xuất hiện khi cần

## 🎉 Kết luận

GUI nâng cao cung cấp trải nghiệm người dùng tuyệt vời với:
- ✅ Giao diện đẹp mắt, dễ sử dụng
- ✅ Xử lý đa luồng, không bị lag
- ✅ Nhiều tính năng nâng cao
- ✅ Thống kê chi tiết
- ✅ Xuất dữ liệu
- ✅ Demo tự động

**Chúc bạn sử dụng vui vẻ! 🚀**
