WORD = "SNAKE"

for guess_num in range(1, 7):
  guess = input(f"\nGuess {guess_num}: ").upper()

  if guess == "WORD":
    print("Correct")
    break # Ends the wordle when the user guesses the word.
  else:
    print("Wrong")

    comprehension_set = {letter for letter, correct in zip(guess, WORD) if letter == correct}
    print(comprehension_set)