#!/bin/bash
# Script khởi động GUI cho Mail Server

echo "🚀 KHỞI ĐỘNG MAIL SERVER GUI"
echo "============================="

# Kiểm tra xem server đã chạy chưa
if pgrep -f "mail_server.py" > /dev/null; then
    echo "✅ Server đã đang chạy!"
else
    echo "🔄 Đang khởi động server..."
    python3 mail_server.py &
    sleep 3
    echo "✅ Server đã khởi động!"
fi

echo ""
echo "🎨 CÁC GIAO DIỆN GUI CÓ SẴN:"
echo "1. GUI cơ bản: python3 mail_gui.py"
echo "2. GUI nâng cao: python3 mail_gui_advanced.py"
echo ""
echo "📋 CÁC CÁCH SỬ DỤNG KHÁC:"
echo "3. Menu console: python3 menu_client.py"
echo "4. Client đơn giản: python3 mail_client.py"
echo "5. Demo tự động: python3 mail_client.py demo"
echo ""
echo "🎯 Khuyến nghị: Sử dụng 'python3 mail_gui_advanced.py' để có trải nghiệm tốt nhất!"
echo ""
echo "🚀 Đang khởi động GUI nâng cao..."
python3 mail_gui_advanced.py
