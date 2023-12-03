import os
import re

directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, 'input.txt')


def part_one(rules):
    total_sum = 0
    val_cubes = []
    id_game = []
    for line in read_file:
        split = line.split("Game ")[1]
        val = split.split(": ")
        id_game.append(int(val[0]))
        val_cubes.append(val[1].split("; | \n"))
    # print(val_cubes)
    val_cubes = zip(id_game, val_cubes)
    mapping = {}
    for game_id, game in val_cubes:
        # print(game)
        poss = True
        for values in game:
            mapping["blue"] = re.findall("\d+ blue", values)
            mapping["red"] = re.findall("\d+ red", values)
            mapping["green"] = re.findall("\d+ green", values)
            for key, values in mapping.items():
                for rule in rules:
                    if rule in key:
                        if len(values) > 0:
                            for value in values:
                                val = value.split(" ")[0]
                                if int(val) > rules[rule]:
                                    poss = False
                                    break
        if poss:
            total_sum += game_id

    print(total_sum)


def part_two(rules):
    total_sum = 0
    val_cubes = []
    id_game = []
    for line in read_file:
        split = line.split("Game ")[1]
        val = split.split(": ")
        id_game.append(int(val[0]))
        val_cubes.append(val[1].split("; | \n"))
    val_cubes = zip(id_game, val_cubes)
    mapping = {}
    for game_id, game in val_cubes:
        total_multpl = 0
        for values in game:
            mapping["blue"] = re.findall("\d+ blue", values)
            mapping["red"] = re.findall("\d+ red", values)
            mapping["green"] = re.findall("\d+ green", values)
            for key, values in mapping.items():
                for rule in rules:
                    max_color = 0
                    if rule in key:
                        if len(values) > 0:
                            for value in values:
                                val = int(value.split(" ")[0])
                                if max_color < val:
                                    print(rule, max_color)
                                    max_color = val
                        if total_multpl == 0:
                            total_multpl = max_color
                        else:
                            total_multpl *= max_color
        total_sum += total_multpl
    print(total_sum)


if __name__ == '__main__':
    read_file = open(file_path, "r")
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    r = {"red": 12, "green": 13, "blue": 14}
    part_two(r)
