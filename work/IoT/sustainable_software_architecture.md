
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

*It is mainly spending more time on the whiteboard, diagrams, maps and models before hitting the keyboard. *
*What we do in the name of architecture, shapes what it is; what we think it is, shapes what we do*

## How ? 

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

- Adapters at the system boundary 
- Abstractions : Boundaries within the boundary must be invented to give our system internal form.

**Design Document 1 : Separation of Concerns : Understanding the problem domains being served by the system/software**
- User
	- Requirements
- Product
	- Goals
	- Vision
	- Principles
- Cross-functional teams
	- Tech support
	- System intelligence 
- Continuous Improvement

**Design Document 2 : Components and Responsibilities**

- 2 Directions
	- Start with a first cut notion of components the system will need and identify allocate responsibilities to them. 
	- OR start with responsibilities from what the system needs to do and factor to find components.
- Continuous Improvement
	- Update the responsibilities for each component as more is learned as the system is explored and built out.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA0NDA2ODQ1MCwtMTIwOTQ4NTMsMTk2MD
Q1MTI5LDQ5NzgxODgxMF19
-->