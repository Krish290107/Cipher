# 🏛️ Caesar Cipher Tool

Hey there! 👋 Welcome to the **Caesar Cipher Tool**. This is a fun, interactive command-line Python script that lets you play around with one of the oldest and simplest encryption techniques in history—the Caesar cipher!

## ✨ Features

This tool gives you a cool menu with a few handy features:

- **🔒 Encrypt:** Got a secret message? Shift the letters and turn it into ciphertext.
- **🔓 Decrypt:** Have a ciphered message and know the key? Shift it back and read the hidden text.
- **🔨 Brute Force:** Forgot the shift key? Or intercepted a secret message? This feature tries all 25 possible shifts and highlights the ones that contain common English words (like "the", "and", "hello").
- **🛡️ Strength Report:** Curious how strong your secret message is? This feature analyzes your message length, chosen shift, and symbol usage to give you a security rating and some helpful tips!

## 🚀 How to Run

Running the script is super easy! All you need is Python installed on your computer.

1. Open your terminal or command prompt.
2. Navigate to the folder containing `cipher.py`.
3. Run the following command:

```bash
python cipher.py
```

## 🎮 How to Use

Once you start the script, you'll see a neat menu:

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

Just type the number of the option you want to choose and hit Enter!
- When asked for a **Shift**, enter a number between 1 and 25. If you enter something invalid, it defaults to a shift of 3 (the classic Julius Caesar shift!).
- The **Brute Force** option will print out all possible decrypted messages. It even points out which ones look like readable English with a little `← readable?` tag.

## ⚠️ A Quick Reality Check

While playing with the Caesar cipher is a lot of fun, please remember that it is a **toy cipher**. It takes a modern computer less than a millisecond to crack it! 

For real-world security:
- **Passwords:** Use strong hashing algorithms like bcrypt or Argon2.
- **Data:** Use modern encryption standards like AES-256.

---

Have fun encrypting your secret messages! 🕵️‍♂️✨
