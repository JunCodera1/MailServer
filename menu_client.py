#!/usr/bin/env python3
"""
Menu Client cho UDP Mail Server
Giao diện menu đơn giản để thao tác với Mail Server
"""

from mail_client import MailClient
import os
import sys

def clear_screen():
    """Xóa màn hình"""
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    """In header của menu"""
    print("=" * 60)
    print("           🚀 UDP MAIL SERVER CLIENT 🚀")
    print("=" * 60)

def print_menu():
    """In menu chính"""
    print("\n📋 DANH MỤC THAO TÁC:")
    print("1. 📧 Tạo tài khoản mới")
    print("2. 📤 Gửi email")
    print("3. 📥 Đăng nhập và xem email")
    print("4. 📖 Đọc nội dung email")
    print("5. 👥 Xem danh sách tài khoản")
    print("6. 📊 Thống kê hệ thống")
    print("7. 🧪 Demo nhanh")
    print("0. ❌ Thoát")
    print("-" * 60)

def create_account_menu():
    """Menu tạo tài khoản"""
    print("\n📧 TẠO TÀI KHOẢN MỚI")
    print("-" * 30)
    username = input("Nhập tên tài khoản: ").strip()
    
    if not username:
        print("❌ Tên tài khoản không được để trống!")
        return
    
    client = MailClient()
    result = client.create_account(username)
    client.close()
    
    if result['status'] == 'success':
        print(f"✅ {result['message']}")
    else:
        print(f"❌ Lỗi: {result['message']}")

def send_email_menu():
    """Menu gửi email"""
    print("\n📤 GỬI EMAIL")
    print("-" * 20)
    
    sender = input("Người gửi: ").strip()
    recipient = input("Người nhận: ").strip()
    subject = input("Tiêu đề: ").strip()
    
    print("Nội dung email (Nhấn Enter 2 lần để kết thúc):")
    content_lines = []
    while True:
        line = input()
        if line == "" and content_lines and content_lines[-1] == "":
            break
        content_lines.append(line)
    
    content = "\n".join(content_lines[:-1]) if content_lines else ""
    
    if not sender or not recipient:
        print("❌ Người gửi và người nhận không được để trống!")
        return
    
    client = MailClient()
    result = client.send_email(sender, recipient, subject, content)
    client.close()
    
    if result['status'] == 'success':
        print(f"✅ {result['message']}")
    else:
        print(f"❌ Lỗi: {result['message']}")

def login_menu():
    """Menu đăng nhập"""
    print("\n📥 ĐĂNG NHẬP VÀ XEM EMAIL")
    print("-" * 35)
    username = input("Tên tài khoản: ").strip()
    
    if not username:
        print("❌ Tên tài khoản không được để trống!")
        return
    
    client = MailClient()
    result = client.login(username)
    client.close()
    
    if result['status'] == 'success':
        files = result['files']
        if files:
            print(f"\n📁 Danh sách email của {username}:")
            for i, filename in enumerate(files, 1):
                print(f"  {i:2d}. {filename}")
        else:
            print(f"📭 {username} chưa có email nào!")
    else:
        print(f"❌ Lỗi: {result['message']}")

def read_email_menu():
    """Menu đọc email"""
    print("\n📖 ĐỌC NỘI DUNG EMAIL")
    print("-" * 30)
    username = input("Tên tài khoản: ").strip()
    filename = input("Tên file email: ").strip()
    
    if not username or not filename:
        print("❌ Tên tài khoản và tên file không được để trống!")
        return
    
    client = MailClient()
    result = client.get_email(username, filename)
    client.close()
    
    if result['status'] == 'success':
        print(f"\n📄 Nội dung email {filename}:")
        print("=" * 60)
        print(result['content'])
        print("=" * 60)
    else:
        print(f"❌ Lỗi: {result['message']}")

def list_accounts():
    """Xem danh sách tài khoản"""
    print("\n👥 DANH SÁCH TÀI KHOẢN")
    print("-" * 25)
    
    accounts_dir = "accounts"
    if not os.path.exists(accounts_dir):
        print("❌ Thư mục accounts không tồn tại!")
        return
    
    accounts = [d for d in os.listdir(accounts_dir) 
                if os.path.isdir(os.path.join(accounts_dir, d))]
    
    if accounts:
        print(f"📊 Tìm thấy {len(accounts)} tài khoản:")
        for i, account in enumerate(accounts, 1):
            email_count = len([f for f in os.listdir(os.path.join(accounts_dir, account)) 
                             if os.path.isfile(os.path.join(accounts_dir, account, f))])
            print(f"  {i:2d}. {account} ({email_count} emails)")
    else:
        print("📭 Chưa có tài khoản nào!")

def system_stats():
    """Thống kê hệ thống"""
    print("\n📊 THỐNG KÊ HỆ THỐNG")
    print("-" * 25)
    
    accounts_dir = "accounts"
    if not os.path.exists(accounts_dir):
        print("❌ Thư mục accounts không tồn tại!")
        return
    
    accounts = [d for d in os.listdir(accounts_dir) 
                if os.path.isdir(os.path.join(accounts_dir, d))]
    
    total_emails = 0
    for account in accounts:
        account_dir = os.path.join(accounts_dir, account)
        emails = [f for f in os.listdir(account_dir) 
                 if os.path.isfile(os.path.join(account_dir, f))]
        total_emails += len(emails)
    
    print(f"👥 Tổng số tài khoản: {len(accounts)}")
    print(f"📧 Tổng số email: {total_emails}")
    print(f"📁 Thư mục lưu trữ: {os.path.abspath(accounts_dir)}")

def quick_demo():
    """Demo nhanh"""
    print("\n🧪 DEMO NHANH")
    print("-" * 15)
    print("Đang thực hiện demo...")
    
    client = MailClient()
    
    # Tạo tài khoản demo
    print("1. Tạo tài khoản demo...")
    client.create_account("demo_user")
    
    # Gửi email demo
    print("2. Gửi email demo...")
    client.send_email("demo_user", "demo_user", "Email tự gửi", "Đây là email demo!")
    
    # Xem email
    print("3. Xem email...")
    result = client.login("demo_user")
    if result['status'] == 'success':
        print(f"   Demo user có {len(result['files'])} email(s)")
    
    client.close()
    print("✅ Demo hoàn thành!")

def main():
    """Hàm chính"""
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        try:
            choice = input("\nChọn thao tác (0-7): ").strip()
            
            if choice == "0":
                print("\n👋 Cảm ơn bạn đã sử dụng! Tạm biệt!")
                break
            elif choice == "1":
                create_account_menu()
            elif choice == "2":
                send_email_menu()
            elif choice == "3":
                login_menu()
            elif choice == "4":
                read_email_menu()
            elif choice == "5":
                list_accounts()
            elif choice == "6":
                system_stats()
            elif choice == "7":
                quick_demo()
            else:
                print("❌ Lựa chọn không hợp lệ! Vui lòng chọn 0-7.")
            
            input("\n⏸️  Nhấn Enter để tiếp tục...")
            
        except KeyboardInterrupt:
            print("\n\n👋 Cảm ơn bạn đã sử dụng! Tạm biệt!")
            break
        except Exception as e:
            print(f"\n❌ Lỗi: {e}")
            input("⏸️  Nhấn Enter để tiếp tục...")

if __name__ == "__main__":
    main()
