"""
Assignment 2 - Sample Tests

=== CSC148 Winter 2024 ===
This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Bogdan Simion, David Liu, Diane Horton, Jacqueline Smith

=== Module Description ===
This module contains sample tests for Assignment 2, Tasks 1 and 2.
The tests use the provided example-directory, so make sure you have downloaded
and extracted it into the same place as this test file.
This test suite is very small. You should plan to add to it significantly to
thoroughly test your code.

IMPORTANT NOTES:
    - If using PyCharm, go into your Settings window, and go to
      Editor -> General.
      Make sure the "Ensure line feed at file end on Save" is NOT checked.
      Then, make sure none of the example files have a blank line at the end.
      (If they do, the data size will be off.)

    - os.listdir behaves differently on different
      operating systems.  These tests expect the outcomes that one gets
      when running on the *Teaching Lab machines*.
      Please run all of your tests there - otherwise,
      you might get inaccurate test failures!

    - Depending on your operating system or other system settings, you
      may end up with other files in your example-directory that will cause
      inaccurate test failures. That will not happen on the Teachin Lab
      machines.  This is a second reason why you should run this test module
      there.
"""
import math
import os

from hypothesis import given
from hypothesis.strategies import integers
from papers import PaperTree

from tm_trees import TMTree, FileSystemTree

EXAMPLE_PATH = os.path.join(os.getcwd(), 'example-directory', 'workshop')


def test_single_file() -> None:
    """Test a tree with a single file.
    """
    tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'draft.pptx'))
    assert tree._name == 'draft.pptx'
    assert tree._subtrees == []
    assert tree._parent_tree is None
    assert tree.data_size == 58
    assert is_valid_colour(tree._colour)


new_path = os.path.join(os.getcwd())


def test_tree_zero_data_nonempty_subtrees():
    tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'activities', 'images'))
    tree.update_rectangles((0, 0, 0, 0))
    assert tree.rect == (0, 0, 0, 0)
    for subtree in tree._subtrees:
        assert subtree.rect == (0, 0, 0, 0)


def test_tree_rect_zero_width():
    tree = FileSystemTree(EXAMPLE_PATH)
    tree.update_rectangles((0, 0, 0, 100))
    assert tree.rect == (0, 0, 0, 100)


def test_tree_rect_zero_height():
    tree = FileSystemTree(EXAMPLE_PATH)
    tree.update_rectangles((0, 0, 100, 0))
    assert tree.rect == (0, 0, 100, 0)


def test_tree_rect_negative_width():
    tree = FileSystemTree(EXAMPLE_PATH)
    tree.update_rectangles((0, 0, -100, 100))
    assert tree.rect == (0, 0, -100, 100)


def test_tree_rect_negative_height():
    tree = FileSystemTree(EXAMPLE_PATH)
    tree.update_rectangles((0, 0, 100, -100))
    assert tree.rect == (0, 0, 100, -100)


path1 = os.path.join(os.getcwd(), "TESTING")
path2 = os.path.join(os.getcwd(), "Test_cases")


def test_data_size_images_folder():
    path = os.path.join(path1, 'images')
    images_folder = FileSystemTree(path)
    expected_size = 25 + 27 + 99 + 8043
    assert images_folder.data_size == expected_size


def test_data_size_wallpapers_folder():
    path = os.path.join(path1, 'images', 'wallpapers')
    wallpapers_folder = FileSystemTree(path)
    expected_size = 99 + 8043
    assert wallpapers_folder.data_size == expected_size


def test_data_size_python_files_folder():
    path = os.path.join(path1, 'python_files')
    python_files_folder = FileSystemTree(path)
    expected_size = 27 + 30 + 216 + 189
    assert python_files_folder.data_size == expected_size


def test_data_size_message_txt():
    path = os.path.join(path1, 'message.txt')
    message_file = FileSystemTree(path)
    expected_size = 590
    assert message_file.data_size == expected_size


def test_data_size_total_testing_folder():
    testing_folder = FileSystemTree(path1)
    # Sum sizes of all sub folder and files
    expected_size = (test_data_size_images_folder.expected_size +
                     test_data_size_python_files_folder.expected_size +
                     test_data_size_message_txt.expected_size + 1032 + 2320)
    assert testing_folder.data_size == expected_size


# Store expected sizes for access
test_data_size_images_folder.expected_size = 25 + 27 + 99 + 8043
test_data_size_wallpapers_folder.expected_size = 8043 + 99
test_data_size_python_files_folder.expected_size = 27 + 30 + 216 + 189
test_data_size_message_txt.expected_size = 590

# get_rectangles


