#!/usr/bin/env python3
"""
UDP Mail Server GUI Client
Giao diện đồ họa cho Mail Server
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, font
from mail_client import MailClient
import os
import threading
from datetime import datetime

class MailGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 UDP Mail Server Client")
        self.root.geometry("900x700")
        self.root.configure(bg='#f0f0f0')
        
        # Tạo style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Cấu hình font
        self.title_font = font.Font(family="Arial", size=16, weight="bold")
        self.button_font = font.Font(family="Arial", size=10, weight="bold")
        
        # Biến lưu trữ
        self.current_user = tk.StringVar()
        self.email_list = []
        
        self.setup_ui()
        self.check_server_connection()
    
    def setup_ui(self):
        """Thiết lập giao diện"""
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill='x', padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="🚀 UDP Mail Server Client", 
                              font=self.title_font, fg='white', bg='#2c3e50')
        title_label.pack(pady=20)
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Left panel - Controls
        left_panel = tk.Frame(main_frame, bg='#ecf0f1', width=300)
        left_panel.pack(side='left', fill='y', padx=(0, 5))
        left_panel.pack_propagate(False)
        
        # Right panel - Content
        right_panel = tk.Frame(main_frame, bg='white')
        right_panel.pack(side='right', fill='both', expand=True, padx=(5, 0))
        
        self.setup_left_panel(left_panel)
        self.setup_right_panel(right_panel)
    
    def setup_left_panel(self, parent):
        """Thiết lập panel bên trái - điều khiển"""
        # User info
        user_frame = tk.LabelFrame(parent, text="👤 Thông tin người dùng", 
                                  font=self.button_font, bg='#ecf0f1')
        user_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(user_frame, text="Tài khoản hiện tại:", bg='#ecf0f1').pack(anchor='w', padx=5, pady=2)
        self.user_entry = tk.Entry(user_frame, textvariable=self.current_user, width=25)
        self.user_entry.pack(padx=5, pady=2)
        
        # Account controls
        account_frame = tk.LabelFrame(parent, text="📧 Quản lý tài khoản", 
                                     font=self.button_font, bg='#ecf0f1')
        account_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Button(account_frame, text="➕ Tạo tài khoản mới", 
                 command=self.create_account_dialog, font=self.button_font,
                 bg='#27ae60', fg='white', width=20).pack(pady=2)
        
        tk.Button(account_frame, text="📥 Đăng nhập", 
                 command=self.login_user, font=self.button_font,
                 bg='#3498db', fg='white', width=20).pack(pady=2)
        
        tk.Button(account_frame, text="👥 Xem tất cả tài khoản", 
                 command=self.show_all_accounts, font=self.button_font,
                 bg='#9b59b6', fg='white', width=20).pack(pady=2)
        
        # Email controls
        email_frame = tk.LabelFrame(parent, text="📤 Gửi email", 
                                   font=self.button_font, bg='#ecf0f1')
        email_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(email_frame, text="Người nhận:", bg='#ecf0f1').pack(anchor='w', padx=5)
        self.recipient_entry = tk.Entry(email_frame, width=25)
        self.recipient_entry.pack(padx=5, pady=2)
        
        tk.Label(email_frame, text="Tiêu đề:", bg='#ecf0f1').pack(anchor='w', padx=5)
        self.subject_entry = tk.Entry(email_frame, width=25)
        self.subject_entry.pack(padx=5, pady=2)
        
        tk.Button(email_frame, text="�� Gửi email", 
                 command=self.send_email_dialog, font=self.button_font,
                 bg='#e74c3c', fg='white', width=20).pack(pady=5)
        
        # System controls
        system_frame = tk.LabelFrame(parent, text="⚙️ Hệ thống", 
                                    font=self.button_font, bg='#ecf0f1')
        system_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Button(system_frame, text="🔄 Làm mới danh sách", 
                 command=self.refresh_email_list, font=self.button_font,
                 bg='#f39c12', fg='white', width=20).pack(pady=2)
        
        tk.Button(system_frame, text="📊 Thống kê hệ thống", 
                 command=self.show_system_stats, font=self.button_font,
                 bg='#34495e', fg='white', width=20).pack(pady=2)
        
        tk.Button(system_frame, text="🧪 Demo nhanh", 
                 command=self.run_demo, font=self.button_font,
                 bg='#16a085', fg='white', width=20).pack(pady=2)
    
    def setup_right_panel(self, parent):
        """Thiết lập panel bên phải - nội dung"""
        # Email list
        list_frame = tk.LabelFrame(parent, text="📁 Danh sách email", 
                                  font=self.button_font, bg='white')
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Listbox with scrollbar
        list_container = tk.Frame(list_frame, bg='white')
        list_container.pack(fill='both', expand=True, padx=5, pady=5)
        
        self.email_listbox = tk.Listbox(list_container, font=('Arial', 10), 
                                       selectmode='single', height=15)
        scrollbar = tk.Scrollbar(list_container, orient='vertical', command=self.email_listbox.yview)
        self.email_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.email_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Bind double click to read email
        self.email_listbox.bind('<Double-1>', self.read_selected_email)
        
        # Email content
        content_frame = tk.LabelFrame(parent, text="�� Nội dung email", 
                                     font=self.button_font, bg='white')
        content_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        self.email_content = scrolledtext.ScrolledText(content_frame, 
                                                      font=('Courier', 9), 
                                                      height=10, wrap='word')
        self.email_content.pack(fill='both', expand=True, padx=5, pady=5)
    
    def check_server_connection(self):
        """Kiểm tra kết nối server"""
        try:
            client = MailClient()
            # Thử gửi một request test
            result = client.create_account("test_connection")
            client.close()
            self.show_status("✅ Kết nối server thành công", "info")
        except Exception as e:
            self.show_status(f"❌ Không thể kết nối server: {str(e)}", "error")
    
    def show_status(self, message, type="info"):
        """Hiển thị thông báo trạng thái"""
        if type == "error":
            messagebox.showerror("Lỗi", message)
        elif type == "warning":
            messagebox.showwarning("Cảnh báo", message)
        else:
            messagebox.showinfo("Thông báo", message)
    
    def create_account_dialog(self):
        """Dialog tạo tài khoản"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Tạo tài khoản mới")
        dialog.geometry("400x200")
        dialog.configure(bg='#f0f0f0')
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        tk.Label(dialog, text="Tên tài khoản:", font=self.button_font, bg='#f0f0f0').pack(pady=10)
        username_entry = tk.Entry(dialog, font=('Arial', 12), width=30)
        username_entry.pack(pady=5)
        username_entry.focus()
        
        def create_account():
            username = username_entry.get().strip()
            if not username:
                messagebox.showerror("Lỗi", "Tên tài khoản không được để trống!")
                return
            
            try:
                client = MailClient()
                result = client.create_account(username)
                client.close()
                
                if result['status'] == 'success':
                    self.show_status(f"✅ {result['message']}", "info")
                    dialog.destroy()
                else:
                    self.show_status(f"❌ {result['message']}", "error")
            except Exception as e:
                self.show_status(f"❌ Lỗi: {str(e)}", "error")
        
        button_frame = tk.Frame(dialog, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Tạo tài khoản", command=create_account,
                 font=self.button_font, bg='#27ae60', fg='white', width=15).pack(side='left', padx=5)
        tk.Button(button_frame, text="Hủy", command=dialog.destroy,
                 font=self.button_font, bg='#95a5a6', fg='white', width=15).pack(side='left', padx=5)
        
        # Bind Enter key
        dialog.bind('<Return>', lambda e: create_account())
    
    def login_user(self):
        """Đăng nhập người dùng"""
        username = self.current_user.get().strip()
        if not username:
            self.show_status("❌ Vui lòng nhập tên tài khoản!", "error")
            return
        
        try:
            client = MailClient()
            result = client.login(username)
            client.close()
            
            if result['status'] == 'success':
                self.email_list = result['files']
                self.update_email_list()
                self.show_status(f"✅ Đăng nhập thành công! Tìm thấy {len(self.email_list)} email(s)", "info")
            else:
                self.show_status(f"❌ {result['message']}", "error")
        except Exception as e:
            self.show_status(f"❌ Lỗi: {str(e)}", "error")
    
    def update_email_list(self):
        """Cập nhật danh sách email"""
        self.email_listbox.delete(0, tk.END)
        for i, filename in enumerate(self.email_list, 1):
            self.email_listbox.insert(tk.END, f"{i:2d}. {filename}")
    
    def read_selected_email(self, event=None):
        """Đọc email được chọn"""
        selection = self.email_listbox.curselection()
        if not selection:
            return
        
        username = self.current_user.get().strip()
        if not username:
            self.show_status("❌ Vui lòng đăng nhập trước!", "error")
            return
        
        filename = self.email_list[selection[0]]
        
        try:
            client = MailClient()
            result = client.get_email(username, filename)
            client.close()
            
            if result['status'] == 'success':
                self.email_content.delete(1.0, tk.END)
                self.email_content.insert(1.0, result['content'])
            else:
                self.show_status(f"❌ {result['message']}", "error")
        except Exception as e:
            self.show_status(f"❌ Lỗi: {str(e)}", "error")
    
    def send_email_dialog(self):
        """Dialog gửi email"""
        sender = self.current_user.get().strip()
        if not sender:
            self.show_status("❌ Vui lòng đăng nhập trước!", "error")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Gửi email")
        dialog.geometry("600x500")
        dialog.configure(bg='#f0f0f0')
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        # Form fields
        tk.Label(dialog, text=f"Người gửi: {sender}", font=self.button_font, bg='#f0f0f0').pack(pady=5)
        
        tk.Label(dialog, text="Người nhận:", font=self.button_font, bg='#f0f0f0').pack(pady=(10, 0))
        recipient_entry = tk.Entry(dialog, font=('Arial', 12), width=50)
        recipient_entry.pack(pady=5)
        
        tk.Label(dialog, text="Tiêu đề:", font=self.button_font, bg='#f0f0f0').pack(pady=(10, 0))
        subject_entry = tk.Entry(dialog, font=('Arial', 12), width=50)
        subject_entry.pack(pady=5)
        
        tk.Label(dialog, text="Nội dung:", font=self.button_font, bg='#f0f0f0').pack(pady=(10, 0))
        content_text = scrolledtext.ScrolledText(dialog, font=('Arial', 10), height=15, width=70)
        content_text.pack(pady=5, padx=10, fill='both', expand=True)
        
        def send_email():
            recipient = recipient_entry.get().strip()
            subject = subject_entry.get().strip()
            content = content_text.get(1.0, tk.END).strip()
            
            if not recipient:
                messagebox.showerror("Lỗi", "Người nhận không được để trống!")
                return
            
            try:
                client = MailClient()
                result = client.send_email(sender, recipient, subject, content)
                client.close()
                
                if result['status'] == 'success':
                    self.show_status(f"✅ {result['message']}", "info")
                    dialog.destroy()
                else:
                    self.show_status(f"❌ {result['message']}", "error")
            except Exception as e:
                self.show_status(f"❌ Lỗi: {str(e)}", "error")
        
        button_frame = tk.Frame(dialog, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Gửi email", command=send_email,
                 font=self.button_font, bg='#e74c3c', fg='white', width=15).pack(side='left', padx=5)
        tk.Button(button_frame, text="Hủy", command=dialog.destroy,
                 font=self.button_font, bg='#95a5a6', fg='white', width=15).pack(side='left', padx=5)
    
    def show_all_accounts(self):
        """Hiển thị tất cả tài khoản"""
        try:
            accounts_dir = "accounts"
            if not os.path.exists(accounts_dir):
                self.show_status("❌ Thư mục accounts không tồn tại!", "error")
                return
            
            accounts = [d for d in os.listdir(accounts_dir) 
                       if os.path.isdir(os.path.join(accounts_dir, d))]
            
            if accounts:
                message = f"📊 Tìm thấy {len(accounts)} tài khoản:\n\n"
                for i, account in enumerate(accounts, 1):
                    email_count = len([f for f in os.listdir(os.path.join(accounts_dir, account)) 
                                     if os.path.isfile(os.path.join(accounts_dir, account, f))])
                    message += f"{i:2d}. {account} ({email_count} emails)\n"
                
                # Show in a new window
                self.show_accounts_window(accounts, message)
            else:
                self.show_status("📭 Chưa có tài khoản nào!", "info")
        except Exception as e:
            self.show_status(f"❌ Lỗi: {str(e)}", "error")
    
    def show_accounts_window(self, accounts, message):
        """Hiển thị cửa sổ danh sách tài khoản"""
        window = tk.Toplevel(self.root)
        window.title("Danh sách tài khoản")
        window.geometry("500x400")
        window.configure(bg='#f0f0f0')
        
        text_widget = scrolledtext.ScrolledText(window, font=('Arial', 10), wrap='word')
        text_widget.pack(fill='both', expand=True, padx=10, pady=10)
        text_widget.insert(1.0, message)
        text_widget.config(state='disabled')
        
        tk.Button(window, text="Đóng", command=window.destroy,
                 font=self.button_font, bg='#95a5a6', fg='white', width=15).pack(pady=10)
    
    def refresh_email_list(self):
        """Làm mới danh sách email"""
        username = self.current_user.get().strip()
        if not username:
            self.show_status("❌ Vui lòng đăng nhập trước!", "error")
            return
        
        self.login_user()
    
    def show_system_stats(self):
        """Hiển thị thống kê hệ thống"""
        try:
            accounts_dir = "accounts"
            if not os.path.exists(accounts_dir):
                self.show_status("❌ Thư mục accounts không tồn tại!", "error")
                return
            
            accounts = [d for d in os.listdir(accounts_dir) 
                       if os.path.isdir(os.path.join(accounts_dir, d))]
            
            total_emails = 0
            for account in accounts:
                account_dir = os.path.join(accounts_dir, account)
                emails = [f for f in os.listdir(account_dir) 
                         if os.path.isfile(os.path.join(account_dir, f))]
                total_emails += len(emails)
            
            message = f"""📊 THỐNG KÊ HỆ THỐNG

👥 Tổng số tài khoản: {len(accounts)}
📧 Tổng số email: {total_emails}
📁 Thư mục lưu trữ: {os.path.abspath(accounts_dir)}
🕒 Thời gian hiện tại: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📋 Chi tiết tài khoản:"""
            
            for account in accounts:
                account_dir = os.path.join(accounts_dir, account)
                emails = [f for f in os.listdir(account_dir) 
                         if os.path.isfile(os.path.join(account_dir, f))]
                message += f"\n  • {account}: {len(emails)} emails"
            
            self.show_accounts_window(accounts, message)
        except Exception as e:
            self.show_status(f"❌ Lỗi: {str(e)}", "error")
    
    def run_demo(self):
        """Chạy demo tự động"""
        def demo_thread():
            try:
                self.show_status("🧪 Đang chạy demo...", "info")
                
                client = MailClient()
                
                # Tạo tài khoản demo
                client.create_account("demo_gui")
                
                # Gửi email demo
                client.send_email("demo_gui", "demo_gui", "Email GUI Demo", 
                                "Đây là email demo từ giao diện GUI!")
                
                # Đăng nhập và xem email
                result = client.login("demo_gui")
                client.close()
                
                if result['status'] == 'success':
                    self.show_status(f"✅ Demo hoàn thành! Demo user có {len(result['files'])} email(s)", "info")
                else:
                    self.show_status("❌ Demo thất bại!", "error")
            except Exception as e:
                self.show_status(f"❌ Lỗi demo: {str(e)}", "error")
        
        # Chạy demo trong thread riêng để không block GUI
        threading.Thread(target=demo_thread, daemon=True).start()

def main():
    root = tk.Tk()
    app = MailGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
