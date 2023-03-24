def calculate_acceleration_initial_velocity_displacement_final_velocity():
    """
    Calculates acceleration, initial velocity, displacement, or final velocity depending on which 3 of the 4 variables
    have a value.

    Returns:
        float: The calculated value of acceleration, initial velocity, displacement, or final velocity, depending on
        which 3 of the 4 variables have a value.

    Raises:
        ValueError: If exactly 3 of the 4 variables are not given or if all 4 variables are given.
    """

    acceleration = input("Enter acceleration (in units (m/s^2)), or press Enter if not known: ")
    initial_velocity = input("Enter initial velocity (in units (m/s)), or press Enter if not known: ")
    displacement = input("Enter displacement (in unit (m)), or press Enter if not known: ")
    final_velocity = input("Enter final velocity (in units (m/s)), or press Enter if not known: ")

    try:
        given_variables = [acceleration, initial_velocity, displacement, final_velocity]
        num_given_variables = sum([1 for var in given_variables if var])
        if num_given_variables != 3:
            raise ValueError("Exactly 3 of the 4 variables (acceleration, initial velocity, displacement, or final "
                             "velocity) must be given.")
        if not acceleration:
            # Calculate acceleration
            acceleration = (float(final_velocity)**2 - float(initial_velocity)**2) / (2 * float(displacement))
            return f"Acceleration: {acceleration} units per time period squared"
        elif not initial_velocity:
            # Calculate initial velocity
            initial_velocity = (float(final_velocity)**2 - 2 * float(acceleration) * float(displacement)) ** 0.5
            return f"Initial velocity: + or - {initial_velocity} units per time period"
        elif not displacement:
            # Calculate displacement
            displacement = (float(final_velocity)**2 - float(initial_velocity)**2) / (2 * float(acceleration))
            return f"Displacement: {displacement} units"
        elif not final_velocity:
            # Calculate final velocity
            final_velocity = (float(initial_velocity)**2 + 2 * float(acceleration) * float(displacement)) ** 0.5
            return f"Final velocity: + or - {final_velocity} units per time period"
    except ValueError:
        print("Invalid input. Please enter numeric/real world values only.")

# Call the function
if __name__ == "__main__":
    result = calculate_acceleration_initial_velocity_displacement_final_velocity()
    if result:
        print(result)