def test_tree_with_single_leaf_not_expanded():
    """Returns a list with a single tuple containing the rectangle and colour
    of the leaf when the tree is not expanded."""
    single_leaf = FileSystemTree(os.path.join(path1, 'message.txt'))
    single_leaf.update_rectangles((0, 0, 100, 100))
    rectangles = single_leaf.get_rectangles()
    assert len(rectangles) == 1
    assert rectangles[0][0] == single_leaf.rect
    assert rectangles[0][1] == single_leaf._colour


def test_tree_with_subtrees_expanded():
    """Returns a list of tuples containing the rectangles and colours of all
    leaves in the tree when the tree is expanded."""
    tree = FileSystemTree(path1)
    tree.update_rectangles((0, 0, 200, 200))
    tree.expand()
    rectangles = tree.get_rectangles()
    assert len(rectangles) > 1  # Ensure we have multiple rectangles
    for rect, colour in rectangles:
        assert isinstance(rect, tuple)
        assert isinstance(colour, tuple)
        assert len(rect) == 4
        assert len(colour) == 3


def test_tree_with_subtrees_not_expanded():
    """Returns the correct rectangles and colours for all leaves in the tree
    when the tree is not expanded."""
    tree = FileSystemTree(path1)
    tree.update_rectangles((0, 0, 200, 200))
    rectangles = tree.get_rectangles()
    # Only one rectangle because the tree is not expanded
    assert len(rectangles) == 1
    assert rectangles[0][0] == tree.rect
    assert rectangles[0][1] == tree._colour


def test_tree_with_single_leaf_one_subtree():
    """Returns the correct rectangles and colours for all leaves in the tree
    when the tree has only one subtree."""
    tree = FileSystemTree(os.path.join(path1, 'images'))
    tree.update_rectangles((0, 0, 200, 200))
    rectangles = tree.get_rectangles()
    assert len(rectangles) == 1  # One subtree with the leaf
    assert rectangles[0][0] == tree.rect
    assert rectangles[0][1] == tree._colour


# TREE AT POSITION

def test_position_outside_tree_rectangle():
    """Returns None if position is outside of tree's rectangle."""
    tree = FileSystemTree(path1)
    tree.update_rectangles((0, 0, 200, 200))
    # Choose a position outside the tree's rectangle
    pos_outside = (300, 300)
    assert tree.get_tree_at_position(pos_outside) is None


def test_position_inside_leaf_rectangle():
    """Returns self if tree is a leaf and position is inside its rectangle."""
    leaf = FileSystemTree(os.path.join(path1, 'message.txt'))
    leaf.update_rectangles((0, 0, 100, 100))
    # Choose a position inside the leaf's rectangle
    pos_inside = (50, 50)
    assert leaf.get_tree_at_position(pos_inside) == leaf


def test_position_on_shared_edge_returns_leftmost_topmost():
    """Returns the leftmost and topmost rectangle if
    position is on shared edge."""
    tree = FileSystemTree(path1)
    tree.update_rectangles((0, 0, 200, 200))
    tree._expanded = True  # Manually set the tree to expanded
    pos_shared_edge = (100, 100)  # This position should be on the edge
    result = tree.get_tree_at_position(pos_shared_edge)
    assert result is not None
    assert (result.rect[0] <= pos_shared_edge[0]
            and result.rect[1] <= pos_shared_edge[1])


def test_position_inside_subtree_rectangle():
    """Returns the correct leaf if position is inside a subtree's rectangle."""
    tree = FileSystemTree(path1)
    tree.update_rectangles((0, 0, 200, 200))
    tree._expanded = True
    subtree = tree._subtrees[0]  # Get the first subtree
    pos_inside_subtree = (subtree.rect[0] + 1, subtree.rect[1] + 1)
    assert tree.get_tree_at_position(pos_inside_subtree) == subtree

# update data_size


def test_leaf_node_data_size_unchanged():
    """Returns the data_size of a leaf node unchanged."""
    leaf_path = os.path.join(path1, 'message.txt')
    leaf = FileSystemTree(leaf_path)
    original_size = leaf.data_size
    leaf.update_data_sizes()
    assert leaf.data_size == original_size


def test_single_level_subtrees_data_size():
    """Updates the data_size of a tree with one level of subtrees."""
    one_level_path = os.path.join(path1, 'images')
    one_level_tree = FileSystemTree(one_level_path)
    expected_size = sum(subtree.data_size
                        for subtree in one_level_tree._subtrees)
    one_level_tree.update_data_sizes()
    assert one_level_tree.data_size == expected_size


def test_multiple_levels_subtrees_data_size():
    """Updates the data_size of a tree with multiple levels of subtrees."""
    multi_level_path = os.path.join(path1)
    multi_level_tree = FileSystemTree(multi_level_path)
    expected_size = multi_level_tree.data_size
    multi_level_tree.update_data_sizes()
    assert multi_level_tree.data_size == expected_size


