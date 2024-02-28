import argparse
import sys


def validate_args() -> tuple:
    """Function to validate input data from arg"""

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", type=int, required=True, help="The size of array")
    parser.add_argument(
        "-a", "--array", type=int, nargs="+", required=True, help="The array to validate duplicate values"
    )
    args = parser.parse_args()
    return (int(args.size), list(args.array))


def find_duplicates(array_size: int, array: list) -> list:
    """
    Find each duplicate numbers in the array. If we found duplicates returns
    a list of duplicate numbers, otherwise -1.

    Args:
        array_size (int): size of array
        array (list): array to validate duplicate numbers
    """

    # If the array_size is different from actual array length then kill program
    if len(array) != array_size:
        print(f"The size of array is different. Specify size {array_size} and actual size {len(array)}")
        sys.exit(-1)

    # Find duplicates - print duplicates otherwise add -1 in the array
    list_of_duplicates = duplicates(array)
    if len(list_of_duplicates) == 0:
        list_of_duplicates.append(-1)
        print("There is no repeating element in the array.")
    else:
        print("Duplicates are", list_of_duplicates)

    return list_of_duplicates


def duplicates(array: list) -> list:
    """By giving an array it check if the arrays contains any duplicate number

    Args:
        array (list): array to validate if contains duplicate values

    Returns:
        list: sort (by asc) with duplicate numbers
    """
    array_of_duplicates = []
    for n in array:
        # if exist in duplicates ignore it - we already got it
        if exist(n, array_of_duplicates) is False:
            if is_duplicate(n, array) is True:
                array_of_duplicates.append(n)

    # sort ascending the found duplicate values e.g. [4, 9]
    array_of_duplicates.sort()

    return array_of_duplicates


def is_duplicate(num: int, array: list) -> bool:
    """check if the num is duplicate in the array

    Args:
        num (int): number to check the duplication
        array (list): array of numbers

    Returns:
        bool: number is a duplicate found at least twice in the array
    """
    occurrance = 0

    for n in array:
        if n == num:
            occurrance += 1
        if occurrance == 2:
            return True
    return False


def exist(num: int, array: list) -> bool:
    """Check if the num exist in the array

    Args:
        num (int): number to check if exist in the array
        array (list): array with numbers

    Returns:
        bool: True: number exists in the array, False: otherwise
    """
    for n in array:
        if n == num:
            return True
    return False


if __name__ == "__main__":
    (array_len, the_array) = validate_args()

    find_duplicates(array_len, the_array)
