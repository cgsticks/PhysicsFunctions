def calculate_acceleration_initial_final_velocity_time():
    """
    Calculates acceleration, initial velocity, final velocity, or time depending on which 3 of the 4 inputs are given.

    Returns:
        float: The calculated value of acceleration, initial velocity, final velocity, or time, depending on which 3 of the 4 inputs are given.

    Raises:
        ValueError: If exactly 3 of the 4 inputs are not given or if all 4 inputs are given.
    """
    # Get user input
    a = input("Enter acceleration (in units (m/s^2)), or press Enter if not known: ")
    u = input("Enter initial velocity (in units (m/s)), or press Enter if not known: ")
    v = input("Enter final velocity (in units (m/s)), or press Enter if not known: ")
    t = input("Enter time period (in unit (s)), or press Enter if not known: ")

    try:
        # check if 3 inputs are given
        if sum(map(bool, [a, u, v, t])) != 3:
            raise ValueError("Exactly 3 of the 4 inputs (acceleration, initial velocity, final velocity, or time) must be given.")

        # Calculate the unknown variable
        if not a:
            a = (float(v) - float(u)) / float(t)
            return f"Acceleration: {a} units per time period"
        elif not u:
            u = float(v) - float(a) * float(t)
            return f"Initial velocity: {u} units per time period"
        elif not v:
            v = float(u) + float(a) * float(t)
            return f"Final velocity: {v} units per time period"
        elif not t:
            t = (float(v) - float(u)) / float(a)
            return f"Time period: {t} units"
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    result = calculate_acceleration_initial_final_velocity_time()
    if result:
        print(result)