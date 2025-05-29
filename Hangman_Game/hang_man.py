import random
import requests
import hangman_visual as hg
res=requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
words=res.text.splitlines()
display=[]
chosen_word=random.choice(words)
# print(chosen_word)
for letter in chosen_word:
    display+='_'
print(display)
lives=6
game_over=False
while not game_over:
    guess_letter= input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess_letter:
            display[position]=letter
    print(display)
    if guess_letter not in chosen_word:
        lives-=1
        if lives ==0:
            game_over=True
            print("YOu Lose!")
            print(f"The Given word is {chosen_word}")
    if '_' not in display:
        game_over=True
        print("You Win!!")
        print(f"The Given word is {chosen_word}")
    print(hg.hangman_stages[lives])

