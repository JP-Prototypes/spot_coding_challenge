"""Establish connection to bosdyn API and authenticate spot robot"""

from bosdyn.client import create_standard_sdk


def connect_to_spot(address, username, password):
    """connect to bosdyn api and authenticate spot robot

    Args:
        address  (str): Network-resolvable address of the robot, e.g. '192.168.80.3'.
        username (str): The username for authentication.
        password (str): The password for authentication.

    Returns:
        robot: The connected Spot robot instance.
    """
    # create SDK instance with specific name "SpotClient".
    sdk = create_standard_sdk("SpotClient")
    
    # create a robot instance initialized with the provided IP address and current SDK settings.
    robot = sdk.create_robot(address)
    
    # Authenticate robot with the provided username and password.
    robot.authenticate(username, password)
    
    # return robot to caller
    return robot
