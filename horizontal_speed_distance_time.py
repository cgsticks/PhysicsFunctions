import tkinter as tk


class calculate_speed_distance_time:
    def __init__(self, window):
        """
        Calculates speed, distance, or time depending on which 2 of the 3 variables have a value.

        Returns:
            float: The calculated value of speed, distance, or time, depending on which 2 of the 3 variables have a value.

        Raises:
            ValueError: If exactly 2 of the 3 variables are not given or if all 3 variables are given.
        """
        self.window = window
        self.input_form = tk.Toplevel(self.window)
        self.speed_label = tk.Label(self.input_form, text="Enter speed (in units (m/s)): ").grid(row=0, column=0)
        self.distance_label = tk.Label(self.input_form, text="Enter distance (in unit (m)): ").grid(row=1, column=0)
        self.time_label = tk.Label(self.input_form, text="Enter time period (in unit (s)): ").grid(row=2, column=0)

        self.speed_entry = tk.Entry(self.input_form, width=5)
        self.speed_entry.grid(row=0, column=1)
        self.distance_entry = tk.Entry(self.input_form, width=5)
        self.distance_entry.grid(row=1, column=1)
        self.time_entry = tk.Entry(self.input_form, width=5)
        self.time_entry.grid(row=2, column=1)

        self.math_button = tk.Button(self.input_form, text="Go", command=self.math)
        self.math_button.grid(row=3, column=0)

        self.result_label = tk.Label(self.input_form, text="")
        self.result_label.grid(row=4, column=0)
        self.input_form.lift()
        self.input_form.focus_set()

    def math(self):
        try:
            if self.speed_entry.get() and self.distance_entry.get():
                # Calculate time
                time = float(self.distance_entry.get()) / float(self.speed_entry.get())
                self.result_label.config(text=time)  # f"Time taken: {time} units"
            elif self.speed_entry.get() and self.time_entry.get():
                # Calculate distance
                distance = float(self.speed_entry.get()) * float(self.time_entry.get())
                self.result_label.config(text=distance)  # f"Distance covered: {distance} units"
            elif self.distance_entry.get() and self.time_entry.get():
                # Calculate speed
                speed = float(self.distance_entry.get()) / float(self.time_entry.get())
                self.result_label.config(text=speed)  # f"Speed: {speed} units per time period"
            else:
                raise ValueError("Exactly 2 of the 3 variables (speed, distance, or time) must be given.")
        except ValueError:
            print("Invalid input. Please enter numeric/real world values only.")


# Call the function
# if __name__ == "__main__":
#     result = calculate_speed_distance_time()
#     if result:
#         print(result)
