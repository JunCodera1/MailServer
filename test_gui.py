#!/usr/bin/env python3
"""
Test script để kiểm tra GUI hoạt động
"""

import tkinter as tk
from tkinter import messagebox

def test_gui():
    """Test GUI cơ bản"""
    root = tk.Tk()
    root.title("Test GUI")
    root.geometry("300x200")
    
    # Test label
    label = tk.Label(root, text="✅ GUI hoạt động bình thường!", 
                     font=('Arial', 14), fg='green')
    label.pack(pady=50)
    
    # Test button
    def show_message():
        messagebox.showinfo("Test", "GUI đã sẵn sàng!")
    
    button = tk.Button(root, text="Test Button", command=show_message,
                       font=('Arial', 12), bg='blue', fg='white')
    button.pack(pady=20)
    
    # Auto close after 3 seconds
    root.after(3000, root.destroy)
    
    root.mainloop()

if __name__ == "__main__":
    test_gui()
