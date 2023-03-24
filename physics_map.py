#Write script to complete the TODO in the following code, be sure to create a GUI using a method of your choice
# function number 1
from horizontal_speed_distance_time import calculate_speed_distance_time
#function number 2
from acceleration_finalvelocity_displacement_time import calculate_acceleration_finalvelocity_displacement_time
# function number 3
from acceleration_velocity_time import calculate_acceleration_initial_final_velocity_time
# function number 4
from initial_final_velocity_displacement_time import calculate_initial_final_velocity_displacement_time
# function number 5
from acceleration_initialvelocity_displacement_time import calculate_acceleration_initial_velocity_displacement_time
# function number 6
from acceleration_initial_velocity_displacement_final_velocity import calculate_acceleration_initial_velocity_displacement_final_velocity

def calculate_formula():
    """
    Prompts the user to choose between physics formulas,
    and then calls the appropriate function to calculate the necessary variables.
    """
    # Get user input
    #TODO create UI
    formula = input("Choose the type of formula (1, 2, 3, 4,... etc see formula sheet): ")

    #TODO display formulas.png with numbered legend or make each formula clickable

    # Call the appropriate function based on the user's choice
    if formula == "1":
        result = calculate_speed_distance_time()
        print(result)
    elif formula == "2":
        result = calculate_acceleration_finalvelocity_displacement_time()
        print(result)
    elif formula == "3":
        result = calculate_acceleration_initial_final_velocity_time()
        print(result)
    elif formula == "4":
        result = calculate_initial_final_velocity_displacement_time()
        print(result)
    elif formula == "5":
        result = calculate_acceleration_initial_velocity_displacement_time()
        print(result)
    elif formula == "6":
        result = calculate_acceleration_initial_velocity_displacement_final_velocity()
        print(result)
    else:
        print("Invalid input. Please choose either 'horizontal' or 'vertical'.")
    # TODO display the appropriate result

if __name__ == "__main__":
    calculate_formula()

