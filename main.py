import random


def play_guessing_game():
    print("Welcome to the Guess game")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts=8
    #while attempts<9:
    for attempts in range(0, max_attempts):
        guess = int(input("Take any guess"))
        attempts += 1
        if guess < secret_number:
            print("too low")
        elif guess > secret_number:
            print("too high")
        elif guess == secret_number:
            print(f"Congratulation, you guessed the number in {attempts} attempts")
            break
        else:
            print("anything")


play_guessing_game()
