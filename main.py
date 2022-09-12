from calculations import omega

if __name__ == "__main__":
    A = [["t", "2*t", "3t"], ["1", "t^2 + 3", "sqrt(t)"]]
    b = [1, 2]

    print(omega.omega(A, b, 1))
