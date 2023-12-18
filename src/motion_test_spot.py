"""Access spot robot and make it move"""

''' commented for future use

#import time
#from bosdyn.geometry import EulerZXY
from bosdyn.client.robot_command import RobotCommandBuilder
'''
import bosdyn.client
from bosdyn.client.robot_command import RobotCommandClient, blocking_stand

def motion_test_spot(robot):
    """
    Establishes E-Stop, lease and power on.
    Make Spot stand.

    Args:
        robot (Robot): The connected Spot robot instance.
    """
    # Configuring Motor Power Authority "E-Stop" for motion control.
    estop_client = robot.ensure_client('estop')
    estop_endpoint = bosdyn.client.estop.EstopEndpoint(client=estop_client, name='my_estop', estop_timeout=9.0)
    estop_endpoint.force_simple_setup()
    estop_keep_alive = bosdyn.client.estop.EstopKeepAlive(estop_endpoint)
    
    # Configuring a lease to aquire ownership of the robot.
    lease_client = robot.ensure_client('lease')
    lease = lease_client.acquire()
    lease_keep_alive = bosdyn.client.lease.LeaseKeepAlive(lease_client)
    
    # Power on robot and synchronize time
    robot.power_on(timeout_sec=20)
    robot.time_sync.wait_for_sync()
    
    # Create a RobotCommandClient to send commands to the robot
    # Ensure a Client for a given service.
    command_client = robot.ensure_client(RobotCommandClient.default_service_name)
    
    # Command the robot to perform a basic stand
    blocking_stand(command_client, timeout_sec=10)
    
''' commented for future use

    # define spot motion command --> rotate clockwise arouned z axis (yaw) with by 0.4 radians ~ 23 degrees
    footprint_R_body = EulerZXY(yaw=0.4, roll=0.0, pitch=0.0)
    
    # build motion command and command Spot to perform the built command --> yaw +0.4 radians
    cmd = RobotCommandBuilder.synchro_stand_command(footprint_R_body=footprint_R_body)
    command_client.robot_command(cmd)
    
    # Build and send the sit command to the robot
    cmd = RobotCommandBuilder.sit_command()
    command_client.robot_command(cmd)
    
    # wait 5 seconds after sitting before power off command
    time.sleep(5)
    
    # Power off
    robot.power_off(cut_immediately=False)
'''
