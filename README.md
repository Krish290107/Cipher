# Cipher Toolkit

A command-line Python script that implements the classic Caesar and Vigenère ciphers. It's a straightforward, interactive tool for encrypting, decrypting, and exploring how to crack historical encryption techniques.

## Features

- **Caesar Cipher (Encrypt/Decrypt):** Shift letters by a specific key to create ciphertext or reverse it to read hidden text.
- **Vigenère Cipher (Encrypt/Decrypt):** Use a keyword to apply multiple Caesar ciphers, making it much harder to crack.
- **Brute Force Attack:** Try all 25 possible Caesar shifts. The script automatically flags outputs that contain common English words.
- **Frequency Analysis:** Analyze the letter frequency of a text and visualize it with a bar chart to help crack substitution ciphers.
- **Strength Report:** Analyzes the length, shift value, and symbol usage of your message to provide a basic security rating.
- **Additional Tools:** Random Key Encrypt, ROT13, Shift Comparison, and File Encryption capabilities.

## Usage

You'll need Python installed to run the script. No external dependencies are required.

1. Clone or download the repository.
2. Open your terminal and navigate to the project folder.
3. Run the script:

```bash
python cipher.py
```

When you start the tool, you'll see an interactive menu:

```text
╔══════════════════════════════════╗
║         CIPHER TOOLKIT          ║
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
```

Select an option by typing the corresponding number or letter.
- When prompted for a shift value, enter a number between 1 and 25. Invalid inputs will default to a shift of 3.
- The brute-force option outputs all possible combinations and marks readable English results with a `← readable?` tag.

## Security Note

The Caesar cipher is historically significant but computationally trivial to crack today. It is essentially a toy cipher and takes less than a millisecond for a computer to break. 

Do not use this for actual security. For real-world applications, rely on modern standards like AES for encryption and algorithms like bcrypt or Argon2 for password hashing.
