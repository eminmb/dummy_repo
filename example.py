import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class FibonacciCalculator:
    def __init__(self):
        self.memo = {}
        logging.info("FibonacciCalculator initialized with an empty memoization dictionary.")

    def recursive_fibonacci(self, n):
        logging.debug(f"Calculating Fibonacci number for n={n} using recursion with memoization.")
        if n < 0:
            logging.error("Negative input is not allowed.")
            raise ValueError("Fibonacci number is not defined for negative numbers")
        if n in (0, 1):
            return n
        if n in self.memo:
            logging.debug(f"Returning memoized value for n={n}.")
            return self.memo[n]
        logging.debug(f"Computing Fibonacci for n={n} by recursion.")
        result = self.recursive_fibonacci(n - 1) + self.recursive_fibonacci(n - 2)
        self.memo[n] = result
        return result

    def iterative_fibonacci(self, n):
        logging.debug(f"Calculating Fibonacci number for n={n} using iteration.")
        if n < 0:
            logging.error("Negative input is not allowed.")
            raise ValueError("Fibonacci number is not defined for negative numbers")
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
            logging.debug(f"i={i}: a={a}, b={b}")
        return a

# Example usage
if __name__ == "__main__":
    calc = FibonacciCalculator()
    try:
        number = 10
        print(f"Recursive Fibonacci of {number} is {calc.recursive_fibonacci(number)}")
        print(f"Iterative Fibonacci of {number} is {calc.iterative_fibonacci(number)}")
    except ValueError as e:
        logging.exception("An error occurred.")
