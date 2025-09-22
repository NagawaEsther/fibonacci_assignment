
def fibonacci(n: int) -> int:
    """
    Return the nth Fibonacci number.
    Fibonacci sequence starts with:
    0, 1, 1, 2, 3, 5, 8, ...
    """
    if n < 0:
        raise ValueError("Input cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
