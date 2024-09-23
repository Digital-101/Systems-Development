import random
import string
import pyperclip

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    """
    Generate a secure password.

    :param length: Length of the password.
    :param use_uppercase: Include uppercase letters.
    :param use_digits: Include digits.
    :param use_special_chars: Include special characters.
    :return: Generated password as a string.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Define character sets
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase) if use_uppercase else []
    digits = list(string.digits) if use_digits else []
    special_chars = list("!@#$%^&*()-_=+[]{}|;:,.<>?") if use_special_chars else []

    # Ensure there is at least one character type in the password
    if not (uppercase or digits or special_chars):
        raise ValueError("At least one character type must be selected.")

    all_chars = lowercase + uppercase + digits + special_chars
    
    # Generate a password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    # Ensure password includes at least one character from each selected set
    if use_uppercase:
        password += random.choice(uppercase)
    if use_digits:
        password += random.choice(digits)
    if use_special_chars:
        password += random.choice(special_chars)
    
    # Shuffle the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))
    
    return password

def main():
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"Generated Password: {password}")

    # Copy password to clipboard
    pyperclip.copy(password)
    print("Password copied to clipboard!")

if __name__ == "__main__":
    main()
