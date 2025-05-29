# Hangman Game

This is a simple Hangman game made using Python.

The program picks a random word from an online list, and the player has to guess the word letter by letter. You have 6 chances (lives). If you guess all letters correctly before your lives run out, you win!

---

## How it works

- A random word is selected from a list of 10,000 common English words.
- You enter one letter at a time to guess the word.
- If your guess is correct, the letter is revealed in the word.
- If the guess is wrong, you lose one life.
- You win if you guess all the letters correctly.
- You lose if you run out of lives.

---

## How to run

1. Install the `requests` module if not already installed:
   ```bash
   pip install requests