def test_tree_data_size_zero_returns_none():
    """Returns None if tree's data_size is 0."""
    tree = FileSystemTree(path1)
    # Set the data_size to 0 to simulate an empty-like state
    tree.data_size = 0
    assert tree.get_tree_at_position((50, 50)) is None


# change-size


def test_increase_data_size_positive_factor():
    testing_folder = FileSystemTree(path1)
    leaf = FileSystemTree(os.path.join(path1, 'message.txt'))
    original_size = leaf.data_size
    parent_size = testing_folder.data_size
    assert parent_size == 12598
    increase_factor = 1.5  # Positive factor greater than 1
    leaf.change_size(increase_factor)
    var = math.ceil(original_size * increase_factor)
    expected_size = original_size + var
    assert leaf.data_size == expected_size


def test_decrease_data_size_negative_factor():
    leaf = FileSystemTree(os.path.join(path1, 'message.txt'))
    original_size = leaf.data_size
    assert original_size == 590
    decrease_factor = -0.5  # Negative factor
    leaf.change_size(decrease_factor)
    var = math.floor(original_size * decrease_factor)
    assert leaf.data_size == original_size + var


def test_increase_data_size_factor_less_than_one():
    leaf = FileSystemTree(os.path.join(path1, 'message.txt'))
    original_size = leaf.data_size
    increase_factor = 0.5  # Factor less than 1
    leaf.change_size(increase_factor)
    expected_size = original_size + int(original_size * increase_factor)
    assert leaf.data_size == expected_size


def test_decrease_data_size_factor_less_than_one():
    leaf = FileSystemTree(os.path.join(path1, 'message.txt'))
    original_size = leaf.data_size
    decrease_factor = 0.5  # Factor less than 1
    leaf.change_size(-decrease_factor)
    expected_size = original_size - int(original_size * decrease_factor)
    assert leaf.data_size == expected_size


def test_increase_data_size_factor_greater_than_one():
    leaf = FileSystemTree(os.path.join(path1, 'message.txt'))
    original_size = leaf.data_size
    increase_factor = 2  # Factor greater than 1
    leaf.change_size(increase_factor)
    expected_size = original_size + int(original_size * increase_factor)
    assert leaf.data_size == expected_size


def test_decrease_data_size_factor_greater_than_one():
    leaf = FileSystemTree(os.path.join(path1, 'message.txt'))
    original_size = leaf.data_size
    decrease_factor = 2  # Factor greater than 1
    leaf.change_size(-decrease_factor)
    expected_size = max(original_size - int(original_size * decrease_factor), 1)
    assert leaf.data_size == expected_size


# delete_self


def test_delete_node_with_one_child():
    parent = FileSystemTree(path1)  # The TESTING directory
    child = parent._subtrees[0]  # Assuming it has at least one child
    assert child.delete_self() is True
    assert child not in parent._subtrees


def test_delete_node_with_multiple_children():
    parent = FileSystemTree(path1)  # The TESTING directory
    child = parent._subtrees[0]
    assert child.delete_self() is True
    assert child not in parent._subtrees


def test_update_parents_data_size_after_deletion():
    parent = FileSystemTree(path1)
    child = parent._subtrees[0]  # Assuming it has at least one child
    original_size = parent.data_size
    child_data_size = child.data_size
    assert child.delete_self() is True
    assert parent.data_size == original_size - child_data_size


def test_return_false_if_node_has_no_parent():
    # A root node will not have a parent
    root = FileSystemTree(path1)
    assert root.delete_self() is False


def test_delete_root_node():
    root = FileSystemTree(path1)
    assert root.delete_self() is False  # Root cannot delete itself


def test_delete_node_with_none_name_nonzero_data_size():
    # Simulate a node with None name and non-zero data_size
    node = FileSystemTree(path1)
    node._name = None
    node.data_size = 100
    assert node.delete_self() is False  # Cannot delete a node with None name


def test_delete_node_with_none_name_empty_subtrees():
    # Simulate a node with None name and empty subtrees list
    node = FileSystemTree(path1)
    node._name = None
    node._subtrees = []
    assert node.delete_self() is False


def test_delete_node_with_none_name_nonempty_subtrees_list_zero_data_size():
    node = FileSystemTree(path1)
    node._name = None
    node._subtrees = [FileSystemTree(os.path.join(path1, 'message.txt'))]
    node.data_size = 0
    assert node.delete_self() is False

# expand


def test_expand_tree_with_subtrees():
    tree_with_subtrees = FileSystemTree(os.path.join(path1, 'images'))
    tree_with_subtrees.expand()
    assert tree_with_subtrees._expanded is True


def test_expand_tree_with_one_subtree():
    tree_with_one_subtree = FileSystemTree(os.path.join(path1, 'python_files'))
    tree_with_one_subtree.expand()
    assert tree_with_one_subtree._expanded is True


