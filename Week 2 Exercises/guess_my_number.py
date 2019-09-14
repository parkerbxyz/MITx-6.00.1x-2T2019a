print("Please think of a number between 0 and 100!")

low = 0.0
high = 100.0
guess = (high + low) // 2

while True:
    print("Is your secret number {}?".format(guess))
    print("Enter 'h' to indicate the guess is too high. "
          "Enter 'l' to indicate the guess is too low. "
          "Enter 'c' to indicate I guessed correctly. ", end='')
    response = input()
    if response == 'h':
        high = guess
    elif response == 'l':
        low = guess
    elif response == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
    guess = (high + low) // 2

print("Game over. Your secret number was: {}".format(guess))
