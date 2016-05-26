"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position == 0:
        return 0
    def next_fib(first, second, counter):
        first, second = second, first + second
        if counter == position:
            return first
        else:
            counter += 1
            return next_fib(first, second, counter)
    return next_fib(0, 1, 1)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)