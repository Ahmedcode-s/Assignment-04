import random
words = ['apple','mango','orange','banana','stawberry']

word = random.choice(words)
guessed_letter = []
attempts = 6

print("Lets play Hangman!")
print("_" * len(word))

while attempts > 0:
    guess = input("\n Guess the letter in this fruit: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("write one alphabet only!")
        continue
    if guess in guessed_letter:
        print("This letter is already guessed chose another letter.")
        continue
    guessed_letter.append(guess)

    if guess in word:
        print("Correct! guess")
    else:
        attempts -= 1
        print(f"Wrong! {attempts} attempts left")

    displayed_word = " ".join([letter if letter in guessed_letter else "_" for letter in word])
    print(displayed_word)

    if "_" not in displayed_word:
        print(f"Congratulations! You have guessed word: {word}")
        break
else:print(f"Game over! the correct word was: {word}")