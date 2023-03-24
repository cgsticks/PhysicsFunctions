from tkinter import *
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

        self.label = Label(master, text="Choose a formula:")
        self.label.pack()

        self.formula_menu = OptionMenu(master, StringVar(), "Speed, Distance, Time", "Acceleration, Final Velocity, Displacement, Time", "Acceleration, Initial and Final Velocity, Time", "Initial and Final Velocity, Displacement, Time", "Acceleration, Initial Velocity, Displacement, Time", "Acceleration, Initial Velocity, Displacement, Final Velocity")
        self.formula_menu.pack()

        self.calculate_button = Button(master, text="Calculate", command=self.calculate_formula)
        self.calculate_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def calculate_formula(self):
        formula = self.formula_menu.cget("text")
        result = ""
        if formula == "Speed, Distance, Time":
            result = calculate_speed_distance_time()
        elif formula == "Acceleration, Final Velocity, Displacement, Time":
            result = calculate_acceleration_finalvelocity_displacement_time()
        elif formula == "Acceleration, Initial and Final Velocity, Time":
            result = calculate_acceleration_initial_final_velocity_time()
        elif formula == "Initial and Final Velocity, Displacement, Time":
            result = calculate_initial_final_velocity_displacement_time()
        elif formula == "Acceleration, Initial Velocity, Displacement, Time":
            result = calculate_acceleration_initial_velocity_displacement_time()
        elif formula == "Acceleration, Initial Velocity, Displacement, Final Velocity":
            result = calculate_acceleration_initial_velocity_displacement_final_velocity()
        self.result_label.config(text=result)

root = Tk()
app = PhysicsFormulaCalculator(root)
root.mainloop()
