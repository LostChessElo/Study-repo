# Bonus if you can get best time and space complexities

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

def delete_kth(head: object, k: int) -> object:
    """
    Given a singly linked list, 
    the task is to remove every kth node of the linked list. 
    Assume that k is always less than or equal to the length of the Linked List.
    """
    pass

def get_middle(head: object) -> int:
    """
    Given the head of singly linked list, find middle node of the linked list.
    If the number of nodes is odd, return the middle node.
    If the number of nodes is even, there are two middle nodes, so return the second middle node.
    e.g
    input: 5 -> 10 -> 15 -> 20 -> 25
    Output: 15 
    input: 5 -> 10 -> 15 -> 20 -> 25 -> 30
    Output: 20
    """
    pass

def count(head: object, key: int) -> int:
    """
    Given a singly linked list and a key,
    count the number of occurrences of the key within the list
    
    Input: 1 -> 2 -> 1 -> 1 -> 3, key = 1
    Output: 3
    """
    pass

def circular_traversal(head: object) -> None:
    """
    Given a circular linked list 
    print all elements within the list
    """
    pass

def check_if_circular(head: object) -> bool:
    """
    Given the head of a singly linked list 
    return True if the linked list is circular,
    False otherwise.
    """
    pass

def singly_to_circular(head: object) -> object:
    """
    Given a singly linked list 
    convert it to a circular singly linked list 
    """
    pass

def swap(head: object) -> object:
    """
    Given a circular linked list 
    swap the first and last nodes 

    Input : 5 4 3 2 1
    Output : 1 4 3 2 5
    """
    pass

def delete_kth_doubly(head: object, k: int) -> object:
    """
    Given a doubly linked list,
    remove every kth node
    TN: the first nodes prev* is null and the last nodes next* is null
    """
    pass

def reverse_singly(head: object) -> object:
    """
    Given a singly linked list 
    return the reversed list

    Input: 1 -> 2 -> 3
    Output: 3 -> 2 -> 1
    """
    pass

def reverse_doubly(head: object) -> object:
    """
    Given a doubly linked list 
    return the reversed list 
    
    Input: Null <- 1 <-> 2 <-> 3 <-> 4 -> Null
    Output: Null <- 4 <-> 3 <-> 2 <-> 1 -> Null
    """
    pass