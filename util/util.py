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

def manhattanDistance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1-x2) + abs(y1-y2)