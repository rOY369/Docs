
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

### Continuous Reliability 

- Data and Commands
	- Setting up reasonable metrics
	- Consistently improving these metrics
- Reliability of NAS
	- SSD unmount (How exactly will we resolve this ?)
- Reliability of JB
	- Finding root cause of JB container stuck issue
	- Introduce a timeout in controllers after which if there is no response from Joulebox container, QOS service will be triggered to save the old data to be sent later when Joulebox container is back online. 


## Vision, Next 6 months steps

- Reliability
- Scalability
	- Software
	- Architecture
- Modularity
	- Software
		- Easy to read and understand 
		- Easy to modify and maintain 
		- Easy to integrate new features
		- Less coupling
	- Architecture
- Technical Debt
	- Refactoring
		- Code should be Easy to read and understand
		- Removing redundancies
	- Quality Unit testing
	- Documentation
		- Code documentation
		- Service documentation
- Software Development Process
	- Design
	- Code Development Pipeline
	- Code Deployment Pipeline
- Setting up Reasonable Metrics
	- Working on Improvements
- Hardware Agnostics

## Known-Known

- Reliability
	- Software Reliability
		- Query transaction 
		- Bottlenecks in terms of data and commands reliability
	- Improve reliability of NAS and JB
		- SSD unmount
		- Root cause of JB container stuck issue
		- Flag timeout when JB is stuck
- Scalability
	- Modularity
		- Software design
		- Feature toggling
		- code optimisation
	- Joule Recipe Load
			- *Alert recipes on server*
			- Minimising unnecessary processing of recipes
				- *Example. use maintenance mode*
			- *Run recipes in NAS controllers*
- Hardware agnostic
	- Software dependencies
		- System services as docker
		- Host database as docker
- Security
	- Client Authentication
	- MQTTS
	- Data encryption

## Known-unknowns

- Modularity
	- Reliability gained to modularity
- Issues in previous Rpi System
	- Improvements in the new system
- Hardware agnostic 
	- SOM or third party ?
- Security
	- Any other critical measures 
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjEzNzU0MDIzLDIwOTU3ODQwNzEsLTg5MD
IxNDMwNiwtNDE0Nzg0NzY3LC03MjU2MjIxOTcsNTU5NTQ0MTAs
MTQ2MjU0ODI4LC0zODIzMjc1NDMsMTIxNDU0ODQ5OSw1ODg0ND
EzNDddfQ==
-->