# UDP Mail Server - VKU Programming Exercise

This project implements a UDP Socket-based Mail Server as required by the VKU programming exercise.

## Features

The mail server implements all the required functionality:

1. **Account Creation**: When users create new accounts on client machines, the server creates a corresponding directory and a `new_email.txt` file with a welcome message.

2. **Email Sending**: When users send emails, the server receives them, determines the recipient account, and creates a file with the email content in the recipient's directory.

3. **Account Login**: When users log into an account, the server opens the corresponding directory and sends all file names back to the client.

4. **Email Reading**: Users can read the content of specific emails.

## Files

- `mail_server.py` - The UDP Mail Server implementation
- `mail_client.py` - The UDP Mail Client for testing
- `accounts/` - Directory where user accounts and emails are stored

## Usage

### Starting the Server

```bash
python3 mail_server.py
```

The server will start on `localhost:12345` by default.

### Using the Client

#### Interactive Mode
```bash
python3 mail_client.py
```

Available commands:
- `create <username>` - Create a new account
- `send <sender> <recipient> <subject> <content>` - Send an email
- `login <username>` - Login and list emails
- `read <username> <filename>` - Read a specific email
- `quit` - Exit the client

#### Demo Mode
```bash
python3 mail_client.py demo
```

This will run a demonstration with predefined commands.

## Example Usage

1. Start the server:
   ```bash
   python3 mail_server.py
   ```

2. In another terminal, start the client:
   ```bash
   python3 mail_client.py
   ```

3. Create accounts and send emails:
   ```
   Enter command: create alice
   Enter command: create bob
   Enter command: send alice bob "Hello" "This is a test email"
   Enter command: login alice
   Enter command: read alice new_email.txt
   ```

## Technical Details

- **Protocol**: UDP Socket communication
- **Data Format**: JSON messages
- **File Storage**: Each user has a directory in `accounts/` folder
- **Email Format**: Plain text files with headers (From, To, Subject, Date)
- **Threading**: Server uses threading for handling multiple client requests

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Directory Structure

```
Mailserver/
├── mail_server.py
├── mail_client.py
├── README.md
└── accounts/
    ├── alice/
    │   ├── new_email.txt
    │   └── email_20241209_094500_bob.txt
    └── bob/
        ├── new_email.txt
        └── email_20241209_094501_alice.txt
```
# MailServer
