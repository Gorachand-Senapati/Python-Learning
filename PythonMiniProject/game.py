import random

easy_words = ["cat", "dog", "sun", "tree", "book", "apple", "ball", "fish", "hat", "car"]

medium_words = ["python", "guitar", "mountain", "computer", "elephant", "bicycle", "diamond", "jungle", "puzzle", "rocket"]

hard_words = ["xylophone", "quasar", "wombat", "juxtaposition", "gobbledygook", "lollypop", "mnemonic", "serendipity", "ephemeral", "ubiquitous"]

print("Welcome to the Word Guessing Game!")
print("Choose a difficulty level: easy, medium or hard")

level = input("Enter difficulty: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("this is not dificulty choose any : default is easy")
    secret = random.choice(easy_words)

attempts = 0
print("\n Guess the secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congrats you guess write in {attempts} attermpts.")
        break
    
    hint =""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint+= guess[i]
        else:
            hint += "_"

    print("Hint: ", hint)

print("Game over! The secret password was:", secret)