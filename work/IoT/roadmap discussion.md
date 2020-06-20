
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
eyJoaXN0b3J5IjpbLTQxNDc4NDc2NywtNzI1NjIyMTk3LDU1OT
U0NDEwLDE0NjI1NDgyOCwtMzgyMzI3NTQzLDEyMTQ1NDg0OTks
NTg4NDQxMzQ3XX0=
-->