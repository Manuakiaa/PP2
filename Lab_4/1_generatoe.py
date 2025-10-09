def square_numbers(upper_bound):
    upper_bound = max(1, upper_bound)
    for i in range(1, upper_bound + 1):
        yield i ** 2


def even_numbers(upper_bound):
    upper_bound = max(0, upper_bound)
    for i in range(0, upper_bound + 1, 2):
        yield i


def magic_numbers(upper_bound):
    upper_bound = max(0, upper_bound)
    for i in range(0, upper_bound + 1):
        if i % 12 == 0:
            yield i


def range_square(lower_bound, upper_bound):
    upper_bound = max(lower_bound, upper_bound)
    for i in range(lower_bound, upper_bound + 1):
        yield i ** 2


def decrease_numbers(upper_bound, lower_bound=0):
    upper_bound = max(lower_bound, upper_bound)
    for i in range(upper_bound, lower_bound - 1, -1):
        yield i


if __name__ == "__main__":
    n = int(input("Enter a number for squares: "))
    print(*square_numbers(n), sep=", ")

    n = int(input("Enter a number for even numbers: "))
    print(*even_numbers(n), sep=", ")

    n = int(input("Enter a number for magic numbers (divisible by 3 and 4): "))
    print(*magic_numbers(n), sep=", ")

    a, b = map(int, input("Enter two numbers (a b) for squares in range: ").split())
    print(*range_square(a, b), sep=", ")

    a, b = map(int, input("Enter two numbers (upper lower) for decreasing numbers: ").split())
    print(*decrease_numbers(a, b), sep=", ")
