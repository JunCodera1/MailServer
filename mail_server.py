#!/usr/bin/env python3
"""
UDP Mail Server Implementation
VKU Programming Exercise - UDP Socket Programming
"""

import socket
import os
import json
import threading
from datetime import datetime
from pathlib import Path

class MailServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, port))
        self.accounts_dir = Path("accounts")
        self.accounts_dir.mkdir(exist_ok=True)
        
        # Welcome message for new accounts
        self.welcome_message = """Thank you for using this service. We hope that you will feel comfortable using our mail system. 
This is your first email in the system. You can now send and receive emails through this platform.

Best regards,
Mail Server Team"""
        
        print(f"Mail Server started on {host}:{port}")
        print(f"Accounts directory: {self.accounts_dir.absolute()}")
    
    def create_account(self, username):
        """Create a new account directory and welcome email"""
        account_dir = self.accounts_dir / username
        account_dir.mkdir(exist_ok=True)
        
        # Create welcome email
        welcome_file = account_dir / "new_email.txt"
        with open(welcome_file, 'w', encoding='utf-8') as f:
            f.write(self.welcome_message)
        
        return f"Account '{username}' created successfully"
    
    def send_email(self, sender, recipient, subject, content):
        """Send an email to a recipient"""
        recipient_dir = self.accounts_dir / recipient
        
        if not recipient_dir.exists():
            return f"Error: Recipient '{recipient}' does not exist"
        
        # Create email file with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        email_filename = f"email_{timestamp}_{sender}.txt"
        email_file = recipient_dir / email_filename
        
        email_content = f"""From: {sender}
To: {recipient}
Subject: {subject}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{content}
"""
        
        with open(email_file, 'w', encoding='utf-8') as f:
            f.write(email_content)
        
        return f"Email sent to '{recipient}' successfully"
    
    def list_emails(self, username):
        """List all emails in a user's account"""
        account_dir = self.accounts_dir / username
        
        if not account_dir.exists():
            return f"Error: Account '{username}' does not exist"
        
        files = [f.name for f in account_dir.iterdir() if f.is_file()]
        return files
    
    def get_email_content(self, username, filename):
        """Get the content of a specific email"""
        email_file = self.accounts_dir / username / filename
        
        if not email_file.exists():
            return f"Error: Email '{filename}' not found"
        
        with open(email_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def handle_client_request(self, data, client_address):
        """Handle incoming client requests"""
        try:
            request = json.loads(data.decode('utf-8'))
            command = request.get('command')
            
            response = {"status": "error", "message": "Unknown command"}
            
            if command == "create_account":
                username = request.get('username')
                if username:
                    message = self.create_account(username)
                    response = {"status": "success", "message": message}
                else:
                    response = {"status": "error", "message": "Username required"}
            
            elif command == "send_email":
                sender = request.get('sender')
                recipient = request.get('recipient')
                subject = request.get('subject', 'No Subject')
                content = request.get('content', '')
                
                if sender and recipient:
                    message = self.send_email(sender, recipient, subject, content)
                    response = {"status": "success", "message": message}
                else:
                    response = {"status": "error", "message": "Sender and recipient required"}
            
            elif command == "login":
                username = request.get('username')
                if username:
                    files = self.list_emails(username)
                    if files and files[0].startswith("Error:"):
                        response = {"status": "error", "message": files[0]}
                    else:
                        response = {"status": "success", "files": files}
                else:
                    response = {"status": "error", "message": "Username required"}
            
            elif command == "get_email":
                username = request.get('username')
                filename = request.get('filename')
                if username and filename:
                    content = self.get_email_content(username, filename)
                    if content.startswith("Error:"):
                        response = {"status": "error", "message": content}
                    else:
                        response = {"status": "success", "content": content}
                else:
                    response = {"status": "error", "message": "Username and filename required"}
            
        except json.JSONDecodeError:
            response = {"status": "error", "message": "Invalid JSON format"}
        except Exception as e:
            response = {"status": "error", "message": f"Server error: {str(e)}"}
        
        # Send response back to client
        response_json = json.dumps(response)
        self.socket.sendto(response_json.encode('utf-8'), client_address)
    
    def start(self):
        """Start the mail server"""
        print("Mail Server is running...")
        print("Commands available:")
        print("- create_account: Create a new user account")
        print("- send_email: Send an email to a user")
        print("- login: List all emails for a user")
        print("- get_email: Get content of a specific email")
        print("\nPress Ctrl+C to stop the server")
        
        try:
            while True:
                data, client_address = self.socket.recvfrom(1024)
                print(f"\nReceived request from {client_address}")
                
                # Handle request in a separate thread for better performance
                thread = threading.Thread(
                    target=self.handle_client_request,
                    args=(data, client_address)
                )
                thread.daemon = True
                thread.start()
                
        except KeyboardInterrupt:
            print("\nShutting down Mail Server...")
        finally:
            self.socket.close()

if __name__ == "__main__":
    server = MailServer()
    server.start()
