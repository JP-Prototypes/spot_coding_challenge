----- Prerequisit information -----

Spot Python SDK works with Python 3.6, Python 3.7 and 3.8.

Please ensure the correct Python version is installed.

windows env:
py.exe --version
py.exe -3.6 --version

Check pip version:
py.exe -3.6 -m pip --version

Please ensure the spot-sdk is updated:
git bash in working directory
git submodule update --init --recursive

Install virtualenv:
cmd in working directory
py.exe -3.6 -m pip install virtualenv

Create virtualenv "my_spot_env":
py.exe -3.6 -m virtualenv my_spot_env

Activate virtualenv:
call "my_spot_env\Scripts\activate.bat"

Deactivate virtualenv:
call "my_spot_env\Scripts\deactivate.bat"

----- Install dependencies on virtual env -----

Set-up:
Activate virtualenv
cd src
pip install -r requirements.txt <-- this will install the required packages for the project.

Verify dependency installation:
pip list --format=columns | findstr bosdyn

Expected output:
bosdyn-api                 3.3.2
bosdyn-client              3.3.2
bosdyn-core                3.3.2

additional packages can be installed if needed:
pip install bosdyn-client==3.3.2 bosdyn-mission==3.3.2 bosdyn-choreography-client==3.3.2

bosdyn-choreography-client 3.3.2
bosdyn-choreography-protos 3.3.2
bosdyn-mission             3.3.2

note: not all of the packages above are strictly needed for this challenge, however it is documented for completeness.

----- Script Clarification -----

authenticate_spot.py --> creates a SDK instance followed by a robot instance and then authenticates the robot instance.
input arguments are IP-Address of the robot, username and password.

motion_test_spot.py --> configures E-Stop and lease, then checks service availability for the given client.
                        once complete, power spot on, commands spot to stand.
input argument is a robot instance.

test_spot.py --> sets the IP-address, username and password for the robot.
                 calls connect_to_spot to connect and authenticate.
                 calls motion_test_spot to perform the motion routine. 

----- Run Test Script -----

open test_spot.py in an editor and input robot IP-Address, username and password.

in src directory using the virtual env previously configured, input to terminal:
python test_spot.py

expectation: connect to spot, authenticate sucessfully, enable motors and stand. 
(motion commands for yaw, sit and shutdown are currently commented)

