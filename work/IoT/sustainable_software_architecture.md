
## Why Software Architecture ? 

**The lack of architecture bonds the organisation or the team inescapably to its past.**
-	Our legacy : Haphazard systems
-	These systems are expensive and hard to change.
-	Drag 
	-	Long and unpredictable development times. 
	-	Ambiguous behaviour 
	-	Unable to adapt to the environment

**Organisational Purpose**
- Communicating high-level design to stakeholders, tech-support, quality assurance and even customers.
	- Even large and complex architectures can be conveyed using presentation slides and documented using an A4. 
- Providing system context for developers and future maintainers 
- Work Allocation 
	- Decomposed system into substructures that are relatively independent with clear responsibilities and limited number of well-defined interfaces to communicate

**Technical Purpose**
- Meet system requirements and objectives
- Enable flexible distribution/partitioning of the system 
- Reduce cost of maintenance and evolution
	- Anticipating main kinds of changes that will occur in the system at the architecture level, ensuring the design will facilitate such changes.
	- And localising as far as possible the effects of such changes on design documents, code and other parts of the system. 
- Increase reuse and integration with third-party software. 

## What is Software Architecture ? 

*All architecture is design but not all design is architecture.*
*The significant design decisions that shape a system, where significant is measured by cost of change.*

**Cost of change**
- Time 
- Energy
- Mental Stress
- Satisfaction 

*It is mainly spending more time on the whiteboard, diagrams, maps and models before hitting the keyboard.*
*What we do in the name of architecture, shapes what it is; what we think it is, shapes what we do*

## Design 

**Decision Template**
- **Title** :
	- Short Phrase
	- Up-front design approach in software development
- **Context** : 
	- Describe the forces at play probably in tension 
	- Every now and then, we realise that the quality of our software does not meet the standards. In order to create a modular, adaptable, clean and robust system we need to change the way we approach development. 
- **Decision** : 
	- Describe our response to the forces. 
	- Adapt and switch to a more disciplined approach like up-front design. 
- **Status** :
	- Proposed
- **Consequences**
	- Describe the resulting context after applying the decision. 

<img src="https://www.tutorialspoint.com/system_analysis_and_design/images/top_down.jpg" width="500px" height="300px" />

**Modular Structure reduces cost of change.**
- Isolate impact of change. 
- Isolate arenas of uncertainty and experiment. 
- Increase reversibility and replaceability 
- Increase responsiveness/adaptability 
- Reduce complexity 
	- Abstractions
	- Crisp, disentangled and simple

**How to create this structure ?**

Design things to make their performance as insensitive to the unknown or uncontrollable external influence as practical.
*Architecture requirements <--> Architecture specification <--> Architecture validation* 

**Design Document 1 : Separation of Concerns : Architecture Requirements/Basis**
- Understanding the problem domains being served by the system/software 
- Business Agenda
- User
	- Requirements and Concerns
- Product
	- Goals
	- Vision
	- Principles
- Cross-functional teams
	- Tech support
	- System intelligence 
- The system value proposition 
	- Top-level high-priority goals are translated into a set of use-cases which are used to document functional requirements. 
	- The system structure fails if it does not support the services or functionality that users value or if the qualities associated with the functionality are unsatisfactory. 
	- System qualities like performance and security are also important in directing architectural choices. 
	- Future requirements that the architecture will need to support will also be mentioned.  
- Document Form : 
	- Top-level high priority goals / Non-Functional requirements
		- System attributes like security, reliability, performance, maintainability, scalability, and usability
	- Use cases / Functional requirements
		- Specification of behaviour 
		- Specification of particular results of the software
- Continuous Improvement
	- Adding new requirements/feature requests

**Design Document 2 : Meta-Architecture**
- Architectural vision 
- research 
	- Architectural styles 
	- Patterns
	- Dominant Designs
	- Reference Architectures 
	- Concepts, Mechanisms and Principles
- Document
	- Will guide the architecture team during the next steps of structuring. 
- Continuous Improvement
	- Consistently explore new designs and patterns
	- Updating this document

**Design Document 3 : Conceptual Architecture**

-  Components and Responsibilities
- The responsibility of architecture is architecture of responsibilities. 
- Useful vehicle for communicating the architecture to non-technical audience/management
- 2 Directions
	- Start with a first cut notion of components the system will need and identify allocate responsibilities to them. 
	- OR start with responsibilities from what the system needs to do and factor to find components.
- Ask : Does this component have a cohesive identity or purpose - a single responsibility ? 
- Document Form
	- CRC Cards
	- Class Diagrams
- Continuous Improvement
	- Update the responsibilities for each component as more is learned as the system is explored and built out.

**Design Document 4 : Logical Architecture**
- Detailed, actionable, unambiguous and complete architecture specification 
	- Defining component interfaces
	- Connection mechanisms and protocols
	- Exploring behaviour
		- Interaction between components
		- How will it work ?
- Document
	- Sequence Diagrams
	- Flow charts
	- Component Specifications
		- Summary description of services the component provides
		- A description of the operations
			- Constraints or pre-post conditions for each operation
		- How the component is instantiated
		- How it is named
		- A typical use scenario
		- Exceptions
		- Owner 
		- Test cases

**Note : Architecture trade-off analysis**
At each step in structuring, it is worthwhile challenging our creativity to expand the solution set under consideration. And then evaluating different alternatives against the prioritised requirements. Selection of the best solution generally involves some compromise but it is best to make this explicit and worth mentioning in the design document. 


**Design Document 6 : Testing Resilience/Architecture Validation**

- Thought experiments with anticipated changes. 
- Assessing impact against current components and their responsibilities to see how well we are doing in isolating change.
- Use lens of various views (Use separation of concerns)
	- Security 
	- Responsiveness 
	- Load spikes 
	- Scope of optimisation 
	- Highly configurable 
- Change of perspective 
	- Invite peers to share what is learned and seek out opportunities and weaknesses that were missed. 
	- Assessment by Experts
	- We need to adopt the discipline of not just accepting our initial understanding, but rather seeking different understandings.
- Exploring behaviour
	- How does this approach contribute to desired system properties and yield needed system behaviours ?
- Document
	- Review
	- Thought experiments with anticipated changes
- Continuous Improvement :
	- Visualise and track changes to see how well the abstractions hold up. 

## Test Cases --> Test Driven Development
## Integration Testing
## Coding Style Guide 
## CICD
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMjUxOTcyMjQsLTEzOTk4MjIwNDgsLT
Y5NDE2NzcyMSwxNzI5NDAxMjQ1LDE4OTQyODYxMCwtMTA0Nzgz
ODA0NiwtMTc1MjcwNjQwNiwzNjIwNjQyMTYsMTE0OTQzNTIxMi
wxNDg0NDAwNzU1LC0xMjA5NDg1MywxOTYwNDUxMjksNDk3ODE4
ODEwXX0=
-->