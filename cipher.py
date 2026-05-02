#2401CS83   Krishkumar
import sys


def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)

def crack(ciphertext):
    print("\n  Trying all 25 shifts...\n")
    common = {"the","and","is","to","a","hello","hi","you","at","we","he","she","it","of"}
    for shift in range(1, 26):
        guess = decrypt(ciphertext, shift)
        readable = any(w in guess.lower().split() for w in common)
        tag = "  ← readable?" if readable else ""
        print(f"  [{shift:>2}]  {guess}{tag}")

def strength_report(message, shift):
    letters = sum(1 for c in message if c.isalpha())
    score = 0
    tips = []

    if len(message) >= 15: score += 1
    else: tips.append("Longer messages are harder to frequency-analyse.")

    if shift not in [1, 3, 13]: score += 1
    else: tips.append(f"Shift {shift} is very common — attackers try it first.")

    if any(c in message for c in "!@#$%^&*"): score += 1
    else: tips.append("Symbols stay unencrypted and reveal message structure.")

    labels = {0: "☠️  Terrible", 1: "🟠 Weak", 2: "🟡 Fair", 3: "🟢 Okay"}
    print(f"\n  ┌─ Strength Report ───────────────────────┐")
    print(f"  │  Rating   : {labels[score]:<30}│")
    print(f"  │  Letters  : {letters:<30}│")
    print(f"  │  Shift    : {shift:<30}│")
    print(f"  │  Key space: 25 possible shifts           │")
    print(f"  │  Crack time (computer): < 0.001 seconds  │")
    print(f"  ├─ Tips ──────────────────────────────────┤")
    if tips:
        for tip in tips:
            # wrap tip to fit box width of 42 chars
            print(f"  │  • {tip[:40]:<40}│")
            if len(tip) > 40:
                print(f"  │    {tip[40:80]:<40}│")
    else:
        print(f"  │  ✓ As good as Caesar cipher gets!       │")
    print(f"  ├─ Reality check ─────────────────────────┤")
    print(f"  │  Caesar is a TOY cipher. For real use:   │")
    print(f"  │  → Passwords : use bcrypt / Argon2       │")
    print(f"  │  → Data      : use AES-256               │")
    print(f"  └─────────────────────────────────────────┘")



def show_menu():
    print("""
  ╔════════════════════════════╗
  ║    CAESAR CIPHER TOOL      ║
  ╠════════════════════════════╣
  ║  1 · 🔒 Encrypt            ║
  ║  2 · 🔓 Decrypt            ║
  ║  3 · 🔨 Brute Force        ║
  ║  4 · 🛡️  Strength Report   ║
  ║  q · Quit                  ║
  ╚════════════════════════════╝""")

def get_shift():
    try:
        s = int(input("  Shift (1–25): ").strip())
        return s % 26 or 3
    except ValueError:
        print("  (Using default shift: 3)")
        return 3



def main():
    print(__doc__)
    while True:
        show_menu()
        choice = input("\n  → ").strip().lower()

        if choice == "1":
            msg = input("\n  Message : ")
            shift = get_shift()
            print(f"\n  🔒  {encrypt(msg, shift)}\n")

        elif choice == "2":
            msg = input("\n  Ciphertext : ")
            shift = get_shift()
            print(f"\n  🔓  {decrypt(msg, shift)}\n")

        elif choice == "3":
            msg = input("\n  Ciphertext to crack : ")
            crack(msg)

        elif choice == "4":
            msg = input("\n  Message : ")
            shift = get_shift()
            strength_report(msg, shift)

        elif choice == "q":
            print("\n  Bye! 👋\n")
            break

        else:
            print("  Try 1, 2, 3, 4, or q.\n")

if __name__ == "__main__":
    main()
