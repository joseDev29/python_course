from utils import *


def main():
    perfumery_section_generator = get_numbers_generator()
    pharmacy_section_generator = get_numbers_generator()
    cosmetics_section_generator = get_numbers_generator()

    exit_program = False

    while not exit_program:

        print("\nWelcome to PyShop\n")

        print('''Sections:
            [ 1 ] : Perfumery
            [ 2 ] : Pharmacy
            [ 3 ] : Cosmetics
        \n''')

        selected_section = input_number("Input a section option: ")

        if selected_section is None or int(selected_section) not in range(1, 4):
            print("Error: Invalid option")
            continue

        match int(selected_section):
            case 1:
                generate_turn(perfumery_section_generator, 'PF')
            case 2:
                generate_turn(pharmacy_section_generator, 'PH')
            case 3:
                generate_turn(cosmetics_section_generator, 'CO')

        take_new_turn = input("\nYou want to take a new turn? (Enter 's' if yes if): ").strip().lower()

        if take_new_turn != 's':
            exit_program = True

    print("\nBye!")


main()

