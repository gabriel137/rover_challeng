# Rovers Control

This is a small Python application that allows you to control rovers on Mars through a series of commands.

## Installation - Manual

Make sure you have Python installed on your system. You can download it from https://www.python.org/downloads/.

Download the source code of this project.

Install the dependencies by running the following command in the project folder:

```
 pip install -r requirements.txt
```

## Installation - Docker

To run the application using Docker, follow these steps:

1. Build the Docker image:

```
    docker build -t rover_app_image .
```

2. Run the Docker container interactively:

```
    docker run -it --rm rover_app_image
```

3. You should see output in the terminal like

```
    Enter 'file' to read data from a file, or press Enter to enter data manually: file
```

4. Write file and press enter

5. You should see output in the terminal like

```
    Enter the name of the input file:
```

6. write the path

```
    ./assets/static/input.txt
```

## Usage

There are two ways to run the application: manually or from an input file.

### Manual Execution:

To run the application manually, follow the instructions below:

1. Open a terminal or command prompt in the project folder.

2. Run the following command to start the application:

```
    python app/main.py
```

3. Follow the instructions in the terminal to provide the necessary information about the plateau and the rovers.

4. After entering all the information, the results of the rovers' movements will be displayed in the terminal.

### Execution from an Input File:

If you prefer to provide the input data from a text file, follow the instructions below:

1. Create a text file with the following format:

```
    [plateau size (x y)]
    [rover 1 position (x y direction)]
    [rover 1 instructions]
    [rover 2 position (x y direction)]
    [rover 2 instructions]
```


For Example:

```
    5 5
    1 2 N
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM
```

2. Save the file with the name "input.txt" in the project folder /assets/static/input.txt.

3. Open a terminal or command prompt in the project folder.

4. Run the following command to start the application from the input file:


```
    python app/main.py
```

Choose "file" in options and write your input file name (e.g., your-file.txt). An example input.txt is provided in the app/ folder for your convenience.

# Running Tests

- To run the automated tests, execute the following command in the project folder:

```
    pytest
```
