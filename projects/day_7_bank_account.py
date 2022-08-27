class Person:

    def __init__(self, name:str, lastname: str):
        self.name = name
        self.lastname = lastname


class Client(Person):

    def __init__(self, name: str, lastname: str, account: str, balance: float):
        super().__init__(name, lastname)
        self.account = account
        self.balance = balance

    def deposit(self, amount: float):
        self.balance = round(self.balance + amount, 2)
        print("Deposit success!")

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance = round(self.balance - amount, 2)
            print("Withdraw success!")
            return
        print("Error: Amount exceeds your account balance")

    def print_info(self):
        print(self)

    def __str__(self):
        return f'Client( name="{self.name}", lastname="{self.lastname}", ' \
               f'account="{self.account}", balance={self.balance} ) '


def press_enter_to_continue():
    input("\nPress 'enter' to continue\n")


def input_number(label: str) -> int | float | None:
    entered_value = input(label).strip()
    if entered_value.isnumeric():
        return int(entered_value)
    try:
        return float(entered_value)
    except ValueError:
        return None


def create_client() -> Client:
    name = input("Input name: ").strip().capitalize()
    lastname = input("Input lastname: ").strip().capitalize()
    account = input("Input account number: ")

    new_client = Client(name=name, lastname=lastname, account=account, balance=0)

    print("Client created success!")

    return new_client


def client_transaction(client: Client, transaction: str):
    amount = input_number("Input amount: ")

    if amount is None:
        print("Error: Invalid amount")
        return

    match transaction:
        case 'deposit':
            client.deposit(float(amount))
        case 'withdraw':
            client.withdraw(float(amount))


def main():
    print("Welcome to PyBank!")

    print("You must first become a client of our bank\n")

    created_client = create_client()

    exit_program = False

    while not exit_program:

        print('''
        Actions:
            - [ 1 ] : Deposit
            - [ 2 ] : Withdraw
            - [ 3 ] : View my info
            - [ 4 ] : Exit
        ''')

        selected_option = input_number("Input option number: ")

        if selected_option is None or int(selected_option) not in range(1, 5):
            print("Error: invalid option")
            continue

        match int(selected_option):
            case 1:
                print("\nDeposit: ")
                client_transaction(created_client, 'deposit')
            case 2:
                print("\nWithdraw: ")
                client_transaction(created_client, 'withdraw')
            case 3:
                print("\n")
                created_client.print_info()
            case 4:
                exit_program = True

        if int(selected_option) != 4:
            press_enter_to_continue()

    del created_client

    print("\nBye!")


main()





