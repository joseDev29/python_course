import random

print("Hello to Guess th number!\n")

username = input("Input name: ").strip()

random_number = random.randint(1, 100)

total_attempts = 8
attempts = total_attempts

print(f"\nHi {username}, I have thought of a number between 1 and 100, try to guess it")
print(f"You have {attempts} attempts\n")

while attempts:
    attempts -= 1
    entered_number = int(input("What number do you think it is?: "))

    if entered_number not in range(1, 101):
        print("Invalid number, the value must be between 1 and 100")
    elif entered_number < random_number:
        print("Ops! You entered a lower number")
    elif entered_number > random_number:
        print("Ops! You have entered a higher number")
    elif entered_number == random_number:
        print(f"Congratulations, you have guessed the number! {random_number}")
        print(f"It took you {total_attempts - attempts} tries to guess it")
        break

    if attempts > 0:
        print(f"You have {attempts} attempts left\n")
        continue

    print(f"You have no more attempts left, the correct number is {random_number}")
