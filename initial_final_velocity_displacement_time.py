def calculate_initial_final_velocity_displacement_time():
    """
    Calculates initial velocity, final velocity, displacement, or time, depending on which 3 of the 4 variables have a value.

    Returns:
        float: The calculated value of initial velocity, final velocity, displacement, or time, depending on which 3 of the 4 variables have a value.

    Raises:
        ValueError: If exactly 3 of the 4 variables are not given or if all 4 variables are given.
    """

    initial_velocity = input("Enter initial velocity (in units (m/s))), or press Enter if not known: ")
    final_velocity = input("Enter final velocity (in units (m/s))), or press Enter if not known: ")
    displacement = input("Enter displacement (in unit (m)), or press Enter if not known: ")
    time = input("Enter time period (in unit (s)), or press Enter if not known: ")

    try:
        if initial_velocity and final_velocity and time:
            # Calculate displacement
            displacement = 0.5 * (float(initial_velocity) + float(final_velocity)) * float(time)
            return f"Displacement: {displacement} units"
        elif initial_velocity and final_velocity and displacement:
            # Calculate time
            time = (float(displacement) * 2) / (float(initial_velocity) + float(final_velocity))
            return f"Time taken: {time} units"
        elif initial_velocity and displacement and time:
            # Calculate final velocity
            final_velocity = (2 * float(displacement) / float(time)) - float(initial_velocity)
            return f"Final velocity: {final_velocity} units per time period"
        elif final_velocity and displacement and time:
            # Calculate initial velocity
            initial_velocity = (2 * float(displacement) / float(time)) - float(final_velocity)
            return f"Initial velocity: {initial_velocity} units per time period"
        else:
            raise ValueError("Exactly 3 of the 4 variables (initial velocity, final velocity, displacement, time) must be given.")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")


# Call the function
if __name__ == "__main__":
    result = calculate_initial_final_velocity_displacement_time()
    if result:
        print(result)
