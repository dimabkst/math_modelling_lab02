from tkinter import *
from tkinter import ttk

MAX_DEFAULT_VALUE = 7 + 1
COMBOBOX_WIDTH = 3
ENTRY_WIDTH = 10


class system_input:

    def __init__(self, root, frame_column_row):

        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white", borderwidth=5, relief='raised')
        s.configure("WhiteBg.TFrame", background="white")
        s.configure("WhiteBg.TLabel", background="white")

        # Frames
        self.system_input_frame = ttk.Frame(root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.system_input_frame.grid(column=frame_column_row[0], row=frame_column_row[1], sticky=(N, W, E, S))

        self.equation_frame = ttk.Frame(self.system_input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
        self.equation_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.matrix_shape_input_frame = ttk.Frame(self.system_input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
        self.matrix_shape_input_frame.grid(column=0, row=1, sticky=(N, W, E, S))

        self.T_input_frame = ttk.Frame(self.system_input_frame, style="WhiteBg.TFrame", padding="3 3 12 12")
        self.T_input_frame.grid(column=1, row=1, sticky=(N, W, E, S))

        self.matrix_input_frame = ttk.Frame(self.system_input_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.matrix_input_frame.grid(column=0, row=2, sticky=(N, W, E, S))

        self.vector_b_input_frame = ttk.Frame(self.system_input_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.vector_b_input_frame.grid(column=1, row=2, sticky=(N, W, E, S))
        #

        # Equation output
        ttk.Label(self.equation_frame, text="T", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=S)
        ttk.Label(self.equation_frame, text="∫", style="WhiteBg.TLabel") \
            .grid(column=0, row=1, sticky=(N, W, E, S))
        ttk.Label(self.equation_frame, text="0", style="WhiteBg.TLabel") \
            .grid(column=0, row=2, sticky=N)
        ttk.Label(self.equation_frame, text="A(t)x(t)dt = b, ",
                  style="WhiteBg.TLabel").grid(column=1, row=1, sticky=W)
        ttk.Label(self.equation_frame, text="x(t) ∈ Rn, b ∈ Rm, A(t) - (m x n) - вимірна матриця",
                  style="WhiteBg.TLabel").grid(column=3, row=1, sticky=E)
        #

        # Shapes input
        self.matrix_shape_input_label_frame = ttk.Frame(self.matrix_shape_input_frame, padding="3 3 12 12",
                                                        style="WhiteBg.TFrame")
        self.matrix_shape_input_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))

        self.matrix_shape_input_m_frame = ttk.Frame(self.matrix_shape_input_frame, padding="3 3 12 12",
                                                    style="WhiteBg.TFrame")
        self.matrix_shape_input_m_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.matrix_shape_input_x_frame = ttk.Frame(self.matrix_shape_input_frame, padding="3 3 12 12",
                                                    style="WhiteBg.TFrame")
        self.matrix_shape_input_x_frame.grid(column=2, row=0, sticky=(N, W, E, S))

        self.matrix_shape_input_n_frame = ttk.Frame(self.matrix_shape_input_frame, padding="3 3 12 12",
                                                    style="WhiteBg.TFrame")
        self.matrix_shape_input_n_frame.grid(column=3, row=0, sticky=(N, W, E, S))

        self.matrix_row_shape_var = StringVar()
        self.matrix_row_shape_var.set("3")
        matrix_row_shape_combobox = ttk.Combobox(self.matrix_shape_input_m_frame, width=COMBOBOX_WIDTH,
                                                 textvariable=self.matrix_row_shape_var,
                                                 values=[f'{i}' for i in range(1, MAX_DEFAULT_VALUE)])
        matrix_row_shape_combobox.bind('<<ComboboxSelected>>', self.change_and_show_matrix)

        self.matrix_col_shape_var = StringVar()
        self.matrix_col_shape_var.set("3")
        matrix_col_shape_combobox = ttk.Combobox(self.matrix_shape_input_n_frame, width=COMBOBOX_WIDTH,
                                                 textvariable=self.matrix_col_shape_var,
                                                 values=[f'{i}' for i in range(1, MAX_DEFAULT_VALUE)])
        matrix_col_shape_combobox.bind('<<ComboboxSelected>>', self.change_and_show_matrix)

        ttk.Label(self.matrix_shape_input_label_frame, text="Розміри A(t) (m x n):", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=W)
        matrix_row_shape_combobox.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.matrix_shape_input_x_frame, text="x", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, W, E, S))
        matrix_col_shape_combobox.grid(column=0, row=0, sticky=(N, W, E, S))
        #

        # T input
        self.T_input_label_frame = ttk.Frame(self.T_input_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.T_input_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.T_input_T_frame = ttk.Frame(self.T_input_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.T_input_T_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.T_var = StringVar()
        self.T_var.set("1")
        ttk.Label(self.T_input_label_frame, text="T =", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=W)
        ttk.Entry(self.T_input_T_frame, width=ENTRY_WIDTH, textvariable=self.T_var).grid(column=0, row=0,
                                                                                         sticky=(N, E, W, S))
        #

        # Matrix vars and entries
        self.matrix_input_label_frame = ttk.Frame(self.matrix_input_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.matrix_input_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.matrix_input_matrix_frame = ttk.Frame(self.matrix_input_frame, padding="3 3 12 12", style="WhiteBg.TFrame")
        self.matrix_input_matrix_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.vector_b_input_label_frame = ttk.Frame(self.vector_b_input_frame, padding="3 3 12 12",
                                                    style="WhiteBg.TFrame")
        self.vector_b_input_label_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.vector_b_input_vector_frame = ttk.Frame(self.vector_b_input_frame, padding="3 3 12 12",
                                                     style="WhiteBg.TFrame")
        self.vector_b_input_vector_frame.grid(column=1, row=0, sticky=(N, W, E, S))

        self.matrix_vars = []
        self.matrix_entries = []
        self.vector_b_vars = []
        self.vector_b_entries = []

        for i in range(int(self.matrix_row_shape_var.get() or 0)):
            self.matrix_vars.append([])
            self.matrix_entries.append([])

            for j in range(int(self.matrix_col_shape_var.get() or 0)):
                self.matrix_vars[i].append(StringVar())
                self.matrix_vars[i][j].set("0")

                self.matrix_entries[i].append(ttk.Entry(self.matrix_input_matrix_frame, width=ENTRY_WIDTH,
                                                        textvariable=self.matrix_vars[i][j]))
                self.matrix_entries[i][j].grid(row=i, column=j, sticky=(N, W, E, S))

            self.vector_b_vars.append(StringVar())
            self.vector_b_vars[i].set("0")

            self.vector_b_entries.append(ttk.Entry(self.vector_b_input_vector_frame, width=ENTRY_WIDTH,
                                                   textvariable=self.vector_b_vars[i]))
            self.vector_b_entries[i].grid(row=i, column=0, sticky=(N, W, E, S))

        ttk.Label(self.matrix_input_label_frame, text="A(t) =", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))
        ttk.Label(self.vector_b_input_label_frame, text="b =", style="WhiteBg.TLabel") \
            .grid(column=0, row=0, sticky=(N, E, W, S))
        #

        # Aligns
        self.align_rows_cols(self.matrix_shape_input_label_frame)
        self.align_rows_cols(self.matrix_shape_input_m_frame)
        self.align_rows_cols(self.matrix_shape_input_x_frame)
        self.align_rows_cols(self.matrix_shape_input_n_frame)

        self.align_rows_cols(self.T_input_label_frame)
        self.align_rows_cols(self.T_input_T_frame)

        self.align_rows_cols(self.matrix_input_label_frame)
        self.align_rows_cols(self.matrix_input_matrix_frame)

        self.align_rows_cols(self.vector_b_input_vector_frame)
        self.align_rows_cols(self.vector_b_input_label_frame)

        self.align_rows_cols(self.system_input_frame)
        #

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)

    def get_matrix(self):
        try:
            return [[str(self.matrix_vars[i][j].get()) for j in range(len(self.matrix_vars[0]))] for i in
                    range(len(self.matrix_vars))]
        except Exception as e:
            raise e

    def get_vector_b(self):
        try:
            return [float(self.vector_b_vars[i].get()) for i in range(len(self.matrix_vars))]
        except Exception as e:
            raise e

    def get_T(self):
        try:
            return float(self.T_var.get())
        except Exception as e:
            raise e

    def change_and_show_matrix(self, *args):
        try:
            old_matrix_row_shape = len(self.matrix_vars)
            old_matrix_col_shape = len(self.matrix_vars[0])

            for i in range(max(old_matrix_row_shape, int(self.matrix_row_shape_var.get() or 0))):
                if i >= min(old_matrix_row_shape, int(self.matrix_row_shape_var.get() or 0)):
                    if old_matrix_row_shape > int(self.matrix_row_shape_var.get() or 0):
                        self.matrix_vars = self.matrix_vars[0:i]
                        self.vector_b_vars = self.vector_b_vars[0:i]

                        for ii in range(i, old_matrix_row_shape):
                            self.vector_b_entries[ii].destroy()
                            for k in range(int(self.matrix_col_shape_var.get() or 0)):
                                self.matrix_entries[ii][k].destroy()

                        self.matrix_entries = self.matrix_entries[0:i]
                        self.vector_b_entries = self.vector_b_entries[0:i]
                        break
                    else:
                        self.matrix_vars.append([StringVar() for _ in range(int(self.matrix_col_shape_var.get() or 0))])
                        self.vector_b_vars.append(StringVar())

                        self.matrix_entries.append([
                            ttk.Entry(self.matrix_input_matrix_frame, width=ENTRY_WIDTH,
                                      textvariable=self.matrix_vars[i][k]) for k in
                            range(int(self.matrix_col_shape_var.get() or 0))])
                        self.vector_b_entries.append(
                            ttk.Entry(self.vector_b_input_vector_frame, width=ENTRY_WIDTH,
                                      textvariable=self.vector_b_vars[i]))

                        for k in range(int(self.matrix_col_shape_var.get() or 0)):
                            self.matrix_vars[i][k].set("0")
                            self.matrix_entries[i][k].grid(row=i, column=k, sticky=(N, W, E, S))

                            self.vector_b_vars[i].set("0")
                            self.vector_b_entries[i].grid(row=i, column=0, sticky=(N, W, E, S))

                for j in range(max(old_matrix_col_shape, int(self.matrix_col_shape_var.get() or 0))):
                    if j >= min(old_matrix_col_shape, int(self.matrix_col_shape_var.get() or 0)):
                        if old_matrix_col_shape > int(self.matrix_col_shape_var.get() or 0):
                            self.matrix_vars[i] = self.matrix_vars[i][0:j]
                            for k in range(j, old_matrix_col_shape):
                                self.matrix_entries[i][k].destroy()
                            self.matrix_entries[i] = self.matrix_entries[i][0:j]
                            break
                        else:
                            self.matrix_vars[i].append(StringVar())
                            self.matrix_vars[i][j].set("0")

                            self.matrix_entries[i].append(
                                ttk.Entry(self.matrix_input_matrix_frame, width=ENTRY_WIDTH,
                                          textvariable=self.matrix_vars[i][j]))
                            self.matrix_entries[i][j].grid(row=i, column=j, sticky=(N, W, E, S))
        except Exception as e:
            print(e)
