from typing import Generator

# Typing generator: Generator[yield_type, send_type, return_type]


def get_squares(limit: int) -> Generator[int, None, None]:
    for n in range(1, limit + 1):
        yield n**2


generator = get_squares(3)

print(next(generator))  # out: 1
print(next(generator))  # out: 4
print(next(generator))  # out: 9
# print(next(generator))  # out: Error


def fibonacci() -> Generator[int, None, None]:
    prev = 0
    curr = 1

    yield prev + curr

    while True:
        result = prev + curr
        prev = curr
        curr = result
        yield result


fibonacci_generator = fibonacci()

for i in range(0, 17):
    print(f"Fibonacci: {next(fibonacci_generator)}")

fibonacci_generator.close()
