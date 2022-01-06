import time
from dronekit import connect, VehicleMode, LocationGlobalRelative

#connection_string='tcp:127.0.0.1:5760'
connection_string='udp:127.0.0.1:14552'
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True)

vehicle.airspeed = 10
print("Close vehicle object")
vehicle.close()
