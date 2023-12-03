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
        id_game.append(int(val[0]))
        val_cubes.append(val[1].split("; | \n"))
    # print(val_cubes)
    val_cubes = zip(id_game, val_cubes)
    mapping = {}
    for game_id, game in val_cubes:
        #print(game)
        poss = True
        for values in game:
            mapping["blue"] = re.findall("\d+ blue", values)
            mapping["red"] = re.findall("\d+ red", values)
            mapping["green"] = re.findall("\d+ green", values)
            # val_extractions.append(values.split(","))
            for map in mapping.items():
                print(map)
                for rule in rules:
                    if(rule in map[0]):
                       if(len(map[1]) > 0):
                           val = map[1][0].split(" ")[0]
                           print(int(val), rules[rule])
                           if(int(val) > rules[rule]):
                                 poss = False
                                 print(game_id)
                                 break
        if(poss):
            total_sum += game_id         
                           
    print(total_sum)
    # for idx, game in enumerate(val_cubes):
    #     print(game)
    #     for value in game:
    #         for spl in value.split(","):
    #             print(spl)
    #             for rule in rules:
    #                 print(rule)
    #                 print(spl in rule)
    # for game in val_cubes:
    #     for values in game:
    #         # print(re.findall("\d", values))
    #         val_extractions.append(values.split(","))
    #
    # for val in val_extractions:
    #     print(val)



if __name__ == '__main__':
    read_file = open(file_path, "r")
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    r = {"red": 12, "green": 13, "blue": 14}
    part_one(r)
