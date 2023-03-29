import tkinter as tk


class calculate_acceleration_initial_final_velocity_time:
    def __init__(self, window):
        self.window = window
        """
        Calculates acceleration, initial velocity, final velocity, or time depending on which 3 of the 4 inputs are given.
    
        Returns:
            float: The calculated value of acceleration, initial velocity, final velocity, or time, depending on which 3 of the 4 inputs are given.
    
        Raises:
            ValueError: If exactly 3 of the 4 inputs are not given or if all 4 inputs are given.
        """

        self.input_form = tk.Toplevel(self.window)
        # Get user input
        self.a_label = tk.Label(self.input_form, text="Enter acceleration (in units (m/s^2)):").grid(row=0, column=0)
        self.u_label = tk.Label(self.input_form, text="Enter initial velocity (in units (m/s)):").grid(row=1, column=0)
        self.v_label = tk.Label(self.input_form, text="Enter final velocity (in units (m/s)):").grid(row=2, column=0)
        self.t_label = tk.Label(self.input_form, text="Enter time period (in unit (s)):").grid(row=3, column=0)
        self.a_entry = tk.Entry(self.input_form, width=5)
        self.u_entry = tk.Entry(self.input_form, width=5)
        self.v_entry = tk.Entry(self.input_form, width=5)
        self.t_entry = tk.Entry(self.input_form, width=5)
        self.a_entry.grid(row=0, column=1)
        self.u_entry.grid(row=1, column=1)
        self.v_entry.grid(row=2, column=1)
        self.t_entry.grid(row=3, column=1)
        self.result_label = tk.Label(self.input_form, text="")
        self.result_label.grid(row=5, column=0)
        self.math_button = tk.Button(self.input_form, text="Go", command=self.do_math)
        self.math_button.grid(row=4, column=0)
        self.input_form.lift()
        self.input_form.focus_set()

    def do_math(self):
        try:
            # check if 3 inputs are given
            if sum(map(bool,
                       [self.a_entry.get(), self.u_entry.get(), self.v_entry.get(), self.t_entry.get()])) != 3:
                raise ValueError(
                    "Exactly 3 of the 4 inputs (acceleration, initial velocity, final velocity, or time) must be given.")
            # Calculate the unknown variable
            if not self.a_entry.get():
                a = (float(self.v_entry.get()) - float(self.u_entry.get())) / float(self.t_entry.get())
                self.result_label.config(text=a)  # f"Acceleration: {a} units per time period"
            elif not self.u_entry.get():
                u = float(self.v_entry.get()) - float(self.a_entry.get()) * float(self.t_entry.get())
                self.result_label.config(text=u)  # f"Initial velocity: {u} units per time period"
            elif not self.v_entry.get():
                v = float(self.u_entry.get()) + float(self.a_entry.get()) * float(self.t_entry.get())
                self.result_label.config(text=v)  # f"Final velocity: {v} units per time period"
            elif not self.t_entry.get():
                t = (float(self.v_entry.get()) - float(self.u_entry.get())) / float(self.a_entry.get())
                self.result_label.config(text=t)  # f"Time period: {t} units"
        except ValueError:
            print("Invalid input. Please enter numeric values only.")

# if __name__ == "__main__":
#     result = calculate_acceleration_initial_final_velocity_time()
#     if result:
#         print(result)
