# Caesar Cipher Encryption-Decryption Program

This is a simple Python implementation of the **Caesar Cipher**, a classic encryption technique used to encode and decode messages by shifting characters of the alphabet by a fixed number of positions.

---

## 🔐 Features

- Encrypts a plaintext message using a Caesar shift
- Decrypts an encrypted message using the same shift value
- Handles non-alphabetic characters (e.g., spaces, punctuation) by leaving them unchanged
- Allows repeated encryption/decryption in a loop
- User-friendly command-line interface

---

## 🧠 How It Works

The Caesar Cipher works by shifting each letter of the alphabet by a specified number of positions. If the shift moves a character past 'z', it wraps around to the beginning of the alphabet.

### Example:
For a shift of `2`:
- `'a'` → `'c'`
- `'x'` → `'z'`
- `'z'` → `'b'`

---

## 💻 Code Structure

- `alphabet`: A list of lowercase English letters
- `encryption(text, shift)`: Encrypts the given message
- `decryption(text, shift)`: Decrypts the given message
- A loop that allows continuous user interaction

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/caesar-cipher.git
   cd caesar-cipher
