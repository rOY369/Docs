
DeJoule reliability 
- Number of commands
- Command success 
	- status 4 + status 1
- Wrong mode
	- status 8
- command failures
	- Total failures : status 3 + status 0 + status 6 
		- x commands reached firmware and processed without any error. These commands failed to execute possibly due to a fault in the equipment. 
	- Failures due to asset
			- asset off
			- asset mode (manual)
				- `automanual` data parameter of vfd.
			- modbus communication error
				- logType write (OSError)
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzgyNzMwMDgzLDk4Njk5NTMxOCwxMjk0OD
kwNjYwLC0xOTg2MDM2ODY3LC0yMDY4MTU3NTI3LDQ5NzgxODgx
MF19
-->