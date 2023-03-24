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

        self.formula_menu = OptionMenu(master, StringVar(), "Speed, Distance, Time",
                                       "Acceleration, Final Velocity, Displacement, Time",
                                       "Acceleration, Initial and Final Velocity, Time",
                                       "Initial and Final Velocity, Displacement, Time",
                                       "Acceleration, Initial Velocity, Displacement, Time",
                                       "Acceleration, Initial Velocity, Displacement, Final Velocity")
        self.formula_menu.pack()

        self.speed_label = Label(master, text="Speed:")
        self.speed_label.pack()
        self.speed_entry = Entry(master)
        self.speed_entry.pack()

        self.distance_label = Label(master, text="Distance:")
        self.distance_label.pack()
        self.distance_entry = Entry(master)
        self.distance_entry.pack()

        self.time_label = Label(master, text="Time:")
        self.time_label.pack()
        self.time_entry = Entry(master)
        self.time_entry.pack()

        self.calculate_button = Button(master, text="Calculate", command=self.calculate_formula)
        self.calculate_button.pack()

        self.result_label = Label(master, text="")
        self.result_label.pack()

    def calculate_formula(self):
        formula = self.formula_menu.cget("text")
        speed = self.speed_entry.get()
        distance = self.distance_entry.get()
        time = self.time_entry.get()

        try:
            if speed and distance:
                # Calculate time
                time = float(distance) / float(speed)
                self.result_label.config(text=f"Time taken: {time} units")
            elif speed and time:
                # Calculate distance
                distance = float(speed) * float(time)
                self.result_label.config(text=f"Distance covered: {distance} units")
            elif distance and time:
                # Calculate speed
                speed = float(distance) / float(time)
                self.result_label.config(text=f"Speed: {speed} units per time period")
            else:
                raise ValueError("Exactly 2 of the 3 variables (speed, distance, or time) must be given.")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter numeric/real world values only.")

root = Tk()
app = PhysicsFormulaCalculator(root)
root.mainloop()
