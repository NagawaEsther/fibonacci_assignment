
def fibonacci(n: int) -> int:
    # Handle invalid input
    if n < 0:
        raise ValueError("Input cannot be negative")
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Calculate Fibonacci iteratively
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Print first 11 Fibonacci numbers when running directly
if __name__ == "__main__":
    for i in range(11):
        print(f"fibonacci({i}) = {fibonacci(i)}")
