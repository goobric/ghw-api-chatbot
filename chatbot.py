import random

print("Hello! I am the Guess My Number chat bot. Let's play a game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

while guess != number:
    if guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Take another guess: "))
    tries += 1

print("Congratulations! You guessed the number in", tries, "tries.")
