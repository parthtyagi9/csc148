# import math
# import os
#
# from tm_trees import TMTree, FileSystemTree
#
# EXAMPLE_PATH = os.path.join(os.getcwd(), 'example-directory', 'workshop')
#
#
#
#
#
# def test_zero_total_size_update_rectangles() -> None:
#     child1 = TMTree('Child1', [], 0)
#     child2 = TMTree('Child2', [], 0)
#     parent = TMTree('Parent', [child1, child2], 0)
#     parent.update_rectangles((0, 0, 100, 100))
#     assert parent.rect == (0, 0, 0, 0)
#     assert child1.rect == (0, 0, 0, 0)
#     assert child2.rect == (0, 0, 0, 0)
#
# def test_collapse_expanded_tree():
#     # Test collapsing an expanded tree
#     child = TMTree('Child', [], 10)
#     parent = TMTree('Parent', [child], 0)
#     parent.expand()
#     parent.collapse()
#     assert parent._expanded, "Parent should NOT be collapsed."
#     # child.collapse()
#     # assert not parent._expanded
#     # assert parent.get_rectangles() == [(parent.rect, parent._colour)], "Only parent rectangle should be returned."
#
# def test_empty_tree_update_rectangles() -> None:
#     tree = TMTree('Root', [], 0)
#     tree.update_rectangles((0, 0, 100, 100))
#     assert tree.rect == (0, 0, 0, 0), "The rectangle should be unchanged for an empty tree."
#
# def test_single_child_update_rectangles() -> None:
#     child = TMTree('Child', [], 100)
#     parent = TMTree('Parent', [child], 0)
#     parent.update_rectangles((0, 0, 100, 100))
#     assert child.rect == (0, 0, 100, 100), "The single child should occupy the entire rectangle."
#
# def test_leaves_with_different_sizes_update_rectangles() -> None:
#     child1 = TMTree('Child1', [], 25)
#     child2 = TMTree('Child2', [], 75)
#     parent = TMTree('Parent', [child1, child2], 0)
#     parent.update_rectangles((0, 0, 100, 100))
#     # Assuming horizontal partitioning for simplicity
#     assert child1.rect == (0, 0, 100, 25), "The first child's rectangle is not correctly sized."
#     assert child2.rect == (0, 25, 100, 75), "The second child's rectangle is not correctly sized."
#
# def test_move_leaf_to_new_parent2():
#     # Test moving a leaf to a new parent
#     leaf = TMTree('Leaf', [], 10)
#     old_parent = TMTree('OldParent', [leaf], 0)
#     new_parent = TMTree('NewParent', [], 0)
#     leaf.move(new_parent)
#     assert leaf not in new_parent._subtrees, "Leaf should be moved to the new parent."
#     assert leaf in old_parent._subtrees, "Leaf should be removed from the old parent."
#
# def test_delete_leaf():
#     # Test deleting a leaf node
#     leaf = TMTree('Leaf', [], 10)
#     parent = TMTree('Parent', [leaf], 10)
#     leaf.delete_self()
#     assert leaf not in parent._subtrees, "Leaf should be deleted from parent."
#     assert parent.data_size == 0, "Parent size should be updated after deletion."
#
# def test_get_tree_at_position_edge():
#     # Test selecting a tree at the edge of its rectangle
#     child1 = TMTree('Child1', [], 25)
#     parent = TMTree('Parent', [child1], 25)
#     parent.update_rectangles((0, 0, 100, 100))
#     parent.expand_all()
#     selected = parent.get_tree_at_position((99, 99))  # At the bottom-right edge
#     assert selected == child1, "Should select the tree at the position's edge."
#
# def test_deeply_nested_tree_update_rectangles() -> None:
#     grandchild = TMTree('Grandchild', [], 50)
#     child = TMTree('Child', [grandchild], 0)
#     parent = TMTree('Parent', [child], 0)
#     parent.update_rectangles((0, 0, 100, 100))
#     assert child.rect == (0, 0, 100, 100), "The child's rectangle is not correctly sized."
#     assert grandchild.rect == (0, 0, 100, 100), "The grandchild's rectangle is not correctly sized."
#
# def test_zero_size_children_update_rectangles() -> None:
#     child1 = TMTree('Child1', [], 0)
#     child2 = TMTree('Child2', [], 100)
#     parent = TMTree('Parent', [child1, child2], 0)
#     parent.update_rectangles((0, 0, 100, 100))
#     # Depending on the implementation, child1 might have a very small or no rectangle at all.
#     # This test needs to be adjusted based on how such cases are handled.
#     assert child2.rect == (0, 0, 100, 100), "The second child should occupy the entire rectangle given its size."
#
# def testtmtree_with_zero_size_files():
#     # Test TMTree with files of size 0
#     zero_size_file = TMTree('zero_file', [], 0)
#     parent = TMTree('parent', [zero_size_file], 0)
#     assert parent.data_size == 0, "Parent of zero-sized file should have size 0."
#
# def test_update_rectangles_single_leaf():
#     # Test with a single leaf node
#     leaf = TMTree('leaf', [], 10)
#     leaf.update_rectangles((0, 0, 100, 100))
#     assert leaf.rect == (0, 0, 100, 100)
#
# def test_update_rectangles_deep_nesting():
#     # Test deeply nested structure
#     deep_child = TMTree('DeepChild', [], 5)
#     for _ in range(5):  # 5 levels deep
#         deepchild = TMTree(f'Level{_}', [deep_child], 0)
#     deep_child.update_rectangles((0, 0, 100, 100))
#     assert deep_child.rect[2] > 0 and deep_child.rect[3] > 0, "Deeply nested child should have a non-zero rectangle."
#
# def test_parent_with_zero_size_update_rectangles() -> None:
#     child1 = TMTree('Child1', [], 10)
#     child2 = TMTree('Child2', [], 10)
#     parent = TMTree('Parent', [child1, child2], 0)
#     parent.update_rectangles((0, 0, 100, 50))
#     assert parent.rect == (0, 0, 100, 50)
#     assert child1.rect == (0, 0, 50, 50)
#     assert child2.rect == (50, 0, 50, 50)
#
#
#
# def test_single_file():
#     tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'draft.pptx'))
#     assert tree._name == 'draft.pptx'
#     assert tree._subtrees == []
#     assert tree._parent_tree is None
#     assert tree.data_size == 58
#
#
# def test_activities_folder():
#     tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'activities/images'))
#     assert tree._name == 'images'
#     assert tree._parent_tree is None
#     assert tree.data_size == 69
#     assert len(tree._subtrees) == 2
#     assert tree._subtrees[0]._name == 'Q3.pdf'
#
#
# images_sample_path = os.path.join(os.getcwd(),
#                                   'example-directory/workshop/activities/images')
#
#
# def test_images_folder():
#     tree = FileSystemTree(os.path.join(images_sample_path))
#     assert tree._name == 'images'
#     assert tree._parent_tree is None
#     assert tree.data_size == 69
#     assert len(tree._subtrees) == 2
#
#
# def test_deleting():
#     subtree1 = TMTree('subtree1', [], 10)
#     subtree2 = TMTree('subtree2', [], 20)
#     parent = TMTree('parent', [subtree1, subtree2], 0)
#     delete_result = subtree1.delete_self()
#     assert delete_result is True
#     assert len(parent._subtrees) == 1
#     assert parent._subtrees[0] == subtree2
#     assert parent.data_size == 20
#
#
# def test_move_leaf_to_new_parent():
#     leaf = TMTree('leaf', [], 15)
#     old_parent = TMTree('old_parent', [leaf], 0)
#     a = TMTree('a', [], 5)
#     new_parent = TMTree('new_parent', [a], 0)
#     leaf.move(new_parent)
#     assert new_parent.data_size == 20
#     assert len(old_parent._subtrees) == 0
#     assert len(new_parent._subtrees) == 2
#     assert new_parent._subtrees[1] == leaf
#     assert old_parent.data_size == 0
#
#
# def test_update_data_sizes_after_removal():
#     g1 = TMTree('g1', [], 45)
#     g2 = TMTree('g2', [], 20)
#     new_tree = TMTree('new_tree', [g1, g2], 0)
#     new_tree._subtrees.remove(g1)
#     new_tree.update_data_sizes()
#     assert len(new_tree._subtrees) == 1
#     assert new_tree._subtrees[0] == g2
#     assert new_tree.data_size == 20
#
#
# def test_increase_leaf_size():
#     leaf = TMTree('leaf', [], 10)
#     increase_factor = 0.25
#     leaf.change_size(increase_factor)
#     expected_size = 13
#     assert leaf.data_size == expected_size
#
#
# def test_decrease_leaf_size():
#     leaf = TMTree('leaf', [], 10)
#     decrease_factor = -0.2
#     leaf.change_size(decrease_factor)
#     expected_size = 8
#     assert leaf.data_size == expected_size
#     leaf.change_size(-0.9)
#     assert leaf.data_size == 1
#
#
# def test_change_size_zero_factor():
#     leaf = TMTree('leaf', [], 10)
#     leaf.change_size(0)
#     assert leaf.data_size == 10
#
#
# def test_change_size_small_positive_factor():
#     leaf = TMTree('leaf', [], 10)
#     small_increase_factor = 0.001
#     leaf.change_size(small_increase_factor)
#     assert leaf.data_size == 11
#
#
# def test_change_size_small_negative_factor():
#     leaf = TMTree('leaf', [], 10)
#     small_decrease_factor = -0.001
#     leaf.change_size(small_decrease_factor)
#     assert leaf.data_size == 9
#
#
# def test_change_size_reduce_below_one():
#     leaf = TMTree('leaf', [], 2)
#     decrease_factor = -0.9
#     leaf.change_size(decrease_factor)
#     assert leaf.data_size == 1
#
#
# def test_change_size_non_leaf_node():
#     child_leaf = TMTree('child_leaf', [], 10)
#     non_leaf = TMTree('non_leaf', [child_leaf], 0)
#     non_leaf.change_size(0.5)
#     assert non_leaf.data_size == 10
#
#
# def test_delete_leaf_node():
#     leaf = TMTree('leaf', [], 10)
#     parent = TMTree('parent', [leaf], 0)
#     result = leaf.delete_self()
#     assert result is True
#     assert leaf not in parent._subtrees
#     assert parent.data_size == 0
#
#
# def test_delete_node_without_parent():
#     standalone_leaf = TMTree('standalone_leaf', [], 15)
#     result = standalone_leaf.delete_self()
#     assert result is False
#
#
# def test_delete_non_leaf_node():
#     child = TMTree('child', [], 20)
#     non_leaf = TMTree('non_leaf', [child], 0)
#     parent = TMTree('parent', [non_leaf], 0)
#     result = non_leaf.delete_self()
#     assert result is True
#     assert non_leaf not in parent._subtrees
#     assert parent.data_size == 0
#
#
# def test_multiple_deletions():
#     leaf1 = TMTree('leaf1', [], 5)
#     leaf2 = TMTree('leaf2', [], 10)
#     parent = TMTree('parent', [leaf1, leaf2], 0)
#     leaf1.delete_self()
#     assert leaf1 not in parent._subtrees
#     assert parent.data_size == 10
#     leaf2.delete_self()
#     assert leaf2 not in parent._subtrees
#     assert parent.data_size == 0
#
#
# def test_empty_tree():
#     empty_tree = TMTree(None, [], 0)
#     assert empty_tree.is_empty() is True
#
#
# def test_update_data_sizes():
#     leaf = TMTree('leaf', [], 10)
#     parent = TMTree('parent', [leaf], 0)
#     parent.update_data_sizes()
#     assert parent.data_size == 10
#
#
# def test_move_leaf():
#     leaf = TMTree('leaf', [], 10)
#     old_parent = TMTree('old_parent', [leaf], 0)
#     new_parent = TMTree('new_parent', [], 0)
#     leaf.move(new_parent)
#     assert leaf not in new_parent._subtrees
#     assert leaf in old_parent._subtrees
#
#
# def test_delete_self_leaf():
#     leaf = TMTree('leaf', [], 10)
#     parent = TMTree('parent', [leaf], 0)
#     assert leaf.delete_self() is True
#     assert leaf not in parent._subtrees
#
#
# def test_delete_self_non_leaf():
#     child = TMTree('child', [], 10)
#     non_leaf = TMTree('non_leaf', [child], 0)
#     assert non_leaf.delete_self() is False
#
#
# def test_change_size_leaf():
#     leaf = TMTree('leaf', [], 10)
#     leaf.change_size(0.5)
#     assert leaf.data_size == 15
#
#
# def test_change_size_non_leaf():
#     child = TMTree('child', [], 10)
#     non_leaf = TMTree('non_leaf', [child], 0)
#     non_leaf.change_size(0.5)
#     assert non_leaf.data_size == 10
#
#
# def test_expand_collapse():
#     leaf = TMTree('leaf', [], 10)
#     parent = TMTree('parent', [leaf], 0)
#     parent.collapse()
#     assert parent._expanded is False
#     parent.expand()
#     assert parent._expanded is True
#
#
# def test_get_tree_at_position_edge_cases():
#     # Test with an empty tree
#     empty_tree = TMTree(None, [], 0)
#     assert empty_tree.get_tree_at_position((5, 5)) is None
#
#     # Test with a tree where the position is outside any rectangle
#     leaf = TMTree('leaf', [], 10)
#     leaf.rect = (0, 0, 10, 10)
#     assert leaf.get_tree_at_position((15, 15)) is None
#
#
# def test_change_size_edge_cases():
#     # Test increasing the size of a leaf node
#     leaf = TMTree('leaf', [], 10)
#     leaf.change_size(0.1)  # Increase by 10%
#     assert leaf.data_size == 11  # Rounded up
#
#     # Test decreasing the size of a leaf node to below 1
#     leaf.change_size(-0.95)  # Decrease by 95%
#     assert leaf.data_size == 1  # Cannot go below 1
#
#     # Test change_size on a non-leaf node should have no effect
#     non_leaf = TMTree('non_leaf', [leaf], 0)
#     non_leaf.change_size(0.5)
#     assert non_leaf.data_size == 1  # Remains unchanged
#
#
# def test_delete_self_edge_cases():
#     # Test deleting a leaf node
#     leaf = TMTree('leaf', [], 10)
#     parent = TMTree('parent', [leaf], 0)
#     assert leaf.delete_self() is True
#     assert len(parent._subtrees) == 0
#
#     # Test deleting the root node (should fail)
#     assert parent.delete_self() is False
#
#     # Test deleting a node with no parent
#     standalone_leaf = TMTree('standalone', [], 5)
#     assert standalone_leaf.delete_self() is False
#
#
# def test_move_leaf_to_destination() -> None:
#     # Create a leaf and a destination with one subtree
#
#     # # THIS TEST SHOULD NOT PASS
#     # leaf1 = TMTree('Leaf', [], 10)
#     # l2 = TMTree('L2', [], 20)
#     # destination = TMTree('Destination', [l2], 0)
#     #
#     # leaf1.move(destination)
#     #
#     # assert destination._subtrees.__len__() == 2
#     pass
#
#
# #
# def test_expanded_rectangles() -> None:
#     nested_leaf = TMTree('nested_leaf', [], 5)
#     parent = TMTree('parent', [nested_leaf], 0)
#     new_leaf = TMTree('a', [], 5)
#     a = TMTree('as', [new_leaf], 0)
#     # new_leaf.move(parent)
#     new_leaf.rect = (8, 2, 6, 6)
#     nested_leaf.rect = (2, 2, 6, 6)
#     parent.rect = (0, 0, 10, 10)
#     assert not new_leaf.get_parent() is parent
#     assert not parent._expanded
#     assert parent.get_tree_at_position((3, 3)) is parent
#     parent.expand_all()
#     assert parent.get_tree_at_position((3, 3)) is nested_leaf
#     # new_leaf.move(parent)
#     assert parent.data_size == 5
#     assert parent.get_tree_at_position((8, 2)) is nested_leaf
#     # assert parent.get_tree_at_position((9, 2)) is new_leaf
#
#
# def test_move_edge_cases():
#     # Test moving a leaf to a new parent
#     leaf = TMTree('leaf', [], 10)
#     old_parent = TMTree('old_parent', [leaf], 0)
#     new_parent = TMTree('new_parent', [], 0)
#     leaf.move(new_parent)
#     assert len(old_parent._subtrees) == 1
#     assert len(new_parent._subtrees) == 0
#
#     # Test moving a non-leaf node (should have no effect)
#     non_leaf = TMTree('non_leaf', [leaf], 0)
#     another_parent = TMTree('another_parent', [], 0)
#     non_leaf.move(another_parent)
#     assert len(another_parent._subtrees) == 0
#
#
# def test_collapse_expand_edge_cases() -> None:
#     # Initially, the tree is expanded
#     leaf1 = TMTree('leaf1', [], 5)
#     leaf2 = TMTree('leaf2', [], 10)
#     parent = TMTree('parent', [leaf1, leaf2], 0)
#     grandparent = TMTree('grandparent', [parent], 0)
#     grandparent.expand_all()
#     assert grandparent._expanded is True
#     assert leaf1._expanded is False
#
#     # # Collapse the tree and check
#     leaf1.collapse_all()
#     assert grandparent._expanded is False
#     assert all(not subtree._expanded for subtree in grandparent._subtrees)
#
#     # # Expand the tree and check
#     grandparent.expand_all()
#     assert grandparent._expanded is True
#     assert all(subtree._expanded for subtree in grandparent._subtrees)
#
#
# def test_complex_interactions() -> None:
#     # Create a complex file system structure
#     leaf1 = TMTree('leaf1', [], 30)
#     leaf2 = TMTree('leaf2', [], 20)
#     leaf3 = TMTree('leaf3', [], 50)
#     subfolder1 = TMTree('subfolder1', [leaf1, leaf2], 0)
#     subfolder2 = TMTree('subfolder2', [leaf3], 0)
#     root = TMTree('root', [subfolder1, subfolder2], 0)
#
#     # Update rectangles for visualization
#     root.update_rectangles((0, 0, 100, 100))
#
#     # Verify initial structure
#     assert subfolder1.data_size == 50
#     assert subfolder2.data_size == 50
#     assert root.data_size == 100
#
#     # Move leaf3 to subfolder1
#     leaf3.move(subfolder1)
#
#     # Verify structure after move
#     assert subfolder1.data_size == 100
#     assert subfolder2.data_size == 0
#     assert root.data_size == 100
#     assert leaf3 in subfolder1._subtrees
#     assert leaf3 not in subfolder2._subtrees
#
#     # Change size of leaf1 by increasing it by 10%
#     leaf1.change_size(0.1)
#
#     # Verify size change
#     assert leaf1.data_size == 33  # Rounded up from 33
#     assert subfolder1.data_size == 103  # Updated to include new size of leaf1
#
#     # Expand subfolder1 and collapse root
#     # MISTAKE
#     subfolder1.expand()
#     root.collapse()
#
#     #Verify expanded and collapsed states
#     assert subfolder1._expanded
#     assert not root._expanded
#
#     # Get rectangles should only include root because it's collapsed
#     rectangles = root.get_rectangles()
#     assert len(rectangles) == 1 # Only root is displayed
#     assert rectangles[0][0] == (0, 0, 100, 100)  # Root rectangle
#
#     # Expand root and collapse subfolder1
#     root.expand()
#     subfolder1.collapse()
#
#     # Verify expanded and collapsed states after change
#     assert not subfolder1._expanded
#     assert not root._expanded
#
#     # Get rectangles should include root and subfolder2 (since subfolder1 is collapsed)
#     rectangles = root.get_rectangles()
#     assert len(rectangles) == 1  # Root and subfolder2 are displayed
#
# def test_complex_interactions2() -> None:
#     # Create a complex file system structure
#     leaf1 = TMTree('leaf1', [], 30)
#     leaf2 = TMTree('leaf2', [], 20)
#     leaf3 = TMTree('leaf3', [], 50)
#     subfolder1 = TMTree('subfolder1', [leaf1, leaf2], 0)
#     subfolder2 = TMTree('subfolder2', [leaf3], 0)
#     root = TMTree('root', [subfolder1, subfolder2], 0)
#
#     # Update rectangles for visualization
#     root.update_rectangles((0, 0, 100, 100))
#
#     # Verify initial structure
#     assert subfolder1.data_size == 50
#     assert subfolder2.data_size == 50
#     assert root.data_size == 100
#
#     # Move leaf3 to subfolder1
#     leaf3.move(subfolder1)
#
#     # Verify structure after move
#     assert subfolder1.data_size == 100
#     assert subfolder2.data_size == 0
#     assert root.data_size == 100
#     assert leaf3 in subfolder1._subtrees
#     assert leaf3 not in subfolder2._subtrees
#
#     # Change size of leaf1 by increasing it by 10%
#     leaf1.change_size(0.1)
#
#     # Verify size change
#     assert leaf1.data_size == 33  # Rounded up from 33
#     assert subfolder1.data_size == 103  # Updated to include new size of leaf1
#
#     # Expand subfolder1 and collapse root
#     subfolder1.expand()
#     # root.collapse()
#     subfolder1.collapse_all()
#
#     # Verify expanded and collapsed states
#     assert not subfolder1._expanded
#     assert not root._expanded  # Root is collapsed
#
#     # Get rectangles should only include root because it's collapsed
#     rectangles = root.get_rectangles()
#     assert len(rectangles) == 1  # Only root is displayed
#     assert rectangles[0][0] == (0, 0, 100, 100)  # Root rectangle
#
#     # Expand root and collapse subfolder1
#     root.expand()
#     subfolder1.collapse()
#
#     # Verify expanded and collapsed states after change
#     assert not subfolder1._expanded
#     assert not root._expanded
#
#     # Get rectangles should include root and subfolder2 (since subfolder1 is collapsed)
#     rectangles = root.get_rectangles()
#     assert len(rectangles) == 1  # Root and subfd
#
#
# def test_collapse_expanded_tree2():
#     # Test collapsing an expanded tree
#     child2 = TMTree('Child2', [], 10)
#     child = TMTree('Child', [child2], 10)
#     parent = TMTree('Parent', [child], 0)
#     parent.expand()
#     parent.collapse()
#     assert parent._expanded, "Parent should NOT be collapsed."
#     # if the tmtree is not in self._rect do nothing
#
# def test_delete_and_structure() -> None:
#     # Setup a tree structure
#     leaf1 = TMTree('leaf1', [], 10)
#     leaf2 = TMTree('leaf2', [], 20)
#     subfolder1 = TMTree('subfolder1', [leaf1], 0)
#     subfolder2 = TMTree('subfolder2', [leaf2], 0)
#     root = TMTree('root', [subfolder1, subfolder2], 0)
#
#     # Delete a leaf and check structure
#     assert leaf1.delete_self()
#     assert leaf1 not in subfolder1._subtrees
#     assert subfolder1.data_size == 0
#
#     # Delete a subtree and check root's structure
#     assert subfolder1.delete_self()
#     assert subfolder1 not in root._subtrees
#     assert root.data_size == 20
#
#
# def test_complex_movement() -> None:
#     # Setup a complex tree structure
#     leaf1 = TMTree('leaf1', [], 10)
#     leaf2 = TMTree('leaf2', [], 20)
#     subfolder1 = TMTree('subfolder1', [leaf1], 0)
#     subfolder2 = TMTree('subfolder2', [leaf2], 0)
#     root = TMTree('root', [subfolder1, subfolder2], 0)
#
#     # Move subfolder1 into subfolder2 and verify
#     subfolder1.move(subfolder2)
#     assert subfolder1 not in subfolder2._subtrees
#     assert subfolder2.data_size == 20  # 20 from leaf2 and 10 from leaf1 in subfolder1
#     assert root.data_size == 30
#     assert subfolder1 in root._subtrees
#
#
# def test_expanded_view() -> None:
#     # Setup a complex tree structure
#     leaf1 = TMTree('leaf1', [], 10)
#     leaf2 = TMTree('leaf2', [], 20)
#     subfolder1 = TMTree('subfolder1', [leaf1], 0)
#     subfolder2 = TMTree('subfolder2', [leaf2], 0)
#     root = TMTree('root', [subfolder1, subfolder2], 0)
#
#     # Expand subfolder1 and check the expanded view
#     subfolder1.expand()
#     assert subfolder1._expanded
#     rectangles = subfolder1.get_rectangles()
#     assert len(rectangles) == 1  # Only leaf1 should be visible
#
#     # Expand root and check the expanded view
#     root.expand_all()
#     rectangles = root.get_rectangles()
#     assert len(rectangles) == 2  # leaf1 and leaf2 should be visible
#
#     # Collapse root and check the collapsed view
#     root.collapse_all()
#     rectangles = root.get_rectangles()
#     assert len(rectangles) == 1  # Only root should be visible
#
#
# def test_user_filesystem():
#     leaf1 = TMTree('file1.txt', [], 10)
#     leaf2 = TMTree('file2.txt', [], 20)
#     leaf3 = TMTree('file3.txt', [], 30)
#     subfolder1 = TMTree('Subfolder1', [leaf1, leaf2], 0)
#     subfolder2 = TMTree('Subfolder2', [leaf3], 0)
#     root = TMTree('Root', [subfolder1, subfolder2], 0)
#
#     root.update_rectangles((0, 0, 300, 300))
#
#     root.expand()
#     subfolder1.expand()
#
#     assert subfolder1._expanded
#     assert len(subfolder1.get_rectangles()) == 2
#
#     leaf1.collapse()
#     leaf3.move(subfolder1)
#
#     assert leaf3 in subfolder1._subtrees
#     assert leaf3 not in subfolder2._subtrees
#     assert subfolder1.data_size == 60
#     assert subfolder2.data_size == 0
#     assert root.data_size == 60
#     assert not subfolder2._subtrees
#
#     subfolder2.expand()
#     subfolder1.collapse()
#     assert root.get_tree_at_position((0, 1)) == root
#
#     a = subfolder2.get_rectangles()
#     assert len(a) == 0
#
#     subfolder1.collapse()
#     root.expand_all()
#
#     assert root._expanded
#     assert subfolder1._expanded
#
#     rectangles = root.get_rectangles()
#     assert len(rectangles) == 3
#
#     assert leaf2.delete_self()
#     assert leaf2 not in subfolder1._subtrees
#     assert subfolder1.data_size == 40
#
#     assert root.data_size == 40
#
#
# def test_detailed_interactions() -> None:
#     # Setup: Creating a more detailed structure with multiple levels of depth
#     leaf_a = TMTree('leaf_a', [], 5)
#     leaf_b = TMTree('leaf_b', [], 10)
#     leaf_c = TMTree('leaf_c', [], 15)
#     leaf_d = TMTree('leaf_d', [], 20)
#     leaf_e = TMTree('leaf_e', [], 25)
#
#     subfolder_a1 = TMTree('subfolder_a1', [leaf_a, leaf_b], 0)
#     subfolder_a2 = TMTree('subfolder_a2', [leaf_c], 0)
#     subfolder_b1 = TMTree('subfolder_b1', [leaf_d, leaf_e], 0)
#
#     root_a = TMTree('root_a', [subfolder_a1, subfolder_a2], 0)
#     root_b = TMTree('root_b', [subfolder_b1], 0)
#     super_root = TMTree('super_root', [root_a, root_b], 0)
#
#     # Initial check
#     assert super_root.data_size == 75  # Total of all leaves
#     assert root_a.data_size == 30  # Total of leaves under root_a
#     assert root_b.data_size == 45  # Total of leaves under root_b
#     #
#     # Expand super_root and check if sub-trees are expanded accordingly
#     super_root.expand()
#     assert super_root._expanded
#     assert not root_a._expanded  # Should remain collapsed since only super_root was expanded
#     assert not root_b._expanded  # Should remain collapsed since only super_root was expanded
#
#     # Expand root_a and check
#     root_a.expand()
#     assert root_a._expanded
#     assert not subfolder_a1._expanded  # Check if subfolders under expanded root are also expanded
#
#     # Move leaf_d from root_b to root_a and check structures and sizes
#     leaf_d.move(root_a)
#     assert leaf_d in root_a._subtrees  # leaf_d should now be a direct child of root_a
#     assert leaf_d not in subfolder_b1._subtrees  # leaf_d should no longer be under subfolder_b1
#     assert root_a.data_size == 50  # Updated size after moving leaf_d
#     assert root_b.data_size == 25  # Updated size after moving leaf_d
#     #
#     # Test deletion and size update
#     leaf_e.delete_self()
#     assert leaf_e not in subfolder_b1._subtrees  # leaf_e should be removed
#     assert root_b.data_size == 0  # Updated size after deleting leaf_e
#
#     # Collapse and expand operations on nested structures
#     root_a.collapse_all()  # Collapse all under root_a
#     assert not subfolder_a1._expanded
#     assert not subfolder_a2._expanded
#     assert not root_a._expanded  # root_a should still be expanded since collapse_all doesn't affect the caller
#
#     root_a.expand_all()  # Expand all under root_a
#     assert subfolder_a1._expanded
#     assert subfolder_a2._expanded
#
#     # Check rectangle updates after structural changes
#     super_root.update_rectangles((0, 0, 100, 100))
#     # Assuming a specific implementation of update_rectangles, check a few key rectangles
#     assert super_root.rect == (0, 0, 100, 100)
#     assert root_a.rect[2] >= 0  # Width of root_a's rectangle should be positive
#     assert root_b.rect[2] >= 0  # Width of root_b's rectangle should be positive
#     #
#     # Check get_tree_at_position after rectangle updates
#     assert super_root.get_tree_at_position((1, 1)) == super_root
#     # Depending on your update_rectangles implementation, you might need to adjust the positions below
#     assert root_a.get_tree_at_position((1, 1)) == leaf_a
#     assert root_b.get_tree_at_position((super_root.rect[2] - 1, 1)) is None
#
#     # # Final consistency check
#     assert super_root.data_size == 50  # Ensure total size is updated and consistent
#
#
# def test_size_manipulation_and_rounding() -> None:
#     # Setup: creating a single file representation with an initial size in kilobytes
#     # Convert kilobytes to bytes for the initial size (10.44 KB -> 10440 bytes)
#     initial_kb_size = 10.44
#     initial_byte_size = int(initial_kb_size * 1024)  # Convert KB to Bytes
#     file_leaf = TMTree('file.txt', [], initial_byte_size)
#
#     # Check initial size in bytes
#     assert file_leaf.data_size == 10690  # 10.44 KB in bytes
#     #
#     # Increase size by 1% and check the rounding behavior
#     increase_percentage = 0.01
#     file_leaf.change_size(increase_percentage)
#
#     # Calculate the expected increase and apply ceiling rounding
#     expected_increase = initial_byte_size * increase_percentage
#     rounded_increase = math.ceil(expected_increase)
#
#     # Check the updated size
#     assert file_leaf.data_size == initial_byte_size + rounded_increase
#
#     # # For the given example, the expected increase is 104.4 bytes
#     # After ceiling rounding, it should become 105 bytes
#     # So, the new size should be 10440 + 105 = 10545 bytes
#     assert file_leaf.data_size == 10797
#
#     # Decrease size by 2% and check the rounding behavior
#     decrease_percentage = -0.02
#     file_leaf.change_size(decrease_percentage)
#
#     # Calculate the expected decrease and apply floor rounding since it's a decrease
#     expected_decrease = file_leaf.data_size * decrease_percentage
#     rounded_decrease = math.floor(expected_decrease)
#
#     # # Check the updated size
#     assert file_leaf.data_size == 10545 + rounded_decrease + (10581 - 10333)
#     #
#     # For a 2% decrease from 10545, the expected decrease is -210.9
#     # After floor rounding, it should become -211
#     # So, the new size should be 10545 - 211 = 10334 bytes
#     assert file_leaf.data_size == 10581
#     #
#     # Ensure the size doesn't go below 1 byte on further reductions
#     massive_decrease_percentage = -0.99  # 99% decrease
#     file_leaf.change_size(massive_decrease_percentage)
#
#     # The size should now be clamped to 1 byte, as it can't go below that
#     assert file_leaf.data_size == 105
#
# def test_zero_size_leaf_rectangles() -> None:
#     zero_size_leaf = TMTree('ZeroSize', [], 0)
#     zero_size_leaf.update_rectangles((0, 0, 100, 100))
#     assert zero_size_leaf.get_rectangles() == [], "Zero size leaf should return an empty list of rectangles."
#
# # def test_parent_with_zero_size_leaf_rectangles() -> None:
# #     zero = TMTree('zero', [], 0)
# #     parent = TMTree('Parent', [zero], 10)
# #     parent.update_rectangles((0, 0, 100, 100))
# #     assert len(parent.get_rectangles()) == 0
#
# # def test_deeply_nested_zero_size_leaf_rectangles() -> None:
# #     deep_zero_leaf = TMTree('DeepZero', [], 0)
# #     mid_parent = TMTree('MidParent', [deep_zero_leaf], 10)
# #     top_parent = TMTree('TopParent', [mid_parent], 20)
# #     top_parent.update_rectangles((0, 0, 100, 100))
# #     rectangles = top_parent.get_rectangles()
# #     assert any(rect for rect in rectangles if rect[0] == deep_zero_leaf.rect), "Deep zero-size leaf's rectangle should still be part of the output."
#
# def test_wide_and_tall_rectangles() -> None:
#     wide_leaf = TMTree('WideLeaf', [], 50)
#     tall_leaf = TMTree('TallLeaf', [], 50)
#     wide_parent = TMTree('WideParent', [wide_leaf], 100)
#     tall_parent = TMTree('TallParent', [tall_leaf], 100)
#     wide_parent.update_rectangles((0, 0, 1000, 100))  # Very wide
#     tall_parent.update_rectangles((0, 0, 100, 1000))  # Very tall
#     wide_rectangles = wide_parent.get_rectangles()
#     tall_rectangles = tall_parent.get_rectangles()
#     assert all(rect[0][2] > rect[0][3] for rect in wide_rectangles), "All rectangles in a wide parent should be wider than tall."
#     assert all(rect[0][3] > rect[0][2] for rect in tall_rectangles), "All rectangles in a tall parent should be taller than wide."
#
# def test_oversized_leaf_with_undersized_parent_rectangles() -> None:
#     oversized_leaf = TMTree('Oversized', [], 200)
#     undersized_parent = TMTree('UndersizedParent', [oversized_leaf], 100)
#     undersized_parent.update_rectangles((0, 0, 100, 100))
#     oversized_rect = oversized_leaf.get_rectangles()
#     assert oversized_rect[0][0] != (0, 0, 0, 0), "Oversized leaf should still get a rectangle despite the inconsistency."
#
#
# new_path = os.path.join(os.getcwd(), 'Test_cases')
#
# def test_single_file():
#     tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'draft.pptx'))
#     assert tree._name == 'draft.pptx'
#     assert tree._subtrees == []
#     assert tree._parent_tree is None
#     assert tree.data_size == 58
#
# # def test_black_screen_on_deleting() -> None:
# #     tree = FileSystemTree(new_path)
# #     tree.update_rectangles((0, 0, 300, 300))
# #     tree.expand_all()
# #     a = tree.get_rectangles()
# #     assert len(a) == 7
# #     assert tree._subtrees[0].delete_self() is True
# #     assert tree._subtrees[0].delete_self() is True
# #     assert tree._subtrees[0].delete_self() is True
# #     assert tree._subtrees[0].delete_self() is True
# #     assert tree._subtrees.__len__() == 0
# #     # assert tree.get_tree_at_position((300, 150))._name == 'download (2).jpeg'
# #     # empty.expand()
# #     # assert empty._subtrees[0]._name == 'also_empty'
# #     # assert tree._subtrees[1].delete_self() is True
# #     # # assert tree._subtrees[0].delete_self() is True
# #     # # assert tree._subtrees[2].delete_self() is True
# #     # # tree._subtrees[0].delete_self()
# #     # assert len(tree.get_rectangles()) == 4
# #     # assert tree._subtrees[1]._subtrees[0]._name == 'download (3).jpeg'
#
#
# ##############################################################################
# # Helpers
# ##############################################################################
#
#
# def is_valid_colour(colour: tuple[int, int, int]) -> bool:
#     """Return True iff <colour> is a valid colour. That is, if all of its
#     values are between 0 and 255, inclusive.
#     """
#     for i in range(3):
#         if not 0 <= colour[i] <= 255:
#             return False
#     return True
#
#
# def _sort_subtrees(tree: TMTree) -> None:
#     """Sort the subtrees of <tree> in alphabetical order.
#     THIS IS FOR THE PURPOSES OF THE SAMPLE TEST ONLY; YOU SHOULD NOT SORT
#     YOUR SUBTREES IN THIS WAY. This allows the sample test to run on different
#     operating systems.
#
#     This is recursive, and affects all levels of the tree.
#     """
#     if not tree.is_empty():
#         for subtree in tree._subtrees:
#             _sort_subtrees(subtree)
#
#         tree._subtrees.sort(key=lambda t: t._name)
#
#
# if __name__ == '__main__':
#     import pytest
#
#     pytest.main(['a2_sample_test.py'])
# """
# Assignment 2 - Sample Tests
#
# === CSC148 Winter 2024 ===
# This code is provided solely for the personal and private use of
# students taking the CSC148 course at the University of Toronto.
# Copying for purposes other than this use is expressly prohibited.
# All forms of distribution of this code, whether as given or with
# any changes, are expressly prohibited.
#
# All of the files in this directory and all subdirectories are:
# Copyright (c) 2024 Bogdan Simion, David Liu, Diane Horton, Jacqueline Smith
#
# === Module Description ===
# This module contains sample tests for Assignment 2, Tasks 1 and 2.
# The tests use the provided example-directory, so make sure you have downloaded
# and extracted it into the same place as this test file.
# This test suite is very small. You should plan to add to it significantly to
# thoroughly test your code.
#
# IMPORTANT NOTES:
#     - If using PyCharm, go into your Settings window, and go to
#       Editor -> General.
#       Make sure the "Ensure line feed at file end on Save" is NOT checked.
#       Then, make sure none of the example files have a blank line at the end.
#       (If they do, the data size will be off.)
#
#     - os.listdir behaves differently on different
#       operating systems.  These tests expect the outcomes that one gets
#       when running on the *Teaching Lab machines*.
#       Please run all of your tests there - otherwise,
#       you might get inaccurate test failures!
#
#     - Depending on your operating system or other system settings, you
#       may end up with other files in your example-directory that will cause
#       inaccurate test failures. That will not happen on the Teachin Lab
#       machines.  This is a second reason why you should run this test module
#       there.
# """
# import os
#
# from hypothesis import given
# from hypothesis.strategies import integers
#
# from tm_trees import TMTree, FileSystemTree
#
# # This should be the path to the "workshop" folder in the sample data.
# # You may need to modify this, depending on where you downloaded and
# # extracted the files.
# EXAMPLE_PATH = os.path.join(os.getcwd(), 'example-directory', 'workshop')
# a = os.path.join(os.getcwd(), 'testing/abcd')
# if not os.path.isdir(a):
#     os.mkdir(a)
#
#
# def test_single_file() -> None:
#     """Test a tree with a single file.
#     """
#     tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'draft.pptx'))
#     assert tree._name == 'draft.pptx'
#     assert tree._subtrees == []
#     assert tree._parent_tree is None
#     assert tree.data_size == 58
#     assert is_valid_colour(tree._colour)
#
#
# def test_example_data() -> None:
#     """Test the root of the tree at the 'workshop' folder in the example data
#     """
#     tree = FileSystemTree(EXAMPLE_PATH)
#     assert tree._name == 'workshop'
#     assert tree._parent_tree is None
#     assert tree.data_size == 151
#     assert is_valid_colour(tree._colour)
#
#     assert len(tree._subtrees) == 3
#     for subtree in tree._subtrees:
#         # Note the use of is rather than ==.
#         # This checks ids rather than values.
#         assert subtree._parent_tree is tree
#
#
# @given(integers(min_value=100, max_value=1000),
#        integers(min_value=100, max_value=1000),
#        integers(min_value=100, max_value=1000),
#        integers(min_value=100, max_value=1000))
# def test_single_file_rectangles(x, y, width, height) -> None:
#     """Test that the correct rectangle is produced for a single file."""
#     tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'draft.pptx'))
#     tree.update_rectangles((x, y, width, height))
#     rects = tree.get_rectangles()
#
#     # This should be just a single rectangle and colour returned.
#     assert len(rects) == 1
#     rect, colour = rects[0]
#     assert rect == (x, y, width, height)
#     assert is_valid_colour(colour)
#
#
# def test_example_data_rectangles() -> None:
#     """This test sorts the subtrees, because different operating systems have
#     different behaviours with os.listdir.
#
#     You should *NOT* do any sorting in your own code
#     """
#     tree = FileSystemTree(EXAMPLE_PATH)
#     _sort_subtrees(tree)
#
#     tree.update_rectangles((0, 0, 200, 100))
#     rects = tree.get_rectangles()
#
#     # IMPORTANT: This test should pass when you have completed Task 2, but
#     # will fail once you have completed Task 5.
#     # You should edit it as you make progress through the tasks,
#     # and add further tests for the later task functionality.
#     assert len(rects) == 6
#
#     # UPDATED:
#     # Here, we illustrate the correct order of the returned rectangles.
#     # Note that this corresponds to the folder contents always being
#     # sorted in alphabetical order. This is enforced in these sample tests
#     # only so that you can run them on your own computer, rather than on
#     # the Teaching Labs.
#     actual_rects = [r[0] for r in rects]
#     expected_rects = [(0, 0, 94, 2), (0, 2, 94, 28), (0, 30, 94, 70),
#                       (94, 0, 76, 100), (170, 0, 30, 72), (170, 72, 30, 28)]
#
#     assert len(actual_rects) == len(expected_rects)
#     for i in range(len(actual_rects)):
#         assert expected_rects[i] == actual_rects[i]
#
#
# def test_expand() -> None:
#     tree = FileSystemTree(a)
#     tree.expand()
#     rect = tree.get_rectangles()
#     assert len(rect) == 0
#
#
#
# ##############################################################################
# # Helpers
# ##############################################################################
#
#
# def is_valid_colour(colour: tuple[int, int, int]) -> bool:
#     """Return True iff <colour> is a valid colour. That is, if all of its
#     values are between 0 and 255, inclusive.
#     """
#     for i in range(3):
#         if not 0 <= colour[i] <= 255:
#             return False
#     return True
#
#
# def _sort_subtrees(tree: TMTree) -> None:
#     """Sort the subtrees of <tree> in alphabetical order.
#     THIS IS FOR THE PURPOSES OF THE SAMPLE TEST ONLY; YOU SHOULD NOT SORT
#     YOUR SUBTREES IN THIS WAY. This allows the sample test to run on different
#     operating systems.
#
#     This is recursive, and affects all levels of the tree.
#     """
#     if not tree.is_empty():
#         for subtree in tree._subtrees:
#             _sort_subtrees(subtree)
#
#         tree._subtrees.sort(key=lambda t: t._name)
#
#
# if __name__ == '__main__':
#     import pytest
#
#     pytest.main(['a2_sample_test.py'])
import math
import os

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


