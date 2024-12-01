import sys
import re

def read_input(file) -> tuple[list[str], list[str]]:
    left = []
    right = []

    for line in file:
        nums = re.split(r"\s+", line)
        if len(nums) < 2:
            raise Exception(f"error processing line - line did not have two numbers: {line}")

        left.append(int(nums[0]))
        right.append(int(nums[1]))

    # Check that the two lists are the same length
    if len(left) != len(right):
        raise Exception("one array was not the same length as the other, check the input file is valid")

    return (left, right)

def main() -> int:
    with open('../input.txt', 'r') as f:
        (leftNums, rightNums) = read_input(f)

    # Sort lists, this naturally puts the smallest with the smallest in each list at the correct index
    leftNums.sort()
    rightNums.sort()

    # Zip the two lists together now they are sorted
    zippedNums = zip(leftNums, rightNums)

    diffTotal = 0
    for (leftNum, rightNum) in zippedNums:
        diffTotal += abs(leftNum - rightNum)

    print(diffTotal)

    return 0

if __name__ == "__main__":
    sys.exit(main())
