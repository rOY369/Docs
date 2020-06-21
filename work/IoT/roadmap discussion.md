
## Roadmap Tasks (3 months)

### Technical Debt

- Refactoring of Services
	- Bridge Service (Owner = Harsh)
	- Thermostat (Owner = Dishant)
	- Host Service (Owner = Dishant)
	- CICD (Owner = Priyam)
- Modular Design 
	- This will be backed by a software development process to be followed by the team which will guide us produce a high quality modular software. 
	- This process will involve the steps for 





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
eyJoaXN0b3J5IjpbMTk4MDc4MjU4MywtNDE0Nzg0NzY3LC03Mj
U2MjIxOTcsNTU5NTQ0MTAsMTQ2MjU0ODI4LC0zODIzMjc1NDMs
MTIxNDU0ODQ5OSw1ODg0NDEzNDddfQ==
-->