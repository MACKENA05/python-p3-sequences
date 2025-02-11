def print_fibonacci(length):
    if length <= 0:
        print("[]")
        return 

    elif length == 1:
       print([0])
       return

    elif length == 2:
        print([0, 1])
        return

    sequence = [0, 1]

    for i in range(2, length):
        next_fib = sequence[-1] + sequence[-2]
        sequence.append(next_fib)

    print(sequence[:length])

# Example usage:
print(print_fibonacci(0))