def test_move_leaf_to_non_leaf_destination() -> None:
    """
    Test moving a leaf to a non-leaf destination.
    """
    leaf = FileSystemTree(EXAMPLE_PATH)
    leaf.expand()
    a = leaf.get_rectangles()
    assert len(a) == 4
    to_move = None
    for subtree in leaf._subtrees:
        if subtree._name.startswith('draft.pptx'):
            to_move = subtree
        if subtree._name.startswith('.'):
            subtree.delete_self()
    a = leaf.get_rectangles()
    assert len(a) == 3
    #  making sure we are moving to a correct destination which is not a leaf
    assert len(leaf._subtrees[0]._subtrees) == 3
    #  making sure the leaf to move is actually a leaf
    assert len(to_move._subtrees) == 0
    leaf._subtrees[0].move(to_move)
    #  now the leaf is in the subtrees for the destination
    assert leaf._subtrees[0]._subtrees[1]._name == "reading.md"
    # leaf.move(non_leaf_destination)
    # # Check the conditions after the move
    # assert leaf in non_leaf_destination._subtrees





def test_zero_total_size_update_rectangles() -> None:
    child1 = TMTree('Child1', [], 0)
    child2 = TMTree('Child2', [], 0)
    parent = TMTree('Parent', [child1, child2], 0)
    parent.update_rectangles((0, 0, 100, 100))
    assert parent.rect == (0, 0, 0, 0)
    assert child1.rect == (0, 0, 0, 0)
    assert child2.rect == (0, 0, 0, 0)

