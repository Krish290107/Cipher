# 🔐 Cipher Toolkit

> A command-line Python tool for encrypting, decrypting, and cracking classical ciphers — built for learning cryptography fundamentals.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Examples](#examples)
- [Security Note](#security-note)

---

## Overview

**Cipher Toolkit** is an interactive terminal application implementing the two most famous classical ciphers — **Caesar** and **Vigenère** — along with tools to analyse and crack them. It's designed as a hands-on way to explore how historical encryption works (and why it doesn't hold up today).

---

## Features

| Feature | Description |
|---|---|
| 🔒 Caesar Encrypt / Decrypt | Shift letters by a numeric key (1–25) to produce or read ciphertext |
| 🔑 Vigenère Encrypt / Decrypt | Use a keyword to apply layered Caesar shifts — much harder to brute-force |
| 💥 Brute Force Attack | Try all 25 shifts automatically; readable English results are flagged and the best guess is highlighted |
| 📊 Frequency Analysis | Count letter occurrences and render a bar chart — the classic technique for cracking substitution ciphers |
| 📋 Strength Report | Rates your message against three criteria: length, shift choice, and case variety |
| 🎲 Random Key Encrypt | Picks a random shift so you don't have to choose |
| 🔄 ROT13 | Apply the well-known ROT13 encoding (shift of 13) in one step |
| 🔁 Compare All Shifts | Print all 25 Caesar encryptions of a message side-by-side |
| 📁 File Encryption | Read a text file, encrypt it, and save the result |

---

## Requirements

- **Python 3.6+**
- `colorama` *(optional)* — adds colour to terminal output

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/cipher-toolkit.git
cd cipher-toolkit

# 2. (Optional) Install colour support
pip install colorama

# 3. Run
python cipher.py
```

No virtual environment is required. The script runs with the Python standard library alone.

---

## Usage

Launch the script and choose from the interactive menu:

```
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
```

Type the number or `q` and press Enter to select an option.

---

## Menu Options

### 1 · Encrypt Caesar
Enter a message and a shift value (1–25). The tool shifts every letter forward in the alphabet by that amount. Non-letter characters (spaces, numbers, punctuation) pass through unchanged.

After encrypting, you are prompted to save the result to a file.

### 2 · Decrypt Caesar
Enter a ciphertext and the same shift used to encrypt it. The tool reverses the shift to recover the original message.

### 3 · Brute Force Attack
Enter a ciphertext whose shift you don't know. The tool tries all 25 possibilities, prints each one, and marks lines containing common English words with `← readable?`. At the end it prints the most likely plaintext along with the shift number.

### 4 · Strength Report
Enter a message and shift. The tool scores the combination across three criteria and returns a rating:

| Score | Rating |
|---|---|
| 0 | Terrible |
| 1 | Weak |
| 2 | Fair |
| 3 | Okay |

Criteria checked: message length ≥ 15 characters, shift is not a common value (1, 3, or 13), and message contains mixed upper and lower case.

### 5 · Frequency Analysis
Enter any text. The tool counts each letter, calculates its percentage, and prints a horizontal bar chart. Compare the pattern against known English letter frequencies (E, T, A, O… are most common) to deduce the shift.

### 6 · Random Key Encrypt
Enter a message. The tool picks a random shift between 1 and 25, encrypts the message, and displays both the shift used and the ciphertext. Keep the shift number somewhere safe — you'll need it to decrypt.

### 7 · ROT13
Enter a message. ROT13 is a Caesar cipher with a fixed shift of 13. Applying it twice returns the original text, so the same option encrypts and decrypts.

### 8 · Compare All Shifts
Enter a message. The tool prints all 25 encrypted versions so you can see how each shift looks at a glance.

### 9 · Vigenere Encrypt
Enter a message and a keyword (letters only, no spaces or digits). Each letter of the message is shifted by a different amount determined by the corresponding letter of the repeating keyword.

### 10 · Vigenere Decrypt
Enter a Vigenère ciphertext and the keyword that was used to encrypt it. The tool reverses the keyword shifts to recover the plaintext.

### 11 · Encrypt File
Enter the path to a plain text file. The tool loads it, applies Caesar encryption with a shift you choose, prints the result, and prompts you to save it to a new file.

### 12 · About Cipher
Displays a brief reference on Caesar and Vigenère ciphers, and points to modern alternatives.

---

## Examples

**Encrypting a message:**
```
→ 1
Message: Hello World
Shift (1-25): 7
Encrypted:
Olssv Dvysk
```

**Brute-forcing a ciphertext:**
```
→ 3
Ciphertext to crack: Olssv Dvysk
...
[ 7] Hello World ← readable?
...
Best Guess (shift=7):
Hello World
```

**Vigenère encryption:**
```
→ 9
Message: AttackAtDawn
Key (letters only): lemon
Encrypted:
LxfopvefrnwA
```

---

## Security Note

> ⚠️ **Do not use these ciphers for anything that needs to be actually secret.**

The Caesar cipher has a key space of only 25 — a computer breaks it in under a millisecond. The Vigenère cipher is stronger but was conclusively broken in the 19th century using the Kasiski examination and index of coincidence.

For real-world security use:

- **AES-256** — symmetric encryption for data at rest and in transit
- **bcrypt / Argon2** — password hashing
- **RSA / ECC** — asymmetric encryption and digital signatures

---

*#2401CS83 — Krishkumar*
