import re
import math
import requests
import os
import random
import string
import pyfiglet

COMMON_PASSWORDS_URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt"

def print_banner():
    ascii_banner = pyfiglet.figlet_format("SecureSphere")
    print(ascii_banner)

def get_common_passwords(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return set(response.text.splitlines())
        else:
            print(f"Failed to fetch password list. Status: {response.status_code}")
            return set()
    except Exception as e:
        print("Error fetching password list:", e)
        return set()

def calculate_entropy(password):
    charset_size = 0
    if re.search(r'[a-z]', password): charset_size += 26
    if re.search(r'[A-Z]', password): charset_size += 26
    if re.search(r'[0-9]', password): charset_size += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset_size += 32
    entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
    return entropy

def classify_password(password, common_passwords):
    if password.lower() in common_passwords:
        return "Easy"
    entropy = calculate_entropy(password)
    length = len(password)
    if entropy < 28 or length < 6:
        return "Easy"
    elif entropy < 36:
        return "Medium"
    elif entropy < 60:
        return "Hard"
    elif entropy < 80:
        return "Hard but still can be cracked"
    else:
        return "Impossible"

def evaluate_passwords(passwords, common_passwords):
    for pw in passwords:
        pw = pw.strip()
        if not pw:
            continue
        rating = classify_password(pw, common_passwords)
        print(f"{pw}: {rating}")

def generate_strong_password(length=20):
    if length < 16:
        length = 16
    all_chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choices(all_chars, k=length))
        entropy = calculate_entropy(password)
        if entropy >= 80:
            return password

def main():
    print_banner()
    print("=== Password Strength Utility ===")
    print("Options:")
    print("1. Check a password")
    print("2. Check passwords from a file")
    print("3. Generate a random strong password")

    choice = input("Choose an option (1, 2, or 3): ")
    common_passwords = get_common_passwords(COMMON_PASSWORDS_URL)

    if choice == "1":
        pw = input("Enter your password: ")
        evaluate_passwords([pw], common_passwords)

    elif choice == "2":
        file_path = input("Enter the path to the password file: ")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                passwords = f.readlines()
                evaluate_passwords(passwords, common_passwords)
        else:
            print("File not found.")

    elif choice == "3":
        length = input("Enter desired length (default 20): ")
        try:
            length = int(length)
        except:
            length = 20
        password = generate_strong_password(length)
        print(f"Generated strong password: {password}")
        print("Rating: Impossible")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
