from director import Director
from gaming_computer_builder import GamingComputerBuilder
from cheap_computer_builder import CheapComputerBuilder

computerBuilder = Director(GamingComputerBuilder())
computerBuilder.build_computer()
computer = computerBuilder.get_computer()
computer.display()

computerBuilder = Director(CheapComputerBuilder())
computerBuilder.build_computer()
computer = computerBuilder.get_computer()
computer.display()