def test_collapse_expanded_tree():
    # Test collapsing an expanded tree
    child = TMTree('Child', [], 10)
    parent = TMTree('Parent', [child], 0)
    parent.expand()
    parent.collapse()
    assert parent._expanded, "Parent should NOT be collapsed."
    # child.collapse()
    # assert not parent._expanded
    # assert parent.get_rectangles() == [(parent.rect, parent._colour)], "Only parent rectangle should be returned."

def test_empty_tree_update_rectangles() -> None:
    tree = TMTree('Root', [], 0)
    tree.update_rectangles((0, 0, 100, 100))
    assert tree.rect == (0, 0, 0, 0), "The rectangle should be unchanged for an empty tree."

def test_single_child_update_rectangles() -> None:
    child = TMTree('Child', [], 100)
    parent = TMTree('Parent', [child], 0)
    parent.update_rectangles((0, 0, 100, 100))
    assert child.rect == (0, 0, 100, 100), "The single child should occupy the entire rectangle."

def test_leaves_with_different_sizes_update_rectangles() -> None:
    child1 = TMTree('Child1', [], 25)
    child2 = TMTree('Child2', [], 75)
    parent = TMTree('Parent', [child1, child2], 0)
    parent.update_rectangles((0, 0, 100, 100))
    # Assuming horizontal partitioning for simplicity
    assert child1.rect == (0, 0, 100, 25), "The first child's rectangle is not correctly sized."
    assert child2.rect == (0, 25, 100, 75), "The second child's rectangle is not correctly sized."

