def woof(number_of_woofs):
    for i in range(number_of_woofs):
        print('Woof! ' * number_of_woofs)


def greeting(name: str):
    print(f'Hello, {name}')


def double_plus_num(num1: int, num2: int=1) -> int:  # type hints
    return num1 * 2 + num2


def shopping(name, *items, shout=False):   # multiargs
    if shout:
        name = name.upper()
    for item in items:
        print(f'{name}!, Don\'t forget {item}')


def add_user():
    """
    Create a new user.
    Prompt for name and e-mail address,
    Store in database.
    """
    pass


add