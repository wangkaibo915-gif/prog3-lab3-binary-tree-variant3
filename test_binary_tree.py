"""Tests for laboratory work 3, variant 3."""

import unittest

from binary_tree import as_namedtuple, gen_bin_tree


class TestBinaryTree(unittest.TestCase):
    def test_default_variant_three(self):
        tree = gen_bin_tree()
        self.assertEqual(tree["value"], 3)
        self.assertEqual(tree["left"]["value"], 5)
        self.assertEqual(tree["right"]["value"], 9)
        self.assertEqual(tree["left"]["left"]["value"], 7)
        self.assertEqual(tree["left"]["right"]["value"], 15)

    def test_height_is_four_levels(self):
        def count_nodes(node):
            if node is None:
                return 0
            return 1 + count_nodes(node["left"]) + count_nodes(node["right"])

        tree = gen_bin_tree()
        self.assertEqual(count_nodes(tree), 15)
        self.assertIsNone(tree["left"]["left"]["left"]["left"])

    def test_custom_parameters_override_defaults(self):
        tree = gen_bin_tree(
            height=2,
            root=10,
            left_leaf=lambda value: value - 1,
            right_leaf=lambda value: value + 1,
        )
        self.assertEqual(
            tree,
            {
                "value": 10,
                "left": {"value": 9, "left": None, "right": None},
                "right": {"value": 11, "left": None, "right": None},
            },
        )

    def test_height_one_is_a_leaf(self):
        self.assertEqual(
            gen_bin_tree(height=1),
            {"value": 3, "left": None, "right": None},
        )

    def test_height_must_be_positive(self):
        with self.assertRaises(ValueError):
            gen_bin_tree(height=0)

    def test_collections_representation(self):
        node = as_namedtuple(gen_bin_tree(height=2))
        self.assertEqual(node.value, 3)
        self.assertEqual(node.left.value, 5)
        self.assertEqual(node.right.value, 9)
        self.assertIsNone(node.left.left)


if __name__ == "__main__":
    unittest.main(argv=[""], verbosity=2, exit=False)
