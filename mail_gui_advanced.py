#!/usr/bin/env python3
"""
UDP Mail Server Advanced GUI Client
Giao diện đồ họa nâng cao cho Mail Server
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, font, filedialog
from mail_client import MailClient
import os
import threading
from datetime import datetime
import json

class AdvancedMailGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("�� UDP Mail Server - Advanced Client")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2c3e50')
        
        # Cấu hình style
        self.setup_styles()
        
        # Biến lưu trữ
        self.current_user = tk.StringVar()
        self.email_list = []
        self.server_status = "disconnected"
        
        self.setup_ui()
        self.check_server_connection()
    
    def setup_styles(self):
        """Thiết lập style cho giao diện"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Cấu hình màu sắc
        self.colors = {
            'primary': '#2c3e50',
            'secondary': '#34495e',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'info': '#3498db',
            'light': '#ecf0f1',
            'dark': '#2c3e50'
        }
        
        # Cấu hình font
        self.fonts = {
            'title': font.Font(family="Arial", size=18, weight="bold"),
            'heading': font.Font(family="Arial", size=12, weight="bold"),
            'normal': font.Font(family="Arial", size=10),
            'small': font.Font(family="Arial", size=9)
        }
    
    def setup_ui(self):
        """Thiết lập giao diện chính"""
        # Header với status
        self.setup_header()
        
        # Main content area
        main_container = tk.Frame(self.root, bg=self.colors['light'])
        main_container.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Left sidebar
        self.setup_sidebar(main_container)
        
        # Right content area
        self.setup_content_area(main_container)
        
        # Status bar
        self.setup_status_bar()
    
    def setup_header(self):
        """Thiết lập header"""
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=100)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(header_frame, text="🚀 UDP Mail Server", 
                              font=self.fonts['title'], fg='white', bg=self.colors['primary'])
        title_label.pack(pady=10)
        
        # Status indicator
        status_frame = tk.Frame(header_frame, bg=self.colors['primary'])
        status_frame.pack(pady=5)
        
        self.status_indicator = tk.Label(status_frame, text="●", font=('Arial', 20), 
                                        fg='red', bg=self.colors['primary'])
        self.status_indicator.pack(side='left', padx=5)
        
        self.status_label = tk.Label(status_frame, text="Disconnected", 
                                    font=self.fonts['heading'], fg='white', bg=self.colors['primary'])
        self.status_label.pack(side='left', padx=5)
    
    def setup_sidebar(self, parent):
        """Thiết lập sidebar bên trái"""
        sidebar = tk.Frame(parent, bg=self.colors['secondary'], width=300)
        sidebar.pack(side='left', fill='y', padx=(0, 5))
        sidebar.pack_propagate(False)
        
        # User section
        self.setup_user_section(sidebar)
        
        # Quick actions
        self.setup_quick_actions(sidebar)
        
        # Email management
        self.setup_email_management(sidebar)
        
        # System tools
        self.setup_system_tools(sidebar)
    
    def setup_user_section(self, parent):
        """Thiết lập phần thông tin người dùng"""
        user_frame = tk.LabelFrame(parent, text="👤 Thông tin người dùng", 
                                  font=self.fonts['heading'], fg='white', bg=self.colors['secondary'])
        user_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(user_frame, text="Tài khoản:", font=self.fonts['normal'], 
                fg='white', bg=self.colors['secondary']).pack(anchor='w', padx=5, pady=2)
        
        self.user_entry = tk.Entry(user_frame, textvariable=self.current_user, 
                                  font=self.fonts['normal'], width=25)
        self.user_entry.pack(padx=5, pady=2)
        
        # Login button
        login_btn = tk.Button(user_frame, text="🔑 Đăng nhập", 
                             command=self.login_user, font=self.fonts['normal'],
                             bg=self.colors['info'], fg='white', width=20)
        login_btn.pack(pady=5)
    
    def setup_quick_actions(self, parent):
        """Thiết lập các thao tác nhanh"""
        actions_frame = tk.LabelFrame(parent, text="⚡ Thao tác nhanh", 
                                     font=self.fonts['heading'], fg='white', bg=self.colors['secondary'])
        actions_frame.pack(fill='x', padx=10, pady=10)
        
        # Create account
        create_btn = tk.Button(actions_frame, text="➕ Tạo tài khoản", 
                              command=self.create_account_dialog, font=self.fonts['normal'],
                              bg=self.colors['success'], fg='white', width=20)
        create_btn.pack(pady=2)
        
        # Send email
        send_btn = tk.Button(actions_frame, text="📤 Gửi email", 
                            command=self.send_email_dialog, font=self.fonts['normal'],
                            bg=self.colors['danger'], fg='white', width=20)
        send_btn.pack(pady=2)
        
        # Refresh
        refresh_btn = tk.Button(actions_frame, text="🔄 Làm mới", 
                               command=self.refresh_email_list, font=self.fonts['normal'],
                               bg=self.colors['warning'], fg='white', width=20)
        refresh_btn.pack(pady=2)
    
    def setup_email_management(self, parent):
        """Thiết lập quản lý email"""
        email_frame = tk.LabelFrame(parent, text="📧 Quản lý email", 
                                   font=self.fonts['heading'], fg='white', bg=self.colors['secondary'])
        email_frame.pack(fill='x', padx=10, pady=10)
        
        # Email list controls
        list_btn = tk.Button(email_frame, text="📋 Xem danh sách", 
                            command=self.show_email_list, font=self.fonts['normal'],
                            bg=self.colors['info'], fg='white', width=20)
        list_btn.pack(pady=2)
        
        # Read email
        read_btn = tk.Button(email_frame, text="�� Đọc email", 
                            command=self.read_selected_email, font=self.fonts['normal'],
                            bg=self.colors['warning'], fg='white', width=20)
        read_btn.pack(pady=2)
        
        # Export emails
        export_btn = tk.Button(email_frame, text="💾 Xuất email", 
                              command=self.export_emails, font=self.fonts['normal'],
                              bg=self.colors['success'], fg='white', width=20)
        export_btn.pack(pady=2)
    
    def setup_system_tools(self, parent):
        """Thiết lập công cụ hệ thống"""
        tools_frame = tk.LabelFrame(parent, text="🔧 Công cụ hệ thống", 
                                   font=self.fonts['heading'], fg='white', bg=self.colors['secondary'])
        tools_frame.pack(fill='x', padx=10, pady=10)
        
        # All accounts
        accounts_btn = tk.Button(tools_frame, text="👥 Tất cả tài khoản", 
                                command=self.show_all_accounts, font=self.fonts['normal'],
                                bg=self.colors['info'], fg='white', width=20)
        accounts_btn.pack(pady=2)
        
        # Statistics
        stats_btn = tk.Button(tools_frame, text="📊 Thống kê", 
                             command=self.show_system_stats, font=self.fonts['normal'],
                             bg=self.colors['warning'], fg='white', width=20)
        stats_btn.pack(pady=2)
        
        # Demo
        demo_btn = tk.Button(tools_frame, text="🧪 Demo", 
                            command=self.run_demo, font=self.fonts['normal'],
                            bg=self.colors['success'], fg='white', width=20)
        demo_btn.pack(pady=2)
        
        # Settings
        settings_btn = tk.Button(tools_frame, text="⚙️ Cài đặt", 
                                command=self.show_settings, font=self.fonts['normal'],
                                bg=self.colors['dark'], fg='white', width=20)
        settings_btn.pack(pady=2)
    
    def setup_content_area(self, parent):
        """Thiết lập vùng nội dung chính"""
        content_frame = tk.Frame(parent, bg='white')
        content_frame.pack(side='right', fill='both', expand=True)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(content_frame)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Email list tab
        self.setup_email_list_tab()
        
        # Email content tab
        self.setup_email_content_tab()
        
        # Statistics tab
        self.setup_statistics_tab()
    
    def setup_email_list_tab(self):
        """Thiết lập tab danh sách email"""
        email_tab = ttk.Frame(self.notebook)
        self.notebook.add(email_tab, text="📧 Danh sách email")
        
        # Email list frame
        list_frame = tk.Frame(email_tab, bg='white')
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Listbox with scrollbar
        list_container = tk.Frame(list_frame, bg='white')
        list_container.pack(fill='both', expand=True)
        
        self.email_listbox = tk.Listbox(list_container, font=self.fonts['normal'], 
                                       selectmode='single', height=20)
        scrollbar = tk.Scrollbar(list_container, orient='vertical', command=self.email_listbox.yview)
        self.email_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.email_listbox.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Bind events
        self.email_listbox.bind('<Double-1>', self.read_selected_email)
        self.email_listbox.bind('<Button-1>', self.on_email_select)
    
    def setup_email_content_tab(self):
        """Thiết lập tab nội dung email"""
        content_tab = ttk.Frame(self.notebook)
        self.notebook.add(content_tab, text="📄 Nội dung email")
        
        # Content frame
        content_frame = tk.Frame(content_tab, bg='white')
        content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Email info frame
        info_frame = tk.Frame(content_frame, bg='#f8f9fa', relief='raised', bd=1)
        info_frame.pack(fill='x', pady=(0, 10))
        
        self.email_info_label = tk.Label(info_frame, text="Chọn email để xem nội dung", 
                                        font=self.fonts['heading'], bg='#f8f9fa')
        self.email_info_label.pack(pady=10)
        
        # Email content
        self.email_content = scrolledtext.ScrolledText(content_frame, 
                                                      font=self.fonts['normal'], 
                                                      height=20, wrap='word')
        self.email_content.pack(fill='both', expand=True)
    
    def setup_statistics_tab(self):
        """Thiết lập tab thống kê"""
        stats_tab = ttk.Frame(self.notebook)
        self.notebook.add(stats_tab, text="📊 Thống kê")
        
        # Stats content
        self.stats_content = scrolledtext.ScrolledText(stats_tab, 
                                                      font=self.fonts['normal'], 
                                                      height=20, wrap='word')
        self.stats_content.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Load initial stats
        self.load_statistics()
    
    def setup_status_bar(self):
        """Thiết lập thanh trạng thái"""
        status_frame = tk.Frame(self.root, bg=self.colors['dark'], height=30)
        status_frame.pack(fill='x', side='bottom')
        status_frame.pack_propagate(False)
        
        self.status_text = tk.Label(status_frame, text="Sẵn sàng", 
                                   font=self.fonts['small'], fg='white', bg=self.colors['dark'])
        self.status_text.pack(side='left', padx=10, pady=5)
        
        # Time label
        self.time_label = tk.Label(status_frame, text="", 
                                  font=self.fonts['small'], fg='white', bg=self.colors['dark'])
        self.time_label.pack(side='right', padx=10, pady=5)
        
        # Update time
        self.update_time()
    
    def update_time(self):
        """Cập nhật thời gian hiện tại"""
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)
    
    def check_server_connection(self):
        """Kiểm tra kết nối server"""
        def check_connection():
            try:
                client = MailClient()
                # Thử gửi một request test
                result = client.create_account("test_connection_gui")
                client.close()
                
                self.server_status = "connected"
                self.status_indicator.config(fg='green')
                self.status_label.config(text="Connected")
                self.update_status("✅ Kết nối server thành công")
            except Exception as e:
                self.server_status = "disconnected"
                self.status_indicator.config(fg='red')
                self.status_label.config(text="Disconnected")
                self.update_status(f"❌ Không thể kết nối server: {str(e)}")
        
        # Chạy kiểm tra trong thread riêng
        threading.Thread(target=check_connection, daemon=True).start()
    
    def update_status(self, message):
        """Cập nhật thanh trạng thái"""
        self.status_text.config(text=message)
    
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
        dialog.geometry("500x300")
        dialog.configure(bg=self.colors['light'])
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 100, self.root.winfo_rooty() + 100))
        
        # Header
        header_frame = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text="➕ Tạo tài khoản mới", 
                font=self.fonts['title'], fg='white', bg=self.colors['primary']).pack(pady=15)
        
        # Form
        form_frame = tk.Frame(dialog, bg=self.colors['light'])
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(form_frame, text="Tên tài khoản:", font=self.fonts['heading'], 
                bg=self.colors['light']).pack(anchor='w', pady=(10, 5))
        
        username_entry = tk.Entry(form_frame, font=self.fonts['normal'], width=40)
        username_entry.pack(fill='x', pady=(0, 10))
        username_entry.focus()
        
        # Rules
        rules_text = """Quy tắc đặt tên tài khoản:
• Chỉ sử dụng chữ cái, số và dấu gạch dưới
• Không được để trống
• Tên tài khoản phải duy nhất"""
        
        rules_label = tk.Label(form_frame, text=rules_text, font=self.fonts['small'], 
                              fg='gray', bg=self.colors['light'], justify='left')
        rules_label.pack(anchor='w', pady=(0, 20))
        
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
        
        # Buttons
        button_frame = tk.Frame(form_frame, bg=self.colors['light'])
        button_frame.pack(fill='x', pady=(20, 0))
        
        tk.Button(button_frame, text="Tạo tài khoản", command=create_account,
                 font=self.fonts['normal'], bg=self.colors['success'], fg='white', 
                 width=15).pack(side='left', padx=(0, 10))
        
        tk.Button(button_frame, text="Hủy", command=dialog.destroy,
                 font=self.fonts['normal'], bg=self.colors['dark'], fg='white', 
                 width=15).pack(side='left')
        
        # Bind Enter key
        dialog.bind('<Return>', lambda e: create_account())
    
    def login_user(self):
        """Đăng nhập người dùng"""
        username = self.current_user.get().strip()
        if not username:
            self.show_status("❌ Vui lòng nhập tên tài khoản!", "error")
            return
        
        def login_thread():
            try:
                self.update_status("Đang đăng nhập...")
                client = MailClient()
                result = client.login(username)
                client.close()
                
                if result['status'] == 'success':
                    self.email_list = result['files']
                    self.update_email_list()
                    self.show_status(f"✅ Đăng nhập thành công! Tìm thấy {len(self.email_list)} email(s)", "info")
                    self.update_status(f"Đã đăng nhập: {username}")
                else:
                    self.show_status(f"❌ {result['message']}", "error")
                    self.update_status("Đăng nhập thất bại")
            except Exception as e:
                self.show_status(f"❌ Lỗi: {str(e)}", "error")
                self.update_status("Lỗi kết nối")
        
        threading.Thread(target=login_thread, daemon=True).start()
    
    def update_email_list(self):
        """Cập nhật danh sách email"""
        self.email_listbox.delete(0, tk.END)
        for i, filename in enumerate(self.email_list, 1):
            # Thêm icon dựa trên loại file
            if filename == "new_email.txt":
                icon = "📧"
            elif filename.startswith("email_"):
                icon = "✉️"
            else:
                icon = "📄"
            
            self.email_listbox.insert(tk.END, f"{icon} {i:2d}. {filename}")
    
    def on_email_select(self, event):
        """Xử lý khi chọn email"""
        selection = self.email_listbox.curselection()
        if selection:
            filename = self.email_list[selection[0]]
            self.email_info_label.config(text=f"📄 {filename}")
    
    def read_selected_email(self, event=None):
        """Đọc email được chọn"""
        selection = self.email_listbox.curselection()
        if not selection:
            self.show_status("❌ Vui lòng chọn email!", "error")
            return
        
        username = self.current_user.get().strip()
        if not username:
            self.show_status("❌ Vui lòng đăng nhập trước!", "error")
            return
        
        filename = self.email_list[selection[0]]
        
        def read_thread():
            try:
                self.update_status("Đang đọc email...")
                client = MailClient()
                result = client.get_email(username, filename)
                client.close()
                
                if result['status'] == 'success':
                    self.email_content.delete(1.0, tk.END)
                    self.email_content.insert(1.0, result['content'])
                    self.notebook.select(1)  # Chuyển sang tab nội dung
                    self.update_status(f"Đã đọc email: {filename}")
                else:
                    self.show_status(f"❌ {result['message']}", "error")
            except Exception as e:
                self.show_status(f"❌ Lỗi: {str(e)}", "error")
        
        threading.Thread(target=read_thread, daemon=True).start()
    
    def send_email_dialog(self):
        """Dialog gửi email"""
        sender = self.current_user.get().strip()
        if not sender:
            self.show_status("❌ Vui lòng đăng nhập trước!", "error")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Gửi email")
        dialog.geometry("700x600")
        dialog.configure(bg=self.colors['light'])
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center dialog
        dialog.geometry("+%d+%d" % (self.root.winfo_rootx() + 50, self.root.winfo_rooty() + 50))
        
        # Header
        header_frame = tk.Frame(dialog, bg=self.colors['primary'], height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text="📤 Gửi email", 
                font=self.fonts['title'], fg='white', bg=self.colors['primary']).pack(pady=15)
        
        # Form
        form_frame = tk.Frame(dialog, bg=self.colors['light'])
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Sender info
        sender_frame = tk.Frame(form_frame, bg=self.colors['light'])
        sender_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(sender_frame, text=f"Người gửi: {sender}", 
                font=self.fonts['heading'], bg=self.colors['light']).pack(anchor='w')
        
        # Recipient
        tk.Label(form_frame, text="Người nhận:", font=self.fonts['heading'], 
                bg=self.colors['light']).pack(anchor='w', pady=(10, 5))
        recipient_entry = tk.Entry(form_frame, font=self.fonts['normal'], width=60)
        recipient_entry.pack(fill='x', pady=(0, 10))
        
        # Subject
        tk.Label(form_frame, text="Tiêu đề:", font=self.fonts['heading'], 
                bg=self.colors['light']).pack(anchor='w', pady=(10, 5))
        subject_entry = tk.Entry(form_frame, font=self.fonts['normal'], width=60)
        subject_entry.pack(fill='x', pady=(0, 10))
        
        # Content
        tk.Label(form_frame, text="Nội dung:", font=self.fonts['heading'], 
                bg=self.colors['light']).pack(anchor='w', pady=(10, 5))
        content_text = scrolledtext.ScrolledText(form_frame, font=self.fonts['normal'], 
                                                height=15, width=70)
        content_text.pack(fill='both', expand=True, pady=(0, 10))
        
        def send_email():
            recipient = recipient_entry.get().strip()
            subject = subject_entry.get().strip()
            content = content_text.get(1.0, tk.END).strip()
            
            if not recipient:
                messagebox.showerror("Lỗi", "Người nhận không được để trống!")
                return
            
            def send_thread():
                try:
                    self.update_status("Đang gửi email...")
                    client = MailClient()
                    result = client.send_email(sender, recipient, subject, content)
                    client.close()
                    
                    if result['status'] == 'success':
                        self.show_status(f"✅ {result['message']}", "info")
                        dialog.destroy()
                        self.update_status("Email đã được gửi")
                    else:
                        self.show_status(f"❌ {result['message']}", "error")
                except Exception as e:
                    self.show_status(f"❌ Lỗi: {str(e)}", "error")
            
            threading.Thread(target=send_thread, daemon=True).start()
        
        # Buttons
        button_frame = tk.Frame(form_frame, bg=self.colors['light'])
        button_frame.pack(fill='x', pady=(10, 0))
        
        tk.Button(button_frame, text="Gửi email", command=send_email,
                 font=self.fonts['normal'], bg=self.colors['danger'], fg='white', 
                 width=15).pack(side='left', padx=(0, 10))
        
        tk.Button(button_frame, text="Hủy", command=dialog.destroy,
                 font=self.fonts['normal'], bg=self.colors['dark'], fg='white', 
                 width=15).pack(side='left')
    
    def show_email_list(self):
        """Hiển thị danh sách email"""
        self.notebook.select(0)  # Chuyển sang tab danh sách email
    
    def show_all_accounts(self):
        """Hiển thị tất cả tài khoản"""
        def load_accounts():
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
                    
                    self.show_accounts_window(accounts, message)
                else:
                    self.show_status("📭 Chưa có tài khoản nào!", "info")
            except Exception as e:
                self.show_status(f"❌ Lỗi: {str(e)}", "error")
        
        threading.Thread(target=load_accounts, daemon=True).start()
    
    def show_accounts_window(self, accounts, message):
        """Hiển thị cửa sổ danh sách tài khoản"""
        window = tk.Toplevel(self.root)
        window.title("Danh sách tài khoản")
        window.geometry("600x500")
        window.configure(bg=self.colors['light'])
        
        # Header
        header_frame = tk.Frame(window, bg=self.colors['primary'], height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text="👥 Danh sách tài khoản", 
                font=self.fonts['title'], fg='white', bg=self.colors['primary']).pack(pady=15)
        
        # Content
        text_widget = scrolledtext.ScrolledText(window, font=self.fonts['normal'], wrap='word')
        text_widget.pack(fill='both', expand=True, padx=20, pady=20)
        text_widget.insert(1.0, message)
        text_widget.config(state='disabled')
        
        # Close button
        tk.Button(window, text="Đóng", command=window.destroy,
                 font=self.fonts['normal'], bg=self.colors['dark'], fg='white', 
                 width=15).pack(pady=10)
    
    def refresh_email_list(self):
        """Làm mới danh sách email"""
        username = self.current_user.get().strip()
        if not username:
            self.show_status("❌ Vui lòng đăng nhập trước!", "error")
            return
        
        self.login_user()
    
    def show_system_stats(self):
        """Hiển thị thống kê hệ thống"""
        def load_stats():
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
�� Tổng số email: {total_emails}
📁 Thư mục lưu trữ: {os.path.abspath(accounts_dir)}
🕒 Thời gian hiện tại: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📋 Chi tiết tài khoản:"""
                
                for account in accounts:
                    account_dir = os.path.join(accounts_dir, account)
                    emails = [f for f in os.listdir(account_dir) 
                             if os.path.isfile(os.path.join(account_dir, f))]
                    message += f"\n  • {account}: {len(emails)} emails"
                
                self.stats_content.delete(1.0, tk.END)
                self.stats_content.insert(1.0, message)
                self.notebook.select(2)  # Chuyển sang tab thống kê
            except Exception as e:
                self.show_status(f"❌ Lỗi: {str(e)}", "error")
        
        threading.Thread(target=load_stats, daemon=True).start()
    
    def load_statistics(self):
        """Tải thống kê ban đầu"""
        self.stats_content.insert(1.0, "📊 Thống kê hệ thống sẽ được hiển thị ở đây...\n\nNhấn nút 'Thống kê' để cập nhật.")
    
    def export_emails(self):
        """Xuất email ra file"""
        username = self.current_user.get().strip()
        if not username:
            self.show_status("❌ Vui lòng đăng nhập trước!", "error")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            title="Lưu email"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(f"Email của {username}\n")
                    f.write("=" * 50 + "\n\n")
                    
                    for email_file in self.email_list:
                        f.write(f"File: {email_file}\n")
                        f.write("-" * 30 + "\n")
                        
                        client = MailClient()
                        result = client.get_email(username, email_file)
                        client.close()
                        
                        if result['status'] == 'success':
                            f.write(result['content'])
                        else:
                            f.write(f"Lỗi: {result['message']}")
                        
                        f.write("\n\n" + "=" * 50 + "\n\n")
                
                self.show_status(f"✅ Đã xuất email ra {filename}", "info")
            except Exception as e:
                self.show_status(f"❌ Lỗi xuất file: {str(e)}", "error")
    
    def show_settings(self):
        """Hiển thị cài đặt"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Cài đặt")
        settings_window.geometry("400x300")
        settings_window.configure(bg=self.colors['light'])
        
        # Header
        header_frame = tk.Frame(settings_window, bg=self.colors['primary'], height=60)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text="⚙️ Cài đặt", 
                font=self.fonts['title'], fg='white', bg=self.colors['primary']).pack(pady=15)
        
        # Settings content
        content_frame = tk.Frame(settings_window, bg=self.colors['light'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(content_frame, text="Cài đặt hệ thống:", 
                font=self.fonts['heading'], bg=self.colors['light']).pack(anchor='w', pady=(0, 10))
        
        # Server settings
        server_frame = tk.LabelFrame(content_frame, text="Server", 
                                    font=self.fonts['normal'], bg=self.colors['light'])
        server_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(server_frame, text="Host: localhost", 
                font=self.fonts['normal'], bg=self.colors['light']).pack(anchor='w', padx=10, pady=5)
        tk.Label(server_frame, text="Port: 12345", 
                font=self.fonts['normal'], bg=self.colors['light']).pack(anchor='w', padx=10, pady=5)
        
        # About
        about_frame = tk.LabelFrame(content_frame, text="Thông tin", 
                                   font=self.fonts['normal'], bg=self.colors['light'])
        about_frame.pack(fill='x', pady=(0, 10))
        
        about_text = """UDP Mail Server GUI Client
Phiên bản: 2.0
Tác giả: Jun ()
Công nghệ: Python + Tkinter"""
        
        tk.Label(about_frame, text=about_text, 
                font=self.fonts['small'], bg=self.colors['light'], 
                justify='left').pack(anchor='w', padx=10, pady=5)
        
        # Close button
        tk.Button(content_frame, text="Đóng", command=settings_window.destroy,
                 font=self.fonts['normal'], bg=self.colors['dark'], fg='white', 
                 width=15).pack(pady=20)
    
    def run_demo(self):
        """Chạy demo tự động"""
        def demo_thread():
            try:
                self.update_status("🧪 Đang chạy demo...")
                
                client = MailClient()
                
                # Tạo tài khoản demo
                client.create_account("demo_gui_advanced")
                
                # Gửi email demo
                client.send_email("demo_gui_advanced", "demo_gui_advanced", "Email GUI Advanced Demo", 
                                "Đây là email demo từ giao diện GUI nâng cao!\n\nTính năng:\n- Giao diện đẹp mắt\n- Xử lý đa luồng\n- Thống kê chi tiết\n- Xuất email")
                
                # Đăng nhập và xem email
                result = client.login("demo_gui_advanced")
                client.close()
                
                if result['status'] == 'success':
                    self.show_status(f"✅ Demo hoàn thành! Demo user có {len(result['files'])} email(s)", "info")
                    self.update_status("Demo hoàn thành")
                else:
                    self.show_status("❌ Demo thất bại!", "error")
            except Exception as e:
                self.show_status(f"❌ Lỗi demo: {str(e)}", "error")
        
        threading.Thread(target=demo_thread, daemon=True).start()

def main():
    root = tk.Tk()
    app = AdvancedMailGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
