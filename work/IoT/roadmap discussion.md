
## Roadmap Tasks (3 months)

### Technical Debt

- Refactoring of Services
	- Bridge Service (Owner = Harsh)
	- Thermostat (Owner = Dishant)
	- Host Service (Owner = Dishant)
	- CICD (Owner = Priyam)
- Modular Design 
	- This will be backed by a software development process to be followed by the team which will guide us produce a high quality modular software. 
	- This process will involve the steps and guidelines related to designing of software components, testing style and other themes which will play an important role in ensuring high quality software. 
	- Team will spend 1.5 months to come up with this process. 
	- Next 1.5 months will be spent on taking some services through this process. 
	- Exact number and which services will be decided based upon the process needs (time and effort) and service condition. 
	- Services which will be considered to work upon through the process :
		- Application
			- Data pipeline
			- Diagnostics
			- Modes
		- 





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
eyJoaXN0b3J5IjpbNzcwMjUwOTIyLC04OTAyMTQzMDYsLTQxND
c4NDc2NywtNzI1NjIyMTk3LDU1OTU0NDEwLDE0NjI1NDgyOCwt
MzgyMzI3NTQzLDEyMTQ1NDg0OTksNTg4NDQxMzQ3XX0=
-->