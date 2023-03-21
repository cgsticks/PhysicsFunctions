from horizontal_speed_distance_time import calculate_speed_distance_time
from acceleration_velocity_time import calculate_acceleration_initial_final_velocity_time

def calculate_motion():
    """
    Prompts the user to choose between horizontal motion and vertical motion, and then calls the appropriate function to calculate the necessary variables.
    """
    # Get user input
    motion = input("Choose the type of motion (horizontal or vertical): ")

    # Call the appropriate function based on the user's choice
    if motion == "horizontal":
        result = calculate_speed_distance_time()
        print(result)
    elif motion == "vertical":
        result = calculate_acceleration_initial_final_velocity_time()
        print(result)
    else:
        print("Invalid input. Please choose either 'horizontal' or 'vertical'.")

if __name__ == "__main__":
    calculate_motion()

