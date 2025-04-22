# 🔐 Password Hasher

## 📌 Overview
This Python script securely hashes passwords using **bcrypt** to ensure strong encryption and verification. It helps protect user credentials from brute-force attacks by using **salting and slow hashing**.

## 🚀 Features
- Uses **bcrypt** for secure password hashing.
- **Salts passwords** to prevent rainbow table attacks.
- **Verifies passwords** against stored hashes.
- Easy to integrate into authentication systems.

## 💻 Installation
Before running the script, make sure you have **bcrypt** installed:

```bash
pip install bcrypt

🛠️ Usage
To hash a password, run:

python
from password_hasher import hash_password

hashed_pw = hash_password("MySecurePassword")
print("Hashed Password:", hashed_pw)

To verify a password, use:

python
from password_hasher import verify_password

is_valid = verify_password("MySecurePassword", hashed_pw)
print("Password verification result:", is_valid)  # True or False
🔑 Why Use bcrypt?
Slow hashing makes brute-force attacks harder.

Automatic salting ensures unique hashes for the same password.

Commonly used in authentication systems for storing passwords securely.

📜 License
This project is licensed under the MIT License—feel free to use and modify it.

🙌 Contributing
Want to improve this script? Feel free to fork, submit pull requests, or suggest enhancements!

📩 Contact
For questions, reach out at yancho506@gmail.com


---
