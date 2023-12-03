import os
import re

directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, 'input.txt')


# Press the green button in the gutter to run the script.
def part_one(rules):
    total_sum = 0
    val_cubes = []
    id_game = []
    for line in read_file:
        split = line.split("Game ")[1]
        val = split.split(": ")
        id_game.append(val[0])
        val_cubes.append(val[1].split(";"))
    val_extractions = []
    for idx, game in enumerate(val_cubes):
        print(game)
        for value in game:
            for spl in value.split(","):
                print(spl)
                for rule in rules:
                    print(rule)
                    print(spl in rule)
    # for game in val_cubes:
    #     for values in game:
    #         # print(re.findall("\d", values))
    #         val_extractions.append(values.split(","))
    #
    # for val in val_extractions:
    #     print(val)



def parse(line):
    line_list = re.findall("\d", line)
    return int(line_list[0] + line_list[-1])




if __name__ == '__main__':
    read_file = open(file_path, "r")
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    r = ["12 red", "13 green", "14 blue"]
    part_one(r)
