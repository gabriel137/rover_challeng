# Rovers Control

This is a small Python application that allows you to control rovers on Mars through a series of commands.

## Installation - Manual

Make sure you have Python installed on your system. You can download it from https://www.python.org/downloads/.

Download the source code of this project.

Install the dependencies by running the following command in the project folder:

```
 pip3 install -r requirements.txt
```

## Run - Docker

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

```
file
```

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
python3 app/main.py
```

3. You should see output in the terminal like

```
    Enter 'file' to read data from a file, or press Enter to enter data manually:
```

4. Write file and press enter

```
file
```

5. You should see output in the terminal like

```
    Enter the name of the input file:
```

6. write the path

```
./assets/static/input.txt
```

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

# Running Tests

- To run the automated tests, execute the following command in the project folder:

```
pytest
```
