#!/bin/python3
from typing import TypeVar, Generic

T = TypeVar('T')

# # Dynamic implementation:


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.top: Node = None

    def is_empty(self) -> bool:
        return self.top == None

    def peek(self) -> T:
        return self.top.data

    def push(self, data: T) -> T:
        node: Node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self) -> T:
        data: T = self.top.data
        top = self.top.next
        return data

 # Static implementation


class Stack(Generic[T]):

    def __init__(self) -> None:
        self.stack: List[T] = []

    def is_empty(self) -> bool:
        return len(self.stack) == None

    def peek(self) -> T:
        return self.stack[len(self.stack) - 1]

    def size(self) -> int:
        return len(self.stack)

    def push(self, data: T) -> T:
        return self.stack.append(data)

    def pop(self) -> T:
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
