import calculations

if __name__ == "__main__":
    A = [["t", "2*t", "3t"], ["1", "t^2 + 3", "sqrt(t)"]]
    b = [1, 2]

    print(calculations.omega(A, b, 1))
    print(calculations.solution(A, b, 1))
    print(calculations.precision(A, b, 1))
