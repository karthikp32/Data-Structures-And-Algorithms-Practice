class UndoBuffer:

    class DoublyLinkedListNode:
        def __init__(self, val, next_node, prev_node):
            self.val = val
            self.next_node = next_node
            self.prev_node = prev_node


    def __init__(self, head_node_of_doubly_linked_list, last_node):
        self.head_node = head_node_of_doubly_linked_list
        self.last_node = last_node

    #add_to_front
    def add_last_typed_text(self, val):
        if self.head_node == None:
            self.head_node = self.DoublyLinkedListNode(val, None, None)
            self.last_node = self.head_node
        else:
            temp_node = self.DoublyLinkedListNode(val, None, None)
            temp_node.next_node = self.head_node
            self.head_node.prev_node = temp_node
            self.head_node = temp_node  

    #pop from front
    def get_last_typed_text(self):
        last_typed_text = self.head_node.val
        self.head_node = self.head_node.next_node
        return last_typed_text    

    #pop from back
    def get_oldest_text_from_buffer(self):
         last_val = self.last_node.val
         temp_node = self.last_node.prev_node
         self.last_node.prev_node.next_node = None       
         self.last_node.prev_node = None
         self.last_node = temp_node
         return last_val

    def print_all_vals(self):
        curr = self.head_node
        print(curr.val)
        while curr.next_node != None:
            curr = curr.next_node
            print(curr.val)


    def add_to_back(self, val):
        temp = self.DoublyLinkedListNode(val, None, None)
        self.last_node.next_node = temp
        temp.prev_node = self.last_node
        self.last_node = temp


if __name__== '__main__':

    #Use Cases/Test Cases/Examples
    #1) Input: empty buffer
    #add_to_front('Hi')
    #pop_from_front()
    #Output: 'Hi'

    undo_buffer = UndoBuffer(None, None)
    undo_buffer.add_last_typed_text('Hi')
    expected_last_typed_text = 'Hi'
    actual_last_typed_text = undo_buffer.get_last_typed_text()
    assert expected_last_typed_text == actual_last_typed_text, "failed test case 1 of undo buffer"

    #2) Input: buffer holding 'Hi' --> ['Hi']
    #add_to_front('Karthik') --> ['Karthik', 'Hi', ]
    #get_last_typed_text()
    #Output: ''Karthik'
    # linked_list_1 = UndoBuffer.DoublyLinkedListNode(1, None)
    undo_buffer.add_last_typed_text('Karthik')
    expected_last_typed_text = 'Karthik'
    actual_last_typed_text = undo_buffer.get_last_typed_text()
    assert expected_last_typed_text == actual_last_typed_text, "failed test case 2 of undo buffer"


    #3) Input: buffer holding 'Karthik', 'Hi' --> ['Karthik', 'Hi']
    #add_to_front('!') --> [ '!', 'Karthik', 'Hi']
    #remove_oldest_text_from_buffer()
    #Output: 'Hi'

    undo_buffer.add_last_typed_text('Hi')
    undo_buffer.add_last_typed_text('Karthik')
    undo_buffer.add_last_typed_text('!')
    undo_buffer.print_all_vals()
    expected = 'Hi'
    actual = undo_buffer.get_oldest_text_from_buffer()
    assert expected == actual, "failed test case 3 of undo buffer"

    #4) Input: buffer holding 1,2 --> [1,2]
    #add_to_back(3) --> [2, 1, 3]
    #remove_oldest_text_from_buffer()
    #Output: 3
    undo_buffer2 = UndoBuffer(None, None)
    undo_buffer2.add_last_typed_text(1)
    undo_buffer2.add_last_typed_text(2)
    undo_buffer2.add_to_back(3)
    undo_buffer2.print_all_vals()
    expected = 3
    actual = undo_buffer2.get_oldest_text_from_buffer()
    assert expected == actual, "failed test case 4 of undo buffer"

