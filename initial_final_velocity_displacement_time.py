import tkinter as tk


class calculate_initial_final_velocity_displacement_time:
    def __init__(self, window):
        self.window = window
        """
        Calculates initial velocity, final velocity, displacement, or time, depending on which 3 of the 4 variables have a value.
    
        Returns:
            float: The calculated value of initial velocity, final velocity, displacement, or time, depending on which 3 of the 4 variables have a value.
    
        Raises:
            ValueError: If exactly 3 of the 4 variables are not given or if all 4 variables are given.
        """
        self.input_form = tk.Toplevel(self.window)
        self.initial_velocity_label = tk.Label(self.input_form, text="Enter initial velocity (in units (m/s))):").grid(
            row=0, column=0)
        self.final_velocity_label = tk.Label(self.input_form, text="Enter final velocity (in units (m/s))):").grid(
            row=1, column=0)
        self.displacement_label = tk.Label(self.input_form, text="Enter displacement (in unit (m)):").grid(row=2,
                                                                                                           column=0)
        self.time_label = tk.Label(self.input_form, text="Enter time period (in unit (s)):").grid(row=3, column=0)

        self.initial_velocity_entry = tk.Entry(self.input_form, width=5)
        self.final_velocity_entry = tk.Entry(self.input_form, width=5)
        self.displacement_entry = tk.Entry(self.input_form, width=5)
        self.time_entry = tk.Entry(self.input_form, width=5)
        self.initial_velocity_entry.grid(row=0, column=1)
        self.final_velocity_entry.grid(row=1, column=1)
        self.displacement_entry.grid(row=2, column=1)
        self.time_entry.grid(row=3, column=1)
        self.math_button = tk.Button(self.input_form, text="Go", command=self.do_math)
        self.math_button.grid(row=4, column=0)
        self.result_label = tk.Label(self.input_form, text="")
        self.result_label.grid(row=5, column=0)
        self.input_form.lift()
        self.input_form.focus_set()

    def do_math(self):
        try:
            if self.initial_velocity_entry.get() and self.final_velocity_entry.get and self.time_entry.get():
                # Calculate displacement
                displacement = 0.5 * (
                            float(self.initial_velocity_entry.get()) + float(self.final_velocity_entry.get())) * float(
                    self.time_entry.get())
                self.result_label.config(text=displacement)  # f"Displacement: {displacement} units"
            elif self.initial_velocity_entry.get() and self.final_velocity_entry.get() and self.displacement_entry.get():
                # Calculate time
                time = (float(self.displacement_entry.get()) * 2) / (
                            float(self.initial_velocity_entry.get()) + float(self.final_velocity_entry.get()))
                self.result_label.config(text=time)  # f"Time taken: {time} units"
            elif self.initial_velocity_entry.get() and self.displacement_entry.get() and self.time_entry.get():
                # Calculate final velocity
                final_velocity = (2 * float(self.displacement_entry.get()) / float(self.time_entry.get())) - float(
                    self.initial_velocity_entry.get())
                self.result_label.config(
                    text=final_velocity)  # f"Final velocity: {final_velocity} units per time period"
            elif self.final_velocity_entry.get() and self.displacement_entry.get() and self.time_entry.get():
                # Calculate initial velocity
                initial_velocity = (2 * float(self.displacement_entry.get()) / float(self.time_entry.get())) - float(
                    self.final_velocity_entry.get())
                self.result_label.config(
                    text=initial_velocity)  # f"Initial velocity: {initial_velocity} units per time period"
            else:
                raise ValueError(
                    "Exactly 3 of the 4 variables (initial velocity, final velocity, displacement, time) must be given.")
        except ValueError:
            print("Invalid input. Please enter numeric values only.")


# Call the function
if __name__ == "__main__":
    result = calculate_initial_final_velocity_displacement_time()
    if result:
        print(result)
