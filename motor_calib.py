import pypot.dynamixel as pd

# get ports and start connection to motors
ports = pd.get_available_ports()
motors = pd.Dxl320IO(ports[0],1000000)

motor_id = motors.scan(range(20))

# only work with one motor at a time
if (len(motor_id)>1):
    print("Only connect one motor at a time!")
    quit()
motor_id = motor_id[0]

# set motor to 100
motors.set_goal_position({motor_id:100})
raw_input("Motor position: 100; Attach horn then press 'Enter'. ")

# set motor to 0
motors.set_goal_position({motor_id:0})
raw_input("Motor position: 0; Calibrate string length then press 'Enter'. ")

# set motor back to 100
motors.set_goal_position({motor_id:100})
print("Motor position: 100; Calibration complete!")
quit()