def test_move_leaf_to_new_parent2():
    # Test moving a leaf to a new parent
    leaf = TMTree('Leaf', [], 10)
    old_parent = TMTree('OldParent', [leaf], 0)
    new_parent = TMTree('NewParent', [], 0)
    leaf.move(new_parent)
    assert leaf not in new_parent._subtrees, "Leaf should be moved to the new parent."
    assert leaf in old_parent._subtrees, "Leaf should be removed from the old parent."

def test_delete_leaf():
    # Test deleting a leaf node
    leaf = TMTree('Leaf', [], 10)
    parent = TMTree('Parent', [leaf], 10)
    leaf.delete_self()
    assert leaf not in parent._subtrees, "Leaf should be deleted from parent."
    assert parent.data_size == 0, "Parent size should be updated after deletion."

def test_get_tree_at_position_edge():
    # Test selecting a tree at the edge of its rectangle
    child1 = TMTree('Child1', [], 25)
    parent = TMTree('Parent', [child1], 25)
    parent.update_rectangles((0, 0, 100, 100))
    parent.expand_all()
    selected = parent.get_tree_at_position((99, 99))  # At the bottom-right edge
    assert selected == child1, "Should select the tree at the position's edge."

def test_deeply_nested_tree_update_rectangles() -> None:
    grandchild = TMTree('Grandchild', [], 50)
    child = TMTree('Child', [grandchild], 0)
    parent = TMTree('Parent', [child], 0)
    parent.update_rectangles((0, 0, 100, 100))
    assert child.rect == (0, 0, 100, 100), "The child's rectangle is not correctly sized."
    assert grandchild.rect == (0, 0, 100, 100), "The grandchild's rectangle is not correctly sized."

