from models.command import process_command
from utils.io_utils import read_input_from_file

def main():
    """
        Executes the rover control program, allowing the user to input data manually or read it from a file.

        If the user chooses to read data from a file, the program prompts for the filename of the input file.
        If the user chooses manual input, the program prompts for the plateau size and rover data in pairs.

        Each pair consists of the initial position of the rover and its instructions.
        After processing the data, the program prints the final coordinates and direction of each rover.

        Raises:
            Exception: If any error occurs during program execution.

        Returns:
            None
    """
    try:
        input_option = input("Enter 'file' to read data from a file, or press Enter to enter data manually: ")

        if input_option.lower() == 'file':
            input_filename = input("Enter the name of the input file: ")
            x_max, y_max, rover_data = read_input_from_file(input_filename)
        else:
            x_max, y_max = map(int, input("Enter the plateau size (x y): ").split())
            rover_data = []
            while True:
                rover_position = input("Enter the rover position (x y direction): ")
                instructions = input("Enter the rover instructions: ")
                rover_data.append((rover_position, instructions))
                choice = input("Do you want to add another rover? (Y/N): ").strip().upper()
                if choice != 'Y':
                    break

        # Process the data as before
        for rover_position, instructions in rover_data:
            result = process_command(x_max, y_max, rover_position, instructions)
            print(result)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()