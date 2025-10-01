#!/bin/bash
# Script khởi động hệ thống Mail Server

echo "🚀 KHỞI ĐỘNG HỆ THỐNG MAIL SERVER"
echo "=================================="

# Kiểm tra xem server đã chạy chưa
if pgrep -f "mail_server.py" > /dev/null; then
    echo "✅ Server đã đang chạy!"
else
    echo "🔄 Đang khởi động server..."
    python3 mail_server.py &
    sleep 2
    echo "✅ Server đã khởi động!"
fi

echo ""
echo "📋 CÁC CÁCH SỬ DỤNG:"
echo "1. Menu tương tác: python3 menu_client.py"
echo "2. Client đơn giản: python3 mail_client.py"
echo "3. Demo tự động: python3 mail_client.py demo"
echo "4. Test toàn diện: python3 test_mail_system.py"
echo ""
echo "📖 Xem hướng dẫn: cat HUONG_DAN_SU_DUNG.md"
echo ""
echo "🎯 Khuyến nghị: Sử dụng 'python3 menu_client.py' để có trải nghiệm tốt nhất!"
