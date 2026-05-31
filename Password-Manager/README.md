Password Manager 🔐

A simple Password Manager application built with Python and Tkinter that allows users to generate, save, and search for passwords securely using a JSON file.

Features
Generate strong random passwords
Copy generated passwords to clipboard automatically
Save website credentials (website, email, password)
Search saved credentials by website name
Store data in JSON format
User-friendly graphical interface using Tkinter
Error handling for missing data files
Technologies Used
Python
Tkinter
JSON
Pyperclip
Random Module
Project Structure
Password-Manager/
│
├── main.py
├── password.json
├── logo.png
└── README.md
How to Run
Install Python.
Install the required package:
pip install pyperclip
Run the application:
python main.py
How It Works
Enter a website name.
Enter your email/username.
Click Generate Password to create a strong password.
Click Add to save the credentials.
Use Search to retrieve saved credentials.
Concepts Practiced
GUI Development with Tkinter
File Handling
JSON Data Storage
Exception Handling
Functions
Event-Driven Programming
Password Generation
Data Persistence
