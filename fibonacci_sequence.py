def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with first two terms

    # Generate Fibonacci sequence up to n terms
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence[:n]  # Return the first n terms


def main():
    # Prompt user for the number of terms
    while True:
        try:
            n = input("Enter the number of terms in the Fibonacci sequence (e.g., 10): ")
            n = int(n)
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate and display Fibonacci sequence
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence with", n, "terms:", fibonacci_sequence)


if __name__ == "__main__":
    main()
