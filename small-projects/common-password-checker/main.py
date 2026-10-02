import os
import sys


# Absolute path to the folder where this script lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASSWORDS_FILE = os.path.join(BASE_DIR, "passwords.txt")


def generate_common_passwords():
    if not os.path.isfile(PASSWORDS_FILE):
        print(f"Error: '{PASSWORDS_FILE}' not found.")
        sys.exit(1)

    with open(PASSWORDS_FILE, 'r') as file:
        passwords = set(file.read().splitlines())

    return passwords


def check_password(user_pass, common_passes):
    return user_pass in common_passes


def main():
    user_input = input("Enter your password: ").lower()
    common_passwords = generate_common_passwords()
    is_common = check_password(user_pass=user_input,
                               common_passes=common_passwords)
    if is_common:
        print("a common password")
    else:
        print("a unique password")


if __name__ == "__main__":
    main()