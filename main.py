#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  guesses = 10
  print(f"You have {guesses} guesses.")
elif difficulty == 'hard':
  guesses = 5
  print(f"You have {guesses} guesses.")
  
random_number = random.randrange(101)
continue_game = True

while continue_game:
  guess = int(input("Guess a number between 1 and 100: "))
  # if str("") or "" or float(""):
  #   print("You must enter an integer between 1 and 100. Try again")
  #   guess
  if guess < random_number:
    guesses -= 1
    print(f"You guessed too low. You have {guesses} guesses left.")
    if guesses == 0:
      print("You ran out of guesses, you lose.")
      print(f"The number was: {random_number}")
      continue_game = False
    guess
  elif guess > random_number: 
    guesses -= 1
    print(f"You guessed too high. You have {guesses} guesses left.")
    if guesses == 0:
      print("You ran out of guesses, you lose.")
      print(f"The number was: {random_number}")
      continue_game = False
    guess
  else:
    print(f"You guessed the correct number: {random_number}, well done!")
    continue_game = False