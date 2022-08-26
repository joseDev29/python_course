from pathlib import Path
from typing import List


def press_enter_to_continue():
    input("\nPress 'enter' to continue")


def get_categories(path: Path) -> List[str]:
    return [path_item.name for path_item in path.iterdir() if path_item.is_dir()]


def get_recipes_by_category_name(path: Path, category_name: str) -> List[str]:
    category_path = Path(path, category_name)
    return [item_path.stem for item_path in category_path.glob('*.txt')]


def is_category_empty(path: Path, category_name: str) -> bool:
    return len(get_recipes_by_category_name(path, category_name)) == 0


def print_all_recipe_book(path: Path):
    print("\nYou currently have in your recipe book\n")

    for category in get_categories(path):
        print(f"- {category}:")
        for recipe in get_recipes_by_category_name(path, category):
            print(f"\t- {recipe}")


def input_selectable_list(select_list: List[str], label: str, return_index: bool = False) -> str | int:
    print(f"\n{label}\n")

    for index, item in enumerate(select_list):
        print(f"\t[ {index + 1} ] : {item}")

    selected_value = ''

    while not selected_value:
        input_value = input(f"\nPlease enter the number of the option you want to select: ")

        if input_value.isnumeric() and int(input_value) in range(1, len(select_list) + 1):
            selected_value = select_list[int(input_value) - 1] if not return_index else int(input_value) - 1
            break

        print(f"Error: Input value must be a number between 1 and {len(select_list)}")

    return selected_value


def select_category(path: Path) -> str:
    return input_selectable_list(
        get_categories(path), "Please enter the number of the category you want to select:"
    )


def select_recipe(path: Path, category: str) -> str:
    return input_selectable_list(
        get_recipes_by_category_name(path, category),
        "Please enter the number of the recipe you want to select:"
    )


def create_category(path: Path):
    category_name: str = input("\n Input category name: ").strip().capitalize()
    new_category_path = Path(path, category_name)
    new_category_path.mkdir()
    print("\nCategory created success!")


def delete_category(path: Path):
    selected_category: str = select_category(path)
    category_path = Path(path, selected_category)
    for recipe_path in category_path.glob('*.*'):
        recipe_path.unlink()
    category_path.rmdir()
    print("\nCategory deleted success!")


def read_recipe(path: Path):
    selected_category: str = select_category(path)
    if is_category_empty(path, selected_category):
        print("Ops!, category empty")
        return
    selected_recipe: str = select_recipe(path, selected_category)
    recipe_file = open(Path(path, selected_category, selected_recipe + '.txt'))
    print(f"\n{selected_recipe}")
    print(f"\t{recipe_file.read()}\n")
    recipe_file.close()


def create_recipe(path: Path):
    selected_category: str = select_category(path)
    recipe_name = input("Input recipe name: ").strip().capitalize()
    recipe_content = input("Input recipe: ").strip().capitalize()
    new_file = open(Path(path, selected_category, recipe_name + '.txt'), "w")
    new_file.write(recipe_content)
    new_file.close()
    print("\nRecipe created success!")


def delete_recipe(path: Path):
    selected_category: str = select_category(path)
    if is_category_empty(path, selected_category):
        print("Ops!, category empty")
        return
    selected_recipe: str = select_recipe(path, selected_category)
    recipe_path = Path(base_path, selected_category, selected_recipe + '.txt')
    recipe_path.unlink()
    print("\nRecipe deleted success!")


base_path = Path(Path.home() / 'Recetas')

print('Welcome to Recipe book!\n')

print("Your recipe book is stored in the following path: ")
print(f"\t{base_path}")

print_all_recipe_book(base_path)

menu_options = [
    'Read recipe', 'Create recipe', 'Delete recipe',
    'Create category', 'Delete category', 'View all recipe book', 'Exit'
]

exit_program = False

while not exit_program:
    selected_menu_option = input_selectable_list(menu_options, label="Select a option:", return_index=True)

    match selected_menu_option:
        case 0:
            read_recipe(base_path)
        case 1:
            create_recipe(base_path)
        case 2:
            delete_recipe(base_path)
        case 3:
            create_category(base_path)
        case 4:
            delete_category(base_path)
        case 5:
            print_all_recipe_book(base_path)
        case 6:
            exit_program = True

    if selected_menu_option != 6:
        press_enter_to_continue()

print("\nBye!")
