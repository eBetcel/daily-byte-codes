def vacuum_cleaner_route(movements_string):
    """
    Given a sequence of movements, returns if a robot goes to the same spot

    Args:
        movements_string (str): The string of movements

    Returns:
        bool: The result of the verification

    Example:
        >>> vacuum_cleaner_rout("UD")
        True
    """

    robot_position = (0, 0)
    for move in movements_string:
        match move:
            case "U":
                robot_position = (robot_position[0], robot_position[1] + 1)
            case "D":
                robot_position = (robot_position[0], robot_position[1] - 1)
            case "R":
                robot_position = (robot_position[0] + 1, robot_position[1])
            case "L":
                robot_position = (robot_position[0] - 1, robot_position[1])

    return robot_position == (0, 0)
