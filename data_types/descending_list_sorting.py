# Given list
buy_list = [
    [0, 'hoody'],
    [4, 'jogging suit'],
    [1, 'shoes'],
    [2, 'swimwear'],
    [3, 'cardigan'],
]


# TODO: sort the buy_list in descending order

def sort_list(array):
    """
    Function returns sorted list
    in descending order
    :param array
    :return: list
    """
    sorted_list = []

    def find_largest_num(array):
        """
        Function return position of the largest element
        in the given list
        """
        max_num = 0
        position = 0
        for i in range(len(array)):
            if array[i][0] >= max_num:
                max_num = array[i][0]
                position = i
        return position

    while len(array) > 0:
        sorted_list.append(array.pop(find_largest_num(array)))
        # print('list:', list, 'sorted:', sorted_list)
    return sorted_list


print(sort_list(buy_list))
