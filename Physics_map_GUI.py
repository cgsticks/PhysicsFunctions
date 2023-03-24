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
        #TODO use canvas along with create image and create rectangle to make six clickable boxes for the image Formulas_Kinematics_Legend.PNG
        image = tk.PhotoImage(file="Formulas_Kinematics_Legend.PNG")
        label = tk.Label(image=image)
        label.image = image
        label.pack()

        # Change formula menu choices to 1-6
        # TODO remove menu and instead use the result of the click to set formula
        self.formula_menu = tk.OptionMenu(master, tk.StringVar(), "1. Speed, Distance, Time", "2. Acceleration, Final Velocity, Displacement, Time", "3. Acceleration, Initial and Final Velocity, Time", "4. Initial and Final Velocity, Displacement, Time", "5. Acceleration, Initial Velocity, Displacement, Time", "6. Acceleration, Initial Velocity, Displacement, Final Velocity")
        self.formula_menu.pack()

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_formula)
        self.calculate_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def calculate_formula(self):
        formula = self.formula_menu.cget("text")
        result = ""
        if formula == "1. Speed, Distance, Time":
            result = calculate_speed_distance_time()
        elif formula == "2. Acceleration, Final Velocity, Displacement, Time":
            result = calculate_acceleration_finalvelocity_displacement_time()
        elif formula == "3. Acceleration, Initial and Final Velocity, Time":
            result = calculate_acceleration_initial_final_velocity_time()
        elif formula == "4. Initial and Final Velocity, Displacement, Time":
            result = calculate_initial_final_velocity_displacement_time()
        elif formula == "5. Acceleration, Initial Velocity, Displacement, Time":
            result = calculate_acceleration_initial_velocity_displacement_time()
        elif formula == "6. Acceleration, Initial Velocity, Displacement, Final Velocity":
            result = calculate_acceleration_initial_velocity_displacement_final_velocity()
        self.result_label.config(text=result)

root = tk.Tk()
app = PhysicsFormulaCalculator(root)
root.mainloop()
