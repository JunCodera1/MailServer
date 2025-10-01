#!/usr/bin/env python3

import socket
import json
import sys

class MailClient:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(5)  # 5 second timeout
    
    def send_request(self, request):
        """Send a request to the server and return the response"""
        try:
            request_json = json.dumps(request)
            self.socket.sendto(request_json.encode('utf-8'), (self.host, self.port))
            
            response_data, server_address = self.socket.recvfrom(1024)
            response = json.loads(response_data.decode('utf-8'))
            return response
        except socket.timeout:
            return {"status": "error", "message": "Request timeout"}
        except Exception as e:
            return {"status": "error", "message": f"Client error: {str(e)}"}
    
    def create_account(self, username):
        """Create a new account"""
        request = {
            "command": "create_account",
            "username": username
        }
        return self.send_request(request)
    
    def send_email(self, sender, recipient, subject, content):
        """Send an email"""
        request = {
            "command": "send_email",
            "sender": sender,
            "recipient": recipient,
            "subject": subject,
            "content": content
        }
        return self.send_request(request)
    
    def login(self, username):
        """Login and get list of emails"""
        request = {
            "command": "login",
            "username": username
        }
        return self.send_request(request)
    
    def get_email(self, username, filename):
        """Get content of a specific email"""
        request = {
            "command": "get_email",
            "username": username,
            "filename": filename
        }
        return self.send_request(request)
    
    def interactive_mode(self):
        """Interactive command line interface"""
        print("=== UDP Mail Client ===")
        print("Available commands:")
        print("1. create <username> - Create a new account")
        print("2. send <sender> <recipient> <subject> <content> - Send an email")
        print("3. login <username> - Login and list emails")
        print("4. read <username> <filename> - Read a specific email")
        print("5. quit - Exit the client")
        print()
        
        while True:
            try:
                command = input("Enter command: ").strip().split()
                
                if not command:
                    continue
                
                if command[0] == "quit":
                    print("Goodbye!")
                    break
                
                elif command[0] == "create" and len(command) == 2:
                    username = command[1]
                    response = self.create_account(username)
                    print(f"Response: {response}")
                
                elif command[0] == "send" and len(command) >= 4:
                    sender = command[1]
                    recipient = command[2]
                    subject = command[3]
                    content = " ".join(command[4:]) if len(command) > 4 else "No content"
                    response = self.send_email(sender, recipient, subject, content)
                    print(f"Response: {response}")
                
                elif command[0] == "login" and len(command) == 2:
                    username = command[1]
                    response = self.login(username)
                    if response["status"] == "success":
                        print(f"Emails for {username}:")
                        for i, filename in enumerate(response["files"], 1):
                            print(f"  {i}. {filename}")
                    else:
                        print(f"Error: {response['message']}")
                
                elif command[0] == "read" and len(command) == 3:
                    username = command[1]
                    filename = command[2]
                    response = self.get_email(username, filename)
                    if response["status"] == "success":
                        print(f"Email content:")
                        print("-" * 50)
                        print(response["content"])
                        print("-" * 50)
                    else:
                        print(f"Error: {response['message']}")
                
                else:
                    print("Invalid command. Use 'quit' to exit.")
                
                print()
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def close(self):
        """Close the client socket"""
        self.socket.close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        # Demo mode with predefined commands
        client = MailClient()
        
        print("=== UDP Mail Client Demo ===")
        
        # Create accounts
        print("1. Creating accounts...")
        print("Creating account 'alice':", client.create_account("alice"))
        print("Creating account 'bob':", client.create_account("bob"))
        print()
        
        # Send emails
        print("2. Sending emails...")
        print("Alice sends email to Bob:", 
              client.send_email("alice", "bob", "Hello Bob", "This is a test email from Alice to Bob."))
        print("Bob sends email to Alice:", 
              client.send_email("bob", "alice", "Reply to Alice", "Thanks for the email, Alice!"))
        print()
        
        # Login and list emails
        print("3. Checking emails...")
        print("Alice's emails:")
        alice_response = client.login("alice")
        if alice_response["status"] == "success":
            for i, filename in enumerate(alice_response["files"], 1):
                print(f"  {i}. {filename}")
        
        print("\nBob's emails:")
        bob_response = client.login("bob")
        if bob_response["status"] == "success":
            for i, filename in enumerate(bob_response["files"], 1):
                print(f"  {i}. {filename}")
        
        print("\n4. Reading an email...")
        if alice_response["status"] == "success" and alice_response["files"]:
            # Read the first email
            first_email = alice_response["files"][0]
            email_content = client.get_email("alice", first_email)
            if email_content["status"] == "success":
                print(f"Content of {first_email}:")
                print("-" * 50)
                print(email_content["content"])
                print("-" * 50)
        
        client.close()
    else:
        # Interactive mode
        client = MailClient()
        try:
            client.interactive_mode()
        finally:
            client.close()
