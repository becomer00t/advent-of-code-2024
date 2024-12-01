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

def countOccurrences(items):
    occurrences = {}

    for item in items:
        if item not in occurrences:
            occurrences[item] = 0

        occurrences[item] += 1

    return occurrences

def main() -> int:
    with open('../input.txt', 'r') as f:
        (leftNums, rightNums) = read_input(f)

    rightNumOccurrences = countOccurrences(rightNums)

    similarityScore = 0
    for leftNum in leftNums:
        occurrences = rightNumOccurrences[leftNum] if leftNum in rightNumOccurrences else 0

        similarityScore += leftNum * occurrences

    print(f"similarityScore: {similarityScore}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
