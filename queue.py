#!/bin/python3
from typing import TypeVar, Generic

T = TypeVar('T')

# # Dynamic implementation:


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def is_empty(self) -> bool:
        return self.head == None

    def peek(self) -> T:
        if self.head == None:
            return self.head == None
        return self.head.data

    def enqueue(self, data: T) -> None:
        if self.tail != None:
            self.tail.next = Node(data)
        self.tail = Node(data)
        if self.head == None:
            self.head = Node(data)

    def dequeue(self) -> T:
        data: T = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail == None
        return data


# # Static implementation:
class Queue(Generic[T]):

    def __init__(self) -> None:
        self.queue: List[T] = []

    def is_empty(self) -> bool:
        return len(self.queue) == None

    def peek(self) -> T:
        return self.queue[0]

    def size(self) -> int:
        return len(self.queue)

    def enqueue(self, data: T) -> T:
        return self.queue.append(data)

    def dequeue(self) -> T:
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
