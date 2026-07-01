"""
С помощью `map`/`filter`/`reduce` удалите заданный элемент из списка.
"""


def delete_elem(list_in, target):

    filtered_iterator = filter(lambda x: x != target, list_in)

    return list(filtered_iterator)
