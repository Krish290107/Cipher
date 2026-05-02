# Caesar Cipher Tool

A command-line Python script that implements the classic Caesar cipher. It's a straightforward, interactive tool for encrypting, decrypting, and exploring how to crack one of the oldest encryption techniques.

## Features

- **Encrypt:** Shift letters by a specific key to create ciphertext.
- **Decrypt:** Reverse the shift to read hidden text if you know the key.
- **Brute Force:** Try all 25 possible shifts. The script automatically flags outputs that contain common English words to help you identify the original message.
- **Strength Report:** Analyzes the length, shift value, and symbol usage of your message to provide a basic security rating.

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
  ╔════════════════════════════╗
  ║    CAESAR CIPHER TOOL      ║
  ╠════════════════════════════╣
  ║  1 · 🔒 Encrypt            ║
  ║  2 · 🔓 Decrypt            ║
  ║  3 · 🔨 Brute Force        ║
  ║  4 · 🛡️  Strength Report   ║
  ║  q · Quit                  ║
  ╚════════════════════════════╝
```

Select an option by typing the corresponding number or letter.
- When prompted for a shift value, enter a number between 1 and 25. Invalid inputs will default to a shift of 3.
- The brute-force option outputs all possible combinations and marks readable English results with a `← readable?` tag.

## Security Note

The Caesar cipher is historically significant but computationally trivial to crack today. It is essentially a toy cipher and takes less than a millisecond for a computer to break. 

Do not use this for actual security. For real-world applications, rely on modern standards like AES for encryption and algorithms like bcrypt or Argon2 for password hashing.
