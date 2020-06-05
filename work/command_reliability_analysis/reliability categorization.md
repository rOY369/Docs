
DeJoule reliability 
- Number of commands
- Command success 
	- status 4 + status 1
- Wrong mode
	- status 8
- command failures
	- Total failures : status 3 + status 0 + status 6 
		- from which x commands got executed in firmware successfully --> should be equal to failures due to asset
	- Failures due to asset -  
		- asset off
		- asset mode (manual)
			- `automanual` data parameter of vfd.
		- modbus communication error
			- logType write (OSError)
	- Failures due to software 
		- Total failures - failures due to asset
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI5NDg5MDY2MCwtMTk4NjAzNjg2NywtMj
A2ODE1NzUyNyw0OTc4MTg4MTBdfQ==
-->