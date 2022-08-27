# noinspection PyBroadException
try:
    pass  # Code to test
except:
    pass  # In error case
else:
    pass  # In not error case
finally:
    pass  # It is always executed


try:
    pass
except NotImplementedError:
    pass


try:
    pass
except NotImplementedError as error:
    pass


try:
    pass
except NotImplementedError:
    pass
except ValueError as value_error:
    pass
except TypeError:
    pass


def add():
    n1 = int(input("Input number 1: "))
    n2 = int(input("Input number 2: "))
    print(n1 + n2)


try:
    add()
except:
    print("Ops, error!")
else:
    print("Good execution!")
finally:
    print("Bye!")


try:
    add()
except ValueError as value_error:
    print(type(value_error))
    print(value_error.args)
except TypeError as type_error:
    print(type(type_error))
    print(type_error.args)
except NotImplementedError:
    print("Ops, not implemented")

