## TEMPERATURE/HUMIDITY SENSOR DEVICE TECHNICAL REQUIREMENTS

  

### OVERVIEW

The temperature and humidity sensor device needs to maintain its connection with the local IoT network. This is majorly because the automation logic process running inside controllers i.e. `JouleRecipe` requires the data from the sensor to be present in the `Network Attached Storage`. The only way the sensor device can run compatible with the current architecture is that it participates in the local IoT network and publishes the data in that local network itself.

The following sections in the document are the technical requirements for this sensor device. The requirements have been divided into 3 categories -

- ***Absolute Critical Requirement
- **Critical Requirement
- *Good-to-have Requirement

### PARAMETERS (DATA)***

- Temperature in degree Celsius
	- Temperature Accuracy: ± 0.5 degree C or Better  
	- Temperature Range (Operating): -40 degree C to 85 degree C  
	- Temperature Range (Functional): -40 degree C to 125 degree C
- Humidity in % RH
	- RH Range: 0% to 100%  
	- RH Accuracy: ± 2%  

### ARCHITECTURE COMPATIBILITY***

- Interface : WiFi
	- The SSID and Password of the WiFi to connect with should be easily configurable.

- Protocol: MQTT
	- The device has to be connected to the local network through MQTT.
	- The MQTT connection has to be established between the device and the mosquitto broker running inside a controller with `hostname=smartjoules.local` on `port=1883`.

- Device Configuration :
	- User should be able to configure the following information somehow in the device such that it is stored in non-volatile memory like `FLASH` or `EEPROM` of the device for future use.
	- `DeviceId`
		- Each sensor device has a unique `deviceId` which is generated from the backend on registering the device onto our cloud portal JouleTrack(Dejoule).
	- `SiteId`
		- Each site has a unique `siteId`.
		- All sensor devices in a site have to be aware of this `siteId`

- Data Format
	- Topic : `data/<deviceId>/recent`
	- Payload (string) :
		- The `"<tmp>"` and `"<hum>"` values mentioned in the data packet below represent temperature and humidity values respectively. These can be of type float up to 2 decimal places.
```
{
"deviceId": "<deviceId>",
"siteId": "<siteId>",
"timestamp": "<YYYY-MM-DD HH:MM:00>",
"captured_at": "<YYYY-MM-DD HH:MM:SS>",
"data": {
"tmp": "<tmp>",
"hum": "<hum>",
}
}
```

- Data frequency = 1 minute(default)/Should be configurable

### Data Quality-of-Service(QOS)**

This service makes sure that the data quantity index is not compromised even if the device is not able to connect to the local network broker. Whenever the device is not able to connect to the broker due to some reason, it saves every minute data in a safe memory like an SD card. At the point, it gets reconnected to the broker it publishes all the old data back to the broker. The service should be able to upload old data of up to at least 3 days. 

**Data Format**

- Topic : `data/<deviceId>/old`
- Payload (string) :

```
{
"deviceId": "<deviceId>",
"siteId": "<siteId>",
"timestamp": "<YYYY-MM-DD HH:MM:00>",
"captured_at": "<YYYY-MM-DD HH:MM:SS>",
"data": {
"tmp": "<tmp>",
"hum": "<hum>",
}
}
```

- The `"<tmp>"` and `"<hum>"` values represent temperature and humidity values respectively. These can be of type float up to 2 decimal places.
- Data frequency = 1 minute(default)/Should be configurable

### Secure OTA firmware updates***

The requirement is that the device should be enabled with a feature where we can push the firmware updates remotely over the secure channel and there should be no manual work of any kind be required for pushing this firmware update onto the device.
  
### Logs*
  
The requirement is to have the device send the following logs to the local network broker.

**Wifi Signal Statistics**

- Network Strength: A number indicating the strength of the WiFi connection device has made with the local network.
- Link Quality: Gives an indication of the quality of data packets received by the device.
- Data frequency = 1 minute(default)/Should be configurable

**Event-based logs**

- Recalibration event: This would log the event when the device started with the sensor data recalibration process having received the command for recalibration.
- MQTT Broker Disconnect/Connect: This would log the event when the device gets disconnected/connected from MQTT local network broker.
-Reboot/Restart: This would log the event when the devices restart or get rebooted manually.

### Sensor data filter service (To ensure high data quality and accuracy)*

The requirement is to have a filter service handling sensor data outliers and sensor value going out of calibration. This requirement is subject to how the device sensor performs in the site environments. The re-calibration of the filter service should be possible via a trigger over the MQTT channel if needed.


### Future Scopes*

**Security** : Secure and encrypted data packets transmission between the Temp/Hum device and our controller running the MQTT local network broker. The encryption methodologies and algorithms on which the communication has to take place will be shared with the partner company team prior to our migration to encrypting our communication channel.

**Possible future security measures**
- Data encryption
- MQTT Client authentication with broker
