
from binarytree import Node, get_parent

PARENT_VALUE = -1


def max_two_sum_magnitude(elems: list[Node]):
    mags = []
    for a in elems:
        for b in elems:
            if a != b:
                num = Node(PARENT_VALUE, a.clone(), b.clone())
                while not is_reduced(num):
                    if not depth_is_ok(num):
                        explode(num)
                    else:
                        split(num)
                mags.append(get_magnitude(num))
    max_sum = max(mags)
    print(f'largest sum of two different numbers: {max_sum}')


def is_leaf(elem: Node) -> bool:
    return elem.value != PARENT_VALUE


def find_next_value(number: Node, elem: Node, direc: int) -> Node:
    res = None
    parent = get_parent(number, elem)
    op_direc = 1 + direc % 2
    if parent:
        if elem is parent[op_direc]:
            if is_leaf(parent[direc]):
                res = parent[direc]
            else:
                other = parent[direc][op_direc]
                while not is_leaf(other):
                    other = other[op_direc]
                res = other
        else:
            res = find_next_value(number, parent, direc)
    return res


def explode(number: Node):
    a, b, *_ = number.levels[-1]
    parent = get_parent(number, a)

    left_node = find_next_value(number, parent, 1)
    if left_node:
        left_node.value += a.value

    right_node = find_next_value(number, parent, 2)
    if right_node:
        right_node.value += b.value

    # clear
    parent.value = 0
    parent.left = None
    parent.right = None


def split(number: Node):
    next_invalid = next(x for x in number.preorder if x.value > 9)
    val = next_invalid.value
    v1 = round(val / 2)
    v2 = val - v1

    next_invalid.value = PARENT_VALUE
    next_invalid.left = Node(min([v1, v2]))
    next_invalid.right = Node(max([v1, v2]))


def depth_is_ok(number: Node) -> bool:
    return number.properties['max_leaf_depth'] <= 4


def values_are_ok(number: Node) -> bool:
    return number.properties['max_node_value'] <= 9


def is_reduced(number: Node) -> bool:
    return depth_is_ok(number) and values_are_ok(number)


def get_magnitude(elem: Node) -> int:
    value = elem.value
    if not is_leaf(elem):
        value = 3 * get_magnitude(elem.left) + 2 * get_magnitude(elem.right)
    return value


def final_magnitude(elems: list[Node]):
    num = elems[0]
    for e in elems[1:]:
        num = Node(PARENT_VALUE, num.clone(), e.clone())
        while not is_reduced(num):
            if not depth_is_ok(num):
                explode(num)
            else:
                split(num)
    final_sum = get_magnitude(num)
    print(f'final sum magnitude: {final_sum}')


def build_bintree(elem) -> Node:
    value, left_tree, right_tree = PARENT_VALUE, None, None
    if type(elem) is list:
        left, right = elem
        left_tree = build_bintree(left)
        right_tree = build_bintree(right)
    else:
        value = elem
    return Node(value, left_tree, right_tree)


def get_input() -> list:
    data = open(0).read().splitlines()
    return [eval(d) for d in data]


def main():
    elems = [build_bintree(e) for e in get_input()]

    final_magnitude(elems)
    max_two_sum_magnitude(elems)


if __name__ == '__main__':
    main()
