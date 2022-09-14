import calculations


def receive_data_from_view(view):
    try:
        process_data_in_calculations(view, view.system_input.get_matrix(), view.system_input.get_vector_b(),
                                     view.system_input.get_T())
    except Exception as e:
        raise e


def process_data_in_calculations(view, matrix, vector_b, T):
    try:
        res = calculations.all(matrix, vector_b, T)
        give_date_to_output(view, res["omega"], res["solution"], True, res["precision"], T)
    except Exception as e:
        raise e


def give_date_to_output(view, omega, solution, uniqueness_condition, precision, T):
    try:
        view.results_output.receive_data_and_show_it(omega, solution, uniqueness_condition, precision)
        view.plots_output.receive_data_and_show_plot(omega, solution, T)
    except Exception as e:
        raise e
