import tkinter as tk
from horizontal_speed_distance_time import calculate_speed_distance_time
from acceleration_finalvelocity_displacement_time import calculate_acceleration_finalvelocity_displacement_time
from acceleration_velocity_time import calculate_acceleration_initial_final_velocity_time
from initial_final_velocity_displacement_time import calculate_initial_final_velocity_displacement_time
from acceleration_initialvelocity_displacement_time import calculate_acceleration_initial_velocity_displacement_time
from acceleration_initial_velocity_displacement_final_velocity import calculate_acceleration_initial_velocity_displacement_final_velocity

class PhysicsFormulaCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Physics Formula Calculator")

        # Display the image of formulas
        image = tk.PhotoImage(file="Formulas_Kinematics_Legend.PNG")
        canvas = tk.Canvas(master, width=image.width(), height=image.height())
        canvas.pack()
        canvas.create_image(0, 0, anchor=tk.NW, image=image)
        # TODO: create six rectangles to make clickable boxes for each formula
        # The rectangles should be located at the positions where each formula is displayed on the image
        # Each rectangle should call a function to set the formula to be used for the calculation

        # TODO: remove the formula menu
        # Change formula menu choices to 1-6
        self.formula_menu = tk.OptionMenu(master, tk.StringVar(), "1. Speed, Distance, Time",
                                          "2. Acceleration, Final Velocity, Displacement, Time",
                                          "3. Acceleration, Initial and Final Velocity, Time",
                                          "4. Initial and Final Velocity, Displacement, Time",
                                          "5. Acceleration, Initial Velocity, Displacement, Time",
                                          "6. Acceleration, Initial Velocity, Displacement, Final Velocity")
        self.formula_menu.pack()

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_formula)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_formula(self):
        formula = self.formula_menu.cget("text")
        result = ""
        if formula == "1. Speed, Distance, Time":
            result = calculate_speed_distance_time(self.master)
        elif formula == "2. Acceleration, Final Velocity, Displacement, Time":
            result = calculate_acceleration_finalvelocity_displacement_time(self.master)
        elif formula == "3. Acceleration, Initial and Final Velocity, Time":
            result = calculate_acceleration_initial_final_velocity_time(self.master)
        elif formula == "4. Initial and Final Velocity, Displacement, Time":
            result = calculate_initial_final_velocity_displacement_time(self.master)
        elif formula == "5. Acceleration, Initial Velocity, Displacement, Time":
            result = calculate_acceleration_initial_velocity_displacement_time(self.master)
        elif formula == "6. Acceleration, Initial Velocity, Displacement, Final Velocity":
            result = calculate_acceleration_initial_velocity_displacement_final_velocity(self.master)
        self.result_label.config(text=result)

root = tk.Tk()
app = PhysicsFormulaCalculator(root)
root.mainloop()
