from fractions import Fraction

while True:
    try:
        # Input matrix x
        x_input = input("Enter matrix x (space-separated numbers): ")
        x = [Fraction(num) for num in x_input.split()]
        
        # Input matrix y
        y_input = input("Enter matrix y (space-separated numbers): ")
        y = [Fraction(num) for num in y_input.split()]
        
        if len(x) != len(y):
            print("Matrices must have the same length.")
            continue
        
        # Input scalars a and b
        ab_input = input("Enter a and b (space-separated): ")
        a, b = [Fraction(num) for num in ab_input.split()]
        
        # Compute a*x + b*y and format as strings
        result = []
        for xi, yi in zip(x, y):
            res = a * xi + b * yi
            if res.denominator == 1:
                result.append(str(res.numerator))
            else:
                result.append(f"{res.numerator}/{res.denominator}")
        
        # Output the result
        print("Result:", result)
        
        # Ask to continue
        cont = input("Continue? (y/n): ").strip().lower()
        if cont != 'y':
            break
    except ValueError:
        print("Invalid input. Please enter numbers correctly.")