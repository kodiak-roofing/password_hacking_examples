import time
import string
import random

# Step 1: Generate a fake password list (simulate a wordlist)


def generate_password_list(count):
    passwords = []
    for _ in range(count):
        pw = ''.join(random.choices(
            string.ascii_lowercase + string.digits, k=8))
        passwords.append(pw)
    return passwords


# Step 2: Set the target password (the one we want to "crack")
TARGET_PASSWORD = "a7x9d2qk"

# Step 3: Simulate the brute force attempt


def brute_force(passwords):
    attempts = 0
    start_time = time.time()

    for password in passwords:
        attempts += 1
        print(f"Attempt {attempts}: Trying '{password}'")

        if password == TARGET_PASSWORD:
            print(f"\n✅ Password cracked! It was: {password}")
            break
    else:
        print("\n❌ Password not found in list.")

    duration = time.time() - start_time
    print(f"\n🔍 Attempts: {attempts}")
    print(f"⏱️ Time taken: {duration:.2f} seconds")


# Run it!
if __name__ == "__main__":
    password_list = generate_password_list(1000)

    # Insert the real password somewhere randomly in the list
    insert_index = random.randint(0, len(password_list)-1)
    password_list[insert_index] = TARGET_PASSWORD

    brute_force(password_list)
