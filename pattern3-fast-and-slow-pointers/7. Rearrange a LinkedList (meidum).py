#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:50:04 2020

@author: dopiwoo

Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half
of the LinkedList are inserted alternatively to the nodes from the first half in reverse order. So if the LinkedList has
nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

Example 1:
Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

Example 2:
Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
"""


class Node:
    def __init__(self, value: int, next_node: 'Node' = None):
        self.value = value
        self.next = next_node

    def __repr__(self) -> str:
        string = ''
        temp_node = self
        while temp_node is not None:
            string += '->' + str(temp_node.value)
            temp_node = temp_node.next
        return string[2:]


def reorder(head: Node):
    return None


def reverse(curr_head: Node) -> Node:
    """
    Reverse a Singly LinkedList.

    Parameters
    ----------
    curr_head : Node
        input head of a Singly LinkedList

    Returns
    -------
    prev : Node
        the head of the reversed Singly LinkedList

    """
    prev = None
    while curr_head is not None:
        next_node = curr_head.next
        curr_head.next = prev
        prev = curr_head
        curr_head = next_node
    curr_head = prev
    return prev


if __name__ == '__main__':
    a = Node(2)
    a.next = Node(4)
    a.next.next = Node(6)
    a.next.next.next = Node(8)
    a.next.next.next.next = Node(10)
    a.next.next.next.next.next = Node(12)
    print(reverse(a))
    print(a)
