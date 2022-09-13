import calculations

if __name__ == "__main__":
    A = [["t", "2*t", "3t"], ["1", "t^2 + 3", "sqrt(t)"]]
    b = [1, 2]

    res = calculations.all(A, b, 1)
    print(res["omega"], res["solution"], res["precision"], sep='\n')