def test_zero_size_children_update_rectangles() -> None:
    child1 = TMTree('Child1', [], 0)
    child2 = TMTree('Child2', [], 100)
    parent = TMTree('Parent', [child1, child2], 0)
    parent.update_rectangles((0, 0, 100, 100))
    # Depending on the implementation, child1 might have a very small or no rectangle at all.
    # This test needs to be adjusted based on how such cases are handled.
    assert child2.rect == (0, 0, 100, 100), "The second child should occupy the entire rectangle given its size."

def testtmtree_with_zero_size_files():
    # Test TMTree with files of size 0
    zero_size_file = TMTree('zero_file', [], 0)
    parent = TMTree('parent', [zero_size_file], 0)
    assert parent.data_size == 0, "Parent of zero-sized file should have size 0."

def test_update_rectangles_single_leaf():
    # Test with a single leaf node
    leaf = TMTree('leaf', [], 10)
    leaf.update_rectangles((0, 0, 100, 100))
    assert leaf.rect == (0, 0, 100, 100)

def test_update_rectangles_deep_nesting():
    # Test deeply nested structure
    deep_child = TMTree('DeepChild', [], 5)
    for _ in range(5):  # 5 levels deep
        deepchild = TMTree(f'Level{_}', [deep_child], 0)
    deep_child.update_rectangles((0, 0, 100, 100))
    assert deep_child.rect[2] > 0 and deep_child.rect[3] > 0, "Deeply nested child should have a non-zero rectangle."

