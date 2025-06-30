import random

def main():
  again = 'y'

  while again == 'y':
    again = guess()
  

def guess():
  ATTEMPT_LIMIT = 5
  guess_number = 0
  attempts = 0
  what_number = random.randint(1,10)

  print('Guess the number between 1 to 100')

  while int(guess_number) != what_number and attempts < 3:
    guess_number = input('Number: ')
    attempts += 1

  if attempts < 3:
    print(f'Congratulation!!! The number is {what_number}')
  else:
    print(f"Game over, the number was {what_number}")

  return input("\n Do you want to play again? y/n: ")

main()