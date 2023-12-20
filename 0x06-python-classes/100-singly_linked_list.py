#!/usr/bin/python3
"""Define a node of a singly linked list."""


class Node:
    """Define a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Constructor for Node.

        Args:
            data: integer, data for the node.
            next_node: Node, reference to the next
                        node in the list (default None).

        Raises:
            TypeError: if data is not an integer
                        or if next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value: integer, data for the node.

        Raises:
            TypeError: if value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value: Node or None, reference to the next node in the list.

        Raises:
            TypeError: if value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Define a singly linked list."""

    def __init__(self):
        """Constructor for SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted
            position in the list (increasing order).

        Args:
            value: integer, data for the new node.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None \
                and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout."""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next_node
        return '\n'.join(elements)
