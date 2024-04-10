"""
Assignment 2: Trees for Treemap

=== CSC148 Winter 2024 ===
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Bogdan Simion, David Liu, Diane Horton,
                   Haocheng Hu, Jacqueline Smith

=== Module Description ===
This module contains the basic tree interface required by the treemap
visualiser. You will both add to the abstract class, and complete a
concrete implementation of a subclass to represent files and folders on your
computer's file system.
"""
from __future__ import annotations

import math
import os
from random import randint
from typing import List, Tuple, Optional


class TMTree:
    """A TreeMappableTree: a tree that is compatible with the treemap
    visualiser.

    This is an abstract class that should not be instantiated directly.

    You may NOT add any attributes, public or private, to this class.
    However, part of this assignment will involve you implementing new public
    *methods* for this interface.
    You should not add any new public methods other than those required by
    the client code.
    You can, however, freely add private methods as needed.

    === Public Attributes ===
    rect:
        The pygame rectangle representing this node in the treemap
        visualization.
    data_size:
        The size of the data represented by this tree.

    === Private Attributes ===
    _colour:
        The RGB colour value of the root of this tree.
    _name:
        The root value of this tree, or None if this tree is empty.
    _subtrees:
        The subtrees of this tree.
    _parent_tree:
        The parent tree of this tree; i.e., the tree that contains this tree
        as a subtree, or None if this tree is not part of a larger tree.
    _expanded:
        Whether or not this tree is considered expanded for visualization.

    === Representation Invariants ===
    - data_size >= 0
    - If _subtrees is not empty, then data_size is equal to the sum of the
      data_size of each subtree.

    - _colour's elements are each in the range 0-255.

    - If _name is None, then _subtrees is empty, _parent_tree is None, and
      data_size is 0.
      This setting of attributes represents an empty tree.

    - if _parent_tree is not None, then self is in _parent_tree._subtrees

    - if _expanded is True, then _parent_tree._expanded is True
    - if _expanded is False, then _expanded is False for every tree
      in _subtrees
    - if _subtrees is empty, then _expanded is False
    """

    rect: Tuple[int, int, int, int]
    data_size: int
    _colour: Tuple[int, int, int]
    _name: str
    _subtrees: List[TMTree]
    _parent_tree: Optional[TMTree]
    _expanded: bool

    def __init__(self, name: str, subtrees: List[TMTree],
                 data_size: int = 0) -> None:
        """Initialize a new TMTree with a random colour and the provided <name>.

        If <subtrees> is empty, use <data_size> to initialize this tree's
        data_size.

        If <subtrees> is not empty, ignore the parameter <data_size>,
        and calculate this tree's data_size instead.

        Set this tree as the parent for each of its subtrees.

        Precondition: if <name> is None, then <subtrees> is empty.
        """
        self.rect = (0, 0, 0, 0)
        self._name = name
        self._subtrees = subtrees[:]
        self._parent_tree = None
        self._expanded = False
        a, b, c = randint(0, 255), randint(0, 255), randint(0, 255)
        self._colour = (a, b, c)
        if len(subtrees) == 0:
            self.data_size = data_size
        else:
            self.data_size = 0
            for subtree in self._subtrees:
                self.data_size = self.data_size + subtree.data_size
            for item in self._subtrees:
                item._parent_tree = self

    def is_empty(self) -> bool:
        """Return True iff this tree is empty.
        """
        return self._name is None

    def get_parent(self) -> Optional[TMTree]:
        """Returns the parent of this tree.
        """
        return self._parent_tree

    def update_rectangles(self, rect: Tuple[int, int, int, int]) -> None:
        """Update the rectangles in this tree and its descendents using the
        treemap algorithm to fill the area defined by pygame rectangle <rect>.
        """
        self.rect = rect
        total = 0
        a, b, w, h = rect
        for subtree in self._subtrees:
            total += subtree.data_size
        if self.data_size == 0 or self.data_size < 0:
            self.rect = (0, 0, 0, 0)
        elif w > h:
            temp = 0
            for x in range(len(self._subtrees)):
                subtree = self._subtrees[x]
                fract = subtree.data_size / total
                if x < len(self._subtrees) - 1:
                    width = int(w * fract)
                    subtree.rect = (a + temp, b, width, h)
                    temp += width
                else:
                    width = w - temp
                    subtree.rect = (a + temp, b, width, h)
        else:
            temp = 0
            for x in range(len(self._subtrees)):
                subtree = self._subtrees[x]
                fract = subtree.data_size / total
                if x < len(self._subtrees) - 1:
                    height = int(h * fract)
                    subtree.rect = (a, b + temp, w, height)
                    temp += height
                else:
                    height = h - temp
                    subtree.rect = (a, b + temp, w, height)
        for subtree in self._subtrees:
            subtree.update_rectangles(subtree.rect)

    def get_rectangles(self) -> List[Tuple[Tuple[int, int, int, int],
                                           Tuple[int, int, int]]]:
        """Return a list with tuples for every leaf in the displayed-tree
        rooted at this tree. Each tuple consists of a tuple that defines the
        appropriate pygame rectangle to display for a leaf, and the colour
        to fill it with.
        """
        if self.is_empty() or self.data_size == 0:
            return []
        if not self._expanded:
            return [(self.rect, self._colour)]
        else:
            lst = []
            for subtree in self._subtrees:
                lst.extend(subtree.get_rectangles())
            return lst

    def get_tree_at_position(self, pos: Tuple[int, int]) -> Optional[TMTree]:
        """Return the leaf in the displayed-tree rooted at this tree whose
        rectangle contains position <pos>, or None if <pos> is outside of this
        tree's rectangle.

        If <pos> is on the shared edge between two or more rectangles,
        always return the leftmost and topmost rectangle (wherever applicable).
        """
        x, y, w, h = self.rect
        if pos > (x + w, y + h):
            return None
        if ((x <= pos[0] <= x + w and y <= pos[1] <= y + h)
                and not self._expanded):
            return self
        elif (x <= pos[0] <= x + w and y <= pos[1] <= y + h) and self._expanded:
            for subtree in self._subtrees:
                x = subtree.get_tree_at_position(pos)
                if x:
                    return x
        return None

    def update_data_sizes(self) -> int:
        """Update the data_size for this tree and its subtrees, based on the
        size of their leaves, and return the new size.

        If this tree is a leaf, return its size unchanged.
        """
        if not self._subtrees:
            return self.data_size
        else:
            self.data_size = 0
            for subtree in self._subtrees:
                self.data_size += subtree.update_data_sizes()
            return self.data_size

    def move(self, destination: TMTree) -> None:
        """If this tree is a leaf, and <destination> is not a leaf, move this
        tree to be the last subtree of <destination>. Otherwise, do nothing.
        >>> leaf1 = TMTree('Leaf', [], 10)
        >>> l2 = TMTree('L2', [], 20)
        >>> destination = TMTree('Destination', [l2], 0)
        >>> leaf1.move(destination)
        >>> leaf = TMTree('Leaf' , [], 10)
        >>> a1 = TMTree('A1' , [], 55)
        >>> b1 = TMTree('B1' , [], 45)
        >>> leaf2 = TMTree('Leaf2' , [a1, b1], 0)
        >>> parent = TMTree('Parent', [leaf, leaf2], 0)
        >>> random1 = TMTree("r1", [], 125)
        >>> random2 = TMTree("r2", [], 125)
        >>> Des = TMTree('des', [random1, random2], 0)
        >>> leaf.move(Des)
        >>> Des._subtrees.__len__()
        3
        >>> Des._subtrees[2] == leaf
        True
        >>> leaf._parent_tree == Des
        True
        >>> Des.data_size
        260
        >>> parent.data_size
        100
        >>> b1.move(Des)
        >>> Des._subtrees.__len__()
        4
        >>> isinstance(Des._subtrees[3], TMTree)
        True
        >>> b1._parent_tree == Des
        True
        >>> Des.data_size
        305
        >>> parent.data_size
        55
        """
        if (not self._subtrees and self._parent_tree
                and destination._subtrees != []):
            self._parent_tree._subtrees.remove(self)
            self._parent_tree._tree_new_size()
            destination._subtrees.append(self)
            self._parent_tree = destination
            destination._tree_new_size()

    def change_size(self, factor: float) -> None:
        """Change the value of this tree's data_size attribute by <factor>.

        Always round up the amount to change, so that it's an int, and
        some change is made.

        Do nothing if this tree is not a leaf.
        """
        if not self._subtrees and not self.is_empty():
            var = self.data_size * factor
            if var > 0:
                self.data_size += math.ceil(var)
            else:
                if self.data_size + math.floor(var) < 1:
                    self.data_size = 1
                else:
                    self.data_size += math.floor(var)
            if self._parent_tree:
                self._parent_tree._tree_new_size()

    def delete_self(self) -> bool:
        """Removes the current node from the visualization and
        returns whether the deletion was successful.

        Only do this if this node has a parent tree.

        Do not set self._parent_tree to None, because it might be used
        by the visualiser to go back to the parent folder.
        >>> leaf = TMTree('Leaf' , [], 10)
        >>> a1 = TMTree('A1' , [], 55)
        >>> b1 = TMTree('B1' , [], 45)
        >>> leaf2 = TMTree('Leaf2' , [a1, b1], 0)
        >>> parent = TMTree('Parent', [leaf, leaf2], 0)
        >>> random1 = TMTree("r1", [], 125)
        >>> random2 = TMTree("r2", [], 125)
        >>> Des = TMTree('des', [random1, random2], 0)
        >>> leaf.delete_self()
        True
        >>> parent._subtrees.__len__()
        1
        >>> leaf._parent_tree == parent
        True
        >>> parent.data_size
        100
        >>> b1.delete_self()
        True
        >>> leaf2._subtrees.__len__() == 1
        True
        >>> parent.data_size
        55
        >>> leaf2.data_size
        55
        >>> g1 = TMTree('g1', [], 45)
        >>> g2 = TMTree('g2', [], 20)
        >>> new_tree = TMTree('new_tree', [g1], 0)
        >>> new_tree.delete_self()
        False
        >>> new_tree.data_size
        45
        >>> g1.delete_self()
        True
        >>> new_tree._subtrees.__len__() == 0
        True
        >>> new_tree.data_size
        0
        >>> t3 = TMTree('t3', [], 5)
        >>> t1 = TMTree('t1', [t3], 0)
        >>> t1.data_size
        5
        >>> t2 = TMTree('t2', [], 20)
        >>> example_tree = TMTree('example_tree', [t1, t2], 0)
        >>> example_tree.data_size
        25
        >>> t3.delete_self()
        True
        >>> t2.data_size
        20
        >>> t1.data_size
        0
        >>> example_tree.data_size
        20
        """
        if self._parent_tree:
            if self._parent_tree._subtrees.__len__() == 1:
                self._parent_tree.data_size -= self.data_size
            self._parent_tree._subtrees.remove(self)
            self._parent_tree._tree_new_size()
            return True
        return False

    def expand(self) -> None:
        """Expand a given file.
        The tree corresponding to that rectangle is expanded in the
        displayed-tree. If the tree is a leaf, nothing happens.
        >>> t1 = TMTree('t1', [], 10)
        >>> t2 = TMTree('t2', [], 20)
        >>> parent = TMTree('Parent', [t1, t2], 0)
        >>> t1.expand()
        >>> t1._expanded
        False
        >>> parent._expanded
        False
        """
        if self._subtrees is not None and self._subtrees:
            self._expanded = True

    def expand_all(self) -> None:
        """
        The tree corresponding to that rectangle, as well as all of its
        subtrees, are expanded in the displayed-tree. If the tree is a leaf,
        nothing happens.
        >>> t1 = TMTree('t1', [], 10)
        >>> t2 = TMTree('t2', [], 20)
        >>> parent = TMTree('Parent', [t1, t2], 0)
        >>> parent.expand_all()  # First expansion
        >>> parent.expand_all()  # Second expansion
        >>> parent._expanded
        True
        >>> t1._expanded
        False
        >>> t2._expanded
        False
        """
        if self._subtrees is not None:
            self.expand()
            for subtree in self._subtrees:
                if subtree is not None:
                    subtree.expand_all()

    def collapse(self) -> None:
        """Collapse a given file.
        The parent of that tree is unexpanded (or "collapsed") in the
        displayed-tree. (Since rectangles correspond to leaves in the
        displayed-tree, it is the parent that needs to be unexpanded.)
        If the parent is None because this is the root of the whole tree,
        nothing happens.
        >>> t1 = TMTree('t1', [], 10)
        >>> parent = TMTree('Parent', [t1], 0)
        >>> grandparent = TMTree('Grandparent', [parent], 0)
        >>> grandparent.expand_all()
        >>> t1.collapse()
        >>> parent._expanded
        False
        >>> grandparent._expanded
        True
        """
        if not self.is_empty() and self._parent_tree:
            self._expanded = False
            self._collapse_helper()
            self._parent_tree._collapse_helper()

    def _collapse_helper(self) -> None:
        """Collapse all subtrees of this tree.
            >>> t1 = TMTree('t1', [], 10)
            >>> t2 = TMTree('t2', [], 20)
            >>> parent = TMTree('parent', [t1, t2], 0)
            >>> grandparent = TMTree('grandparent', [parent], 0)
            >>> grandparent.expand_all()
            >>> t1._collapse_helper()
            >>> t1._expanded
            False
            >>> t2._expanded
            False
            >>> parent._expanded
            True
            >>> grandparent._expanded
            True
            """
        self._expanded = False
        for subtree in self._subtrees:
            subtree._collapse_helper()

    def collapse_all(self) -> None:
        """Collapse every tree contained in the root of this tree.
        the entire displayed-tree is collapsed down to just a single tree node.
        If the displayed-tree is already a single node, nothing happens.
        >>> t1 = TMTree('t1', [], 10)
        >>> t2 = TMTree('t2', [], 20)
        >>> parent = TMTree('Parent', [t1, t2], 0)
        >>> parent.collapse_all()  # First collapse
        >>> parent.collapse_all()  # Second collapse
        >>> parent._expanded
        False
        """
        if self:
            self._collapse_helper()
        if self._parent_tree is not None:
            if self._parent_tree._subtrees:
                self._parent_tree.collapse_all()

    # Methods for the string representation
    def get_path_string(self) -> str:
        """
        Return a string representing the path containing this tree
        and its ancestors, using the separator for this OS between each
        tree's name.
        """
        if self._parent_tree is None:
            return self._name
        else:
            return self._parent_tree.get_path_string() + \
                self.get_separator() + self._name

    def get_separator(self) -> str:
        """Return the string used to separate names in the string
        representation of a path from the tree root to this tree.
        """
        raise NotImplementedError

    def get_suffix(self) -> str:
        """Return the string used at the end of the string representation of
        a path from the tree root to this tree.
        """
        raise NotImplementedError

    # helper:
    def _tree_new_size(self) -> None:
        self.data_size = 0
        for subtree in self._subtrees:
            self.data_size += subtree.data_size
        if self._parent_tree:
            self._parent_tree._tree_new_size()


