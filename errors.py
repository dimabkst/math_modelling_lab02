class Error(Exception):
    def __str__(self) -> str:
        return 'Program aborted\n'


class BadMatrixEquationDimensionsError(Exception):
    def __str__(self):
        return super().__str__() + f"To solve system we need A.rows = b.rows."


class NoNameError(Error):
    def __init__(self, e):
        self.e = e

    def __str__(self) -> str:
        return f'{self.e}'
