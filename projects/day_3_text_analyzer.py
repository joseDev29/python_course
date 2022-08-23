from functools import reduce


def input_text(description):
    return input(description).strip()


# how many times each letter appears
def get_match_count(text, letter):
    # def iterator(acc, char):
    #    if char.lower() == letter.lower():
    #        return acc + 1
    #    return acc
    # return reduce(iterator, list(text), 0)
    return reduce(lambda acc, char: acc + 1 if char.lower() == letter.lower() else acc, list(text), 0)


text_entered = input_text("Input text: ")
letters_input = [input_text("Letter 1: "), input_text("Letter 2: "), input_text("Letter 3: ")]

results = {}

for letter_item in letters_input:
    if results.get('How many times each letter appears') is None:
        results['How many times each letter appears'] = {}
    # results['How many times each letter appears'][letter_item] = get_match_count(text_entered, letter_item)
    results['How many times each letter appears'][letter_item] = text_entered.lower().count(letter_item.lower())

results['Total words'] = len(text_entered.split(' '))
results['First and last letter'] = {'first': text_entered[0], 'last': text_entered[-1]}
results['Words in reverse order'] = ' '.join(reversed(text_entered.split(' ')))
# results['Apper "python" word'] = 'Yes' if text_entered.lower().find('python') != -1 else 'No'
results['Apper "python" word'] = 'Yes' if 'python' in text_entered.lower() else 'No'

print("<----- Results ----->")
for result in results.items():
    print(f'{result[0]}: {result[1]}')
