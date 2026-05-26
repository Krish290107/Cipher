#2401CS83   Krishkumar

import random
import re
import time
from collections import Counter

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False


def green(text):
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}" if COLOR else text

def red(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}" if COLOR else text

def cyan(text):
    return f"{Fore.CYAN}{text}{Style.RESET_ALL}" if COLOR else text

def yellow(text):
    return f"{Fore.YELLOW}{text}{Style.RESET_ALL}" if COLOR else text


def encrypt(message, shift):
    result = ""
    shift = shift % 26  # normalise shift to 0-25

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def decrypt(message, shift):
    return encrypt(message, -shift)


def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()

    # FIX: validate key contains only letters
    if not key or not key.isalpha():
        print(red("Key must contain letters only."))
        return text

    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()

    # FIX: validate key contains only letters
    if not key or not key.isalpha():
        print(red("Key must contain letters only."))
        return text

    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


def crack(ciphertext):
    print(cyan("\n Trying all 25 shifts...\n"))

    common = {
        "the", "and", "is", "to", "a",
        "hello", "hi", "you", "at",
        "we", "he", "she", "it", "of", "in", "that", "are"
    }

    best_score = 0
    best_shift = 1
    best_guess = ""

    for shift in range(1, 26):
        guess = decrypt(ciphertext, shift)

        # FIX: strip punctuation before splitting so words like "hello," still match
        words = re.findall(r"[a-z]+", guess.lower())
        score = sum(word in common for word in words)

        if score > best_score:
            best_score = score
            best_shift = shift
            best_guess = guess

        readable = " ← readable?" if score > 0 else ""
        print(f"[{shift:>2}] {guess}{readable}")
        time.sleep(0.05)

    print(green(f"\n Best Guess (shift={best_shift}):"))
    print(best_guess)


def frequency_analysis(text):
    letters = [c.lower() for c in text if c.isalpha()]

    if not letters:
        print(red("No letters found."))
        return

    counts = Counter(letters)
    total = sum(counts.values())

    print(cyan("\n Letter Frequency:\n"))

    for char, count in sorted(counts.items()):
        percent = (count / total) * 100
        bar = "█" * int(percent)
        print(f"{char}: {count:>3} ({percent:5.1f}%) {bar}")


def strength_report(message, shift):
    letters = sum(1 for c in message if c.isalpha())
    score = 0
    tips = []

    if len(message) >= 15:
        score += 1
    else:
        tips.append("Longer messages are harder to analyse.")

    if shift not in [1, 3, 13]:
        score += 1
    else:
        tips.append("Common shifts (1, 3, ROT13) are easy to guess.")

    # FIX: mixed case is actually more useful than symbols for Caesar strength
    has_upper = any(c.isupper() for c in message if c.isalpha())
    has_lower = any(c.islower() for c in message if c.isalpha())
    if has_upper and has_lower:
        score += 1
    else:
        tips.append("Using mixed case makes frequency analysis slightly harder.")

    labels = {
        0: "Terrible",
        1: "Weak",
        2: "Fair",
        3: "Okay"
    }

    print(cyan("\n ===== Strength Report ====="))
    print(f"Rating      : {labels[score]}")
    print(f"Letters     : {letters}")
    print(f"Shift       : {shift}")
    print(f"Key Space   : 25")
    print(f"Crack Time  : < 0.001 sec")

    print("\nTips:")
    if tips:
        for tip in tips:
            print(f" - {tip}")
    else:
        print(" - Best possible Caesar usage.")

    print(green("\n Caesar Cipher is NOT secure for real-world encryption."))


def save_to_file(text):
    filename = input("Filename to save: ").strip()

    if not filename:
        print(red("No filename entered."))
        return

    try:
        with open(filename, "w") as f:
            f.write(text)
        print(green("Saved successfully."))
    except OSError as e:
        print(red(f"Could not save file: {e}"))


def read_from_file():
    filename = input("Filename to read: ").strip()

    try:
        with open(filename, "r") as f:
            data = f.read()
        print(green("File loaded."))
        return data
    except FileNotFoundError:
        print(red(f"File not found: {filename}"))
        return ""
    except OSError as e:
        print(red(f"Could not read file: {e}"))
        return ""


