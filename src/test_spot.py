"""Test SDK connection, robot authentication and motion control by commanding spot to sit"""

from authenticate_spot import connect_to_spot
from motion_test_spot import motion_test_spot

# Replace with your actual robot IP, username, and password
address = "Robot IP-Address"
username = "username"
password = "password"

# connect to bosdyn API
# authenticate credentials
robot = connect_to_spot(address, username, password)

# perform motion control
# Establishes E-Stop, lease and robot power on.
# Makes Spot stand.
motion_test_spot(robot)