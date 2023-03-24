def calculate_acceleration_initial_velocity_displacement_time():
    """
    Calculates acceleration, initial velocity, displacement,
    or time depending on which 3 of the 4 variables have a value.

    Returns:
        float: The calculated value of acceleration, initial velocity, displacement, or time,
        depending on which 3 of the 4 variables have a value.

    Raises:
        ValueError: If exactly 3 of the 4 variables are not given or if all 4 variables are given.
    """
    # Gather user input, "0" is a valid input and needs to be stored at a float,
    # pressing Enter should set variable to false
    acceleration = input("Enter acceleration (in units m/s^2), or press Enter if not known: ")
    acceleration = float(acceleration) if acceleration != "" else 0.0

    initial_velocity = input("Enter initial velocity (in units m/s), or press Enter if not known: ")
    initial_velocity = float(initial_velocity) if initial_velocity != "" else 0.0

    displacement = input("Enter displacement (in units m), or press Enter if not known: ")
    displacement = float(displacement) if displacement != "" else 0.0

    time = input("Enter time period (in units s), or press Enter if not known (note: will only solve for time when initial velocity is zero): ")
    time = float(time) if time != "" else 0.0

    try:
        if float(initial_velocity) == 0.0:
            if acceleration and displacement:
            # Calculate time
                time = ((float(displacement) * (2))/(float(acceleration)))**0.5
                return f"Time taken: {time} units"
        elif acceleration and initial_velocity and time:
            # Calculate displacement
            displacement = float(initial_velocity) * float(time) + 0.5 * float(acceleration) * float(time) ** 2
            return f"Displacement: {displacement} units"
        elif acceleration and displacement and time:
            # Calculate initial velocity
            initial_velocity = (float(displacement) - 0.5 * float(acceleration) * float(time) ** 2) / float(time)
            return f"Initial velocity: {initial_velocity} units per time period"
        elif initial_velocity and displacement and time:
            # Calculate acceleration
            acceleration = 2 * (float(displacement) - float(initial_velocity) * float(time)) / float(time) ** 2
            return f"Acceleration: {acceleration} units per time period squared"
        else:
            raise ValueError("Exactly 3 of the 4 variables (acceleration, initial velocity, displacement, or time) must be given.")
    except ValueError:
        print("Invalid input. Please enter numeric/real world values only.")


# Call the function
if __name__ == "__main__":
    result = calculate_acceleration_initial_velocity_displacement_time()
    if result:
        print(result)
