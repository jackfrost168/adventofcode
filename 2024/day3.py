import re


def extract_mul_operations(info):
    # Regular expression pattern to match "mul(num1, num2)" format
    pattern = r'mul\((\d+),\s*(\d+)\)'  # Assumes num1 and num2 are integers
    matches = re.findall(pattern, info)

    return matches


def extract_conditional_mul_operations(text):
    text = re.sub(r"(?<=don't\(\)).*?(?=(do\(\)|$))", "", text, flags=re.DOTALL)
    # Step 2: Regular expression to match "do()" followed by mul(num1, num2)
    # or mul(num1, num2) standalone (without "don't()")
    pattern = r'mul\((\d+),\s*(\d+)\)'  # Assumes num1 and num2 are integers

    # Find all matches
    matches = re.findall(pattern, text)
    # Extract the numbers (num1, num2)
    numbers = []

    for match in matches:
        if match[0]:  # From "do()" case
            numbers.append((int(match[0]), int(match[1])))
        elif match[2]:  # Standalone "mul(num1, num2)" case
            numbers.append((int(match[2]), int(match[3])))

    return numbers


def part1(info):
    result = extract_mul_operations(info)
    total = 0
    for (x, y) in result:
        total += int(x) * int(y)

    return total

def part2(info):
    result = extract_conditional_mul_operations(info)

    total = 0
    for (x, y) in result:
        total += int(x) * int(y)

    return total

def main():
    with open("input/input3.txt", "r") as f:
        info = f.read().strip()

    print("part 1:", part1(info))
    print("part 2:", part2(info))


main()
