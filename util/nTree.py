from typing import List, Callable

class Node:
    def __init__(self, name: str, parent: Callable, children: List[Callable]) -> None:
        self.name = name
        self.parent = parent
        self.children = children

class Tree:
    def __init__(self, root: Callable) -> None:
        self.root = root