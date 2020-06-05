
DeJoule reliability 
- Number of commands
- Command success 
	- status 4 + status 1
- Wrong mode
	- status 8
- command failures
	- Total failures : status 3 + status 0 + status 6 
		- from which 
	- Failures due to asset -  
		- asset off
		- asset mode (manual)
			- `automanual` data parameter of vfd.
		- modbus communication error
			- logType write (OSError)
	- Failures due to software 
		- Total failures - failures due to asset
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDQ3MTc4NzcxLC0xOTg2MDM2ODY3LC0yMD
Y4MTU3NTI3LDQ5NzgxODgxMF19
-->