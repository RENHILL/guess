import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = input("Угадайте число от 1 до 100: ")
    guess = int(guess)

    if guess == number:
        print("Вы угадали число!")
    elif guess < number:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
