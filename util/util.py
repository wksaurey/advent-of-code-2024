from typing import List

def read_stripped_lines(path: str, chars: str = "\n", nums = False) -> List[str]:
    with open(path) as f:
        if nums:
            return list(map(lambda line: list(map(int, line.strip(chars))), f.readlines()))
        return list(map(lambda line: line.strip(chars), f.readlines()))

def read_stripped_grid(path: str, chars: str = "\n", nums = False) -> List[str]:
    with open(path) as f:
        if nums:
            return list(map(lambda line: list(map(int, line.strip(chars).split())), f.readlines()))
        return list(map(lambda line: line.strip(chars).split(), f.readlines()))

def read_stripped_columns(path: str, chars: str = '\n', nums = False) -> List[str]:
    with open(path) as f:
        data = []
        for line in f:
            for index, value in enumerate(line.strip(chars).split()):
                while index >= len(data): 
                    data.append([])
                if nums:
                    data[index].append(int(value))
                else:
                    data[index].append(value)
        return data

def windows(data_list, w_size):
    if len(data_list) <= w_size:
        result = []
        result.append(data_list)
        return result

    windows = []
    index = 0
    while index < len(data_list) - w_size + 1:
        windows.append(data_list[index:index+w_size])
        index += 1

    return windows

def manhattanDistance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1-x2) + abs(y1-y2)