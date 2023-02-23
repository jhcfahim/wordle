import pathlib
import random

WORDLIST = pathlib.Path("wordlist.txt")

words = [
  word.upper()
  for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n")
]
word = random.choice(words)

print("Testing secret word: ", word) # testing purposes only, delete later

for guess_num in range(1, 6): # gives the user 5 guesses
  guess = input(f"\nGuess {guess_num}: ").upper()

  if guess == word:
    print("Correct")
    break  # ends the wordle when the user guesses the word.
  else:
    print("Wrong")

    # tells the user which letters are correct, misplaced, and wrong
    correct_letters = {
      letter
      for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

else:
  print(f"The word was {word}")