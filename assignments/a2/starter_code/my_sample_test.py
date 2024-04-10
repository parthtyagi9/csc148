import math
import os

from tm_trees import TMTree, FileSystemTree

EXAMPLE_PATH = os.path.join(os.getcwd(), 'example-directory', 'workshop')

update_rectangles

def test_update_rectangles_disproportionate_sizes():
    small_leaf = TMTree('SmallLeaf', [], 10)
    large_leaf = TMTree('LargeLeaf', [], 90)
    parent = TMTree('Parent', [small_leaf, large_leaf], 100)
    parent.update_rectangles((0, 0, 100, 100))
    assert small_leaf.rect[2] == large_leaf.rect[2]
#
#
# # get_rectangles
#
# def test_get_rectangles_on_deeply_nested_structure():
#     leaf = TMTree('Leaf', [], 10)
#     mid_node = TMTree('MidNode', [leaf], 10)
#     root = TMTree('Root', [mid_node], 10)
#     root.update_rectangles((0, 0, 100, 100))
#     rectangles = root.get_rectangles()
#     assert len(rectangles) == 1
#
#
# # update_data_sizes
#
# def test_update_data_sizes_after_subtree_movement():
#     leaf = TMTree('Leaf', [], 15)
#     old_parent = TMTree('OldParent', [leaf], 0)
#     new_parent = TMTree('NewParent', [], 10)
#     grand_parent = TMTree('grand_parent', [new_parent], 0)
#     leaf.move(grand_parent)
#     old_parent.update_data_sizes()
#     new_parent.update_data_sizes()
#     assert old_parent.data_size == 0, "Old parent's size should be updated to 0."
#     assert grand_parent.data_size == 25, "New parent should include the size of the moved leaf."
#
#
# def test_root_node_expand_collapse():
#     root = TMTree('root', [], 0)
#     root.collapse()  # Should do nothing
#     assert root._expanded is False  # Assuming default _expanded state is True
#     root.expand()  # Confirm it's still expanded
#     assert root._expanded is False
#
# def test_leaf_node_collapse_expand():
#     leaf = TMTree('leaf', [], 10)
#     parent = TMTree('parent', [leaf], 0)
#     leaf.collapse()  # Collapse parent through leaf
#     assert parent._expanded is False
#     leaf.expand()  # Expand should only affect the leaf if designed to do so
#     assert leaf._expanded is False  # Assuming leaf can be expanded independently
#     assert parent._expanded is False  # Parent should remain collapsed
#
# def test_deeply_nested_tree():
#     grandchild = TMTree('grandchild', [], 10)
#     child = TMTree('child', [grandchild], 0)
#     parent = TMTree('parent', [child], 0)
#     grandchild.collapse()  # Collapse up the hierarchy
#     assert child._expanded is False
#     assert parent._expanded is False
#     parent.expand()  # Expanding parent doesn't automatically expand child or grandchild
#     assert parent._expanded is True
#     assert child._expanded is False
#
# def test_multiple_siblings():
#     sibling1 = TMTree('sibling1', [], 10)
#     sibling2 = TMTree('sibling2', [], 20)
#     parent = TMTree('parent', [sibling1, sibling2], 0)
#     sibling1.collapse()  # Collapse parent through sibling1
#     assert parent._expanded is False
#     parent.expand()  # Expand parent
#     assert parent._expanded is True
#     assert sibling1._expanded is False  # Siblings remain collapsed
#     assert sibling2._expanded is False
#
# def test_repeated_collapse_expand():
#     node = TMTree('node', [], 10)
#     node.collapse()  # First collapse
#     assert node._expanded is False
#     node.collapse()  # Second collapse should do nothing
#     assert node._expanded is False
#     node.expand()  # First expand
#     assert node._expanded is False
#     node.expand()  # Second expand should do nothing
#     assert node._expanded is False
#
# def test_get_rectangles_empty_tree():
#     # Test get_rectangles on an empty tree
#     empty_tree = TMTree('Empty', [], 0)
#     rectangles = empty_tree.get_rectangles()
#     assert len(rectangles) == 0, "Empty tree should return an empty list of rectangles."
#
# def test_get_rectangles_collapsed_tree():
#     # Test get_rectangles on a collapsed tree
#     child = TMTree('Child', [], 10)
#     parent = TMTree('Parent', [child], 0)
#     rectangles = parent.get_rectangles()
#     assert len(rectangles) == 1, "Collapsed tree should return a single rectangle."
#     assert rectangles[0][0] == parent.rect, "Incorrect rectangle for collapsed tree."
#
# def test_get_tree_at_position_outside_rect():
#     # Test get_tree_at_position with a position outside the tree's rectangle
#     leaf = TMTree('Leaf', [], 10)
#     leaf.update_rectangles((0, 0, 100, 100))
#     selected = leaf.get_tree_at_position((-10, -10))
#     assert selected is None, "Position outside rectangle should return None."
#
# def test_update_data_sizes_empty_tree():
#     # Test update_data_sizes on an empty tree
#     empty_tree = TMTree('Empty', [], 0)
#     size = empty_tree.update_data_sizes()
#     assert size == 0, "Empty tree should have a data size of 0."
#
# # def test_update_data_sizes_negative_size():
# #     # Test update_data_sizes with a negative data size
# #     negative_leaf = TMTree('NegativeLeaf', [], -10)
# #     parent = TMTree('Parent', [negative_leaf], 0)
# #     size = parent.update_data_sizes()
# #     assert size == 0, "Tree with negative data size should have a size of 0."
#
# def test_get_path_string_root():
#     # Test get_path_string on the root node
#     root = TMTree('Root', [], 0)
#     path = root.get_path_string()
#     assert path == 'Root', "Path string for root should be its name."

# def test_get_suffix_non_leaf():
#     # Test get_suffix on a non-leaf node
#     child = TMTree('Child', [], 10)
#     parent = TMTree('Parent', [child], 0)
#     suffix = parent.get_suffix()
#     assert 'folder' in suffix, "Non-leaf node should have 'folder' in its suffix."
#     assert '1 items' in suffix, "Non-leaf node should have '1 items' in its suffix."

def test_tree_new_size_empty_tree():
    # Test tree_new_size on an empty tree
    empty_tree = TMTree('Empty', [], 0)
    empty_tree._tree_new_size()
    assert empty_tree.data_size == 0, "Empty tree size should remain 0 after tree_new_size."