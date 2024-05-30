import numpy as np
import matplotlib.pyplot as plt

def add_numbers(x, y):
    """Add two numbers and return the result."""
    return x + y

def compute_log_base2(value):
    """Compute the base-2 logarithm of a value."""
    return np.log2(value)

def main():
    # User input
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Computation
    z = add_numbers(x, y)
    if z <= 0:
        print("The sum must be greater than zero to compute the log base 2.")
        return

    log_z = compute_log_base2(z)
    
    # Output
    print(f"The sum of {x} and {y} is {z}")
    print(f"The base-2 logarithm of {z} is {log_z:.4f}")
    
    # Visualization
    values = np.linspace(1, z, 100)
    log_values = np.log2(values)
    
    plt.plot(values, log_values, label='log2(x)')
    plt.xlabel('Value')
    plt.ylabel('Log base 2')
    plt.title('Log base 2 Function')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()