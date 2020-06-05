
DeJoule reliability 
- Number of commands
- Command success 
	- status 4 + status 1
- Wrong mode
	- status 8
- command failures
	- status 3 + status 0 + status 6 
	- Failures due to software - 
	- Failures due to asset -  
		- asset off
		- asset mode (manual)
			- `automanual` data parameter of vfd.
		- modbus communication error
			- logType write (OSError)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwODg4MTE2ODAsLTE5ODYwMzY4NjcsLT
IwNjgxNTc1MjcsNDk3ODE4ODEwXX0=
-->