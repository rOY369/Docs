

### Finalising site and region


- Site Preferences
	- Which is not handed over to client
	- Which is nearby (Delhi NCR)
	- Where deployment team/maintenance team is active
	- Where DQI in general is low
	- Where internet connectivity is reliable.
	- FORTIS Noida 
- Region Preferences
	- Where site team has reported maximum times of device restart cases. (Manash + SI Team)
		- Ensure no power supply problems or any other physical problems in the region (Manash)
		- Confirm with SI team
	- Where network parameters (network strength + `link quality` +`ping_to_gateway` + `hostname_resolve_time`) is average. (Between 60% - 100%) (SI Team)
		- It should be good enough to at least carry out the tests.
- Controller Preferences
	- Where resource consumption on avg. is more (Must-have)
	- Specifications should be at least Rpi-3. (Must-have)
	- Where most number of recipes are running. (Good-2-have)
	- Where there is a large number of slave devices connected to the controller.  (Good-2-have)
	- Where there is a large number of watchdog triggers. (Good-2-have)


### Tests 

- Raspberry Pi Hangup
	- Performance
		- Figure out possible reasons behind high resource consumption. 
		- Mock the same pattern in som.
		- Compare som resource consumption with Rpi controller resource consumption. 
	- Uptime
		- Device restart log
	- Watchdog Triggers
		- Figure out possible reasons behind large number of watchdog triggers.
		- If there is a specific combination or pattern, mock it in som. 
		- Compare the results.
	- Boot time
		- Difference between device Restart time and acknowledgement of all watchdog triggers
		- A better procedure/parameter ?
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
	- disable other nas controllers

### Changes in Software (Logs Integration)
- D2RS ssd unmount log (1 week)
- nas connection status ??
- Under voltage log
- `ping_to_gateway` + `hostname_resolve_time`
- `cpu_load`
- `used memory (MB)`
- Better procedure to calculate boot time. 

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
eyJoaXN0b3J5IjpbMTQ5MjE1NDkxMiwyMDQ1MTQxNTE3LDEzMj
g2OTUzMzUsMTEyNTQwNTQyNiw5NDAzNzg0NjcsMzU2MDg4MDMy
LC0xODcwMjUxOTc5LC0xMzMwNDQyNTcwXX0=
-->