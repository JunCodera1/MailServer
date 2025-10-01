#!/bin/bash
# Script khởi động GUI an toàn với kiểm tra tkinter

echo "🚀 KHỞI ĐỘNG MAIL SERVER GUI (AN TOÀN)"
echo "======================================"

# Kiểm tra tkinter
echo "🔍 Kiểm tra tkinter..."
if python3 -c "import tkinter" 2>/dev/null; then
    echo "✅ tkinter đã sẵn sàng!"
else
    echo "❌ tkinter chưa được cài đặt!"
    echo "📦 Đang cài đặt tkinter..."
    sudo apt update && sudo apt install -y python3-tk
    if [ $? -eq 0 ]; then
        echo "✅ Đã cài đặt tkinter thành công!"
    else
        echo "❌ Không thể cài đặt tkinter!"
        exit 1
    fi
fi

# Kiểm tra server
echo ""
echo "🔍 Kiểm tra server..."
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
echo "3. Test GUI: python3 test_gui.py"
echo ""
echo "📋 CÁC CÁCH SỬ DỤNG KHÁC:"
echo "4. Menu console: python3 menu_client.py"
echo "5. Client đơn giản: python3 mail_client.py"
echo "6. Demo tự động: python3 mail_client.py demo"
echo ""

# Hỏi người dùng chọn giao diện
echo "🎯 Chọn giao diện bạn muốn sử dụng:"
echo "1) GUI nâng cao (khuyến nghị)"
echo "2) GUI cơ bản"
echo "3) Test GUI"
echo "4) Menu console"
echo "5) Thoát"
echo ""
read -p "Nhập lựa chọn (1-5): " choice

case $choice in
    1)
        echo "🚀 Đang khởi động GUI nâng cao..."
        python3 mail_gui_advanced.py
        ;;
    2)
        echo "🚀 Đang khởi động GUI cơ bản..."
        python3 mail_gui.py
        ;;
    3)
        echo "🧪 Đang chạy test GUI..."
        python3 test_gui.py
        ;;
    4)
        echo "📋 Đang khởi động menu console..."
        python3 menu_client.py
        ;;
    5)
        echo "👋 Tạm biệt!"
        exit 0
        ;;
    *)
        echo "❌ Lựa chọn không hợp lệ!"
        exit 1
        ;;
esac
