
IoT command reliability 
- Number of commands
- Command success 
	- status 4 + status 1
- Wrong mode
	- status 8
- command failures
	- Total failures : status 3 + status 0 + status 6 
		- x commands reached firmware and processed without any error. These commands failed to execute possibly due to a fault in the equipment. 
	- Failures due to asset
		- VFD mode is off
			- Firmware executes the command successfully.
			- How to detect this mode ?
					- Need to recheck 
		- VFD mode (manual)
			- `automanual` data parameter of vfd
			- Firmware executes command successfully.
		- VFD powered off
			- Firmware logs command status as False with  `logType write (OSError)`
			- `data = "null"`
		- Modbus communication error
			- Firmware logs command status as False with  `logType write (OSError)`
			- `data = "null"` (possibility)
		- VFD bypass mode
			- `data = "null"`
		- 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgxMDYwODA1OSw5NDIzNjczODgsLTg4OD
Q3MjQwOCw3MDM4NTgzODksNTYwODY1NDE4LC05NzQ3MjI4ODFd
fQ==
-->