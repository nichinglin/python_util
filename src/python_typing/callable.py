from typing import Callable


# Define a function that takes two integers and returns their sum
def add(x: int, y: int) -> int:
    return x + y


# Define a function that takes another function as an argument
def apply_operation(operation: Callable[[int, int], int], x: int, y: int) -> int:
    return operation(x, y)


# Call the apply_operation function with the add function
result = apply_operation(add, 10, 20)
print("Result of applying add function:", result)  # Output: 30


def f(a: int) -> str:
    return str(a)


def test(a: int, func: Callable[[int], str]) -> str:
    return func(a)


print(test(1, f))
