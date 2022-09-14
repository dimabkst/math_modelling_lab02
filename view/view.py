from tkinter import *
from tkinter import ttk
from .system_input import system_input
from .solve_button import solve_button
from .results_output import results_output
from .plots_output import plots_output


class View:

    def __init__(self):
        try:
            self.root = Tk()
            self.root.configure(bg="white")
            self.root.title("Математичне моделювання. Лабораторна робота №2")

            self.frames_columns_rows = {"system_input": [0, 0],
                                        "solve_button": [0, 1],
                                        "results_output": [0, 2],
                                        "omega_plot_output": [0, 3],
                                        }

            self.system_input = system_input(self.root, self.frames_columns_rows["system_input"])
            self.solve_button = solve_button(self.root, self.frames_columns_rows["solve_button"], self)
            self.results_output = results_output(self.root, self.frames_columns_rows["results_output"])
            self.plots_output = plots_output(self.root, self.frames_columns_rows["omega_plot_output"])

            self.align_rows_cols(self.root)

            self.root.mainloop()
        except Exception as e:
            raise e

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
