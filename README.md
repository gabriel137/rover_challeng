# Rovers Control

- This is a small Python application that allows you to control rovers on Mars through a series of commands.

# Installation

Make sure you have Python installed on your system. You can download it from https://www.python.org/downloads/.

Download the source code of this project.

Install the dependencies by running the following command in the project folder:

- pip install -r requirements.txt

# Usage
There are two ways to run the application: manually or from an input file.

# Manual Execution:
## To run the application manually, follow the instructions below:

To run the application manually, follow the instructions below:

Open a terminal or command prompt in the project folder.

Run the following command to start the application:

- python app/main.py

Follow the instructions in the terminal to provide the necessary information about the plateau and the rovers.

After entering all the information, the results of the rovers' movements will be displayed in the terminal.

# Execution from an Input File:

- If you prefer to provide the input data from a text file, follow the instructions below:

# Create a text file with the following format:

[plateau size (x y)]
[rover 1 position (x y direction)]
[rover 1 instructions]
[rover 2 position (x y direction)]
[rover 2 instructions]

# For Example
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM


Save the file with the name "input.txt" in the project folder.

Open a terminal or command prompt in the project folder.

Run the following command to start the application from the input file:
python app/main.py file

#Running Tests

- To run the automated tests, execute the following command in the project folder:
pytest
