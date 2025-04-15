import tkinter as tk
from tkinter import ttk
import time
import random
import string
from threading import Thread

# Target password to "crack"
TARGET_PASSWORD = "a7x9d2qk"
TOTAL_PASSWORDS = 1000

# Generate a fake password list


def generate_password_list(count):
    return [
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        for _ in range(count)
    ]

# Brute-force function


def brute_force(passwords, update_func, done_func):
    attempts = 0
    start_time = time.time()

    for password in passwords:
        attempts += 1
        time.sleep(0.01)  # Slowed for demonstration
        update_func(password, attempts, len(passwords))

        if password == TARGET_PASSWORD:
            duration = time.time() - start_time
            done_func(password, attempts, duration)
            return

# Tkinter UI


class BruteForceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brute Force Password Demo")
        self.root.geometry("520x240")

        self.label = tk.Label(
            root, text="🔐 Brute Forcing...", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.status = tk.Label(root, text="", font=("Courier", 13))
        self.status.pack()

        self.progress = ttk.Progressbar(
            root, orient='horizontal', length=400, mode='determinate')
        self.progress.pack(pady=10)

        self.result = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
        self.result.pack(pady=10)

        # Start brute force in a separate thread
        Thread(target=self.start_brute_force).start()

    def update_status(self, password, attempt, total):
        self.status.config(text=f"Attempt {attempt}: Trying '{password}'")
        self.progress["value"] = (attempt / total) * 100
        self.root.update_idletasks()

    def show_result(self, password, attempts, duration):
        self.result.config(
            text=f"✅ Cracked! Password: {password}\n🔍 Attempts: {attempts} | ⏱️ {duration:.2f}s"
        )

    def start_brute_force(self):
        password_list = generate_password_list(TOTAL_PASSWORDS)
        insert_index = random.randint(0, len(password_list) - 1)
        password_list[insert_index] = TARGET_PASSWORD
        brute_force(password_list, self.update_status, self.show_result)


if __name__ == "__main__":
    root = tk.Tk()
    app = BruteForceApp(root)
    root.mainloop()