class FileSystemTree(TMTree):
    """A tree representation of files and folders in a file system.

    The internal nodes represent folders, and the leaves represent regular
    files (e.g., PDF documents, movie files, Python source code files, etc.).

    The _name attribute stores the *name* of the folder or file, not its full
    path. E.g., store 'assignments', not '/Users/Diane/csc148/assignments'

    The data_size attribute for regular files is simply the size of the file,
    as reported by os.path.getsize.
    """

    def __init__(self, path: str) -> None:
        """Store the file tree structure contained in the given file or folder.

        Precondition: <path> is a valid path for this computer.
        """
        # Remember that you should recursively go through the file system
        # and create new FileSystemTree objects for each file and folder
        # encountered.
        #
        # Also remember to make good use of the superclass constructor!
        if not os.path.isdir(path):
            size = os.path.getsize(path)
            TMTree.__init__(self, name=os.path.basename(path), subtrees=[],
                            data_size=size)
        else:
            TMTree.__init__(self, name=os.path.basename(path), subtrees=[],
                            data_size=0)
            for subtree in os.listdir(path):
                # if subtree.startswith('.DS'):
                #     continue
                extended_path = os.path.join(path, subtree)
                node = FileSystemTree(extended_path)
                self.data_size += node.data_size
                self._subtrees.append(node)
            for i in self._subtrees:
                i._parent_tree = self

    def get_separator(self) -> str:
        """Return the file separator for this OS.
        """
        return os.sep

    def get_suffix(self) -> str:
        """Return the final descriptor of this tree.
        """

        def convert_size(data_size: float, suffix: str = 'B') -> str:
            suffixes = {'B': 'kB', 'kB': 'MB', 'MB': 'GB', 'GB': 'TB'}
            if data_size < 1024 or suffix == 'TB':
                return f'{data_size:.2f}{suffix}'
            return convert_size(data_size / 1024, suffixes[suffix])

        components = []
        if len(self._subtrees) == 0:
            components.append('file')
        else:
            components.append('folder')
            components.append(f'{len(self._subtrees)} items')
        components.append(convert_size(self.data_size))
        return f' ({", ".join(components)})'


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-import-modules': [
            'python_ta', 'typing', 'math', 'random', 'os', '__future__'
        ]
    })