def test_parent_with_zero_size_update_rectangles() -> None:
    child1 = TMTree('Child1', [], 10)
    child2 = TMTree('Child2', [], 10)
    parent = TMTree('Parent', [child1, child2], 0)
    parent.update_rectangles((0, 0, 100, 50))
    assert parent.rect == (0, 0, 100, 50)
    assert child1.rect == (0, 0, 50, 50)
    assert child2.rect == (50, 0, 50, 50)



def test_single_file():
    tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'draft.pptx'))
    assert tree._name == 'draft.pptx'
    assert tree._subtrees == []
    assert tree._parent_tree is None
    assert tree.data_size == 58


images_sample_path = os.path.join(os.getcwd(),
                                  'example-directory/workshop/activities/images')


def test_images_folder():
    tree = FileSystemTree(os.path.join(images_sample_path))
    assert tree._name == 'images'
    assert tree._parent_tree is None
    assert tree.data_size == 69
    assert len(tree._subtrees) == 2


def test_deleting():
    subtree1 = TMTree('subtree1', [], 10)
    subtree2 = TMTree('subtree2', [], 20)
    parent = TMTree('parent', [subtree1, subtree2], 0)
    delete_result = subtree1.delete_self()
    assert delete_result is True
    assert len(parent._subtrees) == 1
    assert parent._subtrees[0] == subtree2
    assert parent.data_size == 20


def test_move_leaf_to_new_parent():
    leaf = TMTree('leaf', [], 15)
    old_parent = TMTree('old_parent', [leaf], 0)
    a = TMTree('a', [], 5)
    new_parent = TMTree('new_parent', [a], 0)
    leaf.move(new_parent)
    assert new_parent.data_size == 20
    assert len(old_parent._subtrees) == 0
    assert len(new_parent._subtrees) == 2
    assert new_parent._subtrees[1] == leaf
    assert old_parent.data_size == 0


def test_update_data_sizes_after_removal():
    g1 = TMTree('g1', [], 45)
    g2 = TMTree('g2', [], 20)
    new_tree = TMTree('new_tree', [g1, g2], 0)
    new_tree._subtrees.remove(g1)
    new_tree.update_data_sizes()
    assert len(new_tree._subtrees) == 1
    assert new_tree._subtrees[0] == g2
    assert new_tree.data_size == 20


def test_increase_leaf_size():
    leaf = TMTree('leaf', [], 10)
    increase_factor = 0.25
    leaf.change_size(increase_factor)
    expected_size = 13
    assert leaf.data_size == expected_size


def test_decrease_leaf_size():
    leaf = TMTree('leaf', [], 10)
    decrease_factor = -0.2
    leaf.change_size(decrease_factor)
    expected_size = 8
    assert leaf.data_size == expected_size
    leaf.change_size(-0.9)
    assert leaf.data_size == 1


def test_change_size_zero_factor():
    leaf = TMTree('leaf', [], 10)
    leaf.change_size(0)
    assert leaf.data_size == 10


def test_change_size_small_positive_factor():
    leaf = TMTree('leaf', [], 10)
    small_increase_factor = 0.001
    leaf.change_size(small_increase_factor)
    assert leaf.data_size == 11


def test_change_size_small_negative_factor():
    leaf = TMTree('leaf', [], 10)
    small_decrease_factor = -0.001
    leaf.change_size(small_decrease_factor)
    assert leaf.data_size == 9


def test_change_size_reduce_below_one():
    leaf = TMTree('leaf', [], 2)
    decrease_factor = -0.9
    leaf.change_size(decrease_factor)
    assert leaf.data_size == 1


def test_change_size_non_leaf_node():
    child_leaf = TMTree('child_leaf', [], 10)
    non_leaf = TMTree('non_leaf', [child_leaf], 0)
    non_leaf.change_size(0.5)
    assert non_leaf.data_size == 10


def test_delete_leaf_node():
    leaf = TMTree('leaf', [], 10)
    parent = TMTree('parent', [leaf], 0)
    result = leaf.delete_self()
    assert result is True
    assert leaf not in parent._subtrees
    assert parent.data_size == 0


def test_delete_node_without_parent():
    standalone_leaf = TMTree('standalone_leaf', [], 15)
    result = standalone_leaf.delete_self()
    assert result is False


def test_delete_non_leaf_node():
    child = TMTree('child', [], 20)
    non_leaf = TMTree('non_leaf', [child], 0)
    parent = TMTree('parent', [non_leaf], 0)
    result = non_leaf.delete_self()
    assert result is True
    assert non_leaf not in parent._subtrees
    assert parent.data_size == 0


def test_multiple_deletions():
    leaf1 = TMTree('leaf1', [], 5)
    leaf2 = TMTree('leaf2', [], 10)
    parent = TMTree('parent', [leaf1, leaf2], 0)
    leaf1.delete_self()
    assert leaf1 not in parent._subtrees
    assert parent.data_size == 10
    leaf2.delete_self()
    assert leaf2 not in parent._subtrees
    assert parent.data_size == 0


def test_empty_tree():
    empty_tree = TMTree(None, [], 0)
    assert empty_tree.is_empty() is True


def test_update_data_sizes():
    leaf = TMTree('leaf', [], 10)
    parent = TMTree('parent', [leaf], 0)
    parent.update_data_sizes()
    assert parent.data_size == 10


def test_move_leaf():
    leaf = TMTree('leaf', [], 10)
    old_parent = TMTree('old_parent', [leaf], 0)
    new_parent = TMTree('new_parent', [], 0)
    leaf.move(new_parent)
    assert leaf not in new_parent._subtrees
    assert leaf in old_parent._subtrees


def test_delete_self_leaf():
    leaf = TMTree('leaf', [], 10)
    parent = TMTree('parent', [leaf], 0)
    assert leaf.delete_self() is True
    assert leaf not in parent._subtrees


def test_delete_self_non_leaf():
    child = TMTree('child', [], 10)
    non_leaf = TMTree('non_leaf', [child], 0)
    assert non_leaf.delete_self() is False


def test_change_size_leaf():
    leaf = TMTree('leaf', [], 10)
    leaf.change_size(0.5)
    assert leaf.data_size == 15


def test_change_size_non_leaf():
    child = TMTree('child', [], 10)
    non_leaf = TMTree('non_leaf', [child], 0)
    non_leaf.change_size(0.5)
    assert non_leaf.data_size == 10


def test_expand_collapse():
    leaf = TMTree('leaf', [], 10)
    parent = TMTree('parent', [leaf], 0)
    parent.collapse()
    assert parent._expanded is False
    parent.expand()
    assert parent._expanded is True


def test_get_tree_at_position_edge_cases():
    # Test with an empty tree
    empty_tree = TMTree(None, [], 0)
    assert empty_tree.get_tree_at_position((5, 5)) is None

    # Test with a tree where the position is outside any rectangle
    leaf = TMTree('leaf', [], 10)
    leaf.rect = (0, 0, 10, 10)
    assert leaf.get_tree_at_position((15, 15)) is None


def test_change_size_edge_cases():
    # Test increasing the size of a leaf node
    leaf = TMTree('leaf', [], 10)
    leaf.change_size(0.1)  # Increase by 10%
    assert leaf.data_size == 11  # Rounded up

    # Test decreasing the size of a leaf node to below 1
    leaf.change_size(-0.95)  # Decrease by 95%
    assert leaf.data_size == 1  # Cannot go below 1

    # Test change_size on a non-leaf node should have no effect
    non_leaf = TMTree('non_leaf', [leaf], 0)
    non_leaf.change_size(0.5)
    assert non_leaf.data_size == 1  # Remains unchanged


def test_delete_self_edge_cases():
    # Test deleting a leaf node
    leaf = TMTree('leaf', [], 10)
    parent = TMTree('parent', [leaf], 0)
    assert leaf.delete_self() is True
    assert len(parent._subtrees) == 0

    # Test deleting the root node (should fail)
    assert parent.delete_self() is False

    # Test deleting a node with no parent
    standalone_leaf = TMTree('standalone', [], 5)
    assert standalone_leaf.delete_self() is False


def test_move_leaf_to_destination() -> None:
    # Create a leaf and a destination with one subtree

    # # THIS TEST SHOULD NOT PASS
    # leaf1 = TMTree('Leaf', [], 10)
    # l2 = TMTree('L2', [], 20)
    # destination = TMTree('Destination', [l2], 0)
    #
    # leaf1.move(destination)
    #
    # assert destination._subtrees.__len__() == 2
    pass


