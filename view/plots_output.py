from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import sympy


class plots_output:

    def __init__(self, root, frame_column_row):

        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white", borderwidth=5, relief='raised')
        s.configure("WhiteBg.TFrame", background="white")
        s.configure("WhiteBg.TLabel", background="white")

        self.omega_plot_output_frame = ttk.Frame(root, padding="3 3 12 12", style="TopWhiteBg.TFrame")
        self.omega_plot_output_frame.grid(column=frame_column_row[0], row=frame_column_row[1], sticky=(N, W, E, S))

        self.align_rows_cols(self.omega_plot_output_frame)

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)

    def receive_data_and_show_plot(self, omega, solution, T):
        # Cleaning everything that was before
        for child in self.omega_plot_output_frame.winfo_children():
            child.destroy()

        if omega and 2 <= len(list(omega)[0]) <= 3:
            t = sympy.symbols('t')
            if len(list(omega)[0]) == 2:
                omega_plot = sympy.plot_parametric(show=False)
                for el in omega:
                    omega_plot.extend(sympy.plot_parametric((el[0], el[1]), (t, 0, T), show=False))
                solution_plot = sympy.plot_parametric((solution[0], solution[1]), (t, 0, T), show=False)

            else:  # == 3
                omega_plot = sympy.plotting.plot3d_parametric_line(show=False)
                for el in omega:
                    omega_plot.extend(sympy.plotting.plot3d_parametric_line(el[0], el[1], el[2], (t, 0, T), show=False))
                solution_plot = sympy.plotting.plot3d_parametric_line(solution[0], solution[1], solution[2], (t, 0, T),
                                                                      show=False)

            omega_plot.show()
            solution_plot.show()

        else:
            ttk.Label(self.omega_plot_output_frame, text="Графік Ωxt можна вивести лише при n = 2 або n = 3",
                      style="WhiteBg.TLabel").grid(column=0, row=0, sticky=(N, W, E, S))
