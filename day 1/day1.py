import time
import os
from collections import Counter

def read_data(path):
    """
    Read data from a file specified by the given path.

    Args:
        path (str): The path to the input file.

    Returns:
        list: A list containing lines read from the file.
    """
    with open(path) as file:
        data = file.readlines()
    return data

def set_working_directory():
    """
    Set the working directory to the script's directory and return the folder path.

    Returns:
        str: The absolute path to the current working directory.
    """
    # Retrieve the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Change the current working directory to the script's directory
    os.chdir(script_directory)
    return script_directory

def main():
    """
    Solve the Day 1 puzzle "Historian Hysteria".

    Args:
        None

    Returns:
        None
    """

    # Define the path to the input file
    folder_path = set_working_directory()
    input_name = "input.txt"
    # input_name = "input_test.txt"
    path = os.path.join(folder_path, input_name)
       
    # Part 1
    start_time_part1 = time.time()
    result1 = 0

    data = read_data(path)

    list1 = []
    list2 = []

    for line in data:
        # Split each line into two integers and add them to respective lists
        numbers = list(map(int, line.split()))
        list1.append(numbers[0])
        list2.append(numbers[1])
    
    list1.sort()
    list2.sort()
    
    result1 = 0

    for i in range(len(list1)):
        result1 += abs(list1[i] - list2[i])

    end_time_part1 = time.time()
    execution_duration_part1 = end_time_part1 - start_time_part1

    print("Part 1:", result1)
    print(f"Part 1 took {execution_duration_part1} seconds to run.")

    # Part 2
    start_time_part2 = time.time()
    result2 = 0

    col = Counter(list2)

    for i in range(len(list1)):
        result2 += list1[i] * col[list1[i]]

    end_time_part2 = time.time()
    execution_duration_part2 = end_time_part2 - start_time_part2
    print("Part 2:", result2)
    print(f"Part 2 took {execution_duration_part2} seconds to run.")

if __name__ == "__main__":
    main()