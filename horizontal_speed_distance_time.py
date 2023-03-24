def calculate_speed_distance_time():
    """
    Calculates speed, distance, or time depending on which 2 of the 3 variables have a value.

    Returns:
        float: The calculated value of speed, distance, or time, depending on which 2 of the 3 variables have a value.

    Raises:
        ValueError: If exactly 2 of the 3 variables are not given or if all 3 variables are given.
    """

    speed = input("Enter speed (in units (m/s)), or press Enter if not known: ")
    distance = input("Enter distance (in unit (m)), or press Enter if not known: ")
    time = input("Enter time period (in unit (s)), or press Enter if not known: ")

    try:
        if speed and distance:
            # Calculate time
            time = float(distance) / float(speed)
            return f"Time taken: {time} units"
        elif speed and time:
            # Calculate distance
            distance = float(speed) * float(time)
            return f"Distance covered: {distance} units"
        elif distance and time:
            # Calculate speed
            speed = float(distance) / float(time)
            return f"Speed: {speed} units per time period"
        else:
            raise ValueError("Exactly 2 of the 3 variables (speed, distance, or time) must be given.")
    except ValueError:
        print("Invalid input. Please enter numeric/real world values only.")


# Call the function
if __name__ == "__main__":
    result = calculate_speed_distance_time()
    if result:
        print(result)
