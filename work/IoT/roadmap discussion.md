
## Roadmap Tasks (3 months)

### Technical Debt

- Refactoring of Services (Readable code + unit test + code documentation + service documentation)
	- Bridge Service (Owner = Harsh)
	- Thermostat (Owner = Dishant)
	- Host Service (Owner = Dishant)
	- CICD (Owner = Priyam)
- Modular Design 
	- This will be backed by a software development process to be followed by the team which will guide us produce a high quality modular software. 
	- This process will involve the steps and guidelines related to designing of software components, testing style and other themes which will play an important role in ensuring high quality software. 
	- The process will make sure that software is  : 
		- Easy to read and understand 
		- Easy to modify and maintain 
		- Easy to integrate new features
		- Less coupled
		- Easy to optimise
		- Configurable (Feature toggling)
	- Team will spend 1.5 months to come up with this process. 
	- Next 1.5 months will be spent on taking some services through this process. 
	- Services which will be considered to work upon through the process :
		- Application
			- Data pipeline
			- Diagnostics
			- Modes
		- CEP (Command Execution Pipeline)
		- QOS
		- Feedback
		- Firmware L4
		- Common Libraries
			- Database Interface
			- MQTT
	- Exact number and which services out of those mentioned above will be decided based upon the process needs (time and effort) and service condition.
	- Both services inside architecture and inter services architecture will be considered in the above process.

### Reliability 

- Data and Commands
	- Setting up reasonable metrics
	- Consistently improving these metrics
- Reliability of NAS
	- **SSD unmount (How exactly will we resolve this in Rpi systems?)
- Reliability of JB
	- Finding root cause of JB container stuck issue
	- Introduce a timeout in controllers after which if there is no response from Joulebox container, QOS service will be triggered to save the old data to be sent later when Joulebox container is back online. 

### SOM

### Scalability 

- Better Handling of Joule-Recipe Load
	- Shift alert recipes on server*
	- Minimising unnecessary processing of recipes
		- Recipe should not run if the mode is not `joule recipe`
		- Possible solution : Use maintenance card/modes to play pause the recipes*
	- Ability to run recipes in NAS controllers

### Hardware Agnostic

- System services as docker**
- Host database as docker**

### Code Development and Deployment Pipeline

### Security

- Client Authentication
- MQTTS
- Data encryption

### Features

###  Known-unknowns

- Modularity
	- Whether modular design will increase reliability or not, will increase efficiency or not -- is unknown. 
	- It will be a challenge for modular design process to ensure higher reliability as well as efficiency in the new designs and its implementation. 
- Issues due to limitations in previous Rpi System and whether these will be solved with the new hardware or not.  
- Hardware agnostic 
	- SOM or third party ?
- Security
	- Any other critical measures 


```
* --> Dependent on other teams
** --> Doubt --> Needs internal discussion before final edit
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY2OTQ5NzIwMCwyMDk1Nzg0MDcxLC04OT
AyMTQzMDYsLTQxNDc4NDc2NywtNzI1NjIyMTk3LDU1OTU0NDEw
LDE0NjI1NDgyOCwtMzgyMzI3NTQzLDEyMTQ1NDg0OTksNTg4ND
QxMzQ3XX0=
-->