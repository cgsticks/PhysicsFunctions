import tkinter as tk


class calculate_acceleration_initial_velocity_displacement_final_velocity:
    def __init__(self, window):
        self.window = window
        """
        Calculates acceleration, initial velocity, displacement, or final velocity depending on which 3 of the 4 variables
        have a value.

        Returns:
            float: The calculated value of acceleration, initial velocity, displacement, or final velocity, depending on
            which 3 of the 4 variables have a value.

        Raises:
            ValueError: If exactly 3 of the 4 variables are not given or if all 4 variables are given.
        """
        # Opens new tkinter window
        self.input_form = tk.Toplevel(self.window)
        # self.wait_var = wait_var
        # Creates labels for each entry
        acceleration_label = tk.Label(self.input_form, text="Enter acceleration (in units (m/s^2)):").grid(row=0, column=0)
        initial_velocity_label = tk.Label(self.input_form, text="Enter initial velocity (in units (m/s)):").grid(row=1, column=0)
        displacement_label = tk.Label(self.input_form, text="Enter displacement (in unit (m)):").grid(row=2, column=0)
        final_velocity_label = tk.Label(self.input_form, text="Enter final velocity (in units (m/s)):").grid(row=3, column=0)

        # Creates entry fields for each variable
        self.acceleration_entry = tk.Entry(self.input_form, width=5)
        self.acceleration_entry.grid(row=0, column=1)
        self.initial_velocity_entry = tk.Entry(self.input_form, width=5)
        self.initial_velocity_entry.grid(row=1, column=1)
        self.displacement_entry = tk.Entry(self.input_form, width=5)
        self.displacement_entry.grid(row=2, column=1)
        self.final_velocity_entry = tk.Entry(self.input_form, width=5)
        self.final_velocity_entry.grid(row=3, column=1)

        self.math_button = tk.Button(self.input_form, text="Start Number Crunching", command=self.math)
        self.math_button.grid(row=4, column=0)

        self.result_label = tk.Label(self.input_form, text="")
        self.result_label.grid(row=5, column=0)
        self.input_form.lift()
        self.input_form.focus_set()

    def math(self):
        try:
            given_variables = [self.acceleration_entry.get(), self.initial_velocity_entry.get(),
                               self.displacement_entry.get(), self.final_velocity_entry.get()]
            num_given_variables = sum([1 for var in given_variables if var])
            if num_given_variables != 3:
                raise ValueError("Exactly 3 of the 4 variables (acceleration, initial velocity, displacement, or final "
                                 "velocity) must be given.")
            if not self.acceleration_entry.get():
                # Calculate acceleration
                acceleration = (float(self.final_velocity_entry.get()) ** 2 - float(
                    self.initial_velocity_entry.get()) ** 2) / (
                                       2 * float(self.displacement_entry.get()))
                # print(f"Acceleration: {acceleration} units per time period squared")
                self.result_label.config(text=acceleration)  # f"Acceleration: {acceleration} units per time period squared"
            elif not self.initial_velocity_entry.get():
                # Calculate initial velocity
                initial_velocity = (float(self.final_velocity_entry.get()) ** 2 - 2 * float(
                    self.acceleration_entry.get()) * float(self.displacement_entry.get())) ** 0.5
                # print(f"Initial velocity: + or - {initial_velocity} units per time period")
                self.result_label.config(text=initial_velocity)  # f"Initial velocity: + or - {initial_velocity} units per time period"
            elif not self.displacement_entry.get():
                # Calculate displacement
                displacement = (float(self.final_velocity_entry.get()) ** 2 - float(
                    self.initial_velocity_entry.get()) ** 2) / (
                                       2 * float(self.acceleration_entry.get()))
                # print(f"Displacement: {displacement} units")
                self.result_label.config(text=displacement)  # f"Displacement: {displacement} units"
            elif not self.final_velocity_entry.get():
                # Calculate final velocity
                final_velocity = (float(self.initial_velocity_entry.get()) ** 2 + 2 * float(
                    self.acceleration_entry.get()) * float(self.displacement_entry.get())) ** 0.5
                # print(f"Final velocity: + or - {final_velocity} units per time period")
                self.result_label.config(text=final_velocity)  # f"Final velocity: + or - {final_velocity} units per time period"
        except ValueError:
            print("Invalid input. Please enter numeric/real world values only.")

# if name == main not needed when function is called from another file

# Call the function
# if __name__ == "__main__":
#     result = calculate_acceleration_initial_velocity_displacement_final_velocity()
#     if result:
#         print(result)
