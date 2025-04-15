# 🔐 Password Brute Force Demo

This project demonstrates how brute force password attacks work through various methods:
- a **basic terminal script**
- a **GUI-based visual simulation**
- and a **browser automation script using Selenium**

It’s meant for educational purposes only — to help people understand how password attacks function and why secure password practices are important.

---

## 🗂 File Descriptions

### `brute_force_example.py`
A simple Python script that simulates a brute force attack using a randomly generated list of 1,000 passwords. The script "cracks" a hardcoded target password by iterating through each password one-by-one.

- **Highlights:**
  - Uses a fake password list
  - Inserts the real password at a random spot
  - Tracks number of attempts and time taken

---

### `brute_force_gui.py`
A GUI version of the brute force simulation using `tkinter`. It visually shows the progress of the attack in real-time with a progress bar and attempt log.

- **Highlights:**
  - Real-time password attempts displayed
  - Progress bar visualization
  - Slowed down for educational demo
  - Threaded to keep UI responsive

---

### `selenium_fill_form.py`
Uses Selenium with Firefox to simulate a password attack on a demo website ([Practice Test Automation Login](https://practicetestautomation.com/practice-test-login/)).

- **Highlights:**
  - Uses Selenium to control Firefox
  - Iterates over a list of passwords (`Password100` to `Password123`)
  - Inputs each password into the login form
  - Demonstrates how bots can brute-force web login forms

> ⚠️ **This script is for educational use only**. Only run this script on practice or authorized pages like the one provided.

---

## 🖥 How to Run Each Script

### ✅ Prerequisites

To install all pre-requisites, run this command:
```bash
pip install -r requirements.txt
```

Requirements include:
- Python 3.7+
- `tkinter` (usually pre-installed)
- `selenium`
- Firefox Browser
- `geckodriver` in your system PATH

Install Selenium:
```bash
pip install selenium
```

---

### ▶️ Run the Terminal Brute Force Demo
```bash
python brute_force_example.py
```

---

### 🖼 Run the GUI Version
```bash
python brute_force_gui.py
```

---

### 🌐 Run the Selenium Web Form Demo
Ensure Firefox and `geckodriver` are installed.

```bash
python selenium_fill_form.py
```

If you need to specify the `geckodriver` path:
```python
from selenium.webdriver.firefox.service import Service
service = Service(executable_path="/path/to/geckodriver")
driver = webdriver.Firefox(service=service)
```

---

## 💡 What You’ll Learn

- Why short and simple passwords are easily guessed
- How brute force attacks work in principle
- Why password length and complexity matter
- How tools like Selenium can be (mis)used for automation

---

## 🔒 Important Note

This project is **strictly for educational purposes** to raise awareness around cybersecurity and password safety. Do **not** use this code to attack any real system.

Always use secure passwords and enable multi-factor authentication wherever possible.

---


## Additional Resources

[Password Strength Tester​](https://bitwarden.com/password-strength/)

[Check if your password has been leaked](https://haveibeenpwned.com/)

[Justice – Catching the bad guys](https://www.youtube.com/watch?v=VrKW58MS12g)
