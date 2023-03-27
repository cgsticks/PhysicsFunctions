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
        self.master.title("Physics Formula Menu")
        self.master.configure(background='white')

        # Init equation photos
        self.e1_img = tk.PhotoImage(file="equation_1.png")
        self.e2_img = tk.PhotoImage(file="equation_2.png")
        self.e3_img = tk.PhotoImage(file="equation_3.png")
        self.e4_img = tk.PhotoImage(file="equation_4.png")
        self.e5_img = tk.PhotoImage(file="equation_5.png")
        self.e6_img = tk.PhotoImage(file="equation_6.png")
        # Create labels and add equation photos
        self.e1_label = tk.Label(self.master, image=self.e1_img)
        self.e2_label = tk.Label(self.master, image=self.e2_img)
        self.e3_label = tk.Label(self.master, image=self.e3_img)
        self.e4_label = tk.Label(self.master, image=self.e4_img)
        self.e5_label = tk.Label(self.master, image=self.e5_img)
        self.e6_label = tk.Label(self.master, image=self.e6_img)
        # Change the background of labels to match the background of the photos, so it looks like the photos are all
        # the exact same size
        self.e1_label.configure(background='white')
        self.e2_label.configure(background='white')
        self.e3_label.configure(background='white')
        self.e4_label.configure(background='white')
        self.e5_label.configure(background='white')
        self.e6_label.configure(background='white')
        # Place labels
        self.e1_label.grid(row=0, column=0)
        self.e2_label.grid(row=0, column=1)
        self.e3_label.grid(row=1, column=0)
        self.e4_label.grid(row=1, column=1)
        self.e5_label.grid(row=2, column=0)
        self.e6_label.grid(row=2, column=1)
        # Bind mouse 1 event to each equation label with each coresponding function call
        # I could call the 'calculateX_X_X(self.master) in these, but pycharm has a conniption when a line is too long
        self.e1_label.bind('<Button-1>', lambda event: self.e1())
        self.e2_label.bind('<Button-1>', lambda event: self.e2())
        self.e3_label.bind('<Button-1>', lambda event: self.e3())
        self.e4_label.bind('<Button-1>', lambda event: self.e4())
        self.e5_label.bind('<Button-1>', lambda event: self.e5())
        self.e6_label.bind('<Button-1>', lambda event: self.e6())

    def e1(self):
        calculate_speed_distance_time(self.master)

    def e2(self):
        calculate_acceleration_finalvelocity_displacement_time(self.master)

    def e3(self):
        calculate_acceleration_initial_final_velocity_time(self.master)

    def e4(self):
        calculate_initial_final_velocity_displacement_time(self.master)

    def e5(self):
        calculate_acceleration_initial_velocity_displacement_time(self.master)

    def e6(self):
        calculate_acceleration_initial_velocity_displacement_final_velocity(self.master)


root = tk.Tk()
app = PhysicsFormulaCalculator(root)
root.mainloop()
