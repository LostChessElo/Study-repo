import unittest
import easy_linked_lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Helper function to convert linked list to list
def list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result

# Helper function to convert circular list to array (limit iterations)
def circular_to_array(head, max_len=10):
    if not head:
        return []
    result = []
    current = head
    count = 0
    while count < max_len:
        result.append(current.data)
        current = current.next
        if current == head:
            break
        count += 1
    return result

class TestDeleteKth(unittest.TestCase):
    def test_delete_second_node(self):
        head = Node(5)
        head.next = Node(10)
        head.next.next = Node(15)
        head.next.next.next = Node(25)
        
        result = easy_linked_lists.delete_kth(head, 2)
        self.assertEqual(list_to_array(result), [5, 15, 25])
    
    def test_delete_first_node(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        
        result = easy_linked_lists.delete_kth(head, 1)
        self.assertEqual(list_to_array(result), [2, 3])
    
    def test_delete_last_node(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        
        result = easy_linked_lists.delete_kth(head, 3)
        self.assertEqual(list_to_array(result), [1, 2])
    
    def test_single_node(self):
        head = Node(10)
        result = easy_linked_lists.delete_kth(head, 1)
        self.assertIsNone(result)

class TestGetMiddle(unittest.TestCase):
    def test_odd_length(self):
        head = Node(5)
        head.next = Node(10)
        head.next.next = Node(15)
        head.next.next.next = Node(20)
        head.next.next.next.next = Node(25)
        
        result = easy_linked_lists.get_middle(head)
        self.assertEqual(result, 15)
    
    def test_even_length(self):
        head = Node(5)
        head.next = Node(10)
        head.next.next = Node(15)
        head.next.next.next = Node(20)
        head.next.next.next.next = Node(25)
        head.next.next.next.next.next = Node(30)
        
        result = easy_linked_lists.get_middle(head)
        self.assertEqual(result, 20)
    
    def test_single_node(self):
        head = Node(42)
        result = easy_linked_lists.get_middle(head)
        self.assertEqual(result, 42)
    
    def test_two_nodes(self):
        head = Node(1)
        head.next = Node(2)
        result = easy_linked_lists.get_middle(head)
        self.assertEqual(result, 2)

class TestCount(unittest.TestCase):
    def test_multiple_occurrences(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(1)
        head.next.next.next = Node(1)
        head.next.next.next.next = Node(3)
        
        result = easy_linked_lists.count(head, 1)
        self.assertEqual(result, 3)
    
    def test_no_occurrences(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        
        result = easy_linked_lists.count(head, 5)
        self.assertEqual(result, 0)
    
    def test_all_same(self):
        head = Node(7)
        head.next = Node(7)
        head.next.next = Node(7)
        
        result = easy_linked_lists.count(head, 7)
        self.assertEqual(result, 3)
    
    def test_single_occurrence(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        
        result = easy_linked_lists.count(head, 2)
        self.assertEqual(result, 1)

class TestCheckIfCircular(unittest.TestCase):
    def test_circular_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = head  # Make it circular
        
        result = easy_linked_lists.check_if_circular(head)
        self.assertTrue(result)
    
    def test_non_circular_list(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        
        result = easy_linked_lists.check_if_circular(head)
        self.assertFalse(result)
    
    def test_single_node_circular(self):
        head = Node(1)
        head.next = head
        
        result = easy_linked_lists.check_if_circular(head)
        self.assertTrue(result)
    
    def test_single_node_non_circular(self):
        head = Node(1)
        
        result = easy_linked_lists.check_if_circular(head)
        self.assertFalse(result)

class TestSinglyToCircular(unittest.TestCase):
    def test_convert_to_circular(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        
        result = easy_linked_lists.singly_to_circular(head)
        
        # Check if last node points back to head
        current = result
        for _ in range(3):
            if current.next == result:
                break
            current = current.next
        
        self.assertEqual(current.next, result)
    
    def test_single_node(self):
        head = Node(5)
        result = easy_linked_lists.singly_to_circular(head)
        self.assertEqual(result.next, result)
    
    def test_two_nodes(self):
        head = Node(1)
        head.next = Node(2)
        
        result = easy_linked_lists.singly_to_circular(head)
        self.assertEqual(result.next.next, result)

class TestSwap(unittest.TestCase):
    def test_swap_first_last(self):
        head = Node(5)
        second = Node(4)
        third = Node(3)
        fourth = Node(2)
        fifth = Node(1)
        
        head.next = second
        second.next = third
        third.next = fourth
        fourth.next = fifth
        fifth.next = head  # Make circular
        
        result = easy_linked_lists.swap(head)
        values = circular_to_array(result, 5)
        self.assertEqual(values, [1, 4, 3, 2, 5])
    
    def test_two_nodes(self):
        head = Node(1)
        second = Node(2)
        head.next = second
        second.next = head
        
        result = easy_linked_lists.swap(head)
        values = circular_to_array(result, 2)
        self.assertEqual(values, [2, 1])
    
    def test_three_nodes(self):
        head = Node(1)
        second = Node(2)
        third = Node(3)
        head.next = second
        second.next = third
        third.next = head
        
        result = easy_linked_lists.swap(head)
        values = circular_to_array(result, 3)
        self.assertEqual(values, [3, 2, 1])

class TestDeleteKthDoubly(unittest.TestCase):
    def test_delete_second(self):
        head = DoublyNode(1)
        second = DoublyNode(2)
        third = DoublyNode(3)
        fourth = DoublyNode(4)
        
        head.next = second
        second.prev = head
        second.next = third
        third.prev = second
        third.next = fourth
        fourth.prev = third
        
        result = easy_linked_lists.delete_kth_doubly(head, 2)
        values = list_to_array(result)
        self.assertEqual(values, [1, 3, 4])
    
    def test_delete_first(self):
        head = DoublyNode(1)
        second = DoublyNode(2)
        third = DoublyNode(3)
        
        head.next = second
        second.prev = head
        second.next = third
        third.prev = second
        
        result = easy_linked_lists.delete_kth_doubly(head, 1)
        values = list_to_array(result)
        self.assertEqual(values, [2, 3])
    
    def test_delete_last(self):
        head = DoublyNode(1)
        second = DoublyNode(2)
        third = DoublyNode(3)
        
        head.next = second
        second.prev = head
        second.next = third
        third.prev = second
        
        result = easy_linked_lists.delete_kth_doubly(head, 3)
        values = list_to_array(result)
        self.assertEqual(values, [1, 2])

class TestReverseSingly(unittest.TestCase):
    def test_reverse_multiple_nodes(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        
        result = easy_linked_lists.reverse_singly(head)
        self.assertEqual(list_to_array(result), [4, 3, 2, 1])
    
    def test_reverse_single_node(self):
        head = Node(1)
        result = easy_linked_lists.reverse_singly(head)
        self.assertEqual(list_to_array(result), [1])
    
    def test_reverse_two_nodes(self):
        head = Node(1)
        head.next = Node(2)
        result = easy_linked_lists.reverse_singly(head)
        self.assertEqual(list_to_array(result), [2, 1])

class TestReverseDoubly(unittest.TestCase):
    def test_reverse_multiple_nodes(self):
        head = DoublyNode(1)
        second = DoublyNode(2)
        third = DoublyNode(3)
        fourth = DoublyNode(4)
        
        head.next = second
        second.prev = head
        second.next = third
        third.prev = second
        third.next = fourth
        fourth.prev = third
        
        result = easy_linked_lists.reverse_doubly(head)
        values = list_to_array(result)
        self.assertEqual(values, [4, 3, 2, 1])
        
        # Check prev pointers
        self.assertIsNone(result.prev)
        self.assertEqual(result.next.prev, result)
    
    def test_reverse_single_node(self):
        head = DoublyNode(1)
        result = easy_linked_lists.reverse_doubly(head)
        self.assertEqual(list_to_array(result), [1])
        self.assertIsNone(result.prev)
        self.assertIsNone(result.next)
    
    def test_reverse_two_nodes(self):
        head = DoublyNode(1)
        second = DoublyNode(2)
        head.next = second
        second.prev = head
        
        result = easy_linked_lists.reverse_doubly(head)
        values = list_to_array(result)
        self.assertEqual(values, [2, 1])

if __name__ == '__main__':
    unittest.main()