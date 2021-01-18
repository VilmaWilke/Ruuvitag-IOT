import AzureIoTDeviceClientPY.DeviceClient as DeviceClient
import datetime, requests
from ruuvitag_sensor.ruuvi_rx import RuuviTagSensor
from ruuvitag_sensor.ruuvitag import RuuviTag
import json
import time


# START: Azure IoT Hub settings
KEY = "KEY";
HUB = "HUB";
DEVICE_NAME = "NAME";
# END: IoT Hub Settings

#List of MAC addresses to collect data for
macs = ['MAC ADDRESS']
timeout_in_sec = 5

def get_sensor_data():
	datas = RuuviTagSensor.get_data_for_sensors(macs, timeout_in_sec)

	#Create valid SAS token
	device = DeviceClient.DeviceClient(HUB, DEVICE_NAME, KEY)
	device.create_sas(600)

	#Encode in to a format that Azure accepts
	encode_weatherdata = json.dumps(datas, indent=1).encode('utf-8')

	#Device to Cloud
	print(device.send(encode_weatherdata))
	
	
while True:
	#Simple loop to indefinetly send data every 60 seconds
	get_sensor_data()
	time.sleep(60)
