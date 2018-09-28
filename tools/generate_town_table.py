"""Generate python code for town table
"""
import os


def get_town_table(screenshot_dir):
    """Generate python code for town table

    Its format is
        table[town_name] = (nearby town1, nearby town2...nearby town5)

    The length of tuple may be different depends on town.

    Arguments:
        screenshot_dir (str): Directory which have town_name directory
                              and label.

    Return:
        python code style string (str)
    """
    result = "TOWNS_TABLE = {}\n"
    for di in sorted(os.listdir(screenshot_dir)):
        dir_path = screenshot_dir + "/" + di
        if not os.path.isdir(dir_path):
            continue
        for f in os.listdir(dir_path):
            if f.lower().endswith(".txt"):
                result += "TOWNS_TABLE[("

                lines = open(dir_path + "/" + f).read().splitlines()
                for i in range(3, len(lines), 3):
                    result += "'%s', " % lines[i]
                result = result[:-2] + ")]\\"
                result += "\n= '%s'\n" % di
                break
    return result
