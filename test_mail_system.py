#!/usr/bin/env python3
"""
Test script for the UDP Mail Server system
"""

from mail_client import MailClient
import time

def test_mail_system():
    print("=== Testing UDP Mail Server System ===\n")
    
    client = MailClient()
    
    # Test 1: Create accounts
    print("1. Creating user accounts...")
    alice_result = client.create_account("alice")
    print(f"   Alice account: {alice_result}")
    
    bob_result = client.create_account("bob")
    print(f"   Bob account: {bob_result}")
    
    charlie_result = client.create_account("charlie")
    print(f"   Charlie account: {charlie_result}")
    print()
    
    # Test 2: Send emails
    print("2. Sending emails...")
    email1 = client.send_email("alice", "bob", "Meeting Tomorrow", "Hi Bob, let's meet tomorrow at 2 PM for our project discussion.")
    print(f"   Alice -> Bob: {email1}")
    
    email2 = client.send_email("bob", "alice", "Re: Meeting Tomorrow", "Sure Alice, 2 PM works for me. See you then!")
    print(f"   Bob -> Alice: {email2}")
    
    email3 = client.send_email("charlie", "alice", "Project Update", "Alice, I've completed the backend integration. Ready for testing.")
    print(f"   Charlie -> Alice: {email3}")
    
    email4 = client.send_email("alice", "charlie", "Great Work!", "Thanks Charlie! I'll test it this afternoon.")
    print(f"   Alice -> Charlie: {email4}")
    print()
    
    # Test 3: Login and check emails
    print("3. Checking emails for each user...")
    
    for user in ["alice", "bob", "charlie"]:
        print(f"\n   {user.capitalize()}'s inbox:")
        login_result = client.login(user)
        if login_result["status"] == "success":
            files = login_result["files"]
            for i, filename in enumerate(files, 1):
                print(f"     {i}. {filename}")
        else:
            print(f"     Error: {login_result['message']}")
    
    # Test 4: Read specific emails
    print(f"\n4. Reading specific emails...")
    
    # Read Alice's first email
    alice_login = client.login("alice")
    if alice_login["status"] == "success" and alice_login["files"]:
        first_email = alice_login["files"][0]
        print(f"\n   Reading Alice's email: {first_email}")
        email_content = client.get_email("alice", first_email)
        if email_content["status"] == "success":
            print("   Content:")
            print("   " + "-" * 60)
            for line in email_content["content"].split('\n'):
                print(f"   {line}")
            print("   " + "-" * 60)
    
    # Read Bob's email from Alice
    bob_login = client.login("bob")
    if bob_login["status"] == "success":
        for filename in bob_login["files"]:
            if "alice" in filename:
                print(f"\n   Reading Bob's email from Alice: {filename}")
                email_content = client.get_email("bob", filename)
                if email_content["status"] == "success":
                    print("   Content:")
                    print("   " + "-" * 60)
                    for line in email_content["content"].split('\n'):
                        print(f"   {line}")
                    print("   " + "-" * 60)
                break
    
    print(f"\n=== Test completed! ===")
    print("Check the 'accounts/' directory to see all created files.")
    
    client.close()

if __name__ == "__main__":
    test_mail_system()
