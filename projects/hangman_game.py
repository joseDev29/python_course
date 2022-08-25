from typing import List, Set
import random

print("Hello to Hangman game!\n")

words: List[str] = ['house', 'planet', 'car', 'work', 'school', 'super']
random_word: str = random.choice(words)


def generate_progress_string(word: str, progress: Set[str]) -> str:
    list_result = [char if char in progress else '-' for char in word]
    return ''.join(list_result).capitalize()


def calculate_attempts(word: str) -> int:
    return len(word) + round(len(word) / 2) + 1


def is_completed(word: str, progress: Set[str]) -> bool:
    return len(set(word)) == len(progress)


attempts: int = calculate_attempts(random_word)
round_progress: Set[str] = set()
incorrect_inputs: Set[str] = set()

while attempts:
    print(generate_progress_string(random_word, round_progress))
    print(f"Attempts: {attempts}")

    if len(incorrect_inputs):
        print(f"Incorrect entered letters: {', '.join(incorrect_inputs)}")

    entered_letter = input("Input a letter: ")[0].strip().lower()

    if entered_letter in random_word:
        round_progress.add(entered_letter)
    else:
        incorrect_inputs.add(entered_letter)
        attempts -= 1

    if is_completed(random_word, round_progress):
        print('Congratulations!')
        print(f"Word is: {random_word.capitalize()}")
        break

    if attempts == 0:
        print("Ops! Failed")
        print(f"Word is: {random_word.capitalize()}")

    print("\n")
