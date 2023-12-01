import os
import re

directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, 'input.txt')


# Press the green button in the gutter to run the script.
def part_one():
    total_sum = 0
    for line in read_file:
        total_sum += parse(line)
    return total_sum


def parse(line):
    line_list = re.findall("\d", line)
    return int(line_list[0] + line_list[-1])


def part_two():
    total_sum = 0
    words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    total_sum = 0
    for line in read_file:
        for word, numb in words.items():
            line = line.replace(word, word + numb + word)

        total_sum += parse(line)
    print(total_sum)
    return total_sum


if __name__ == '__main__':
    read_file = open(file_path, "r")
    # part_one()
    part_two()
