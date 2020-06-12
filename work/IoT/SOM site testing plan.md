

### Finalising site and region

*Should all tests and metrics be carried out in one region and in one controller ?*
- depends on usage as normal controller or as a nas controller

- Site Preferences
	- Which is not handed over to client
	- Which is nearby (Delhi NCR)
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

- Raspberry Pi Hangup
	- Performance
		- Figure out possible reasons behind high resource consumption. 
		- Mock the same pattern in som.
		- Compare som resource consumption with Rpi controller resource consumption. 
		- Any possible change in system logs ( cpu, ram, disk) ? 
	- Uptime
	- Watchdog Triggers
		- Figure out possible reasons behind large number of watchdog triggers.
		- If there is a specific combination or pattern, mock it in som. 
		- Compare the results.
	- Boot time
		- Difference between uptime and time host_service creates the first log
	- Data Quantity
	- Power fluctuation
- Network Latch out
	- Network Strength
	- Link Quality
	- Power Fluctuation 
	- Data Quantity
- SSD unmount
	- D2RS ssd unmount log to be run for 1 week at least before starting the test
	- Nas connection status log ?
	- Power fluctuation
	- Recipes commands reliability

### Procedure

- Finalise the site and controller with SOM 
- Configure it with the same controller ID
- Replace it on site
- Run it for 1-1.5 weeks as general controller and conduct tests except ssd unmount
- Re-configure it as a NAS controller. 
- Run it as NAS master for 1-1.5 weeks and conduct ssd unmount test. 
	- 

### Changes in Software (Logs Integration)
- D2RS ssd unmount log

### Other pre-requisite measures/requirements
- All software repo tags for SOM to be deployed
- remote 3 ?
- CICD should be tested
- reverse ssh should be tested
- Firmware for SOM should be ready and tested
- Contact deployment team beforehand 
- Contact site teams beforehand (data/commands could be non-reliable)

### Timeline

2-3 weeks testing.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMwNzgwMDQ1NCw5NDAzNzg0NjcsMzU2MD
g4MDMyLC0xODcwMjUxOTc5LC0xMzMwNDQyNTcwXX0=
-->