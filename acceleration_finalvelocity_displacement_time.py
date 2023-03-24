def calculate_acceleration_finalvelocity_displacement_time():
    """
    Calculates acceleration, final velocity, displacement, or time depending on which 3 of the 4 variables have a value.

    Returns:
        float: The calculated value of acceleration, final velocity, displacement, or time, depending on which 3 of the 4 variables have a value.

    Raises:
        ValueError: If exactly 3 of the 4 variables are not given or if all 4 variables are given.
    """

    acceleration = input("Enter acceleration (in units per time period squared), or press Enter if not known: ")
    final_velocity = input("Enter final velocity (in units per time period), or press Enter if not known: ")
    displacement = input("Enter displacement (in units), or press Enter if not known: ")
    time = input("Enter time period (in units), or press Enter if not known: ")

    try:
        if acceleration and final_velocity and time:
            # Calculate displacement
            displacement = float(final_velocity) * float(time) - 0.5 * float(acceleration) * float(time) ** 2
            return f"Displacement: {displacement} units"
        elif acceleration and final_velocity and displacement:
            # Calculate time
            time = (float(final_velocity) - ((float(final_velocity) ** 2) - (2 * float(acceleration) * float(displacement))) ** 0.5) / float(acceleration)
            return f"Time taken: {time} units"
        elif acceleration and displacement and time:
            # Calculate final velocity
            final_velocity = (float(acceleration) * float(time) + (float(displacement))) / float(time)
            return f"Final velocity: {final_velocity} units per time period"
        elif final_velocity and displacement and time:
            # Calculate acceleration
            acceleration = (2 * float(displacement) - float(final_velocity) * float(time)) / (float(time) ** 2)
            return f"Acceleration: {acceleration} units per time period squared"
        else:
            raise ValueError("Exactly 3 of the 4 variables (acceleration, final velocity, displacement, or time) must be given.")
    except ValueError:
        print("Invalid input. Please enter numeric/real world values only.")


# Call the function
if __name__ == "__main__":
    result = calculate_acceleration_finalvelocity_displacement_time()
    if result:
        print(result)
