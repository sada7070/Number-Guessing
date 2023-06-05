haimport random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between a number between 1 and 100.")

ANSWER = random.randint(1,100)
EASY_LVL_TURNS=10
HARD_LVL_TURNS=5
turns = 0

def defficulty():
  level=input("choose a difficulty.Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LVL_TURNS
  else:
    return HARD_LVL_TURNS



def number_guessing():
  guess=int(input("Make a guess: "))
  if guess > ANSWER:
    print("Too high \nGuess again")
    global turns
    turns-=1
  elif guess < ANSWER:
    print("Too low \nGuess again")
    turns-=1
  else:
    print(f"You got it! the answer was {ANSWER}.")
    turns=-1

turns=defficulty()

while turns > 0:
  print(f"You have {turns} attempts remaining to guess the number.")
  number_guessing()
if turns==0:
  print("You've run out of guesses. You lose.")
elif turns == -1:
  exit
  
  