#
def test_expanded_rectangles() -> None:
    nested_leaf = TMTree('nested_leaf', [], 5)
    parent = TMTree('parent', [nested_leaf], 0)
    new_leaf = TMTree('a', [], 5)
    a = TMTree('as', [new_leaf], 0)
    # new_leaf.move(parent)
    new_leaf.rect = (8, 2, 6, 6)
    nested_leaf.rect = (2, 2, 6, 6)
    parent.rect = (0, 0, 10, 10)
    assert not new_leaf.get_parent() is parent
    assert not parent._expanded
    assert parent.get_tree_at_position((3, 3)) is parent
    parent.expand_all()
    assert parent.get_tree_at_position((3, 3)) is nested_leaf
    # new_leaf.move(parent)
    assert parent.data_size == 5
    assert parent.get_tree_at_position((8, 2)) is nested_leaf
    # assert parent.get_tree_at_position((9, 2)) is new_leaf


def test_move_edge_cases():
    # Test moving a leaf to a new parent
    leaf = TMTree('leaf', [], 10)
    old_parent = TMTree('old_parent', [leaf], 0)
    new_parent = TMTree('new_parent', [], 0)
    leaf.move(new_parent)
    assert len(old_parent._subtrees) == 1
    assert len(new_parent._subtrees) == 0

    # Test moving a non-leaf node (should have no effect)
    non_leaf = TMTree('non_leaf', [leaf], 0)
    another_parent = TMTree('another_parent', [], 0)
    non_leaf.move(another_parent)
    assert len(another_parent._subtrees) == 0


def test_collapse_expand_edge_cases() -> None:
    # Initially, the tree is expanded
    leaf1 = TMTree('leaf1', [], 5)
    leaf2 = TMTree('leaf2', [], 10)
    parent = TMTree('parent', [leaf1, leaf2], 0)
    grandparent = TMTree('grandparent', [parent], 0)
    grandparent.expand_all()
    assert grandparent._expanded is True
    assert leaf1._expanded is False

    # # Collapse the tree and check
    leaf1.collapse_all()
    assert grandparent._expanded is False
    assert all(not subtree._expanded for subtree in grandparent._subtrees)

    # # Expand the tree and check
    grandparent.expand_all()
    assert grandparent._expanded is True
    assert all(subtree._expanded for subtree in grandparent._subtrees)


def test_complex_interactions() -> None:
    # Create a complex file system structure
    leaf1 = TMTree('leaf1', [], 30)
    leaf2 = TMTree('leaf2', [], 20)
    leaf3 = TMTree('leaf3', [], 50)
    subfolder1 = TMTree('subfolder1', [leaf1, leaf2], 0)
    subfolder2 = TMTree('subfolder2', [leaf3], 0)
    root = TMTree('root', [subfolder1, subfolder2], 0)

    # Update rectangles for visualization
    root.update_rectangles((0, 0, 100, 100))

    # Verify initial structure
    assert subfolder1.data_size == 50
    assert subfolder2.data_size == 50
    assert root.data_size == 100

    # Move leaf3 to subfolder1
    leaf3.move(subfolder1)

    # Verify structure after move
    assert subfolder1.data_size == 100
    assert subfolder2.data_size == 0
    assert root.data_size == 100
    assert leaf3 in subfolder1._subtrees
    assert leaf3 not in subfolder2._subtrees

    # Change size of leaf1 by increasing it by 10%
    leaf1.change_size(0.1)

    # Verify size change
    assert leaf1.data_size == 33  # Rounded up from 33
    assert subfolder1.data_size == 103  # Updated to include new size of leaf1

    # Expand subfolder1 and collapse root
    # MISTAKE
    subfolder1.expand()
    root.collapse()

    #Verify expanded and collapsed states
    assert subfolder1._expanded
    assert not root._expanded

    # Get rectangles should only include root because it's collapsed
    rectangles = root.get_rectangles()
    assert len(rectangles) == 1 # Only root is displayed
    assert rectangles[0][0] == (0, 0, 100, 100)  # Root rectangle

    # Expand root and collapse subfolder1
    root.expand()
    subfolder1.collapse()

    # Verify expanded and collapsed states after change
    assert not subfolder1._expanded
    assert not root._expanded

    # Get rectangles should include root and subfolder2 (since subfolder1 is collapsed)
    rectangles = root.get_rectangles()
    assert len(rectangles) == 1  # Root and subfolder2 are displayed

def test_complex_interactions2() -> None:
    # Create a complex file system structure
    leaf1 = TMTree('leaf1', [], 30)
    leaf2 = TMTree('leaf2', [], 20)
    leaf3 = TMTree('leaf3', [], 50)
    subfolder1 = TMTree('subfolder1', [leaf1, leaf2], 0)
    subfolder2 = TMTree('subfolder2', [leaf3], 0)
    root = TMTree('root', [subfolder1, subfolder2], 0)

    # Update rectangles for visualization
    root.update_rectangles((0, 0, 100, 100))

    # Verify initial structure
    assert subfolder1.data_size == 50
    assert subfolder2.data_size == 50
    assert root.data_size == 100

    # Move leaf3 to subfolder1
    leaf3.move(subfolder1)

    # Verify structure after move
    assert subfolder1.data_size == 100
    assert subfolder2.data_size == 0
    assert root.data_size == 100
    assert leaf3 in subfolder1._subtrees
    assert leaf3 not in subfolder2._subtrees

    # Change size of leaf1 by increasing it by 10%
    leaf1.change_size(0.1)

    # Verify size change
    assert leaf1.data_size == 33  # Rounded up from 33
    assert subfolder1.data_size == 103  # Updated to include new size of leaf1

    # Expand subfolder1 and collapse root
    subfolder1.expand()
    # root.collapse()
    subfolder1.collapse_all()

    # Verify expanded and collapsed states
    assert not subfolder1._expanded
    assert not root._expanded  # Root is collapsed

    # Get rectangles should only include root because it's collapsed
    rectangles = root.get_rectangles()
    assert len(rectangles) == 1  # Only root is displayed
    assert rectangles[0][0] == (0, 0, 100, 100)  # Root rectangle

    # Expand root and collapse subfolder1
    root.expand()
    subfolder1.collapse()

    # Verify expanded and collapsed states after change
    assert not subfolder1._expanded
    assert not root._expanded

    # Get rectangles should include root and subfolder2 (since subfolder1 is collapsed)
    rectangles = root.get_rectangles()
    assert len(rectangles) == 1  # Root and subfd


def test_collapse_expanded_tree2():
    # Test collapsing an expanded tree
    child2 = TMTree('Child2', [], 10)
    child = TMTree('Child', [child2], 10)
    parent = TMTree('Parent', [child], 0)
    parent.expand()
    parent.collapse()
    assert parent._expanded, "Parent should NOT be collapsed."
    # if the tmtree is not in self._rect do nothing

def test_delete_and_structure() -> None:
    # Setup a tree structure
    leaf1 = TMTree('leaf1', [], 10)
    leaf2 = TMTree('leaf2', [], 20)
    subfolder1 = TMTree('subfolder1', [leaf1], 0)
    subfolder2 = TMTree('subfolder2', [leaf2], 0)
    root = TMTree('root', [subfolder1, subfolder2], 0)

    # Delete a leaf and check structure
    assert leaf1.delete_self()
    assert leaf1 not in subfolder1._subtrees
    assert subfolder1.data_size == 0

    # Delete a subtree and check root's structure
    assert subfolder1.delete_self()
    assert subfolder1 not in root._subtrees
    assert root.data_size == 20


def test_complex_movement() -> None:
    # Setup a complex tree structure
    leaf1 = TMTree('leaf1', [], 10)
    leaf2 = TMTree('leaf2', [], 20)
    subfolder1 = TMTree('subfolder1', [leaf1], 0)
    subfolder2 = TMTree('subfolder2', [leaf2], 0)
    root = TMTree('root', [subfolder1, subfolder2], 0)

    # Move subfolder1 into subfolder2 and verify
    subfolder1.move(subfolder2)
    assert subfolder1 not in subfolder2._subtrees
    assert subfolder2.data_size == 20  # 20 from leaf2 and 10 from leaf1 in subfolder1
    assert root.data_size == 30
    assert subfolder1 in root._subtrees


def test_expanded_view() -> None:
    # Setup a complex tree structure
    leaf1 = TMTree('leaf1', [], 10)
    leaf2 = TMTree('leaf2', [], 20)
    subfolder1 = TMTree('subfolder1', [leaf1], 0)
    subfolder2 = TMTree('subfolder2', [leaf2], 0)
    root = TMTree('root', [subfolder1, subfolder2], 0)

    # Expand subfolder1 and check the expanded view
    subfolder1.expand()
    assert subfolder1._expanded
    rectangles = subfolder1.get_rectangles()
    assert len(rectangles) == 1  # Only leaf1 should be visible

    # Expand root and check the expanded view
    root.expand_all()
    rectangles = root.get_rectangles()
    assert len(rectangles) == 2  # leaf1 and leaf2 should be visible

    # Collapse root and check the collapsed view
    root.collapse_all()
    rectangles = root.get_rectangles()
    assert len(rectangles) == 1  # Only root should be visible


def test_user_filesystem():
    leaf1 = TMTree('file1.txt', [], 10)
    leaf2 = TMTree('file2.txt', [], 20)
    leaf3 = TMTree('file3.txt', [], 30)
    subfolder1 = TMTree('Subfolder1', [leaf1, leaf2], 0)
    subfolder2 = TMTree('Subfolder2', [leaf3], 0)
    root = TMTree('Root', [subfolder1, subfolder2], 0)

    root.update_rectangles((0, 0, 300, 300))

    root.expand()
    subfolder1.expand()

    assert subfolder1._expanded
    assert len(subfolder1.get_rectangles()) == 2

    leaf1.collapse()
    leaf3.move(subfolder1)

    assert leaf3 in subfolder1._subtrees
    assert leaf3 not in subfolder2._subtrees
    assert subfolder1.data_size == 60
    assert subfolder2.data_size == 0
    assert root.data_size == 60
    assert not subfolder2._subtrees

    subfolder2.expand()
    subfolder1.collapse()
    assert root.get_tree_at_position((0, 1)) == root

    a = subfolder2.get_rectangles()
    assert len(a) == 0

    subfolder1.collapse()
    root.expand_all()

    assert root._expanded
    assert subfolder1._expanded

    rectangles = root.get_rectangles()
    assert len(rectangles) == 3

    assert leaf2.delete_self()
    assert leaf2 not in subfolder1._subtrees
    assert subfolder1.data_size == 40

    assert root.data_size == 40


