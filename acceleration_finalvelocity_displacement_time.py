import tkinter as tk
class calculate_acceleration_finalvelocity_displacement_time:
    def __init__(self, window):
        self.window = window
        """
        Calculates acceleration, final velocity, displacement, or time depending on which 3 of the 4 variables have a value.

        Returns:
            float: The calculated value of acceleration, final velocity, displacement, or time, depending on which 3 of the 4 variables have a value.

        Raises:
            ValueError: If exactly 3 of the 4 variables are not given or if all 4 variables are given.
        """
        self.input_form = tk.Toplevel(self.window)
        self.acceleration_label = tk.Label(self.input_form, text="Enter acceleration (in units per time period squared):").grid(row=0, column=0)
        self.final_velocity_label = tk.Label(self.input_form, text="Enter final velocity (in units per time period):").grid(row=1, column=0)
        self.displacement_label = tk.Label(self.input_form, text="Enter displacement (in units):").grid(row=2, column=0)
        self.time_label = tk.Label(self.input_form, text="Enter time period (in units):").grid(row=3, column=0)

        self.acceleration = tk.Entry(self.input_form, width=5)
        self.acceleration.grid(row=0, column=1)
        self.final_velocity = tk.Entry(self.input_form, width=5)
        self.final_velocity.grid(row=1, column=1)
        self.displacement = tk.Entry(self.input_form, width=5)
        self.displacement.grid(row=2, column=1)
        self.time = tk.Entry(self.input_form, width=5)
        self.time.grid(row=3, column=1)

        self.math_button = tk.Button(self.input_form, text="Go", command=self.math)
        self.math_button.grid(row=4, column=0)

        self.result_label = tk.Label(self.input_form, text="")
        self.result_label.grid(row=5, column=0)
        self.input_form.lift()
        self.input_form.focus_set()

    def math(self):
        try:
            if self.acceleration and self.final_velocity and self.time:
                # Calculate displacement
                displacement = float(self.final_velocity.get()) * float(self.time.get()) - 0.5 * float(self.acceleration.get()) * float(self.time.get()) ** 2
                self.result_label.config(text=displacement)  # f"Displacement: {displacement} units"
            elif self.acceleration and self.final_velocity and self.displacement:
                # Calculate time
                time = (float(self.final_velocity.get()) - ((float(self.final_velocity.get()) ** 2) - (2 * float(self.acceleration.get()) * float(self.displacement.get()))) ** 0.5) / float(self.acceleration.get())
                self.result_label.config(text=time)  # f"Time taken: {time} units"
            elif self.acceleration and self.displacement and self.time:
                # Calculate final velocity
                final_velocity = (float(self.acceleration.get()) * float(self.time.get()) + (float(self.displacement.get()))) / float(self.time.get())
                self.result_label.config(text=final_velocity)  # f"Final velocity: {final_velocity} units per time period"
            elif self.final_velocity and self.displacement and self.time:
                # Calculate acceleration
                acceleration = (2 * float(self.displacement.get()) - float(self.final_velocity.get()) * float(self.time.get())) / (float(self.time.get()) ** 2)
                self.result_label.config(text=acceleration)  # f"Acceleration: {acceleration} units per time period squared"
            else:
                raise ValueError("Exactly 3 of the 4 variables (acceleration, final velocity, displacement, or time) must be given.")
        except ValueError:
            print("Invalid input. Please enter numeric/real world values only.")


# Call the function
if __name__ == "__main__":
    result = calculate_acceleration_finalvelocity_displacement_time()
    if result:
        print(result)
