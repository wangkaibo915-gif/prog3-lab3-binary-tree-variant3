"""Лабораторная работа 3: построение бинарного дерева, вариант 3."""

from collections import namedtuple
from typing import Callable


Node = namedtuple("Node", ["value", "left", "right"])


def gen_bin_tree(
    height: int = 4,
    root: int = 3,
    left_leaf: Callable[[int], int] = lambda value: value + 2,
    right_leaf: Callable[[int], int] = lambda value: value * 3,
) -> dict:
    """Построить бинарное дерево высоты height в виде вложенных словарей.

    Корень находится на первом уровне. На последнем уровне у каждого узла
    поля left и right равны None. Переданные аргументы заменяют значения
    варианта 3 по умолчанию.

    Args:
        height: Число уровней дерева, не меньше одного.
        root: Значение корневого узла.
        left_leaf: Правило вычисления левого потомка.
        right_leaf: Правило вычисления правого потомка.

    Returns:
        Словарь с ключами value, left и right.

    Raises:
        ValueError: Если height меньше одного.
    """
    if height < 1:
        raise ValueError("height должен быть не меньше 1")

    tree = {"value": root, "left": None, "right": None}
    if height > 1:
        tree["left"] = gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf)
        tree["right"] = gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf)
    return tree


def as_namedtuple(tree: dict) -> Node:
    """Представить то же дерево с помощью контейнера namedtuple."""
    left = as_namedtuple(tree["left"]) if tree["left"] is not None else None
    right = as_namedtuple(tree["right"]) if tree["right"] is not None else None
    return Node(tree["value"], left, right)


if __name__ == "__main__":
    print(gen_bin_tree())