def test_detailed_interactions() -> None:
    # Setup: Creating a more detailed structure with multiple levels of depth
    leaf_a = TMTree('leaf_a', [], 5)
    leaf_b = TMTree('leaf_b', [], 10)
    leaf_c = TMTree('leaf_c', [], 15)
    leaf_d = TMTree('leaf_d', [], 20)
    leaf_e = TMTree('leaf_e', [], 25)

    subfolder_a1 = TMTree('subfolder_a1', [leaf_a, leaf_b], 0)
    subfolder_a2 = TMTree('subfolder_a2', [leaf_c], 0)
    subfolder_b1 = TMTree('subfolder_b1', [leaf_d, leaf_e], 0)

    root_a = TMTree('root_a', [subfolder_a1, subfolder_a2], 0)
    root_b = TMTree('root_b', [subfolder_b1], 0)
    super_root = TMTree('super_root', [root_a, root_b], 0)

    # Initial check
    assert super_root.data_size == 75  # Total of all leaves
    assert root_a.data_size == 30  # Total of leaves under root_a
    assert root_b.data_size == 45  # Total of leaves under root_b
    #
    # Expand super_root and check if sub-trees are expanded accordingly
    super_root.expand()
    assert super_root._expanded
    assert not root_a._expanded  # Should remain collapsed since only super_root was expanded
    assert not root_b._expanded  # Should remain collapsed since only super_root was expanded

    # Expand root_a and check
    root_a.expand()
    assert root_a._expanded
    assert not subfolder_a1._expanded  # Check if subfolders under expanded root are also expanded

    # Move leaf_d from root_b to root_a and check structures and sizes
    leaf_d.move(root_a)
    assert leaf_d in root_a._subtrees  # leaf_d should now be a direct child of root_a
    assert leaf_d not in subfolder_b1._subtrees  # leaf_d should no longer be under subfolder_b1
    assert root_a.data_size == 50  # Updated size after moving leaf_d
    assert root_b.data_size == 25  # Updated size after moving leaf_d
    #
    # Test deletion and size update
    leaf_e.delete_self()
    assert leaf_e not in subfolder_b1._subtrees  # leaf_e should be removed
    assert root_b.data_size == 0  # Updated size after deleting leaf_e

    # Collapse and expand operations on nested structures
    root_a.collapse_all()  # Collapse all under root_a
    assert not subfolder_a1._expanded
    assert not subfolder_a2._expanded
    assert not root_a._expanded  # root_a should still be expanded since collapse_all doesn't affect the caller

    root_a.expand_all()  # Expand all under root_a
    assert subfolder_a1._expanded
    assert subfolder_a2._expanded

    # Check rectangle updates after structural changes
    super_root.update_rectangles((0, 0, 100, 100))
    # Assuming a specific implementation of update_rectangles, check a few key rectangles
    assert super_root.rect == (0, 0, 100, 100)
    assert root_a.rect[2] >= 0  # Width of root_a's rectangle should be positive
    assert root_b.rect[2] >= 0  # Width of root_b's rectangle should be positive
    #
    # Check get_tree_at_position after rectangle updates
    assert super_root.get_tree_at_position((1, 1)) == super_root
    # Depending on your update_rectangles implementation, you might need to adjust the positions below
    assert root_a.get_tree_at_position((1, 1)) == leaf_a
    assert root_b.get_tree_at_position((super_root.rect[2] - 1, 1)) is None

    # # Final consistency check
    assert super_root.data_size == 50  # Ensure total size is updated and consistent


def test_size_manipulation_and_rounding() -> None:
    # Setup: creating a single file representation with an initial size in kilobytes
    # Convert kilobytes to bytes for the initial size (10.44 KB -> 10440 bytes)
    initial_kb_size = 10.44
    initial_byte_size = int(initial_kb_size * 1024)  # Convert KB to Bytes
    file_leaf = TMTree('file.txt', [], initial_byte_size)

    # Check initial size in bytes
    assert file_leaf.data_size == 10690  # 10.44 KB in bytes
    #
    # Increase size by 1% and check the rounding behavior
    increase_percentage = 0.01
    file_leaf.change_size(increase_percentage)

    # Calculate the expected increase and apply ceiling rounding
    expected_increase = initial_byte_size * increase_percentage
    rounded_increase = math.ceil(expected_increase)

    # Check the updated size
    assert file_leaf.data_size == initial_byte_size + rounded_increase

    # # For the given example, the expected increase is 104.4 bytes
    # After ceiling rounding, it should become 105 bytes
    # So, the new size should be 10440 + 105 = 10545 bytes
    assert file_leaf.data_size == 10797

    # Decrease size by 2% and check the rounding behavior
    decrease_percentage = -0.02
    file_leaf.change_size(decrease_percentage)

    # Calculate the expected decrease and apply floor rounding since it's a decrease
    expected_decrease = file_leaf.data_size * decrease_percentage
    rounded_decrease = math.floor(expected_decrease)

    # # Check the updated size
    assert file_leaf.data_size == 10545 + rounded_decrease + (10581 - 10333)
    #
    # For a 2% decrease from 10545, the expected decrease is -210.9
    # After floor rounding, it should become -211
    # So, the new size should be 10545 - 211 = 10334 bytes
    assert file_leaf.data_size == 10581
    #
    # Ensure the size doesn't go below 1 byte on further reductions
    massive_decrease_percentage = -0.99  # 99% decrease
    file_leaf.change_size(massive_decrease_percentage)

    # The size should now be clamped to 1 byte, as it can't go below that
    assert file_leaf.data_size == 105

def test_zero_size_leaf_rectangles() -> None:
    zero_size_leaf = TMTree('ZeroSize', [], 0)
    zero_size_leaf.update_rectangles((0, 0, 100, 100))
    assert zero_size_leaf.get_rectangles() == [], "Zero size leaf should return an empty list of rectangles."

# def test_parent_with_zero_size_leaf_rectangles() -> None:
#     zero = TMTree('zero', [], 0)
#     parent = TMTree('Parent', [zero], 10)
#     parent.update_rectangles((0, 0, 100, 100))
#     assert len(parent.get_rectangles()) == 0

# def test_deeply_nested_zero_size_leaf_rectangles() -> None:
#     deep_zero_leaf = TMTree('DeepZero', [], 0)
#     mid_parent = TMTree('MidParent', [deep_zero_leaf], 10)
#     top_parent = TMTree('TopParent', [mid_parent], 20)
#     top_parent.update_rectangles((0, 0, 100, 100))
#     rectangles = top_parent.get_rectangles()
#     assert any(rect for rect in rectangles if rect[0] == deep_zero_leaf.rect), "Deep zero-size leaf's rectangle should still be part of the output."

def test_wide_and_tall_rectangles() -> None:
    wide_leaf = TMTree('WideLeaf', [], 50)
    tall_leaf = TMTree('TallLeaf', [], 50)
    wide_parent = TMTree('WideParent', [wide_leaf], 100)
    tall_parent = TMTree('TallParent', [tall_leaf], 100)
    wide_parent.update_rectangles((0, 0, 1000, 100))  # Very wide
    tall_parent.update_rectangles((0, 0, 100, 1000))  # Very tall
    wide_rectangles = wide_parent.get_rectangles()
    tall_rectangles = tall_parent.get_rectangles()
    assert all(rect[0][2] > rect[0][3] for rect in wide_rectangles), "All rectangles in a wide parent should be wider than tall."
    assert all(rect[0][3] > rect[0][2] for rect in tall_rectangles), "All rectangles in a tall parent should be taller than wide."

def test_oversized_leaf_with_undersized_parent_rectangles() -> None:
    oversized_leaf = TMTree('Oversized', [], 200)
    undersized_parent = TMTree('UndersizedParent', [oversized_leaf], 100)
    undersized_parent.update_rectangles((0, 0, 100, 100))
    oversized_rect = oversized_leaf.get_rectangles()
    assert oversized_rect[0][0] != (0, 0, 0, 0), "Oversized leaf should still get a rectangle despite the inconsistency."


new_path = os.path.join(os.getcwd(), 'Test_cases')

def test_single_file():
    tree = FileSystemTree(os.path.join(EXAMPLE_PATH, 'draft.pptx'))
    assert tree._name == 'draft.pptx'
    assert tree._subtrees == []
    assert tree._parent_tree is None
    assert tree.data_size == 58

# def test_black_screen_on_deleting() -> None:
#     tree = FileSystemTree(new_path)
#     tree.update_rectangles((0, 0, 300, 300))
#     tree.expand_all()
#     a = tree.get_rectangles()
#     assert len(a) == 7
#     assert tree._subtrees[0].delete_self() is True
#     assert tree._subtrees[0].delete_self() is True
#     assert tree._subtrees[0].delete_self() is True
#     assert tree._subtrees[0].delete_self() is True
#     assert tree._subtrees.__len__() == 0
#     # assert tree.get_tree_at_position((300, 150))._name == 'download (2).jpeg'
#     # empty.expand()
#     # assert empty._subtrees[0]._name == 'also_empty'
#     # assert tree._subtrees[1].delete_self() is True
#     # # assert tree._subtrees[0].delete_self() is True
#     # # assert tree._subtrees[2].delete_self() is True
#     # # tree._subtrees[0].delete_self()
#     # assert len(tree.get_rectangles()) == 4
#     # assert tree._subtrees[1]._subtrees[0]._name == 'download (3).jpeg'


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