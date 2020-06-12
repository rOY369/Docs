

### Finalising site and region

*Should all tests and metrics be carried out in one region and in one controller ?*

- Site Preferences
	- Which is not handed over to client
	- Which is nearby 
	- Where deployment team/maintenance team is active
	- Where DQI in general is low
	- Where internet connectivity is reliable.
- Region Preferences
	- Where site team has reported maximum times of device restart cases. 
		- Ensure no power supply problems or any other physical problems in the region
		- Confirm with SI team
	- Where network strength is average. (Between 60% - 100%)
		- Network strength should be good enough to at least carry out the tests.
- Controller Preferences
	- Where resource consumption on avg. is more than x. 
	- Where number of recipes running are at least x. 
	- Where there is a large number of slave devices connected to the controller. 
	- Where there is a large number of watchdog triggers.


### Tests 
- Performance
	- Figure out possible reasons behind high resource consumption. 
	- Mock the same pattern in som.
	- Compare som resource consumption with Rpi controller resource consumption. 
	- Any possible change in system logs ( cpu, ram, disk) ? 
- Uptime
- Watchdog Triggers
	- Figure out possible reasons behind large number of watchdog triggers.
	- If there is a specific configuration 
### Changes in Software (Logs Integration)
### Other pre-requisite measures
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4ODQ0ODcwNjUsLTE4NzAyNTE5NzksLT
EzMzA0NDI1NzBdfQ==
-->