def random_shift():
    return random.randint(1, 25)


def rot13(text):
    return encrypt(text, 13)


def compare_shifts(message):
    print(cyan("\n Caesar Cipher Comparison:\n"))
    for i in range(1, 26):
        print(f"{i:>2}: {encrypt(message, i)}")


def about():
    print(cyan("""
==============================
        ABOUT CIPHER
==============================

Caesar Cipher:
- Monoalphabetic substitution cipher
- Invented by Julius Caesar
- Uses alphabet shifting
- Key space = 25
- Vulnerable to brute force
- Broken using frequency analysis

Vigenere Cipher:
- Polyalphabetic substitution cipher
- Uses a keyword to apply multiple shifts
- Stronger than Caesar but still breakable
- Key must contain letters only

Real-world encryption:
- AES-256 for data encryption
- bcrypt / Argon2 for passwords

==============================
"""))


def show_menu():
    print(yellow("""
╔══════════════════════════════════╗
║        CIPHER TOOLKIT           ║
╠══════════════════════════════════╣
║ 1  · Encrypt Caesar             ║
║ 2  · Decrypt Caesar             ║
║ 3  · Brute Force Attack         ║
║ 4  · Strength Report            ║
║ 5  · Frequency Analysis         ║
║ 6  · Random Key Encrypt         ║
║ 7  · ROT13                      ║
║ 8  · Compare All Shifts         ║
║ 9  · Vigenere Encrypt           ║
║ 10 · Vigenere Decrypt           ║
║ 11 · Encrypt File               ║
║ 12 · About Cipher               ║
║ q  · Quit                       ║
╚══════════════════════════════════╝
"""))


def get_shift():
    # FIX: accept 1-25 strictly; don't silently accept 0 or 26 as valid
    try:
        s = int(input("Shift (1-25): ").strip())
        if 1 <= s <= 25:
            return s
        print(red("Shift out of range (1-25). Using default shift: 3"))
        return 3
    except ValueError:
        print(red("Invalid input. Using default shift: 3"))
        return 3


def main():
    while True:
        show_menu()
        choice = input("→ ").strip().lower()

        if choice == "1":
            msg = input("Message: ")
            shift = get_shift()
            result = encrypt(msg, shift)
            print(green(f"\nEncrypted:\n{result}\n"))
            save = input("Save to file? (y/n): ").lower()
            if save == "y":
                save_to_file(result)

        elif choice == "2":
            msg = input("Ciphertext: ")
            shift = get_shift()
            print(green(f"\nDecrypted:\n{decrypt(msg, shift)}\n"))

        elif choice == "3":
            msg = input("Ciphertext to crack: ")
            crack(msg)

        elif choice == "4":
            msg = input("Message: ")
            shift = get_shift()
            strength_report(msg, shift)

        elif choice == "5":
            msg = input("Text: ")
            frequency_analysis(msg)

        elif choice == "6":
            msg = input("Message: ")
            shift = random_shift()
            result = encrypt(msg, shift)
            print(green(f"\nRandom Shift Used: {shift}"))
            print(result)

        elif choice == "7":
            msg = input("Message: ")
            print(green(f"\nROT13:\n{rot13(msg)}\n"))

        elif choice == "8":
            msg = input("Message: ")
            compare_shifts(msg)

        elif choice == "9":
            msg = input("Message: ")
            key = input("Key (letters only): ")
            print(green(f"\nEncrypted:\n{vigenere_encrypt(msg, key)}\n"))

        elif choice == "10":
            msg = input("Ciphertext: ")
            key = input("Key (letters only): ")
            print(green(f"\nDecrypted:\n{vigenere_decrypt(msg, key)}\n"))

        elif choice == "11":
            data = read_from_file()
            if data:
                shift = get_shift()
                encrypted = encrypt(data, shift)
                print(green("\nEncrypted File Content:\n"))
                print(encrypted)
                save_to_file(encrypted)

        elif choice == "12":
            about()

        elif choice == "q":
            print(green("\nBye 👋\n"))
            break

        else:
            print(red("Invalid option.\n"))


if __name__ == "__main__":
    main()
