#!/bin/python3
from typing import TypeVar, Generic
T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None


class LinkedLists(Generic[T]):
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.current_size: int = 0

    def add_first(self, data: T) -> None:
        if self.head == None:
            self.head = Node(data)
            self.current_size += 1
            return
        new_node: Node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.current_size += 1

    def add_last(self, data: T) -> None:
        if self.head == None:
            self.head = self.tail = Node(data)
            self.current_size += 1
            return
        new_node: Node = Node(data)
        self.tail.next = new_node
        self.tail = new_node
        self.current_size += 1

    def remove_first(self) -> T:
        if self.head == None:
            return None
        tem_data: Node = self.head.data
        self.head = self.head.next
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.current_size -= 1
        return tem_data

    # def remove_add_last(self):

        # def add_last2(self, data: T) -> None:
        #     if self.head == None:
        #         self.head = Node(data)
        #         self.current_size += 1
        #         return
        #     new_node: Node = Node(data)
        #     tem_pointer: Node = self.head
        #     while tem_pointer.next != None:
        #         tem_pointer = tem_pointer.next
        #     tem_pointer.next = new_node
        #     self.current_size += 1