def test_expand_tree_with_multiple_subtrees():
    tree_with_multiple_subtrees = FileSystemTree(os.path.join(path1, 'images'))
    tree_with_multiple_subtrees.expand()
    assert tree_with_multiple_subtrees._expanded is True


def test_expand_tree_with_large_data_size():
    # Assuming 'wallpapers' folder has a large data size.
    tree_with_large_data_size = FileSystemTree(os.path.join(path1, 'images',
                                                            'wallpapers'))
    tree_with_large_data_size.expand()
    assert tree_with_large_data_size._expanded is True


def test_expand_tree_with_rectangle_of_minimum_size():
    tree_with_minimum_size = FileSystemTree(os.path.join(path1, 'python_files'))
    tree_with_minimum_size.update_rectangles((0, 0, 1, 1))
    tree_with_minimum_size.expand()
    assert tree_with_minimum_size._expanded is True


def test_expand_tree_with_rectangle_of_maximum_size():
    tree_with_maximum_size = FileSystemTree(os.path.join(path1, 'python_files'))
    tree_with_maximum_size.update_rectangles((0, 0, 10000, 10000))
    tree_with_maximum_size.expand()
    assert tree_with_maximum_size._expanded is True


def test_expand_tree_with_rectangle_of_equal_width_and_height():
    tree_with_equal_dimensions = FileSystemTree(os.path.join(path1,
                                                             'python_files'))
    # For equal width and height, we use a square rectangle
    tree_with_equal_dimensions.update_rectangles((0, 0, 100, 100))
    tree_with_equal_dimensions.expand()
    assert tree_with_equal_dimensions._expanded is True

# EXPAND_ALL


def test_does_not_expand_already_expanded_subtrees():
    already_expanded_tree = FileSystemTree(path1)
    already_expanded_tree.expand()  # First expand
    # Mark each subtree as expanded
    for subtree in already_expanded_tree._subtrees:
        subtree._expanded = True
    already_expanded_tree.expand()  # Second expand should do nothing
    for subtree in already_expanded_tree._subtrees:
        assert subtree._expanded


def test_expands_previously_collapsed_subtrees():
    collapsed_tree = FileSystemTree(path1)
    collapsed_tree.expand()  # First expand
    collapsed_tree.collapse()  # Then collapse
    collapsed_tree.expand()  # Expand again
    assert collapsed_tree._expanded

# task - 6


def test_paper_tree_years() -> None:
    """testing the amount of years in cs1_papers.csv"""
    paper = PaperTree('CS1', [], all_papers=True, by_year=True)
    paper.update_rectangles((0, 0, 100, 100))
    paper.expand()
    years = paper.get_rectangles()
    assert len(years) == 45


def test_paper_tree_number_total():
    """testing the total amount of papers in the entire csv"""
    paper = PaperTree('CS1', [], all_papers=True, by_year=True)
    paper.update_rectangles((0, 0, 100, 100))
    paper.expand_all()
    pages = paper.get_rectangles()
    assert len(pages) == 428


def test_paper_tree_papers():
    paper = PaperTree('CS1', [], all_papers=True, by_year=True)
    paper.update_rectangles((0, 0, 100, 100))
    paper.expand()
    a2018 = paper.get_tree_at_position((40, 40))
    a2018.expand()
    assert len(a2018.get_rectangles()) == 8


def test_paper_tree_number():
    """since there are only 9 categories that should be correct"""
    # since we want to know the categories and not the year
    # by_year will be False
    paper = PaperTree('CS1', [], all_papers=True, by_year=False)
    paper.update_rectangles((0, 0, 30, 30))
    paper.expand()
    categories = paper.get_rectangles()
    assert len(categories) == 9


##############################################################################
# Helpers
##############################################################################


def is_valid_colour(colour: tuple[int, int, int]) -> bool:
    """Return True iff <colour> is a valid colour. That is, if all of its
    values are between 0 and 255, inclusive.
    """
    for i in range(3):
        if not 0 <= colour[i] <= 255:
            return False
    return True


def _sort_subtrees(tree: TMTree) -> None:
    """Sort the subtrees of <tree> in alphabetical order.
    THIS IS FOR THE PURPOSES OF THE SAMPLE TEST ONLY; YOU SHOULD NOT SORT
    YOUR SUBTREES IN THIS WAY. This allows the sample test to run on different
    operating systems.

    This is recursive, and affects all levels of the tree.
    """
    if not tree.is_empty():
        for subtree in tree._subtrees:
            _sort_subtrees(subtree)

        tree._subtrees.sort(key=lambda t: t._name)


if __name__ == '__main__':
    import pytest

    pytest.main(['a2_sample_test.py'])
